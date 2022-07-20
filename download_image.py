from tkinter import *
import requests
import os
from bs4 import BeautifulSoup
from PIL import Image
import PIL.ImageTk

def show():
    global photo_1,photo_2,image_1,image_2,name 
    print("showing.....")
    Extra = 100
    try:
        photo_1 = Image.open("images/searchimag.jpg")
        image_1 = PIL.ImageTk.PhotoImage(photo_1)
        H = int(image_1.height())+Extra
        W = int(image_1.width())+Extra

        print(H,W)
        photo_2 = Image.open("images/searchimag.jpg")
        image_2 = PIL.ImageTk.PhotoImage(photo_2,size=(H,W))
        lable = Label(image=image_2)
        lable.place(x=100,y=190)
    except:
        photo_1 = Image.open("images/searchimag.png")
        image_1 = PIL.ImageTk.PhotoImage(photo_1)
        H = int(image_1.height())+Extra
        W = int(image_1.width())+Extra

        print(H,W)
        photo_2 = Image.open("images/searchimag.png")
        image_2 = PIL.ImageTk.PhotoImage(photo_2,size=(H,W))

        lable = Label(image=image_2)
        lable.place(x=100,y=190)

    name = Label(text=f"Name: {name}",font="lucida 13",fg="blue")
    name.place(x=40,y=450)

    # getting screen's height in pixels
 

def Download_img(type):
    global search_var,current_image,total_images,name
    if type=="next" and current_image<=total_images:
        current_image+=1
    elif type=="start":
        current_image=0
    print("Downloading......")
    URL = f"https://www.google.com/search?q={str(search_var.get()).replace(' ','+')}&sxsrf=ALeKk03DekqkSq7VV_P9jdO7r_EG1yuwDA:1621686398735&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiJz-7NpN3wAhUolEsFHbEXBd0Q_AUoAXoECAEQAw"

    r = requests.get(URL)

    soup = BeautifulSoup(r.content,"html.parser")

    images = soup.find_all('img')
    
    total_images = len(images)
    name = ""
    try:
        link = images[current_image]['src']
        name = images[current_image]['alt']

        # os.

        with open(f"images/searchimag.png","wb") as f:
            im = requests.get(link)
            f.write(im.content)
        with open(f"images/searchimag.jpg","wb") as f:
            im = requests.get(link)
            f.write(im.content)
    except:
        current_image+=1
        link = images[current_image]['src']
        name = images[current_image]['alt']

        # os.

        with open(f"images/searchimag.png","wb") as f:
            im = requests.get(link)
            f.write(im.content)
        with open(f"images/searchimag.jpg","wb") as f:
            im = requests.get(link)
            f.write(im.content)
    print("Name: ",name)

    print("Downloaded")
    show()
   
total_images = 1
current_image = 0

root = Tk()
root.geometry("500x500")

search_var = StringVar()

L1 = Label(text="Seach Image",font="lucida 15",fg="blue")
L1.place(x=10,y=10)

Label(text="Output Image :",font="lucida 12 bold").place(x=10,y=140)

name = Label(text="",font="lucida 13",fg="black")
L1.place(x=10,y=10)

Search = Entry(root,textvariable=search_var,font="lucida 15 bold")
Search.place(x=150,y=10)

Button(text="See image",font="lucida 15 bold",command=lambda:Download_img("start")).place(x=200,y=60)
next = Button(text="Next",font="lucida 15 bold",command=lambda:Download_img("next"))
next.place(x=400,y=400)

# next['']

root.mainloop()
