# David Raby-Pepin (p0918119)

# Description: Algorithme qui resout le probleme Pano (i.e. construire un panorama minimal pour un ensemble de blocs
# donnes) en un temps qui n'appartient pas a Omega(n2)

import math

# fonction qui construit un panorama minimal pour un ensemble de blocs donnes
def panorama(ensemble):

    # si l'ensemble est de taille 1, il est necessairement trie, le retourner en tant que liste
    if len(ensemble) <= 1:
        listeTriee = []

        for e in ensemble:
            listeTriee.append(e)

        return listeTriee

    # sinon, diviser l'ensemble en 2 parties de longueurs presques egales et retourner la combinaison de l'appel de la
    # fonction panorama effectue sur les 2 parties
    else:
        milieu = math.floor(len(ensemble) / 2)
        sousEns1 = ensemble.copy()
        sousEns2 = set()

        for i in range(milieu):
            sousEns2.add(sousEns1.pop())

        return combiner(panorama(sousEns1), (panorama(sousEns2)))


# fonction qui combine 2 panoramas en un seul qui respecte tous les blocs
def combiner(pano1, pano2):

    # initialiser les iterateurs qui traversent les 2 panoramas, la valeur minimal de depart et les constructeurs
    # de blocs du nouveau panorama
    i = 0
    j = 0

    minActuel = min(pano1[0][0], pano2[0][0])
    minProchain = 0
    panoCombines = []

    blocActuel = None
    blocPrecendent = None

    # traverser entierement les 2 panoramas
    while (i <= len(pano1) or j <= len(pano2)):

        # si un des panoramas est traverse, lui assigner un bloc de valeur (infini, 0, infini)
        # sinon, enregistrer les valeurs (x, h, xProchain) du bloc actuel en lecture
        if i >= len(pano1):
            x1 = float("inf")
            h1 = 0
            x1Prochain = float("inf")
        else:
            x1 = pano1[i][0]
            h1 = pano1[i][1]
            x1Prochain = pano1[i][2]

        if j >= len(pano2):
            x2 = float("inf")
            h2= 0
            x2Prochain = float("inf")
        else:
            x2 = pano2[j][0]
            h2 = pano2[j][1]
            x2Prochain = pano2[j][2]

        # trier les valeurs rattachees aux 2 blocs en lecture
        ordre = [x1, x1Prochain, x2, x2Prochain]
        ordre.sort()

        # trouver la seconde valeur minimale
        for k in ordre:
            if k > minActuel:
                minProchain = k
                break

        # selon la position relative des 2 blocs en lecture, determiner la valeur du h appropriee pour le bloc
        # combine en construction
        if x1 < minProchain and x2 < minProchain:
            h = max(h1, h2)
        elif x1 >= minProchain and x2 >= minProchain:
            h = 0
        elif x1 < minProchain:
            h = h1
        else:
            h = h2

        # construire le bloc combine
        blocPrecendent = blocActuel
        blocActuel = (minActuel, h, minProchain)

        # passer a la prochaine valeur minimale
        minActuel = minProchain

        # si necessaire, lire le prochain bloc dans les panoramas 1 ou 2
        if x1Prochain <= minActuel:
            i += 1
        if x2Prochain <= minActuel:
            j += 1

        # si le bloc precedent et le bloc courant ont la meme valeur pour h, les combiner en un seul bloc
        # sinon, ajouter le bloc en construction au panorama combine
        if (blocPrecendent != None and blocPrecendent[1] == blocActuel[1]):
            blocActuel = (blocPrecendent[0], blocPrecendent[1], blocActuel[2])
        else:
            panoCombines.append(blocPrecendent)

    panoCombines.remove(None)
    return panoCombines


E = {(8, 3, 16), (2, 3, 6), (8, 5, 11), (25, 2, 125), (14, 3, 18), (7, 6, 10), (14, 1, 30)}
print(panorama(E))
