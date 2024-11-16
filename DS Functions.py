import numpy as np

Average_pulse_max = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)

print ('Maximum pulse rate=',Average_pulse_max)

Average_pulse_min = min(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)

print ('Minimum pulse rate=',Average_pulse_min)


Calorie_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]

Average_calorie_burnage = np.mean(Calorie_burnage)

print('mean =',Average_calorie_burnage)