import PIL
import pytesseract as tess
from tkinter import*
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import cv2

tess.pytesseract.tesseract_cmd = r'C:\Users\ACER\AppData\Local\Tesseract-OCR\tesseract.exe'

window = tk.Tk()
window.title('Image Assistant with OCR Recognition')#TITLE
window.geometry("900x740")
window.configure(bg="black")



def r(): #THIS FUNCTION RETURNS THE OPENED IMAGE FROM ITS PATH 
    file_path = filedialog.askopenfilenames()
    x = str(file_path)
    string = x.replace("'", "")
    string = string.replace(",", "")
    string = string.replace("(", "", 1)
    string = string[:-1]
    img_path = string
    
    image = Image.open(img_path)
    return image




lbl1 = tk.Label(window, text="Welcome To Image Processing Tool", font=("Franklin Gothic Demi", 25), bg="black", fg="white")#HEADING
lbl1.pack()
lbl2 = tk.Label(window, text ="Choose a command from below:\n\n\n\n\n", font=10, bg="black", fg="white", padx=20)
lbl2.pack()


bg_image = PhotoImage(file ="resized.png")#IMAGE AS A BACKGROUND 
x = Label (image = bg_image,bg="#000000",width=700,height=700)
x.pack()



def func1(): #THIS FUNCTION USED TO RETURN THE RESIZED IMAGE
    img = r()
    window1 = tk.Tk()
    window1.title("Resize Image")
    window1.geometry("500x180")
    window1.configure(bg="black")
    lb1 = tk.Label(window1, text="Enter the Dimensions of both Width and Height:", font=1, bg="black", fg="white")
    lb1.pack()

    alabel = tk.Label(window1, text="Width -", bg="black", fg="white")
    alabel.pack()
    alabel.place(x=100, y=35)
    a1 = tk.Entry(window1,  width=20)
    a1.pack()
    a1.place(x=160, y=35)

    blabel = tk.Label(window1, text="Height -", bg="black", fg="white")
    blabel.pack()
    blabel.place(x=100, y=60)
    b1 = tk.Entry(window1, width=20)
    b1.pack()
    b1.place(x=160, y=60)

    def m1(): #THIS FUNCTION WILL POP A NEW WINDOW TO ENTER THE DIMENSIONS OF IMAGE
        a = int(a1.get())
        b = int(b1.get())
        img_small = img.resize((a, b))
        img_small.save('C:/Users/ACER/Desktop/resized.png')
        lm1 = tk.Label(window1, text="Image is saved at desktop", fg="red")
        lm1.pack()
        lm1.place(x=120, y=120)
        img_small.show()

    bm1 = tk.Button(window1, text="Click on to save the image on desktop", command=m1, background="#3DA8AA") #IMAGE WILL AUTOMATICALLY SAVED IN DESKTOP
    bm1.pack()
    bm1.place(x=90, y=90)


def func2(): #THIS FUNCTIONS IS USED TO RETURN CROPED IMAGE 
    img = r()
    window2 = tk.Tk()
    window2.title("Crop Image")
    window2.geometry("500x250")
    window2.configure(bg="black")
    lb21 = tk.Label(window2, text="Set the points for the cropped image:", font=1, bg="black", fg="white")
    lb21.pack()

    leftlabel = tk.Label(window2, text="Left -", bg="black", fg="white")
    leftlabel.pack()
    leftlabel.place(x=100, y=35)
    left = tk.Entry(window2, width=10)
    left.pack()
    left.place(x=160, y=35)

    toplabel = tk.Label(window2, text="Top -", bg="black", fg="white")
    toplabel.pack()
    toplabel.place(x=100, y=60)
    top = tk.Entry(window2, width=10)
    top.pack()
    top.place(x=160, y=60)

    rightlabel = tk.Label(window2, text="Right -", bg="black", fg="white")
    rightlabel.pack()
    rightlabel.place(x=100, y=85)
    right = tk.Entry(window2, width=10)
    right.pack()
    right.place(x=160, y=85)

    bottomlabel = tk.Label(window2, text="Bottom -", bg="black", fg="white")
    bottomlabel.pack()
    bottomlabel.place(x=100, y=110)
    bottom = tk.Entry(window2, width=10)
    bottom.pack()
    bottom.place(x=160, y=110)

    def m2(): #THIS FUNCTION WILL POP UP THE NEW GUI WINDOW TO ENTER ALL DIMENSIONS OF IMAGE
        e = int(left.get())
        f = int(top.get())
        g = int(right.get())
        h = int(bottom.get())
        cropped_img = img.crop((e, f, g, h))
        cropped_img.save('C:/Users/ACER/Desktop/cropped.jpg') #IMAGE WILL AUTOMATICALLY SAVED IN DESKTOP
        l23 = tk.Label(window2, text="Image is saved at desktop", fg="red")
        l23.pack()
        l23.place(x=120, y=170)
        cropped_img.show()

    bm2 = tk.Button(window2, text="Click to save the image on desktop", command=m2, background="#3DA8AA")
    bm2.pack()
    bm2.place(x=90, y=140)


