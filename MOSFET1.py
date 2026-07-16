print('Welcome To MOSFET diagnostic Assistant')
def data_inp (param):
       value = float(input(f"Enter the {param} to be checked"))
       return value
def compare_less(name, value, threshold, repairv):
       if value < threshold:
           print(f"Checking {name}")
           print(f"We optimized to {repairv}")
           return repairv
       else:
           print("Checking successful no changes made")
           print(f"Current value {value}")
           return value
def compare_more(name, value, threshold, repairv):
       if value > threshold:
           print(f"Checking {name}")
           print(f"We optimized to {repairv}")
           return repairv
       else:
           print("Checking successful no changes made")
           print(f"Current value {value}")
           return value
VG = data_inp("VGS")
VG = compare_less ("VGS value ", VG, 0.7, 0.8)
VD = data_inp("VDS")
VD = compare_more ("VDS value ", VD, 5.0, 3.0)
TEMP = data_inp("Temperature ")
TEMP = compare_more ("Temperature ", TEMP, 100.0, 90.0)
CL = data_inp("Channel Length")
CL = compare_more ("Channel Length ", CL, 20.0, 18.0)
CW = data_inp("Channel Width")
CW = compare_more ("Chennel Width ", CW, 15.0, 12.0)
