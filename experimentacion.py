
import random
import string
import time

from lcs_recursivo import lcs_recursivo
from lcs_dinamica import lcs_dinamica
from hirschberg import hirschberg


def generar_cadena(longitud):
    return "".join(
        random.choice(string.ascii_uppercase)
        for _ in range(longitud)
    )


def medir_tiempo(func, *args):

    inicio = time.perf_counter()

    func(*args)

    fin = time.perf_counter()

    return fin - inicio


tamanos = [50, 100, 200, 500, 1000]

print("-" * 70)
print(f"{'N':>8} {'Recursivo':>15} {'Hirschberg':>15} {'Dinámico':>15}")
print("-" * 70)

for n in tamanos:

    X = generar_cadena(n)
    Y = generar_cadena(n)

    if n <= 20:
        tiempo_rec = medir_tiempo(
            lcs_recursivo,
            X,
            Y,
            len(X),
            len(Y)
        )
    else:
        tiempo_rec = None

    tiempo_h = medir_tiempo(hirschberg, X, Y)
    tiempo_d = medir_tiempo(lcs_dinamica, X, Y)

    print(
        f"{n:>8} "
        f"{str(round(tiempo_rec,4)) if tiempo_rec else 'N/A':>15} "
        f"{tiempo_h:>15.6f} "
        f"{tiempo_d:>15.6f}"
    )