def func3(): #THIS FUNCTION RETURN ROTATED IMAGE 
    img = r()
    window3 = tk.Tk()
    window3.title("Rotate Image")
    window3.geometry("500x180")
    window3.configure(bg="black")
    l3 = tk.Label(window3, text="Enter the angle(in degree) to rotate the image:", font=1, bg="black", fg="white")
    l3.pack()

    a1label = tk.Label(window3, text="Angle -", bg="black", fg="white")
    a1label.pack()
    a1label.place(x=150, y=35)
    a1 = tk.Entry(window3, width=10)
    a1.pack()
    a1.place(x=200, y=35)

    def m3(): #POP A NEW WINDOW
        a = int(a1.get())
        rotate_img = img.rotate(a)
        rotate_img.save('C:/Users/ACER/Desktop/rotated.jpg')
        l32 = tk.Label(window3, text="Image is saved at desktop", fg="red") #IMAGE SAVED IN DESKTOP
        l32.pack()
        l32.place(x=140, y=95)
        rotate_img.show()

    bm3 = tk.Button(window3, text="Click to rotate the image", command=m3, background="#3DA8AA")
    bm3.pack()
    bm3.place(x=140, y=65)


def func4(): #RETURN FLIPPED IMAGE
    window4 = tk.Tk()
    window4.title("Flip Image")
    window4.geometry("500x180")
    window4.configure(bg="black")

    def m41(): #RETURN TO HORIZONTAL FLIPPED IMAGE 
        img = r()
        flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        flip_img.save('C:/Users/ACER/Desktop/flipped.jpg')
        l4 = tk.Label(window4, text="Image is saved at desktop", fg="red")
        l4.pack()
        l4.place(x=83, y=70)
        flip_img.show()

    def m42(): #RETURN VERTICAL FLIPPED IMAGE
        img = r()
        flip_img = img.transpose(Image.FLIP_TOP_BOTTOM)
        flip_img.save('C:/Users/ACER/Desktop/flipped.jpg')
        l4 = tk.Label(window4, text="Image is saved at desktop", fg="red")
        l4.pack()
        l4.place(x=83, y=70)
        flip_img.show()

    bm41 = tk.Button(window4, text="Rotate Horizontal", command=m41, background="#3DA8AA", width=20)
    bm41.pack()
    bm41.place(x=80, y=10)
    bm42 = tk.Button(window4, text="Rotate Vertical", command=m42, background="white", width=20)
    bm42.pack()
    bm42.place(x=80, y=40)


def func5(): #THIS FUNCTION RETURN BLACK AND WHITE FILETERED IMAGE
    img = r()
    bw_img = img.convert('L')
    window5 = tk.Tk()
    window5.title("Greyscale Image")
    window5.geometry("300x100")
    window5.configure(bg="black")

    def m5(): #POP A NEW WINDOW TO SAVE THE IMAGE
        bw_img.save('C:/Users/ACER/Desktop/B&WImage.jpg')
        lm5 = tk.Label(window5, text="Image is saved at desktop", fg="red")
        lm5.pack()
        lm5.place(x=75, y=40)
        bw_img.show()

    mb5 = tk.Button(window5, text="Click to save the image on desktop", command=m5, background="#3DA8AA")
    mb5.pack()
    mb5.place(x=55, y=10)


