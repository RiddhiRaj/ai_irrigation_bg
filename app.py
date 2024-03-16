# app.py
from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load and preprocess the dataset
dataset = pd.read_csv('smart_irrigation_dataset.csv')
X = dataset.drop(['Irrigation Requirement (mm)', 'Date'], axis=1)
y = dataset['Irrigation Requirement (mm)']
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    temperature = float(data['temperature'])
    humidity = float(data['humidity'])
    precipitation = float(data['precipitation'])
    soil_moisture = float(data['soil_moisture'])
    
    weather_data = [[temperature, humidity, precipitation, soil_moisture]]
    irrigation_requirement = model.predict(weather_data)[0]
    
    return jsonify({'prediction': irrigation_requirement})

if __name__ == '__main__':
    app.run(debug=True)
