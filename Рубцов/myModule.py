def sosedi_chek(i: int, j: int, list1: list):
    # место для описания

    x = len(list1[0]) - 1
    if i == 0:
        if j == 0:  # угол1
            summa = sum((list1[x][x][0], list1[x][j][0],
                         list1[x][j + 1][0], list1[i][x][0], list1[i][j + 1][0],
                         list1[i + 1][x][0], list1[i + 1][j][0], list1[i + 1][j + 1][0]))
        elif j == x:  # угол 2
            summa = sum((list1[x][j - 1][0], list1[x][j][0], list1[0][x][0],
                         list1[i][j - 1][0], list1[0][0][0], list1[i + 1][j - 1][0], list1[i + 1][j][0],
                         list1[i + 1][0][0]))
        elif j != 0 and j != x:  # сторона при i=0
            summa = sum((list1[x][j - 1][0], list1[x][j][0], list1[x][j + 1][0],
                         list1[i][j - 1][0], list1[i][j + 1][0],
                         list1[i + 1][j - 1][0], list1[i + 1][j][0], list1[i + 1][j + 1][0]))
    elif i == x:
        if j == 0:  # угол 3
            summa = sum((list1[i - 1][x][0], list1[i - 1][j][0], list1[i - 1][j + 1][0],
                         list1[i][x][0], list1[i][j + 1][0], list1[0][x][0],
                         list1[0][j][0], list1[0][j + 1][0]))
        elif j == x:  # угол 4
            summa = sum((list1[i - 1][j - 1][0], list1[i - 1][j][0], list1[i - 1][0][0],
                         list1[i][j - 1][0], list1[i][0][0],
                         list1[0][j - 1][0], list1[0][j][0], list1[0][0][0]))
        elif j != 0 and j != x:  # сторона при i=x
            summa = sum((list1[i - 1][j - 1][0], list1[i - 1][j][0], list1[i - 1][j + 1][0],
                         list1[i][j - 1][0], list1[i][j + 1][0],
                         list1[0][j - 1][0], list1[0][j][0], list1[0][j + 1][0]))
    elif i != 0 and i != x:
        if j == 0:  # строна при j=0
            summa = sum((list1[i - 1][x][0], list1[i - 1][j][0], list1[i - 1][j + 1][0],
                         list1[i][x][0], list1[i][j + 1][0],
                         list1[i + 1][x][0], list1[i + 1][j][0], list1[i + 1][j + 1][0]))
        elif j == x:  # сторона при j=x
            summa = sum((list1[i - 1][j - 1][0], list1[i - 1][j][0], list1[i - 1][0][0],
                         list1[i][j - 1][0], list1[i][0][0],
                         list1[i + 1][j - 1][0], list1[i + 1][j][0], list1[i + 1][0][0]))
        else:
            summa = sum((list1[i - 1][j - 1][0], list1[i - 1][j][0], list1[i - 1][j + 1][0],
                         list1[i][j - 1][0], list1[i][j + 1][0],
                         list1[i + 1][j - 1][0], list1[i + 1][j][0], list1[i + 1][j + 1][0]))
    match summa:
        case 0:
            return 0
        case 1:
            return 0
        case 2:
            if list1[i][j][0]:
                return 1
            else:
                return 0
        case 3:
            return 1
        case _:
            return 0


list1 = [[[1], [1], [0], [0], [0], [0], [0], [0]],
         [[1], [1], [0], [0], [0], [0], [0], [0]],
         [[0], [0], [0], [0], [0], [0], [0], [0]],
         [[0], [0], [0], [1], [1], [0], [0], [0]],
         [[0], [0], [1], [1], [0], [0], [0], [0]],
         [[1], [0], [0], [0], [0], [1], [1], [0]],
         [[0], [1], [0], [0], [0], [0], [1], [0]],
         [[0], [1], [1], [0], [0], [0], [1], [0]]]

######трёх-мерный список в трёх-мерный кортеж
for i in range(len(list1)):
    for j in range(len(list1)):
        list1[i][j] = tuple(list1[i][j])
list1 = [tuple(i) for i in list1]
list1 = tuple(list1)
#####

print("list1=", list1)
list2 = list1
print("list2=", list2)

#####трёх-мерный кортеж в трёх-мерный список
list2 = list(list2)
list2 = [list(i) for i in list2]
for i in range(len(list2)):
    for j in range(len(list2)):
        list2[i][j] = list(list2[i][j])
#######

print("list2=", list2)

for i in range(len(list2)):
    for j in range(len(list2)):
        print(f"{i=}", f"{j=}")
        list2[i][j][0] = sosedi_chek(i, j, list1)

# for i in range(len(list1)):
#     print(list1[i])
# print("\n")
# for i in range(len(list2)):
#     print(list2[i])
for i in list1:
    print(i, "\n")
print("\n")
for i in list2:
    print(i, "\n")
