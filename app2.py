from speechtotext import *
from spreadsheet import *

#spreadsheet ---->  https://docs.google.com/spreadsheets/d/1B8Uq14UWNG15-rhGtnaUTkaelHqlJOf6aoKGTvFcSoY/edit#gid=1671752174

def add():
    data = transcribe(sound)
    udata = []
    cost = []

    udata = data.split(' ')
    for element in udata:
        if element in ['Automobilis','automobilis']:
            udata.remove(element)
            row = 'C'
            row2 = 'D'
        if element.isdigit():
            cost.append(element)
            udata.remove(element)
            udata[1 : 3] = [' '.join(udata[1 : 3])]

    for element in udata:
        if element in ['Maistas','maistas']:
            udata.remove(element)
            row = 'A'
            row2 = 'B'
        if element.isdigit():
            cost.append(element)
            udata.remove(element)
            udata[1: 3] = [' '.join(udata[1: 3])]

    for element in udata:
        if element in ['Mokesčiai','mokesčiai']:
            udata.remove(element)
            row = 'E'
            row2 = 'F'
        if element.isdigit():
            cost.append(element)
            udata.remove(element)
            udata[1: 3] = [' '.join(udata[1: 3])]

    for element in udata:
        if element in ['Rūbai','rūbai']:
            udata.remove(element)
            row = 'G'
            row2 = 'H'
        if element.isdigit():
            cost.append(element)
            udata.remove(element)
            udata[1: 3] = [' '.join(udata[1: 3])]

    empty = check_sheet(row)
    insert(row, row2, empty+1, cost, udata)

