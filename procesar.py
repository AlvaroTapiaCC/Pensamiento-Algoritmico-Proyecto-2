import json
import pickle
import sys

input_file = "datos/" + sys.argv[1]
output_json = "datos/" + str(sys.argv[1])[:-4] + ".json"
output_json = "datos/" + str(sys.argv[1])[:-4] + ".pkl"

with open(input_file, "r") as f:
    data = f.readlines()
    filtered_data = []
    for line in data:
        linea = line.strip().split('|')
        if linea[2] == "VIB" and (float(linea[3]) >= 0.0 and float(linea[3]) <= 50.0):
            filtered_data.append(line)
        elif linea[2] == "TEMP" and (float(linea[3]) >= -10.0 and float(linea[3]) <= 60.0):
            filtered_data.append(line)


    struct = {"sectores": {}, "sensores": {}}
    for line in filtered_data:
        time_stamp, sensor, tipo, magn, sector = line.strip().split('|')

        sector_dict = {"VIB": [], "TEMP": [], "sensores": []}
        sensor_dict = {"VIB": [], "TEMP": [], "sectores": []}
        
        if sector not in (struct["sectores"]).keys():
            struct["sectores"][sector] = sector_dict

        struct["sectores"][sector][tipo].append((time_stamp, float(magn)))

        if sensor not in struct["sectores"][sector]["sensores"]:
            struct["sectores"][sector]["sensores"].append(sensor)

        struct["sectores"][sector]["sensores"].sort(key = lambda x: int(x[1:]))

        if sensor not in (struct["sensores"]).keys():
            struct["sensores"][sensor] = sensor_dict
        
        struct["sensores"][sensor][tipo].append((time_stamp, float(magn)))

        if sector not in struct["sensores"][sensor]["sectores"]:
            struct["sensores"][sensor]["sectores"].append(sector)

    for sector in struct["sectores"]:
        struct["sectores"][sector]["VIB"].sort()
        struct["sectores"][sector]["TEMP"].sort()

    for sensor in struct["sensores"]:
        struct["sensores"][sensor]["VIB"].sort()
        struct["sensores"][sensor]["TEMP"].sort()

    
print("Serializando datos en formato json...")                                         
with open("datos/datos.json", "w") as f:
    json.dump(struct, f, indent=2)
print("Listo")

print("Serializando datos en formato pickle...")
with open("datos/datos.pkl", "wb") as f:
    pickle.dump(struct, f)
print("Listo")