import numpy as np
from utils.utils import load_instance

scaler = load_instance("model/scaler")
model = load_instance("model/model")

names = ["Area", "Perimeter", "Compactness",
         "Length of kernel", "Width of kernel",
         "Asymmetry coefficient", "Length of kernel groove"]

answers = []
for name in names:
    answer = input(f"Enter value for {name}: ")
    answers.append(answer)

answers = np.array(answers).reshape(1, -1)
answers = scaler.transform(answers)
prediction = model.predict(answers.reshape(1, -1))

print(f"The prediction is class no.: {prediction}")
