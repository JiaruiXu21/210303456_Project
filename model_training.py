import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
import pickle
import os

purchase_data = pd.read_excel('data/purchase_data.xlsx', sheet_name='records (5)')

feature_cols = ["Age Group", "Profession", "Personality", "Lifestyle", "Design", "Price Range", "Material", "Functionality"]
target_col = "Purchased Brand"

X = purchase_data[feature_cols]
y = purchase_data[target_col]

if X.isnull().sum().sum() == 0:
    print("Test Passed: No missing values found in feature columns")
else:
    print("Test Failed: Missing values found in feature columns")

X_encoded = pd.get_dummies(X, drop_first=True)

if X_encoded.shape[1] > len(feature_cols):
    print("Test Passed: One-hot encoding of categorical columns successful")
else:
    print("Test Failed: One-hot encoding failed for categorical columns")

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

if len(set(y_encoded)) == len(label_encoder.classes_):
    print("Test Passed: Label encoding successful")
else:
    print("Test Failed: Label encoding failed for target variable")

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_encoded, test_size=0.2, random_state=42)

if len(X_train) == len(y_train):
    print("Test Passed: Training data split is correct")
else:
    print("Test Failed: Training data split mismatch")

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30, None],
    'min_samples_leaf': [1, 2, 5],
    'max_features': ['auto', 'sqrt']
}

rf = RandomForestClassifier(n_estimators=100, random_state=42)
grid_search = GridSearchCV(rf, param_grid, cv=3, n_jobs=-1, scoring='accuracy')
grid_search.fit(X_train, y_train)

best_rf = grid_search.best_estimator_
print("Best Parameters:", grid_search.best_params_)

accuracy = best_rf.score(X_test, y_test)
print("Test accuracy with best parameters:", accuracy)

# Save the best model
os.makedirs('model', exist_ok=True)
with open('model/random_forest_model.pkl', 'wb') as f:
    pickle.dump(best_rf, f)

with open('model/brand_label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

X_encoded.columns.to_series().to_pickle('model/X_encoded_columns.pkl')



