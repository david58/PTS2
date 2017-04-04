from random import randint
import sys


def vypíš(gs):
    print('Hráč číslo 1: ',gs[0])
    print('Hráč číslo 2: ',gs[1])
    print('Hráč číslo 3: ',gs[2])
    print('Hráč číslo 4: ',gs[3])


def update_gs(gs, hod, hrac, figurka):
    gs = gs[:hrac] + (gs[hrac][:figurka] + ((gs[hrac][figurka] + hod) % 40,) + gs[hrac][figurka+1:],) + gs[hrac+1:]
    return gs


stav_hry = ((0, 1, 2, 3), (10, 11, 12, 13), (20, 21, 22, 23), (30, 31, 32, 33))
hrac = 0
print('zadaj -1 pre ukončenie')
while 1:
    vypíš(stav_hry)
    hrac += 1
    hrac %= 4
    kocka = randint(1, 6)
    print('hráč číslo: ',hrac+1, 'kocka: ',kocka)
    print('zadaj číslo panáčika (1-4):')
    prikaz = int(input())-1
    if prikaz == -2:
        sys.exit()
    stav_hry = update_gs(stav_hry, kocka, int(hrac), prikaz)
