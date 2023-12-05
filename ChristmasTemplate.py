from tkinter import *
from PIL import ImageTk
from random import randint
import time


def hidesnowman():
    myCanvas.delete("snowman")
    if b['state'] == DISABLED:
        b['state'] = NORMAL
        b1['state'] = DISABLED


def snowman():
    # FROSTY THE SNOWMAN
    myCanvas.create_oval(947, 649, 1147, 849, fill="white", outline='white', tag="snowman")
    myCanvas.create_oval(972, 519, 1122, 669, fill="white", outline='white', tag="snowman")
    myCanvas.create_oval(997, 429, 1097, 529, fill="white", outline='white', tag="snowman")
    #  SWANKY TOP HAT
    myCanvas.create_rectangle(1010, 360, 1085, 440, fill='black', outline='black', tag="snowman")
    myCanvas.create_line(970, 440, 1125, 440, fill="black", width=6, tag = "snowman")
    ## PEEPERS
    myCanvas.create_oval(1031, 459, 1041, 469, fill="black", outline='black', tag = "snowman")
    myCanvas.create_oval(1053, 459, 1063, 469, fill="black", outline='black', tag = "snowman")
    ## TASTY NOSE
    myCanvas.create_line(1035, 480, 1140, 460, fill="orange", width=8, tag = "snowman")
    ## CHEESE!!
    myCanvas.create_oval(1020, 494, 1030, 504, fill="black", outline='black', tag = "snowman")
    myCanvas.create_oval(1031, 499, 1041, 509, fill="black", outline='black', tag = "snowman")
    myCanvas.create_oval(1042, 499, 1052, 509, fill="black", outline='black', tag = "snowman")
    myCanvas.create_oval(1053, 499, 1063, 509, fill="black", outline='black', tag = "snowman")
    myCanvas.create_oval(1064, 494, 1074, 504, fill="black", outline='black', tag = "snowman")
    # SCARF
    myCanvas.create_rectangle(1000, 520, 1095, 535, fill='green', outline='pink', tag = "snowman")
    myCanvas.create_rectangle(1070, 520, 1085, 600, fill='green', outline='pink', tag = "snowman")
    # BUTTONS
    myCanvas.create_oval(1042, 559, 1052, 569, fill="black", outline='black', tag = "snowman")
    myCanvas.create_oval(1042, 579, 1052, 589, fill="black", outline='black', tag = "snowman")
    myCanvas.create_oval(1042, 599, 1052, 609, fill="black", outline='black', tag = "snowman")
    #  ARMS
    myCanvas.create_line(1000, 580, 900, 560, fill="brown", width=6, tag = "snowman")
    myCanvas.create_line(1095, 580, 1200, 510, fill="brown", width=6, tag = "snowman")
    if (b['state'] == NORMAL):
        b['state'] = DISABLED
        b1['state'] = NORMAL

def lightsoff():
    if (("red")== "red"):
        myCanvas.itemconfigure("red", fill="grey")
    if (("green")== "green"):
        myCanvas.itemconfigure("green", fill="black")
    if (b2['state'] == NORMAL):
        b2['state'] = DISABLED
        b3['state'] = NORMAL

def lightson():
    if (("red")== "red"):
        myCanvas.itemconfigure("red", fill="red")
    if (("green") == "green"):
        myCanvas.itemconfigure("green", fill="green")
    if (b3['state'] == NORMAL):
        b3['state'] = DISABLED
        b2['state'] = NORMAL


root = Tk()
root.title("Happy Holidays Christmas Card")
root.iconbitmap("santa icon.ico")
width = root.winfo_screenwidth()# this is the width
height = root.winfo_screenheight()
root.resizable(False,False)
myCanvas = Canvas(root, width=width, height=height)
pic = ImageTk.PhotoImage(file= "snowy_backdrop.jpg")
myCanvas.pack(expand = True, fill = BOTH)
myCanvas.create_image(0, 0, image =pic, anchor = 'nw' )
myCanvas.create_text(
    950,120,
    fill="darkblue",
    font="Times 90 italic bold",
    text="Happy \nHolidays")

##  HOUSE BODY, AND ROOF
myCanvas.create_rectangle(280, 300, 360, 550, fill='brown', outline='brown')
myCanvas.create_rectangle(230, 450, 630, 850, fill='yellow', outline='yellow')
myCanvas.create_line(165, 480, 440, 320, fill="brown", width=8)
myCanvas.create_line(720, 510, 440, 320, fill="brown", width=8)
points = [623, 450, 226, 450, 440, 320]
myCanvas.create_polygon(points, outline='brown', fill='brown', width=2)

