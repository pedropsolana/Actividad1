def lcs_length(a, b):

    prev = [0] * (len(b) + 1)

    for x in a:

        curr = [0]

        for j, y in enumerate(b):

            if x == y:
                curr.append(prev[j] + 1)
            else:
                curr.append(max(curr[-1], prev[j + 1]))

        prev = curr

    return prev


def hirschberg(a, b):

    if len(a) == 0:
        return ""

    if len(a) == 1:

        if a in b:
            return a

        return ""

    i = len(a) // 2

    score_l = lcs_length(a[:i], b)
    score_r = lcs_length(a[i:][::-1], b[::-1])

    k = max(
        range(len(b) + 1),
        key=lambda j: score_l[j] + score_r[len(b) - j]
    )

    return (
        hirschberg(a[:i], b[:k]) +
        hirschberg(a[i:], b[k:])
    )


if __name__ == "__main__":

    X = "AGGTAB"
    Y = "GXTXAYB"

    resultado = hirschberg(X, Y)

    print("LCS:", resultado)
    print("Longitud:", len(resultado))
