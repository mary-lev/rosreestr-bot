from collections import namedtuple
import pandas as pd


Region = namedtuple("Region", ["name", "case", "local_case", "filename"])

palkino = Region("палкин", "Палкино", "Палкинском районе", "./data/palkino.csv")
pskov = Region("псков", "Пскову", "Псковском районе", "./data/pskov_new.csv")
bezh = Region("бежаниц", "Бежаницам", "Бежаницком районе", "./data/bezh.csv")
dedovichi = Region("дедович", "Дедовичам", "Дедовичском районе", "./data/dedovichi.csv")
dno = Region("дно", "Дно", "Дновском районе", "./data/dno.csv")
gdov = Region("гдов", "Гдову", "Гдовском районе", "./data/gdov.csv")
krasnogorodsk = Region("красногородск", "Красногородску", "Красногородском районе", "./data/krasnogorodsk.csv")
kun = Region("кун", "Кунье", "Куньинском районе", "./data/kun.csv")
lok = Region("локн", "Локне", "Локнянском районе", "./data/lok.csv")
luki = Region("лук", "ВЛукам", "Великолукском районе", "./data/luki_new.csv")
nevel = Region("невел", "Невелю", "Невельском районе", "./data/nevel.csv")
novorzhev = Region("новоржев", "Новоржеву", "Новоржевском районе", "./data/novorzhev.csv")
novosokolniki = Region("сокол", "Новосокольникам", "Новосокольническом районе", "./data/novosokolniki.csv")
opochka = Region("опоч", "Опочке", "Опочецком районе", "./data/opochka.csv")
ostrov = Region("остров", "Острову", "Островском районе", "./data/ostrov.csv")
pechory = Region("печор", "Печорам", "Печорском районе", "./data/pechory.csv")
plussa = Region("плюс", "Плюссе", "Плюсском районе", "./data/plussa.csv")
porhov = Region("порх", "Порхову", "Порховском районе", "./data/porhov.csv")
pushkin = Region("пушк", "Пушкинским горам", "Пушкиногорском районе", "./data/pushkin.csv")
pustoshka = Region("пустош", "Пустошке", "Пустошкинском районе", "./data/pustoshka.csv")
pytalovo = Region("пыталов", "Пыталово", "Пыталовском районе", "./data/pytalovo.csv")
sebezh = Region("себеж", "Себежу", "Себежском районе", "./data/sebezh.csv")
strugi = Region("струг", "Стругам Красным", "Стругокрасненском районе", "./data/strugi.csv")
usvyaty = Region("усвят", "Усвятам", "Усвятском районе", "./data/usvyaty.csv")

regions = [
    pskov,
    palkino,
    bezh,
    dedovichi,
    dno,
    gdov,
    krasnogorodsk,
    kun,
    lok,
    luki,
    nevel,
    novorzhev,
    novosokolniki,
    opochka,
    ostrov,
    pechory,
    plussa,
    porhov,
    pushkin,
    pustoshka,
    pytalovo,
    sebezh,
    strugi,
    usvyaty,
    ]
