import random
import math
import time


PI_REAL = 3.14159


# --------------------------------------------------
# 1. MONTE CARLO
# --------------------------------------------------
def monte_carlo_pi(N):
    """
    Genera N puntos aleatorios en el cuadrado
    [-0.5,0.5] x [-0.5,0.5]
    y estima el valor de pi.
    """

    dentro = 0

    inicio = time.perf_counter()

    for _ in range(N):
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)

        if x * x + y * y < 0.5 * 0.5:
            dentro += 1

    pi_estimado = 4 * (dentro / N)

    tiempo = time.perf_counter() - inicio
    error = abs(PI_REAL - pi_estimado)

    return {
        "N": N,
        "dentro": dentro,
        "pi": pi_estimado,
        "error": error,
        "tiempo": tiempo
    }


# --------------------------------------------------
# 2. LAS VEGAS
# --------------------------------------------------
def las_vegas_pi(K):
    """
    Genera puntos hasta conseguir exactamente
    K puntos dentro del círculo.
    """

    dentro = 0
    total_generados = 0

    inicio = time.perf_counter()

    while dentro < K:

        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)

        total_generados += 1

        if x * x + y * y < 0.5 * 0.5:
            dentro += 1

    pi_estimado = 4 * (K / total_generados)

    tiempo = time.perf_counter() - inicio
    error = abs(PI_REAL - pi_estimado)

    return {
        "K": K,
        "puntos_generados": total_generados,
        "pi": pi_estimado,
        "error": error,
        "tiempo": tiempo
    }


# --------------------------------------------------
# 3. COMPARACIÓN
# --------------------------------------------------
def comparar():

    valores_N = [1000, 10000, 100000]
    valores_K = [1000, 10000, 100000]

    print("\n========== MONTE CARLO ==========")

    for N in valores_N:
        r = monte_carlo_pi(N)

        print(
            f"N={r['N']:>8} | "
            f"PI={r['pi']:.6f} | "
            f"Error={r['error']:.6f} | "
            f"Tiempo={r['tiempo']:.6f}s"
        )

    print("\n========== LAS VEGAS ==========")

    for K in valores_K:
        r = las_vegas_pi(K)

        print(
            f"K={r['K']:>8} | "
            f"Generados={r['puntos_generados']:>8} | "
            f"PI={r['pi']:.6f} | "
            f"Error={r['error']:.6f} | "
            f"Tiempo={r['tiempo']:.6f}s"
        )


if __name__ == "__main__":
    comparar()