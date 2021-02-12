# Filip Wrzesień & Patryk Szczepański
# Miles to Gallons Converters for 1970s Cars

import click
import joblib
import numpy as np
from tensorflow import keras

model = keras.models.load_model('model/')
click.clear()
with open('model/model_metric', 'r') as m:
    mae = float(m.read())

scaler = joblib.load("model/scaler")
predictors = ['Cylinders', 'Displacement', 'Horsepower', 'Weight',
              'Acceleration', 'Model Year', 'USA', 'Europe', 'Japan']
print("-----------------------------------------------")
print("INSTRUCTION")
print("How Many Cylinders")
print("Displacment in CU IN")
print("1l = 60 CU IN")
print("Horsepower in KM")
print("Weight in LBS")
print("1kg = 2.2 LBS")
print("Acceleration value up to 100 MPH in time ... ")
print("Moder Year in the years 70 to 82")
print("-----------------------------------------------")

data_to_predict = []
for predictor in predictors:
    if predictor in ['USA', 'Europe', 'Japan']:
        answer = int(input(f"Press 1 if origin country = {predictor} or 0 to skip: "))
    else:
        answer = float(input(f"Enter {predictor} value: "))
    data_to_predict.append(answer)

data_to_predict = np.array(data_to_predict).reshape(1, -1)
data_to_predict = scaler.transform(data_to_predict)
prediction = model.predict(data_to_predict)[0][0]

print(f"Your prediction is {round(float(prediction), 2)} +- {mae} mile per gallons")

