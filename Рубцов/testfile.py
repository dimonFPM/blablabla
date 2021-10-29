import time
import tkinter as tk
from loguru import logger
import tkinter.messagebox as mbox
import random

logger.info("начало программы")
now_list = None  # глобальная переменная


def paint_grid(canvas: tk.Canvas, width_win: int, size: int):
    # описание
    logger.info("вызвана функция paint_grid")
    if size > 0:  # проверка на ноль, size не может быть равным нулю
        shag = (width_win - width_win * 0.07) / size
        canvas.delete("line")
        canvas.delete("circle")
        for i in range(size - 1):  # от 0 до size-1 последняя линия это стороны квадрата они уже нарисованны
            canvas.create_line(0 + width_win * 0.003 + shag * (i + 1),
                               0 + width_win * 0.003,  # 2
                               0 + width_win * 0.003 + shag * (i + 1),
                               width_win - width_win * 0.069, tag="line")
        for i in range(size - 1):
            canvas.create_line(0 + width_win * 0.003,
                               0 + width_win * 0.003 + shag * (i + 1),
                               width_win - width_win * 0.069,
                               0 + width_win * 0.003 + shag * (i + 1), tag="line")
    else:
        mbox.showerror("Ошибка", "Размерность поля меньше 1")
        logger.error("Размерность поля не может быть меньше 1")


def paint_canvas(root: tk.Tk, width_win: int) -> tk.Canvas:
    # Отрисовка поля в процентах.Функция отрисовывает поле в процентах от разрешения экрана.
    # На вход подаётся экземпляр класса Tk.
    # Функция возвращает экземпляр класса Canvas.
    logger.info("вызвана функция paint_canvas")
    canvas_for_field = tk.Canvas(root, width=width_win - width_win * 0.07, height=width_win - width_win * 0.07,
                                 bg="white")
    canvas_for_field.pack(side=tk.LEFT, padx=width_win * 0.015, pady=width_win * 0.015)
    canvas_for_field.create_rectangle(0 + width_win * 0.003,
                                      0 + width_win * 0.003,
                                      width_win - width_win * 0.069,
                                      width_win - width_win * 0.069,
                                      outline='black')
    return canvas_for_field


def paint_circle(canvas: tk.Canvas, circle_tuple: tuple):
    # Отрисовка кругов всего массива. Отрисовывает круги на Canvas согласно списку.
    # На вход получает экземляр класса  Canvas и список, элементы которого требуется отрисовать. Ничего не воозвращает.
    logger.info("вызвана функция paint_circle")
    canvas.delete("circle")
    shag = (width_win - width_win * 0.07) / int(size.get())  #######################передать ширину и размер
    for i in range(1, len(circle_tuple) - 1):
        for j in range(1, len(circle_tuple) - 1):
            if circle_tuple[i][j][0] == 1:
                canvas.create_oval(shag * (j - 1) + width_win * 0.0065,
                                   shag * (i - 1) + width_win * 0.0065,
                                   shag * (j - 1) + shag,
                                   shag * (i - 1) + shag,
                                   fill="red",
                                   tag="circle")


