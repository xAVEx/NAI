# Filip Wrzesień & Patryk Szczepański
# Miles to Gallons Converters for 1970s Cars

from tensorflow import keras
from tensorflow.keras import layers

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
column_names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight',
                'Acceleration', 'Model Year', 'Origin']

raw_dataset = pd.read_csv(url, na_values='?', names=column_names, comment='\t', sep=' ', skipinitialspace=True).dropna()

raw_dataset['Origin'] = raw_dataset['Origin'].map({1: 'USA', 2: 'Europe', 3: 'Japan'})
raw_dataset[['USA', 'Europe', 'Japan']] = pd.get_dummies(raw_dataset['Origin'], prefix='', prefix_sep='_')
raw_dataset.drop('Origin', axis=1, inplace=True)


labels = raw_dataset['MPG']
raw_features = raw_dataset.drop('MPG', axis=1)

scaler = StandardScaler()
scaler.fit(raw_features)
scaled_features = scaler.transform(raw_features)

# Save scaler
joblib.dump(scaler, "model/scaler")

# split to train and test sets
X_train, X_test, y_train, y_test = train_test_split(scaled_features, labels, test_size=0.3, random_state=101)

# Sequential model with 4 layers
model = keras.models.Sequential(name="MPG_predictor")
model.add(keras.Input(shape=(scaled_features.shape[1],)))
model.add(layers.Dense(scaled_features.shape[1], activation="relu"))
model.add(layers.Dense(5, activation="relu"))
model.add(layers.Dense(3, activation="relu"))
model.add(layers.Dense(1))

# Compile and fit model
model.compile(loss='mean_squared_error')
model.fit(X_train, y_train, epochs=200)  # verbose=0 jak ma być cicho

# Test model
mae = round(mean_absolute_error(y_test, model.predict(X_test)), 2)

# Save model
model.save('model/')

# Save MAE metric
print(f"Your model has mean absolute error equal to {mae}")
with open("model/model_metric", "w") as m:
    m.write(f"{mae}")
