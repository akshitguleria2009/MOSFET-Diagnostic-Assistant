print('Welcome To MOSFET diagnostic Assistant')
def data_inp (param):
       value = float(input(f"Enter the parameters= {param} "))
       return value
vgs = data_inp("Gate-Source Voltage (VGS)")
vds = data_inp("Drain-Source Voltage (VDS)")
vt = data_inp("Threshold Voltage (VT)")
k = data_inp("Process Constant (k)")
vov= vgs - vt
print(f"Your current overdrive voltage {vov} V")
if vgs < vt:
    region = "Cutoff"

elif vds < vov:
    region = "Linear"

else:
    region = "Saturation"
print(f"Operating Region: {region}")
import numpy as np
if region == "Cutoff":
    ID = 0
elif region == "Linear":
    ID = k*(((vgs - vt)*vds) - ((vds)**2)/2)
else:
    ID = k*((vgs - vt)**2)/2
vgs_sweep = np.linspace(0,5,500)
print()

print("---------MOSFET REPORT---------")

print(f"Operating Region : {region}")

print(f"Overdrive Voltage : {vov} V")

print(f"Drain Current : {ID:.6f} A")

print(f"Overdrive Voltage : {vov:.2f} V")
id_sweep = np.zeros_like(vgs_sweep)
for i, vg in enumerate(vgs_sweep):

    vov = vg - vt

    if vg < vt:
        id_sweep[i] = 0

    elif vds < vov:
        id_sweep[i] = k * (((vg - vt) * vds) - ((vds**2)/2))

    else:
        id_sweep[i] = k * ((vg - vt)**2) / 2
        
import matplotlib.pyplot as plt
plt.plot(vgs_sweep, id_sweep)
plt.xlabel("VGS (V)")
plt.ylabel("Drain Current (A)")
plt.title("MOSFET Transfer Characteristics")
plt.grid(True)
plt.legend(["Transfer Curve"])
plt.tight_layout()
plt.savefig("transfer_curve.png")
plt.show()
