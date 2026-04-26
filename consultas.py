import sys
import json
import pickle
import time

DATA_TYPE = "json"         # Cambiar json/pkl para probar ambos
DATOS_FILE = "datos/datos." + DATA_TYPE

def max_vib_rango(params: list, out_file, datos):
    sector = str(params[0])
    ts_ini = str(params[1])
    ts_fin = str(params[2])
    max_vib = None
    for registro in datos["sectores"][sector]["VIB"]:
        if registro[0] >= ts_ini and (max_vib is None or registro[1] > float(max_vib)):
            max_vib = registro[1]
        elif registro[0] > ts_fin:
            break
    if max_vib is None:
        result = "NONE"
    else:
        result = f"{max_vib:.1f}"
    out_file.write(result + "\n")

def prom_temp(params: list, out_file, datos):
    sector = str(params[0])
    fecha = str(params[1])
    registros = []
    for registro in datos["sectores"][sector]["TEMP"]:
        if registro[0][:10] == fecha:
            registros.append(registro[1])
        elif registro[0][:10] > fecha:
            break
    if len(registros) > 0:
        result = f"{(sum(registros) / len(registros)):.1f}"
    else:
        result = "NODATA"
    out_file.write(result + "\n")

def picos_vib(params: list, out_file, datos):
    sensor = str(params[0])
    umbral = float(params[1])
    timestamps = []
    for registro in datos["sensores"][sensor]["VIB"]:
        if registro[1] > umbral:
            timestamps.append(registro[0])
    if len(timestamps) > 0:
        out_file.write(",".join(timestamps) + "\n")
    else:
        out_file.write("NODATA\n")

def rango_temp_ts(params: list, out_file, datos):
    sector = str(params[0])
    ts_ini = str(params[1])
    ts_fin = str(params[2])
    registros = []
    for registro in datos["sectores"][sector]["TEMP"]:
        if registro[0] >= ts_ini:
            registros.append(registro[1])
        elif registro[0] > ts_fin:
            break
    if len(registros) > 0:
        result = f"{min(registros):.1f},{max(registros):.1f},{(sum(registros) / len(registros)):.1f}"
    else:
        result = "NODATA"
    out_file.write(result + "\n")

def sensores_sector(params: list, out_file, datos):
    sector = str(params[0])
    sensores = datos["sectores"][sector]["sensores"]
    sensores.sort(key=lambda x: int(x[1:]))
    if len(sensores) > 0:
        out_file.write(",".join(sensores) + "\n")
    else:
        out_file.write("NODATA\n")

def siguiente_medicion(params: list, out_file, datos):
    sensor = str(params[0])
    tipo = str(params[1])
    timestamp = str(params[2])
    next_valid = False
    for registro in datos["sensores"][sensor][tipo]:
        if registro[0] == timestamp:
            next_valid = True
            continue
        if next_valid:
            res = registro
            break
    if res:
        result = f"{res[0]},{res[1]:.1f}"
    else:
        result = "NONE"
    out_file.write(result + "\n")

def clear_file(filename: str):
    with open(filename, "w") as f:
        f.write("")

def open_data(data_file: str):
    if data_file.endswith(".json"):
        with open(data_file, "r") as f:
            return json.load(f)
    elif data_file.endswith(".pkl"):
        with open(data_file, "rb") as f:
            return pickle.load(f)


handlers = {
    "MAX_VIB_RANGO": max_vib_rango,
    "PROM_TEMP": prom_temp,
    "PICOS_VIB": picos_vib,
    "RANGO_TEMP_TS": rango_temp_ts,
    "SENSORES_SECTOR": sensores_sector,
    "SIGUIENTE_MEDICION": siguiente_medicion,
}

def main():
    inicio = time.time()

    consultas_file = sys.argv[1]
    resultados_file = sys.argv[2]

    datos = open_data(DATOS_FILE)

    
    clear_file(resultados_file)

    with open(resultados_file, "w") as out:
        with open(consultas_file, "r") as f:
            for line in f:
                line_list = line.strip().split(" ")
                consulta = line_list[0]
                params = line_list[1:]

                handler = handlers.get(consulta)
                if handler:
                    handler(params, out, datos) 
            
    fin = time.time()

    print(f"Tiempo usando {DATA_TYPE}: {(fin - inicio) * 1e3:.6f} milisegundos")

if __name__ == "__main__":
    main()