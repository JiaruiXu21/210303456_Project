# Watch Recommendation System

A machine learning-powered web application that recommends watches based on user preferences and personal attributes.

## Overview

This system uses a Random Forest classifier trained on watch purchase data to predict suitable watch brands based on user inputs such as age group, profession, lifestyle, personality traits, and watch preferences.

## Features

- Interactive web form for collecting user preferences
- Machine learning-based recommendation engine
- Display of personalized watch recommendations
- User feedback collection for continuous improvement

## Project Structure

```
recommend_watch/
├── app/                  # Flask web application
│   ├── static/           # CSS, JS, and image files
│   ├── templates/        # HTML templates
│   ├── __init__.py       # Application initialization
│   ├── forms.py          # Form definitions
│   └── routes.py         # Application routes
├── data/                 # Data files
│   ├── purchase_data.xlsx    # Training data for the model
│   ├── watch_data.xlsx       # Watch information data
│   └── feedback_data.csv     # User feedback data
├── model/                # Trained models and encoders
│   ├── random_forest_model.pkl
│   ├── brand_label_encoder.pkl
│   └── X_encoded_columns.pkl
├── model_training.py     # Script for training the ML model
├── main.py               # Main application entry point
└── README.md             # This file
```

## Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, pandas
- **Frontend**: HTML, CSS, JavaScript (via Flask templates)
- **Data Storage**: Excel files, CSV

## Setup and Installation

1. Clone the repository
2. Install the required dependencies:
   ```
   pip install flask pandas scikit-learn flask-wtf openpyxl
   ```
3. Train the model:
   ```
   python model_training.py
   ```
4. Run the application:
   ```
   python main.py
   ```
5. Access the application at `http://localhost:5000`

## How It Works

1. Users fill out a form with their personal preferences and attributes
2. The system processes this input through a trained Random Forest model
3. The model predicts the most suitable watch brands based on the input
4. The application displays recommendations from those brands
5. Users can provide feedback on the recommendations, which is stored for future model improvements

## Future Improvements

- Integration with watch retailer APIs for real-time data
- Enhanced recommendation algorithm with collaborative filtering
- User accounts for personalized recommendation history
- Mobile application version 