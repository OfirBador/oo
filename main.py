from tkinter import *


def gui():
    root = Tk()
    root.title("unknown")
    root.geometry("1000x1000")

    w = 800
    h = 600
    x = w // 2
    y = h // 2
    i = 0
    press = False
    can = Canvas(root, width=w, height=h, bg='black')
    can.pack()
    # Create line________(x1, y1, x2, y2, fill="color")
    can.create_line(0, 300, 800, 300, fill="red")
    can.create_line(400, 0, 400, 800, fill="red")
    my_circle = can.create_oval(x - 20, y - 20, x + 20, y + 20, outline='red', fill='blue')

    def left(event):
        x = -10
        y = 0
        can.move(my_circle, x, y)

    def right(event):
        x = +10
        y = 0
        can.move(my_circle, x, y)

    def up(event):
        x = 0
        y = -10
        can.move(my_circle, x, y)

    def down(event):
        x = 0
        y = +10
        can.move(my_circle, x, y)

    def button():
        global i
        if i % 2 == 0:
            press = True
        if i % 2 == 1:
            press = False
        i = i + 1

    if press:
        print("true")


    button1 = Button(root, text="Move", bg='white', command=button)
    button1.pack()

    root.bind("<Up>", up)
    root.bind("<Right>", right)
    root.bind("<Left>", left)
    root.bind("<Down>", down)

    root.mainloop()


def main():
    gui()
    print("0")


if __name__ == '__main__':
    main()
