# a = {}
# a["name"] = "Dima"
# a["secondName"] = "Snetkov"
# print(a.values())
# f = list(a.items())
# print(f)
# print(type(f))
# q = open("../ttt.txt")
# a = []
# a = list(q.readlines())
# print(a)
# print(type(a))


def a(x: int, list1: list):
    list1 = (0, 0, 0, 0, 0, 0)
    return [i ** 2 for i in list1]


list1 = [1, 2, 3, 4, 5]
rezalt = a(1, list1[:])
print(f"{list1=}\n{rezalt=}")
# print(rezalt)
