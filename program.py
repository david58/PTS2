from random import randint
import sys


def vypíš(gs):
    print('Hráč číslo 1: ', gs[0])
    print('Hráč číslo 2: ', gs[1])
    print('Hráč číslo 3: ', gs[2])
    print('Hráč číslo 4: ', gs[3])


def vyhod(gs, hrac, figurka):
    nova_pozicia = hrac * 10 + figurka
    gs = gs[:hrac]\
        + (gs[hrac][:figurka] + (nova_pozicia,) + gs[hrac][figurka+1:],)\
        + gs[hrac+1:]
    return gs


def update_gs(gs, hod, hrac, figurka):
    nova_pozicia = (gs[hrac][figurka] + hod) % 40
    for i in range(4):
        for j in range(4):
            if gs[i][j] == nova_pozicia and gs[i][j] != 10 * i + j:
                gs = vyhod(gs, i, j)
    gs = gs[:hrac]\
        + (gs[hrac][:figurka] + (nova_pozicia,) + gs[hrac][figurka+1:],)\
        + gs[hrac+1:]
    return gs


stav_hry = ((0, 1, 2, 3), (10, 11, 12, 13), (20, 21, 22, 23), (30, 31, 32, 33))
hrac_na_tahu = 0
print('zadaj -1 pre ukončenie')
while 1:
    vypíš(stav_hry)
    hrac_na_tahu += 1
    hrac_na_tahu %= 4
    kocka = 0
    while kocka<1 or kocka>6:
        print('zadaj číslo na kocke:')
#       kocka = randint(1, 6)
        kocka = int(input())
        if kocka<1 or kocka>6:
            print('nesprávne číslo, ešte raz')
    print('hráč číslo: ', hrac_na_tahu+1, 'kocka: ', kocka)
    prikaz=-3
    while prikaz<-2 or prikaz>3:
        print('zadaj číslo panáčika (1-4):')
        prikaz = int(input())-1
        if prikaz == -2:
            sys.exit()
        if prikaz<-2 or prikaz>3:
            print('nesprávne číslo, ešte raz')

    stav_hry = update_gs(stav_hry, kocka, int(hrac_na_tahu), prikaz)
