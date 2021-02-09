import time

taulukko = [[0, 1, 1, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0a
            [1, 0, 0, 12, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1b
            [1, 0, 0, 0, 0, 8, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0],  # 2c
            [22, 12, 0, 0, 0, 0, 0, 0, 7, 4, 0, 0, 6, 0, 0, 0],  # 3d
            [0, 10, 0, 0, 0, 0, 15, 0, 20, 0, 0, 0, 0, 0, 0, 0],  # 4e
            [0, 0, 8, 0, 0, 0, 0, 15, 0, 20, 0, 0, 0, 0, 0, 0],  # 5f
            [0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0],  # 6g
            [0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0],  # 7h
            [0, 0, 0, 7, 20, 0, 0, 0, 0, 0, 15, 0, 6, 0, 0, 0], # 8i
            [0, 0, 10, 4, 0, 20, 0, 0, 0, 0, 0, 18, 9, 0, 0, 0], # 9j
            [0, 0, 0, 0, 0, 0, 9, 0, 15, 0, 0, 0, 0, 13, 0, 0], # 10k
            [0, 0, 0, 0, 0, 0, 0, 10, 0, 18, 0, 0, 0, 0, 12, 0], # 11l
            [0, 0, 0, 6, 0, 0, 0, 0, 6, 9, 0, 0, 0, 28, 0, 13], # 12m
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 28, 0, 0, 12], # 13n
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 5], # 14o
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 5, 0]] # 15p

v = 0

[]
[]
[]
"""
taulukko = [[0, 6, 9, 9, 0, 0, 0],
            [0, 0, 8, 0, 6, 0, 9],
            [0, 0, 0, 0, 6, 7, 0],
            [0, 10, 9, 0, 0, 7, 0],
            [11, 0, 0, 6, 0, 0, 0],
            [10, 6, 0, 5, 5, 0, 8],
            [7, 5, 10, 11, 0, 0, 0]]"""
def Dijk(g, v):
    #y = 0
    known = []
    known_cost = []
    unknown_cost = []
    path = []
    for x in range(len(g)):  # alustetaan muuttujat
        known.append(False)
        unknown_cost.append(2147)  # INF
        known_cost.append(2147)  # INF
        path.append(-1)
    unknown_cost[v] = 0  # alustetaan aloitus node
    while False in known:  # kun tuntemattomia nodeja on listalla "known"
        time.sleep(0.2)
        w = unknown_cost.index(min(unknown_cost))  # w on kevyin tuntematon node
        known_cost[w] = unknown_cost[w]  # node tunnetaan joten lisätään sen paino tunnettuihin
        known[w] = True  # tehdään nodesta tunnettu
        unknown_cost[w] = 2147  # node tunnetaan joten poistetaan se listalta unknown_node #inf
        print(w)
        for x in range(len(g)):  # käydään kaikki nodet läpi
           # print(g[w][x])
           # print(known_cost[w] + g[w][x]) w = 0 x = 1
            if g[w][x] != 0:  # Käydään vain ne nodet läpi joihin meillä on reitti nykyisestä nodesta
                if known_cost[x] > g[w][x] + known_cost[w] and known[x] is True: #jos tiedetyn noden reitti nykyisestä nodesta ja noden paino ovat kevyempiä kuin jo tiedetty paino
                    #print(known_cost[w] + g[w][x])
                    known_cost[x] = g[w][x] + known_cost[w] #asetetaan kevyin paino matkalle
                    path[x] = w #mistä nodesta tultu
                elif g[w][x] + known_cost[w] < unknown_cost[x] and known[x] is False: #jos ei tiedetyn noden paino ja reitti uuteen nodeen on kevyempi kuin jo tiedetty reitin paino.
                    unknown_cost[x] = g[w][x] + known_cost[w] #asetetaan paino tuntemattomalle nodelle johon tiedetään matka
                    path[x] = w #mistä nodesta tultu
        print(known_cost, path)
        #y = y +1
    return known_cost
        #print(w)

Dijk(taulukko, v)
input("paina entteriä poistuaksesi")

