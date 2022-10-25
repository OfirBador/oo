from tkinter import *

root = Tk()
root.title("unknown")
root.geometry("500x500")

w=500
h=500
x=w//2
y=h//2


#create rectangle (root,  x           y             color)
my_canvas = Canvas(root, width=500, height=500, bg="white")

my_canvas.pack(pady=0)
# Create line________(x1, y1, x2, y2, fill="color")
my_canvas.create_line(0, 0, 500, 500, fill="red")

# Create rectangle________(x1, y1, x2, y2, fill="color")
#Rectangle x1,y1: Top Left
#Rectangle x2,y2: Bottom Right
my_canvas.create_rectangle(50, 450, 450, 50, fill="blue")

# Create Oval
# Oval x1,y1:
y = my_canvas.create_oval(60, 100, 110, 50, fill="yellow")


root.mainloop()



def main():
    print("gg")


if __name__ == '__main__':
    main()