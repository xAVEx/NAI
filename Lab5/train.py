import numpy as np
import pandas as pd

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import classification_report

from utils.utils import save_instance

data = pd.read_table("data/seeds_dataset.txt", names=["Area", "Perimeter", "Compactness",
                                                      "Length of kernel", "Width of kernel",
                                                      "Asymmetry coefficient", "Length of kernel groove",
                                                      "Class"])
labels = data.pop("Class")
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
save_instance(scaler, "model/scaler")

X_train, X_test, y_train, y_test = train_test_split(scaled_data, labels, random_state=101,
                                                    stratify=labels, train_size=0.7)

model = SVC(kernel="poly")
rs = RandomizedSearchCV(estimator=model, param_distributions={"C": np.arange(0.1, 1, 0.1), "degree": [2, 3, 4, 5, 6]},
                        random_state=101, n_iter=50, n_jobs=4, cv=3, scoring="f1_macro", refit=True, verbose=1)

rs.fit(X_train, y_train)

final_model = rs.best_estimator_
save_instance(final_model, "model/model")

print(classification_report(y_test, final_model.predict(X_test)))