def func6(): # FUNCTION RETURN COMPRESSED IMAGE
    img = r()
    window6 = tk.Tk()
    window6.title("Compress Image")
    window6.geometry("350x70")
    window6.configure(bg="black")
    w = img.size[0]
    wp = (w / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wp)))
    compressed_img = img.resize((w, hsize), PIL.Image.ANTIALIAS)
    compressed_img.save('C:/Users/ACER/Desktop/compressed.jpg')
    l6 = tk.Label(window6, text="Image is saved at desktop", fg="red")
    l6.pack()
    l6.place(x=75, y=10)


def func7(): #FUNCTION RETURN DIFFERENT FORMATED IMAGE
    window7 = tk.Tk()
    window7.title("Change Image Format")
    window7.geometry("400x190")
    window7.configure(bg="black")

    def m71(): #TO SAVE JPG IMAGE
        img = r()
        img.save('C:/Users/ACER/Desktop/Converted.jpg')
        l7 = tk.Label(window7, text="Image is saved at desktop", fg="red")
        l7.pack()
        l7.place(x=80, y=100)

    def m72(): #TO SAVE PNG IMAGE
        img = r()
        img.save('C:/Users/ACER/Desktop/Converted.png')
        l7 = tk.Label(window7, text="Image is saved at desktop", fg="red")
        l7.pack()
        l7.place(x=80, y=100)

    def m73(): #TO SAVE JFIF IMAGE
        img = r()
        img.save('C:/Users/ACER/Desktop/Converted.jfif')
        l7 = tk.Label(window7, text="Image is saved at desktop", fg="red")
        l7.pack()
        l7.place(x=80, y=100)

    bm71 = tk.Button(window7, text="Convert into .jpg", command=m71, background="#3DA8AA", width=20)
    bm71.pack()
    bm71.place(x=75, y=10)
    bm72 = tk.Button(window7, text="Convert into .png", command=m72, background="white", width=20)
    bm72.pack()
    bm72.place(x=75, y=40)
    bm73 = tk.Button(window7, text="Convert into .jfif", command=m73, background="#3DA8AA", width=20)
    bm73.pack()
    bm73.place(x=75, y=70)


def func8(): #FUNCTION RETURN TEXT FROM IMAGE(OCR)
    img = r()
    window8 = tk.Tk()
    window8.title("Image to Text Converter")
    window8.geometry("620x185")
    window8.configure(bg="black")
    t = tess.image_to_string(img)
    l8 = tk.Text(window8, width=53, height=10,font=("Arialbold"),  background="#3DA8AA")
    l8.pack()
    l8.place(x=10, y=10)
    l8.insert(tk.END, t)


def func9(): #FUNCTION WILL DETECT CHARACTERS FROM IMAGE
    file_path = filedialog.askopenfilenames()
    x = str(file_path)
    string = x.replace("'", "")
    string = string.replace(",", "")
    string = string.replace("(", "", 1)
    string = string[:-1]
    img_path = string
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hImg, wImg, _ = img.shape
    boxes = tess.image_to_boxes(img)
    for b in boxes.splitlines():
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 3)
        cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

    cv2.imshow('Image', img)
    cv2.waitKey(0)


def func10(): #FUNCTION WILL DETECT WORDS FROM IMAGE
    file_path = filedialog.askopenfilenames()
    x = str(file_path)
    string = x.replace("'", "")
    string = string.replace(",", "")
    string = string.replace("(", "", 1)
    string = string[:-1]
    img_path = string
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hImg, wImg, _ = img.shape
    boxes = tess.image_to_data(img)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w + x, y + h), (0, 0, 255), 3)
                cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

    cv2.imshow('Image', img)
    cv2.waitKey(0)


def func11(): #FUNCTION WILL DETECT DIGITS FROM IMAGE
    file_path = filedialog.askopenfilenames()
    x = str(file_path)
    string = x.replace("'", "")
    string = string.replace(",", "")
    string = string.replace("(", "", 1)
    string = string[:-1]
    img_path = string
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hImg, wImg, _ = img.shape
    conf = r'--oem 3 --psm 6 outputbase digits' #oem= operating engine mode, psm= page segmentation mode
    boxes = tess.image_to_boxes(img, config=conf)
    for b in boxes.splitlines():
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 2)
        cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

    cv2.imshow('Image', img)
    cv2.waitKey(0)

