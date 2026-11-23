def lcs_recursivo(X, Y, m, n):
    if m == 0 or n == 0:
        return ""

    if X[m - 1] == Y[n - 1]:
        return lcs_recursivo(X, Y, m - 1, n - 1) + X[m - 1]

    lcs1 = lcs_recursivo(X, Y, m - 1, n)
    lcs2 = lcs_recursivo(X, Y, m, n - 1)

    return lcs1 if len(lcs1) > len(lcs2) else lcs2


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"

    resultado = lcs_recursivo(X, Y, len(X), len(Y))

    print("LCS:", resultado)
    print("Longitud:", len(resultado))
