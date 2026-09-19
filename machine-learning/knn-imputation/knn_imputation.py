from sklearn.impute import KNNImputer
import numpy as np

data = np.array([
    [2, 4, np.nan],
    [5, 1, 6],
    [np.nan, 5, 7],
    [9, 8, 0]
])

knn_imputer = KNNImputer(n_neighbors=2)
impute = knn_imputer.fit_transform(data)
print(data)
print(impute)
