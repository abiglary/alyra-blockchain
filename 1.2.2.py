transactions = [
    { "taille": 2000, "pourboire": 13000},
    {"taille": 6000, "pourboire": 9000},
    {"taille": 800,"pourboire": 2000},
    {"taille": 700,"pourboire": 1500},
    {"taille": 1200,"pourboire": 3500},
    {"taille": 1000,"pourboire": 2800},
    {"taille": 1300,"pourboire": 5000},
    {"taille": 600,"pourboire": 1500}
]

def combinliste_k(seq, k):
    p = []
    i, imax = 0, 2 ** len(seq) - 1
    while i <= imax:
        s = []
        j, jmax = 0, len(seq) - 1
        while j <= jmax:
            if (i >> j) & 1 == 1:
                s.append(seq[j])
            j += 1
        if len(s) == k:
            p.append(s)
        i += 1
    return p

def combinliste(seq):
    q = []
    for m in range(1,len(seq)+1):
        q.extend(combinliste_k(seq,m))
    return q

def somme(liste_transactions):
    somme_taille = 0
    somme_pourboire = 0
    for x in liste_transactions:
        somme_taille += x["taille"]
        somme_pourboire += x["pourboire"]
    return { "taille_totale": somme_taille, "pourboire_total": somme_pourboire}

def determine_max(liste_transactions):
    liste_combinaisons = combinliste(liste_transactions)
    liste_combinaisons_sommees = list(map(somme,liste_combinaisons))

    max_pourboire = 0
    index_max = None

    for i in range(0,len(liste_combinaisons_sommees)):
        x = liste_combinaisons_sommees[i]
        if x["taille_totale"] > 6000:
            continue
        else:
            if x["pourboire_total"] > max_pourboire:
                max_pourboire = x["pourboire_total"]
                index_max = i

    return {"taille_du_max":liste_combinaisons_sommees[index_max]["taille_totale"],"max_pourboire":max_pourboire,"index_max":index_max, "meilleure_combi":liste_combinaisons[index_max]}



result = determine_max(transactions)

print("La meilleure combinaison est la suivante:")
for x in result["meilleure_combi"]:
    print(x)

print("Le pourboire total correspondant est:", determine_max(transactions)["max_pourboire"])
print("La taille de cette combinaison est:", determine_max(transactions)["taille_du_max"])