def func12(): #FUNCTION WILL RETURN DETAILS OF Project
    window12 = tk.Tk()
    window12.title("Resize Image")
    window12.geometry("500x300")
    window12.configure(bg="black")
    lb12 = tk.Label(window12, text="Project Details:", font=("Arial bold",15), bg="#3DA8AA", fg="white")
    lb12.pack()
    
    lb121 = tk.Label(window12, text="- Complete Image Editing Tool", font=5, bg="black", fg="white")
    lb121.pack()
    lb121.place(x=80, y=40)
    lb122 = tk.Label(window12, text="- Convert Image into Text (OCR) Conversion", font=5, bg="black", fg="white")
    lb122.pack()
    lb122.place(x=80, y=80)
    lb123 = tk.Label(window12, text="- Image compressor", font=5, bg="black", fg="white")
    lb123.pack()
    lb123.place(x=80, y=120)
    lb124 = tk.Label(window12, text="- Can change Format of Image accordingly", font=5, bg="black", fg="white")
    lb124.pack()
    lb124.place(x=80, y=160)
    lb125 = tk.Label(window12, text="- Digits, Words, Character Detection", font=5, bg="black", fg="white")
    lb125.pack()
    lb125.place(x=80, y=200)
    

# receiving commands from user
btn1 = tk.Button(text="Resize the Image", command=func1,font=("Arialbold"), width=26, height=1, background="#3DA8AA")#RESIZE BUTTON
btn1.pack()
btn1.place(x=105, y=120)

btn2 = tk.Button(text="Crop the Image", command=func2,font=("Arialbold"), width=26, height=1, background="white")#CROP BUTTON
btn2.pack()
btn2.place(x=505, y=120)

btn3 = tk.Button(text="Rotate the Image", command=func3,font=("Arialbold"), width=26, height=1, background="white")#ROTATE BUTTON
btn3.pack()
btn3.place(x=105, y=180)

btn4 = tk.Button(text="Flip the Image", command=func4,font=("Arialbold"), width=26, height=1, background="#3DA8AA")#FLIP BUTTON
btn4.pack()
btn4.place(x=505, y=180)

btn5 = tk.Button(text="Edit Image to Grescale(B&W)", font=("Arialbold"),command=func5, width=26, height=1, background="#3DA8AA")#B&W BUTTON
btn5.pack()
btn5.place(x=105, y=240)

btn6 = tk.Button(text="Compress the Image", command=func6,font=("Arialbold"), width=26, height=1, background="white")#COMPRESS BUTTON
btn6.pack()
btn6.place(x=505, y=240)

btn7 = tk.Button(text="Change the Image Format",font=("Arialbold"), command=func7, width=26, height=1, background="white")#CHANGED FORMAT BUTTON
btn7.pack()
btn7.place(x=105, y=300)

btn8 = tk.Button(text="Convert the Image to Text", command=func8,font=("Arialbold"), width=26, height=1, background="#3DA8AA")#IMAGE TO TEXT BUTTON
btn8.pack()
btn8.place(x=505, y=300)

btn9 = tk.Button(text="Detect Character Wise Boxes", command=func9,font=("Arialbold"), width=26, height=1, background="#3DA8AA")#DETECT CHARACTERS BUTTON
btn9.pack()
btn9.place(x=105, y=360)

btn10 = tk.Button(text="Detect Word Wise Boxes", command=func10,font=("Arialbold"), width=26, height=1, background="white")#DETECT WORDS BUTTON
btn10.pack()
btn10.place(x=505, y=360)

btn11 = tk.Button(text="Detect Digits Wise Boxes", command=func11,font=("Arialbold"), width=26, height=1, background="white")#DETECT DIGITS BUTTON
btn11.pack()
btn11.place(x=105, y=420)

btn12 = tk.Button(text="Project Details",command=func12,font=("Arialbold"), width=26,height=1,background="#3DA8AA")#Details BUTTON
btn12.pack()
btn12.place(x=505, y=420)

window.mainloop()
