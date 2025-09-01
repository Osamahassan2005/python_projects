import matplotlib.pyplot as plt
import numpy as np

# Data
distances = np.array([1, 2, 3, 4, 5])
candle = np.array([10, 2, 0, 0, 0])
led = np.array([190, 78, 35, 21, 11])
tecno_flash = np.array([16, 3, 1, 0, 0])

# Plot setup
plt.figure(figsize=(10, 6))

# Measured data only (no theoretical line)
plt.scatter(distances, led, color='#1f77b4', s=100, label="LED Bulb")
plt.plot(distances, led, 'b--', linewidth=2)

plt.scatter(distances, tecno_flash, color='#2ca02c', s=100, label="Smartphone Flashlight")
plt.plot(distances, tecno_flash, 'g--', linewidth=2)

plt.scatter(distances, candle, color='#d62728', s=100, label="Candle")
plt.plot(distances, candle, 'r--', linewidth=2)

# Labels and Title
plt.xlabel("Distance (m)", fontsize=12)
plt.ylabel("Light Intensity (lux)", fontsize=12)
plt.title("Measured Light Intensity vs. Distance", fontsize=14)

# Legend & Grid
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)

# Save and Show
plt.savefig('measured-intensity-vs-distance.png', dpi=300)
plt.show()
