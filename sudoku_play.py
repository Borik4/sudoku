from tabulate import tabulate

sudoku_1 = "add from sudoku.game.py"

for i in sudoku_1:
    if type(i) is list:
        for q in range(1, 10):
            i.append(q)
sudoku = {}
for i in range(1, 82):
    sudoku[i] = sudoku_1[i - 1]


def horizon():
    for i in range(9):
        a = []
        for q in range(9 * i + 1, 9 * (i + 1) + 1):
            a.append(sudoku[q])
        stugum({(i, 'horizon'): a})
        horizon_stugum({i: a})


def uxxadzig():
    for i in range(9):
        a = []
        for q in range(i + 1, 82, 9):
            a.append(sudoku[q])
        stugum({(i, 'uxxadziq'): a})
        uxxadzig_stuguum({i: a})


def kubik():
    for i in range(3):
        for a in range(3):
            rt = []
            for k in range(i * 3 + 1, 3 * (1 + i) + 1):
                for s in range(a * 3 + 1, 3 * (1 + a) + 1):
                    rt.append(sudoku[k + (s - 1) * 9])
            stugum({(i, a): rt})
            kubik_stugum({(i, a): rt})


def stugum(o):
    int_1 = []
    list_1 = []
    q = list(o.values())[0]
    for w in range(len(q)):
        if type(q[w]) is int:
            int_1.append(q[w])
        else:
            list_1.append(q[w])
    for a in int_1:
        for q in list_1:
            if a in q:
                q.pop(q.index(a))


def nshum():
    for i in sudoku:
        if type(sudoku[i]) is list:
            if len(sudoku[i]) == 1:
                sudoku[i] = sudoku[i][0]


def horizon_stugum(l):
    list_1 = []
    tox = list(l.keys())[0]
    s = list(l.values())[0]
    for i in s:
        if type(i) is list:
            list_1.append(i)
    for i in range(len(list_1)):
        for w in list_1[i]:
            y = 0
            for o in list_1:
                if w in o:
                    y += 1
            if y == 1:
                for g in range(tox * 9 + 1, (tox * 9) + 10):
                    if sudoku[g] == list_1[i]:
                        sudoku[g] = w


def uxxadzig_stuguum(l):
    list_1 = []
    tox = list(l.keys())[0]
    s = list(l.values())[0]
    for i in s:
        if type(i) is list:
            list_1.append(i)
    for i in range(len(list_1)):
        for w in list_1[i]:
            y = 0
            for o in list_1:
                if w in o:
                    y += 1
            if y == 1:
                for g in range(tox + 1, 82, 9):
                    if sudoku[g] == list_1[i]:
                        sudoku[g] = w


def kubik_stugum(l):
    list_1 = []
    tox = list(l.keys())[0]
    s = list(l.values())[0]
    for i in s:
        if type(i) is list:
            list_1.append(i)
    for i in range(len(list_1)):
        for w in list_1[i]:
            y = 0
            for o in list_1:
                if w in o:
                    y += 1
            if y == 1:
                ty = []
                a = tox[0]
                b = tox[1]
                for r in range(a * 3 + 1, (a + 1) * 3 + 1):
                    for q in range(b * 3, 3 * b + 3):
                        ty.append(r + q * 9)
                for g in ty:
                    if sudoku[g] == list_1[i]:
                        sudoku[g] = w


for i in range(10):
    kubik()
    horizon()
    uxxadzig()
    nshum()
    print(sudoku)

d = list(sudoku.values())
d_1 = [[], [], [], [], [], [], [], [], [], ]
l = -1
for i in range(len(d)):
    if i % 9 == 0:
        l += 1
    d_1[l].append(d[i])
print(tabulate(d_1))