# TYPICAL CHRISTMAS LIGHTS
myCanvas.create_oval(205, 449, 255, 499, fill="green", outline='green', tag = "green")
myCanvas.create_oval(252, 466, 302, 516, fill="red", outline='red', tag = "red")
myCanvas.create_oval(300, 479, 350, 529, fill="green", outline='green', tag = "green")
myCanvas.create_oval(349, 489, 399, 539, fill="red", outline='red', tag = "red")
myCanvas.create_oval(400, 494, 450, 544, fill="green", outline='green', tag = "green")
myCanvas.create_oval(450, 489, 500, 539, fill="red", outline='red', tag = "red")
myCanvas.create_oval(500, 479, 550, 529, fill="green", outline='green', tag = "green")
myCanvas.create_oval(549, 466, 599, 516, fill="red", outline='red', tag = "red")
myCanvas.create_oval(596, 449, 646, 499, fill="green", outline='green', tag = "green")

## CHARLIE BROWN CHRISTMAS TREE
myCanvas.create_rectangle(1330, 450, 1430, 850, fill='brown', outline='brown')
myCanvas.create_line(1335, 580, 1540, 320, fill="brown", width=12)
myCanvas.create_line(1235, 360, 1340, 640, fill="brown", width=8)
#   CHRISTMAS LIGHTS ON THE CHRISTMAS TREE
myCanvas.create_oval(1205, 349, 1255, 399, fill="green", outline='green', tag = "green")
myCanvas.create_oval(1516, 316, 1566, 366, fill="red", outline='red', tag = "red")
myCanvas.create_oval(1235, 449, 1285, 499, fill="red", outline='red', tag = "red")
myCanvas.create_oval(1436, 416, 1486, 466, fill="green", outline='green', tag = "green")
myCanvas.create_oval(1275, 549, 1325, 599, fill="green", outline='green', tag = "green")
myCanvas.create_oval(1356, 516, 1406, 566, fill="red", outline='red', tag = "red")
myCanvas.create_oval(1356, 451, 1406, 501, fill="green", outline='green', tag = "green")
b = Button(root, text="hello", bg="blue", fg="red", command=snowman)
b.pack()
b.place(x=100, y=110)

b1 = Button(root, text="goodbye", bg="blue", fg="red", command=hidesnowman)
b1.pack()
b1.place(x=100, y=320)

b2 = Button(root, text="lights off", bg="blue", fg="red", command=lightsoff)
b2.pack()
b2.place(x=100, y=520)

b3 = Button(root, text="lights on", bg="blue", fg="red", command=lightson)
b3.pack()
b3.place(x=100, y=620)

Refreshrate = 0.01

snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snowspeed = randint(1, 3)


snow1 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)

snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow2 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)

snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow3 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)

snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow4 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)

snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)


snow5 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)

snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow6 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)

snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow7 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)


snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)


snow8 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)

snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)


snow9 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)


snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow10 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)


snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow11 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)


snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow12 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)


snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow13 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)



snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow14 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)




snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow15 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)



snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow16 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)



snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow17 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)


snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow18 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)



snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow19 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)



snowxpos = randint(0, width)

snowypos = randint(0, int(height / 16))

snowsize = randint(8, 12)

snow20 = myCanvas.create_oval(snowxpos - snowsize,
                            snowypos - snowsize,
                            snowxpos + snowsize,
                            snowypos + snowsize,
                            outline="white", fill="white", width=4)

# SNOW FALLING FUNCTION
while True:
    myCanvas.move(snow1, snowspeed, snowspeed)
    myCanvas.move(snow2, snowspeed, snowspeed)
    myCanvas.move(snow3, snowspeed, snowspeed)
    myCanvas.move(snow4, snowspeed, snowspeed)
    myCanvas.move(snow5, snowspeed, snowspeed)
    myCanvas.move(snow6, snowspeed, snowspeed)
    myCanvas.move(snow7, snowspeed, snowspeed)
    myCanvas.move(snow8, snowspeed, snowspeed)
    myCanvas.move(snow9, snowspeed, snowspeed)
    myCanvas.move(snow10, snowspeed, snowspeed)
    myCanvas.move(snow11, snowspeed, snowspeed)
    myCanvas.move(snow12, snowspeed, snowspeed)
    myCanvas.move(snow13, snowspeed, snowspeed)
    myCanvas.move(snow14, snowspeed, snowspeed)
    myCanvas.move(snow15, snowspeed, snowspeed)
    myCanvas.move(snow16, snowspeed, snowspeed)
    myCanvas.move(snow17, snowspeed, snowspeed)
    myCanvas.move(snow18, snowspeed, snowspeed)
    myCanvas.move(snow19, snowspeed, snowspeed)
    myCanvas.move(snow20, snowspeed, snowspeed)

    root.update()
    time.sleep(Refreshrate)
    snowfall = myCanvas.coords(snow1)


    # unpack array to variables
    al, bl, ar, br = snowfall
    if al < abs(snowspeed) or ar > width - abs(snowspeed):
        snowspeed = -snowspeed
    if bl < abs(snowspeed) or br > height - abs(snowspeed):
        snowspeed = -snowspeed

root.mainloop()
