import sys

def max_vib_rango(params: list):
    sector = str(params[0])
    ts_ini = str(params[1])
    ts_fin = str(params[2])
    max_vib = 0.0
    return f"{max_vib:.1f}"

def prom_temp(params: list):
    sector = str(params[0])
    fecha = str(params[1])
    prom_temp = 0.0
    return f"{prom_temp:.1f}"

def picos_vib(params: list):
    sensor = str(params[0])
    umbral = float(params[1])
    timestamps = []
    return timestamps

def rango_temp_ts(params: list):
    sector = str(params[0])
    ts_ini = str(params[1])
    ts_fin = str(params[2])
    min = 0.0
    max = 0.0
    avg = 0.0
    return f"{min:.1f},{max:.1f},{avg:.1f}"

def sensores_sector(params: list):
    sector = str(params[0])
    sensores = []
    return sensores.sort(key=lambda x: int(x[1:]))

def siguiente_medicion(params: list):
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


def main():
    consultas_file = sys.argv[1]
    resultados_file = sys.argv[2]
    clear_file(resultados_file)
    with open(consultas_file, "r") as f:
        for line in f.readlines():
            line_list = line.strip().split(" ")
            consulta = line_list[0]
            params = line_list[1:]

            if consulta == "MAX_VIB_RANGO":
                #write_output(resultados_file, consulta)
                max_vib_rango(params)
            elif consulta == "PROM_TEMP":
                #write_output(resultados_file, consulta)
                prom_temp(params)
            elif consulta == "PICOS_VIB":
                #write_output(resultados_file, consulta)
                picos_vib(params)
            elif consulta == "RANGO_TEMP_TS":
                #write_output(resultados_file, consulta)
                rango_temp_ts(params)
            elif consulta == "SENSORES_SECTOR":
                #write_output(resultados_file, consulta)
                sensores_sector(params)
            elif consulta == "SIGUIENTE_MEDICION":
                #write_output(resultados_file, consulta)
                siguiente_medicion(params)  
            

if __name__ == "__main__":
    main()