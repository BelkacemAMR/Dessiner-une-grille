def draw_n_squares(n):
    if n % 2 == 1:
        v = n * 2 + 1
        h = v + (n * 2)

    result = ""

    for i in range(v):
        if i % 2 == 0:
            for j in range(h):
                if j % 4 == 0:
                    result += "+"
                else:
                    result += "-"
        else:
            for j in range(h):
                if j % 4 == 0:
                    result += "|"
                else:
                    result += " "

        result += "\n"

    return result

# On teste le programme :

print(draw_n_squares(1))

print(draw_n_squares(3))