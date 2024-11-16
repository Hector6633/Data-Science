# Three lines to make our compiler able to draw:
import sys
import matplotlib

matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data.plot(x='Average_Pulse', y='Calorie_Burnage', kind='line')
plt.ylim(ymin=0)
plt.xlim(xmin=0)

plt.show()
# Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


# To find the slope (Slope = f(x2) - f(x1) / x2-x1)   linear fun(f(x)) = 2x+80 = 2*80+80=240
def slope(x1, y1, x2, y2):
    s = (y2 - y1) / (x2 - x1)
    return s


print("\nslope=",slope(80, 240, 90, 260))
