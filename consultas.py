import sys
import json
import pickle

DATOS_FILE = "datos/datos.json"       # Cambiar a .pkl para probar ambos      

def max_vib_rango(params: list, out_file):
    sector = str(params[0])
    ts_ini = str(params[1])
    ts_fin = str(params[2])
    result = ""
    out_file.write(result + "\n")

def prom_temp(params: list, out_file):
    sector = str(params[0])
    fecha = str(params[1])
    result = ""
    out_file.write(result + "\n")

def picos_vib(params: list, out_file):
    sensor = str(params[0])
    umbral = float(params[1])
    timestamps = []
    out_file.write(",".join(timestamps) + "\n")

def rango_temp_ts(params: list, out_file):
    sector = str(params[0])
    ts_ini = str(params[1])
    ts_fin = str(params[2])
    result = ""
    out_file.write(result + "\n")

def sensores_sector(params: list, out_file):
    sector = str(params[0])
    sensores = []
    sensores.sort(key=lambda x: int(x[1:]))
    out_file.write(",".join(sensores) + "\n")

def siguiente_medicion(params: list, out_file):
    sensor = str(params[0])
    tipo = str(params[1])
    timestamp = str(params[2])
    result = ""
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
    consultas_file = sys.argv[1]
    resultados_file = sys.argv[2]

    clear_file(resultados_file)

    with open(resultados_file, "w") as out:
        with open(consultas_file, "r") as f:
            for line in f:
                line_list = line.strip().split(" ")
                consulta = line_list[0]
                params = line_list[1:]

                handler = handlers.get(consulta)
                if handler:
                    handler(params, out) 
            

if __name__ == "__main__":
    main()