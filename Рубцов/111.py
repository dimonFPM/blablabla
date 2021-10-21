# def paint_canvas(root, size):  # отрисовка поля
#     canvas_for_field = tk.Canvas(root, width=width_win - 49, height=width_win - 49, bg="white")
#     canvas_for_field.pack(side=tk.TOP, padx=10, pady=10)
#     canvas_for_field.create_rectangle(2, 2, width_win - 48, width_win - 48, outline='black')
#     for i in range(size - 1):  # от 0 до size
#         canvas_for_field.create_line(2 + shag * (i + 1), 2, 2 + shag * (i + 1), width_win - 48)
#     for i in range(size - 1):
#         canvas_for_field.create_line(2, 2 + shag * (i + 1), width_win - 48, 2 + shag * (i + 1))
#     return canvas_for_field
#
#
# def paint_circle(canvas, circle_tuple):#отрисовка кругов всего массива
#     canvas.delete("circle")
#     circle_list = list(circle_tuple)
#     for i in range(len(circle_list)):
#         for j in range(len(circle_list)):
#             if circle_list[i][j][0] == 1:
#                 canvas.create_oval(shag * i + 4, shag * j + 4, shag * i + shag, shag * j + shag, fill="red",
#                                    tag="circle")


from tkinter import *


def motion():
    c.move(ball, 1, -1)
    if c.coords(ball)[2] < 300:
        root.after(10, motion)


root = Tk()
c = Canvas(root, width=300, height=200,
           bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140,
                     fill='green')
motion()
root.mainloop()