def list_generation(e_size: tk.Entry, procent_zapolnenia=50, test=0) -> tuple:
    logger.info(f"Вызвана функция list_generation (size={int(e_size.get())}, {procent_zapolnenia=}%)")
    match test:
        case 0:
            if e_size["fg"] == "black":
                size = int(e_size.get())
                count_element = size * size
                logger.info(f"Количество клеток у поля={count_element}")
                now_list = [[[0, True] for j in range(size + 2)] for i in range(size + 2)]
                ####заполенение случайных полей
                logger.info(f"Количество заполняемых клеток={round(count_element * (procent_zapolnenia / 100))}")
                k = 0
                while k < round(count_element * (procent_zapolnenia / 100)):
                    logger.info(f"{k=}")
                    i = random.randint(1, len(now_list) - 2)
                    j = random.randint(1, len(now_list) - 2)
                    logger.info(f"{i=} {j=}")
                    if now_list[i][j][0] == 0:
                        now_list[i][j][0] = 1
                        k += 1
                ####
                for j in range(1, len(now_list) - 1):
                    now_list[0][j] = now_list[len(now_list) - 2][j]
                    now_list[len(now_list) - 1][j] = now_list[1][j]

                for i in range(0, len(now_list)):
                    now_list[i][0] = now_list[i][len(now_list) - 2]
                    now_list[i][len(now_list) - 1] = now_list[i][1]

                for i in range(len(now_list)):
                    for j in range(len(now_list)):
                        now_list[i][j] = tuple(now_list[i][j])  # добавить вложенный список
                    now_list[i] = tuple(now_list[i])
                now_list = tuple(now_list)
                logger.info(f"Сгенерированный список:")
                for i in range(len(now_list)):
                    logger.info(now_list[i])
                paint_circle(canvas, now_list)
                return now_list
            else:
                mbox.showerror("Ошибка", "Размерность поля не целое число")
                logger.error("Размерность поля не целое число")
        case 1:
            logger.info(f"Запущен тестовый вариант номер {test}")
            now_list = (((1,), (1,), (1,), (0,), (1,), (1,)),
                        ((1,), (0,), (1,), (1,), (1,), (0,)),
                        ((0,), (0,), (1,), (0,), (0,), (0,)),
                        ((1,), (0,), (0,), (0,), (1,), (0,)),
                        ((1,), (1,), (1,), (0,), (1,), (1,)),
                        ((1,), (0,), (1,), (1,), (1,), (0,)))
            paint_circle(canvas, now_list)
            logger.info(f"сгенерированный список")
            for i in range(len(now_list)):
                logger.info(now_list[i])
            return now_list


def generate_button(e_size: tk.Entry, e_procent_zapolnenia: tk.Entry):
    # if e_size["fg"] == "red" or e_procent_zapolnenia["fg"] == "red":
    #     logger.error("Процент заполнения или размерность поля заданы не правильно")
    #     mbox.showerror("Ошибка", "Процент заполнения или размерность поля заданы не правильно")
    #

    global now_list
    now_list = list_generation(e_size)


def sosedi_chek(i: int, j: int, list1: list) -> int:
    # место для описания
    logger.info("Вызвана функция sosedi_chek")
    # x = len(list1[0]) - 1

    summa = sum((list1[i - 1][j - 1][0], list1[i - 1][j][0], list1[i - 1][j + 1][0],
                 list1[i][j - 1][0], list1[i][j + 1][0],
                 list1[i + 1][j - 1][0], list1[i + 1][j][0], list1[i + 1][j + 1][0]))
    print(*((list1[i - 1][j - 1][0], list1[i - 1][j][0], list1[i - 1][j + 1][0], "\n",
             list1[i][j - 1][0], list1[i][j + 1][0], "\n",
             list1[i + 1][j - 1][0], list1[i + 1][j][0], list1[i + 1][j + 1][0])))
    logger.info(f"{summa=}")
    print("\n")
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


def check_nomer_age(*args):
    logger.info("Вызвана функция check_nomer_age")
    nomer_age = e_nomer_age.get()
    if nomer_age != "":
        if nomer_age.isnumeric():
            if int(nomer_age) > 0:
                nomer_age = int(nomer_age)
                e_nomer_age.config(fg='black')
                logger.info(f"nomer_age={int(e_nomer_age.get())}")
            else:
                e_nomer_age.config(fg='red')
                logger.info("e_nomer_age=0")
        else:
            e_nomer_age.config(fg='red')
            logger.info("e_nomer_age либо отрицательное либо текстовое значение")
    else:
        logger.info("e_nomer_age пустое поле")
        e_nomer_age.config(fg='red')


