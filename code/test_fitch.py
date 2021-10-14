# if "ерунда" and "ппп" in list:
#     print("прошло через if")


# while True:
#     list = input("введите 3 числа: ").split()
#     if len(list) == 3:
#         try:
#             a, b, c = map(int, list)
#             break
#         except ValueError:
#             print("вы ввели не целые числа\n")
#     else:
#         print("не правильная длина\n")

# while True:
#     list = input("введите три числа: ").split()
#     match list:
#         case a, b, c:
#             try:
#                 a, b, c = map(abs, map(int, list))
#                 break
#             except ValueError:
#                 print("вы ввели не целые числа")
#         case a, b:
#             a, b = list
#             print("вы ввели два числа!!!")
#             # exit()
#         case "ерунда" | "fff",:
#             print("эта фраза прошла шаблон!!!")
#             # exit()
#         case "9" | "0",:
#             print("работает or")
#         case a,:
#             print("вы вели одно значение")
#         case _:
#             print("не правильный параметры ввода")
#             # exit()

# print(f"{a=},{b=},{c=}")
a = [list(i) for i in "ijsi sfsef sfasf asefa".split() if i[0] == "s"]
print(a)

a = ("asdad", "afaafe", "sgsg", "sstjyj")
# a = [12, 34, 463, 785, 45, 34, 7, 334, 8, 9]
# a = list(filter(lambda x: x >= 300, a))
# a.sort(reverse=True)
a = list(filter(lambda x: x[0] == "a", a))
print(a)

# "тернарный оператор"
a = 0
c = 12 if a > 0 else 13
print(c)
###
