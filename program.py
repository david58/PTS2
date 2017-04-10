from random import randint
import sys


def vypíš(gs):
    print('Hráč číslo 1: ',gs[0])
    print('Hráč číslo 2: ',gs[1])
    print('Hráč číslo 4: ',gs[2])
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

# REVIEW
# -doprogramovanie funkcionality
#   treba doprogramovat vyhadzovanie panacikov (bolo povedane na prednaske),
# teda aby nemohli stat na jednom policku dvaja panacikovia (netreba dorabat
# domcek, staci aby sa vyhodeny panacik presunie na jeho zaciatocne policko
#
# -zacinajuci hrac
#   nedava zmysel aby zacinajuci hrac bol prave hrac 2, bud by mal zacinat
# hrac 1, alebo by malo byt nahodne urcene, ktory hrac zacina
#
# -treba opravit chyby v README subore (aj ked tam boli napisane v zadani)
#
# -nie je podla pep8
#    program.py:5:8: E999 SyntaxError: invalid syntax
#    program.py:6:31: E231 missing whitespace after ','
#    program.py:7:31: E231 missing whitespace after ','
#    program.py:8:31: E231 missing whitespace after ','
#    program.py:9:31: E231 missing whitespace after ','
#    program.py:13:80: E501 line too long (115 > 79 characters)
#    program.py:25:29: E231 missing whitespace after ','
#    program.py:25:47: E231 missing whitespace after ','rom random import randint
import sys


def vypíš(gs):
    print('Hráč číslo 1: ',gs[0])
    print('Hráč číslo 2: ',gs[1])
    print('Hráč číslo 4: ',gs[2])
    print('Hráč číslo 4: ',gs[3])


def update_gs(gs, hod, hrac, figurka):
    gs = gs[:hrac] + (gs[hrac][:figurka] + ((gs[hrac][figurka] + hod) % 40,) + gs[hrac][figurka+1:],) + gs[hrac+1:]
    print(id(gs[1]))
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
    print(id(stav_hry[1]));
    stav_hry = update_gs(stav_hry, kocka, int(hrac), prikaz)

# REVIEW
# -doprogramovanie funkcionality
#   treba doprogramovat vyhadzovanie panacikov (bolo povedane na prednaske),
# teda aby nemohli stat na jednom policku dvaja panacikovia (netreba dorabat
# domcek, staci aby sa vyhodeny panacik presunie na jeho zaciatocne policko
#
# -zacinajuci hrac
#   nedava zmysel aby zacinajuci hrac bol prave hrac 2, bud by mal zacinat
# hrac 1, alebo by malo byt nahodne urcene, ktory hrac zacina
#
# -nie je podla pep8
#    program.py:5:8: E999 SyntaxError: invalid syntax
#    program.py:6:31: E231 missing whitespace after ','
#    program.py:7:31: E231 missing whitespace after ','
#    program.py:8:31: E231 missing whitespace after ','
#    program.py:9:31: E231 missing whitespace after ','
#    program.py:13:80: E501 line too long (115 > 79 characters)
#    program.py:25:29: E231 missing whitespace after ','
#    program.py:25:47: E231 missing whitespace after ','