def check_size(*args):
    logger.info("Вызвана функция check_size")
    if e_size.get() != "":
        if e_size.get().isnumeric():
            if int(e_size.get()) > 0:
                size = int(e_size.get())
                e_size.config(fg='black')
                logger.info(f"size={int(e_size.get())}")
                paint_grid(canvas, width_win, size)  # попробовать передать через необязательные аргументы функции
                #######
                global now_list
                now_list = list_generation(e_size)

                #######
            else:
                e_size.config(fg='red')
                logger.info("e_size=0")
        else:
            e_size.config(fg='red')
            logger.info("e_size либо отрицательное либо текстовое значение")
    else:
        logger.info("e_size пустое поле")
        e_size.config(fg='red')


def check_procent_zapolnenia(*args):
    logger.info("Вызвана функция check_procent_zapolnenia")
    if e_procent_zapolnenia.get() != "":
        if e_procent_zapolnenia.get().isnumeric():
            if int(e_procent_zapolnenia.get()) > 0 and int(e_procent_zapolnenia.get()) < 100:
                e_procent_zapolnenia.config(fg='black')
                logger.info(f"procent_zapolnenia={int(e_procent_zapolnenia.get())}")
            else:
                e_procent_zapolnenia.config(fg='red')
                logger.info("e_procent_zapolnenia=0 или 100 и более")
        else:
            e_procent_zapolnenia.config(fg='red')
            logger.info("e_procent_zapolnenia либо отрицательное либо текстовое значение")
    else:
        logger.info("e_procent_zapolnenia пустое поле")
        e_procent_zapolnenia.config(fg='red')


@logger.catch()
def action(now_list: tuple, e_nomer_age: tk.Entry, e_size: tk.Entry):
    logger.info("Вызвана функция action")
    if e_nomer_age["fg"] == "red":
        logger.info("Номер поколения должен быть целым не отрицатьельным числом")
        mbox.showerror("Ошибка", "Номер поколения должен быть целым не отрицательным числом")
        # pass
    elif e_size["fg"] == "red":
        logger.info("Размерност поля должна быть целым положительным числом больше 0")
        mbox.showerror("Ошибка", "Размерность поля должна быть целым положительным числом")
        # pass
    elif e_procent_zapolnenia["fg"] == "red":
        logger.info("Процент заполнения <0 или >=100")
        mbox.showerror("Ошибка", "Процент заполнения меньше нуля или больше или равен ста")
        # pass
    else:
        future_list = now_list
        future_list = list(future_list)
        for i in range(len(future_list)):
            future_list[i] = list(future_list[i])
            for j in range(len(future_list)):
                future_list[i][j] = list(future_list[i][j])
        logger.info(future_list)  # future_list - список
        # logger.info(f"{type(future_list)=}")
        k = 0
        l_age.config(text=f"{k}")  # надо бы передать в функцию объект класса Label
        logger.info(f"{len(now_list)=} {len(future_list)=}")
        while True:
            logger.info(f"{k=}")
            for i in range(1, len(now_list) - 1):
                for j in range(1, len(now_list) - 1):
                    logger.info(f"{i=} {j=}")
                    future_list[i][j][0] = sosedi_chek(i, j, now_list)

            k += 1
            # if now_list == future_list:#############################################   не сработает так как один элемент массив, а другой кортеж
            #     logger.info("конфигурации совпали, изменений больше небудет")
            #     break
            # заполнение внешних границ
            for j in range(1, len(future_list) - 1):
                future_list[0][j] = future_list[len(future_list) - 2][j]
                future_list[len(future_list) - 1][j] = future_list[1][j]

            for i in range(0, len(future_list)):
                future_list[i][0] = future_list[i][len(future_list) - 2]
                future_list[i][len(future_list) - 1] = future_list[i][1]
            #######

            l_age.config(text=f"{k}")  # надо бы передать в функцию объект класса Label
            paint_circle(canvas, tuple(future_list))
            canvas.update()
            time.sleep(0.2)

            if k == int(e_nomer_age.get()):
                logger.info("финальное k={}".format(k))
                break

            # кортеж в список
            now_list = list(now_list)
            for i in range(len(now_list)):
                now_list[i] = list(now_list[i])
                for j in range(len(now_list)):
                    now_list[i][j] = list(now_list[i][j])

            now_list = future_list
            ####

            # список в кортеж
            for i in range(len(now_list)):
                for j in range(len(now_list)):
                    now_list[i][j] = tuple(now_list[i][j])
                now_list[i] = tuple(now_list[i])
            now_list = tuple(now_list)

            for i in range(len(future_list)):
                future_list[i] = list(future_list[i])
                for j in range(len(future_list)):
                    future_list[i][j] = list(future_list[i][j])

            logger.info(f"{len(now_list)=}\n{len(future_list)=}")
            logger.info(f"{future_list=}")
            logger.info(f"{now_list=}")
            #####


