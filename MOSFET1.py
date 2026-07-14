print('Welcome To MOSFET diagnostic Assistant')
Dict = {"Dv" : input("Enter device name"),
"VG" : input('Enter VGS'),
"VD" : input('Enter VDS'),
"Temp" : input('Enter Temperature'),
"CL" : input('Enter Channel Length'),
"CW" : input('Enter Channel Width'),
}
print(f"current status {Dict}")
VG = float(Dict.get("VG"))
VD = float(Dict.get("VD"))
T = float(Dict.get("Temp"))
CL = float(Dict.get("CL"))
CW = float(Dict.get("CW"))
n = 0
while n < 1:
     if VG < 0.7:
        print('Device will not work')
        print('Repair Cost= 150')
        Dict ['VG'] = str(0.8)
     else:
        print('Your VGS is fine')
     if T > 100.0:
        print ('''Overheated
        COOLING REQUIRED''')
        Dict['Temp'] = 90
     else:
        print("Good going")
     if VD > 5:
        print('''High drain voltage''')
        Dict['VD'] = 3
     else :
         print("DRAIN VOLTAGE IS FINE")
     if CL < 20:
         print("No requirement with length")
     else :
        print("Changes made free of cost")         
        Dict['CL'] = 18
     if CW < 15:
         print("No requirement with width")
     else :
        print("Changes made")         
        Dict['CL'] = 12       
     n+= 1
print(f"Changes made to the Conductor{Dict}")
