def trova_parola(file, parola):
    with open (file, "r") as f:
        testo= f.readlines()
    d_c = {i + 1: j for i, j in enumerate(testo)}
    d_parola = {}
    for k, v in d_c.items():
        c = 0
        for el in v.split():
            if el == parola:
                c += 1
        d_parola[k] = c
    return (d_parola)

print(trova_parola("Manzoni.txt", "ma"))