# region установка параметров окна приложения
logger.add("log_life.log", level="DEBUG", format="{time} {level} {message}", compression="zip", rotation="10 MB")
# logger.remove()
root = tk.Tk()
root.title("стартовое окно testfile")
width_win, height_win = map(int, (root.winfo_screenwidth() * 0.5,
                                  root.winfo_screenheight() * 0.5))  # задание размеров окна приложения
root.geometry(f"{int(width_win * 1.5)}x{width_win}+0+0")
root.resizable(False, False)
# endregion


# region Canvas и  Frame
canvas = paint_canvas(root, width_win)
fr = tk.Frame(root)
# endregion

# region Button
b_action = tk.Button(fr, text="Поехали", command=lambda: action(now_list, e_nomer_age, e_size),
                     width=int(width_win * 0.03125))
b_cancel = tk.Button(fr, text="Отмена", width=int(width_win * 0.03125))
b_start_config = tk.Button(fr, text="Начальное состояние", width=int(width_win * 0.03125),
                           command=lambda: paint_circle(canvas, now_list))
b_generation = tk.Button(fr, text="Генерация\nначального состояния", width=int(width_win * 0.03125),
                         command=lambda: generate_button(e_size,e_procent_zapolnenia))
# endregion

# region Label
l_size = tk.Label(fr, text="Размерность поля:", width=int(width_win * 0.03125))
l_nomer_age = tk.Label(fr, text="Номер поколения", width=int(width_win * 0.03125))
l_age = tk.Label(fr, text="0", width=int(width_win * 0.01156), bg="gray", height=int(width_win * 0.01156), font="16")
l_procent_zapolnenia = tk.Label(fr, text="Процент заполнения поля", width=int(width_win * 0.03125))
# endregion

# region Entry
size = tk.StringVar()
size.trace('w', check_size)
e_size = tk.Entry(fr, justify=tk.CENTER, fg="black", textvariable=size, width=int(width_win * 0.03125))

nomer_age = tk.StringVar()
nomer_age.trace('w', check_nomer_age)
e_nomer_age = tk.Entry(fr, justify=tk.CENTER, fg="black", width=int(width_win * 0.03125), textvariable=nomer_age)

procent_zapolnenia = tk.StringVar()
procent_zapolnenia.trace("w", check_procent_zapolnenia)
e_procent_zapolnenia = tk.Entry(fr, justify=tk.CENTER, fg="black", width=int(width_win * 0.03125),
                                textvariable=procent_zapolnenia)

e_size.insert(0, "4")  #####удалить
e_nomer_age.insert(0, "1")  #####удалить
e_procent_zapolnenia.insert(0, "50")  # удалить

# endregion

# region Pack
fr.pack(side=tk.LEFT)
l_age.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
l_size.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
e_size.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
l_nomer_age.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
e_nomer_age.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
b_action.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
# b_cancel.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
b_start_config.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
b_generation.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
l_procent_zapolnenia.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
e_procent_zapolnenia.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
# endregion


# paint_circle(canvas, now_list)

root.mainloop()
