# Low-Cost_Quad-Interferometer
This research experiment recreates a quadrature Mach-Zenhder optical inferometer using Adafruit microcontroller for analog-to-digital data acquisiton. 



// insert picture of the working setup
![image](https://user-images.githubusercontent.com/37032927/162936383-63b10e86-2fae-4593-b529-db24f3bb2851.png)

# Motivation
For this project, we wanted to be able to utilize a cheap store-bought laser and 3d printed mounts to simulate an expensive mach-zenhder interferometer which will plot real-time data of expansion. The two photodiodes should be perfectly pi/4 out of phase to obtain perfect quadrature.

# Quick Start
Use the package manager pip to install all required libraries
```bash
pip install notebook
pip install numpy
pip install matplotlib
pip install serial
```

# Usage
We utilized Mu Editor and edit our code in circuit-python.

# Screenshots
#Insert code snippets

# List of Components
Quantity | Item Description | Brand/Supplier | Cost 
-------- | ---------------- | -------------- | ------
1 | Green Laser Pointer | Pinty | $23.99
1 | Aluminum Plate | Kaylan | $19.99
1 | Pair of 3D glasses | Real D 3D | $4.99
1 | Plastic Sheet Polarizer | Ixgut | $12.99
1 | Spool 3D printer filament | Geeetech | $19.53
1 | 120-pack Arts Mirror | Juvale | $11.99
2 | Nonpolarizing Beamsplitter | Edmund Optics | $90.00
2 | Kinematic mount | Thorlabs | $79.72
2 | Home-built Photodetectors | Various | $xx.xx
1 | LM35 Temperature Sensor | TI | $2.29
1 | Trinket M0 MicroController | Adafruit | $8.39
1 | Container Superglue | Loctite | $2.79
1 | Package 5 minute epoxy | Loctite | $3.69
Total | | |$263.20


# 3D Print Files
These were the STL files for our mounts for the adafruit m0 trinket and the photodiode. 

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
# License
