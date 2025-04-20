from flask import Blueprint, render_template, request, redirect, url_for
from .forms import WatchRecommendationForm
import pandas as pd
import pickle
import os
import json
import random

main = Blueprint('main', __name__)

# Load watch data
watch_data_path = 'data/watch_data.xlsx'
if not os.path.exists(watch_data_path):
    print("Watch data not found at:", watch_data_path)
else:
    watch_data = pd.read_excel(watch_data_path, sheet_name='Sheet1')
    watch_data = watch_data.dropna()

    # Ensure brand names are lowercase
    watch_data['Brands'] = watch_data['Brands'].str.lower()

# Load model and encoders
model_path = 'model/random_forest_model.pkl'
encoder_path = 'model/brand_label_encoder.pkl'
columns_path = 'model/X_encoded_columns.pkl'

if not (os.path.exists(model_path) and os.path.exists(encoder_path) and os.path.exists(columns_path)):
    print("Model files not found. Please run model_training.py first.")
    rf_model = None
    brand_label_encoder = None
    training_columns = None
else:
    with open(model_path, 'rb') as f:
        rf_model = pickle.load(f)
    with open(encoder_path, 'rb') as f:
        brand_label_encoder = pickle.load(f)
    training_columns = pd.read_pickle(columns_path)

@main.route('/', methods=['GET', 'POST'])
def home():
    form = WatchRecommendationForm()
    if form.validate_on_submit() and rf_model is not None and brand_label_encoder is not None and training_columns is not None:
        # Extract user inputs
        age_group = form.age_group.data.strip().lower()
        profession = form.profession.data.strip().lower()
        if profession == "other" and form.other_profession.data.strip():
            profession = form.other_profession.data.strip().lower()
        personality = form.personality.data.strip().lower()
        lifestyle = form.lifestyle.data.strip().lower()
        design = form.design.data.strip().lower()
        price_range = form.price_range.data.strip().lower()
        material = form.material.data.strip().lower()
        functionality = form.functionality.data.strip().lower()

        user_input = {
            "Age Group": age_group,
            "Profession": profession,
            "Personality": personality,
            "Lifestyle": lifestyle,
            "Design": design,
            "Price Range": price_range,
            "Material": material,
            "Functionality": functionality
        }

        user_df = pd.DataFrame([user_input])
        user_encoded = pd.get_dummies(user_df, drop_first=True)
        user_encoded = user_encoded.reindex(columns=training_columns, fill_value=0)

        print("\n--- DEBUG INFO START ---")
        print("User Input:", user_input)
        print("Encoded Input:\n", user_encoded)

        if rf_model is not None:
            brand_probs = rf_model.predict_proba(user_encoded)[0]

            print("Brand probabilities:")
            for brand_name, prob in zip(brand_label_encoder.classes_, brand_probs):
                print(f"{brand_name}: {prob:.2f}")

            sorted_indices = brand_probs.argsort()[::-1]
            top_5_indices = sorted_indices[:5]
            top_5_brands = brand_label_encoder.inverse_transform(top_5_indices)
            print("Top 5 Predicted Brands:", top_5_brands)

            top_5_brands_lower = [b.lower() for b in top_5_brands]
            print("Filtering watch_data for:", top_5_brands_lower)

            recommendations = watch_data[watch_data['Brands'].isin(top_5_brands_lower)]
            print("Found recommendations before random sampling:", len(recommendations))

            # Random sample 5 watches
            if len(recommendations) >= 5:
                # random_state ensures slightly variable results, remove it for pure randomness
                recommendations = recommendations.sample(5, random_state=random.randint(0, 9999))
            else:
                # If fewer than 5, just use all found
                pass

            print("Final Recommendations:\n", recommendations)
            print("--- DEBUG INFO END ---\n")

            return render_template('result.html', recommendations=recommendations)
        else:
            print("Model not loaded properly.")
            return render_template('form.html', form=form)

    return render_template('form.html', form=form)

@main.route('/feedback', methods=['POST'])
def feedback():
    # Get feedback from the form
    feedback_value = request.form.get("feedback")  # "satisfied" or "not_satisfied"
    
    # Retrieve user inputs
    age_group = request.form.get("age_group", "")
    profession = request.form.get("profession", "")
    personality = request.form.get("personality", "")
    lifestyle = request.form.get("lifestyle", "")
    design = request.form.get("design", "")
    price_range = request.form.get("price_range", "")
    material = request.form.get("material", "")
    functionality = request.form.get("functionality", "")

    recommended_watches_json = request.form.get("recommended_watches", "[]")
    recommended_watches = json.loads(recommended_watches_json)

    # Prepare feedback data row
    feedback_row = {
        "Age Group": age_group,
        "Profession": profession,
        "Personality": personality,
        "Lifestyle": lifestyle,
        "Design": design,
        "Price Range": price_range,
        "Material": material,
        "Functionality": functionality,
        "Feedback": feedback_value,
        "Recommended Watches": str(recommended_watches)
    }

    # Save feedback to a CSV file
    feedback_file = "data/feedback_data.csv"
    if not os.path.exists(feedback_file):
        pd.DataFrame([feedback_row]).to_csv(feedback_file, index=False)
    else:
        pd.DataFrame([feedback_row]).to_csv(feedback_file, mode='a', header=False, index=False)

    # Redirect back to home or show a thank-you message
    return redirect(url_for('main.home'))