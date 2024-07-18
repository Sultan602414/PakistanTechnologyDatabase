import joblib
import pandas as pd
import numpy as np

# Load the trained model from file
model = joblib.load("model.pkl")

# Mapping of professions to numbers (adjust as per your specific mapping)
profession_mapping = {
    1: "Profession_Content/Design Powerhouse-Where Ideas Come to Life",
    2: "Profession_Developers I Animators I Designers",
    3: "Profession_Ghost Writer | Research Analyst I Business Writer",
    4: "Profession_NFT Artist | Illustrations | Graphic Design",
    5: "Profession_PHP JavaScript Laravel Wordpress CSS Node React CI",
    6: "Profession_Professional Illustrator & WordPress Developer",
    7: "Profession_Top Rated PHP/WordPress/Shopify Dev & UIX Designer",
    8: "Profession_Web & Mobile App Developer",
    9: "Profession_Where imagination & art meet.",
    10: "Profession_Wordpress|Woocommerce|Shopify|PHP7",
}

# Display professions to user
print("Select Profession:")
for num, profession in profession_mapping.items():
    print(f"{num}. {profession}")

# Ask user to select profession number
profession_input = int(input("Enter profession number: "))
rating_input = float(input("Enter Rating: "))
reviews_input = int(input("Enter Reviews: "))

# Create a DataFrame for prediction
input_data = [0,0,0,0,0,0,0,0,0,0,0,0]
input_data[0] = rating_input
input_data[1] = reviews_input
input_data[profession_input+1] = 1

# Predict HourRate using the loaded model
predicted_hour_rate = model.predict([input_data])[0]
print(f"Predicted HourRate: ${predicted_hour_rate}")
