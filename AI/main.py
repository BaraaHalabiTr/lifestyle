import pandas as pd
import numpy as np
from sklearn.preprocessing import minmax_scale

data = pd.read_csv("dataset.csv")

df = pd.DataFrame(data)

cols = df.select_dtypes(np.number).columns
df[cols] = minmax_scale(df[cols])


def detect_outliers(_data):
    outliers = []
    threshold = 1.2
    mean = np.mean(_data)
    std = np.std(_data)

    for i in _data:
        z_score = (i - mean) / std
        if np.abs(z_score) > threshold:
            print(np.abs(z_score))
            outliers.append(i)
    return outliers


print(detect_outliers(df['WEEKLY_MEDITATION']))
