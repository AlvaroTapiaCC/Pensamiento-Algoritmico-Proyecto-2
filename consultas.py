import sys
import json
import pickle

def max_vib_rango(params: list, filename: str):
    sector = str(params[0])
    ts_ini = str(params[1])
    ts_fin = str(params[2])
    max_vib = 0.0
    return f"{max_vib:.1f}"

def prom_temp(params: list, filename: str):
    sector = str(params[0])
    fecha = str(params[1])
    prom_temp = 0.0
    return f"{prom_temp:.1f}"

def picos_vib(params: list, filename: str):
    sensor = str(params[0])
    umbral = float(params[1])
    timestamps = []
    return timestamps

def rango_temp_ts(params: list, filename: str):
    sector = str(params[0])
    ts_ini = str(params[1])
    ts_fin = str(params[2])
    min = 0.0
    max = 0.0
    avg = 0.0
    return f"{min:.1f},{max:.1f},{avg:.1f}"

def sensores_sector(params: list, filename: str):
    sector = str(params[0])
    sensores = []
    return sensores.sort(key=lambda x: int(x[1:]))

def siguiente_medicion(params: list, filename: str):
    sensor = str(params[0])
    tipo = str(params[1])
    timestamp = str(params[2])
    next_timestamp = ""
    return next_timestamp

def clear_file(filename: str):
    with open(filename, "w") as f:
        f.write("")

def write_output(filename: str, result: str):
    with open(filename, "a") as f:
        f.write(result + "\n")

def open_data(filename: str):
    if filename[:-4] == "json":
        with open(filename, "r") as f:
            return json.load(f)
    elif filename[:-3] == "pkl":
        with open(filename, "rb") as f:
            return pickle.load(f)


def main():
    consultas_file = sys.argv[1]
    resultados_file = sys.argv[2]
    datos_file = "datos/datos.json"     # Cambiar a .pkl para probar ambos
    clear_file(resultados_file)
    with open(consultas_file, "r") as f:
        for line in f.readlines():
            line_list = line.strip().split(" ")
            consulta = line_list[0]
            params = line_list[1:]

            if consulta == "MAX_VIB_RANGO":
                max_vib_rango(params, resultados_file)
            elif consulta == "PROM_TEMP":
                prom_temp(params, resultados_file)
            elif consulta == "PICOS_VIB":
                picos_vib(params, resultados_file)
            elif consulta == "RANGO_TEMP_TS":
                rango_temp_ts(params, resultados_file)
            elif consulta == "SENSORES_SECTOR":
                sensores_sector(params, resultados_file)
            elif consulta == "SIGUIENTE_MEDICION":
                siguiente_medicion(params, resultados_file)  
            

if __name__ == "__main__":
    main()