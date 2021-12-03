f = open('data_day1.txt', 'r')
lines = f.readlines()


def increase_depth(liste):
    cpt = 0
    for i in range(len(liste)-1):
        if int(liste[i+1]) > int(liste[i]):
            cpt += 1
    return cpt
