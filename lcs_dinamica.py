def lcs_dinamica(X, Y):

    m = len(X)
    n = len(Y)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i = m
    j = n
    lcs = []

    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    return "".join(reversed(lcs))


if __name__ == "__main__":

    X = "AGGTAB"
    Y = "GXTXAYB"

    resultado = lcs_dinamica(X, Y)

    print("LCS:", resultado)
    print("Longitud:", len(resultado))
