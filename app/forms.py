from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Optional


class WatchRecommendationForm(FlaskForm):
    # Age Group
    age_group = SelectField(
        "What is your age group?",
        choices=[
            ("Below 20", "Below 20"),
            ("21–30", "21–30"),
            ("31–40", "31–40"),
            ("41–50", "41–50"),
            ("51–60", "51–60"),
            ("Above 60", "Above 60")
        ],
        validators=[DataRequired()]
    )

    # Profession
    profession = SelectField(
        "What is your profession?",
        choices=[
            ("Student", "Student"),
            ("Engineer", "Engineer"),
            ("Business Executive", "Business Executive"),
            ("Entrepreneur", "Entrepreneur"),
            ("Doctor", "Doctor"),
            ("Artist", "Artist"),
            ("Lawyer", "Lawyer"),
            ("Teacher", "Teacher"),
            ("Athlete", "Athlete"),
            ("Scientist", "Scientist"),
            ("Other", "Other")
        ],
        validators=[DataRequired()]
    )
    other_profession = StringField("If other, please specify:", validators=[Optional()])

    # Lifestyle
    lifestyle = SelectField(
        "What kind of lifestyle best describes you?",
        choices=[
            ("Adventurous", "Adventurous"),
            ("Professional", "Professional"),
            ("Casual", "Casual"),
            ("Elegant", "Elegant"),
            ("Balanced", "Balanced"),
            ("Sporty", "Sporty")
        ],
        validators=[DataRequired()]
    )

    # Personality
    personality = SelectField(
        "Which personality trait resonates with you most?",
        choices=[
            ("Outgoing", "Outgoing"),
            ("Analytical", "Analytical"),
            ("Creative", "Creative"),
            ("Ambitious", "Ambitious"),
            ("Tech-Savvy", "Tech-Savvy"),
            ("Detail-Oriented", "Detail-Oriented"),
            ("Organised", "Organised"),
            ("Bold", "Bold")
        ],
        validators=[DataRequired()]
    )

    # Design Preference
    design = SelectField(
        "What type of design do you prefer in a watch?",
        choices=[
            ("Sporty", "Sporty"),
            ("Elegant", "Elegant"),
            ("Classic", "Classic"),
            ("Modern", "Modern"),
            ("Minimalist", "Minimalist")
        ],
        validators=[DataRequired()]
    )

    price_range = SelectField(
        "What is your preferred price range for a watch?",
        choices=[
            ("Very Affordable", "Very Affordable"),
            ("Affordable", "Affordable"),
            ("Between Affordable and Luxury", "Between Affordable and Luxury"),
            ("Luxury", "Luxury")
        ],
        validators=[DataRequired()]
    )

    material = SelectField(
        "What kind of watch material do you like the most?",
        choices=[
            ("Stainless Steel", "Stainless Steel"),
            ("Gold", "Gold"),
            ("Titanium", "Titanium"),
            ("Platinum", "Platinum"),
            ("Bronze", "Bronze"),
            ("Carbon Fiber", "Carbon Fiber")
        ],
        validators=[DataRequired()]
    )

    functionality = SelectField(
        "What functionalities do you value most in a watch?",
        choices=[
            ("Water Resistance", "Water Resistance"),
            ("Chronograph/Complications", "Chronograph/Complications"),
            ("Diver Functionality", "Diver Functionality"),
            ("Standard Features", "Standard Features"),
            ("Lightweight Design", "Lightweight Design"),
            ("Durability", "Durability")
        ],
        validators=[DataRequired()]
    )

    submit = SubmitField("Get Recommendations")
