import numpy as np
import matplotlib.pyplot as plt
from fracturing_model import *

# Input parameters
rates = np.linspace(20, 80, 10)  # bpm
viscosity = 30       # cp
youngs_modulus = 25  # GPa
height = 30          # m

pressures = []
widths = []
lengths = []

for r in rates:
    p = calculate_net_pressure(r, viscosity, height)
    w = calculate_fracture_width(p, height, youngs_modulus)
    l = calculate_fracture_length(r, w)

    pressures.append(p)
    widths.append(w)
    lengths.append(l)

# Plot Pressure vs Rate
plt.figure()
plt.plot(rates, pressures)
plt.xlabel("Injection Rate (bpm)")
plt.ylabel("Net Pressure (MPa)")
plt.title("Pressure vs Pump Rate")
plt.grid()
plt.savefig("results/pressure_vs_rate.png")

# Plot Fracture Geometry
plt.figure()
plt.plot(rates, widths, label="Width (mm)")
plt.plot(rates, lengths, label="Length (m)")
plt.xlabel("Injection Rate (bpm)")
plt.ylabel("Fracture Geometry")
plt.title("Fracture Geometry vs Pump Rate")
plt.legend()
plt.grid()
plt.savefig("results/fracture_geometry.png")

plt.show()