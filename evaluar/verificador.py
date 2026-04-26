import argparse
import base64
import sys
from typing import List, Tuple


def xor_desencriptar(data_encriptado: bytes, clave: str) -> str:
    """Desencripta datos usando XOR con la clave."""
    clave_bytes = base64.b64decode(clave)
    resultado = bytearray()
    for i, byte in enumerate(data_encriptado):
        resultado.append(byte ^ clave_bytes[i % len(clave_bytes)])
    return resultado.decode("utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verificador de resultados para Proyecto 2"
    )
    parser.add_argument(
        "resultados",
        type=str,
        help="Archivo con los resultados generados por consultas.py",
    )
    parser.add_argument(
        "--expected",
        type=str,
        default="resultados_esperados.enc",
        help="Archivo encriptado con los resultados esperados (default: resultados_esperados.enc)",
    )
    parser.add_argument(
        "--key",
        type=str,
        required=True,
        help="Clave secreta para desencriptar los resultados esperados",
    )
    parser.add_argument(
        "--keep-plaintext",
        action="store_true",
        default=False,
        help="Mantener el archivo de texto plano resultados_esperados.txt después de la verificación",
    )
    return parser.parse_args()


def leer_archivo(path: str, clave: str = None) -> List[str]:
    try:
        if clave and path.endswith(".enc"):
            with open(path, "rb") as f:
                contenido_encriptado = f.read()
            contenido = xor_desencriptar(contenido_encriptado, clave)
            return [line.strip() for line in contenido.split("\n") if line.strip()]
        else:
            with open(path, "r") as f:
                return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{path}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error al leer '{path}': {e}")
        sys.exit(1)


def comparar_resultados(
    resultados: List[str], esperados: List[str]
) -> Tuple[int, int, List[str]]:
    if len(resultados) != len(esperados):
        print(f"Advertencia: Diferente número de líneas")
        print(f"  Resultados: {len(resultados)}")
        print(f"  Esperados:  {len(esperados)}")

    num_lineas = min(len(resultados), len(esperados))
    coincidencias = 0
    diferencias = []

    for i in range(num_lineas):
        if resultados[i] == esperados[i]:
            coincidencias += 1
        else:
            diferencias.append(
                {"linea": i + 1, "esperado": esperados[i], "obtenido": resultados[i]}
            )

    return coincidencias, num_lineas, diferencias


def main():
    args = parse_args()

    print(f"Verificando resultados...")
    print(f"  Resultados:  {args.resultados}")
    print(f"  Esperados:   {args.expected}")
    print()

    resultados = leer_archivo(args.resultados)
    esperados = leer_archivo(args.expected, args.key)

    coincidencias, total, diferencias = comparar_resultados(resultados, esperados)

    print(f"Total de consultas: {total}")
    print(
        f"Coincidencias:      {coincidencias}/{total} ({100 * coincidencias / total:.1f}%)"
    )
    print(f"Diferencias:        {len(diferencias)}")
    print()

    if diferencias:
        print("Primeras 10 diferencias:")
        for diff in diferencias[:10]:
            print(f"  Línea {diff['linea']}:")
            print(f"    Esperado: {diff['esperado']}")
            print(f"    Obtenido: {diff['obtenido']}")

        if len(diferencias) > 10:
            print(f"  ... y {len(diferencias) - 10} más")

        print()
        print("Resultado: FALLÓ")
        sys.exit(1)
    else:
        print("Resultado: OK - Todas las respuestas son correctas")

    if args.keep_plaintext:
        plaintext_path = args.expected.replace(".enc", ".txt")
        with open(plaintext_path, "w") as f:
            for line in esperados:
                f.write(line + "\n")
        print(f"Archivo de texto plano guardado en: {plaintext_path}")

    sys.exit(0)


if __name__ == "__main__":
    main()
