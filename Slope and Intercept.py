import pandas as pd
import numpy as np

health_data = pd.read_csv("data.csv", header=0, sep=",")

x = health_data["Average_Pulse"]
y = health_data["Calorie_Burnage"]
slope_intercept = np.polyfit(x, y, 1)

print(str(slope_intercept))
