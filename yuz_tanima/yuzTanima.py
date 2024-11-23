import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk

def openFile():
    filePath=filedialog.askopenfilename()
    if filePath:
        img = cv2.imread(filePath)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces= faceCascade.detectMultiScale(gray,scaleFactor=1.30,minNeighbors=5,minSize=(30,30))

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w , y+h), (255,0,0),2)
            cv2.putText(img,"insan",(x,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img=Image.fromarray(img)
        img=img.resize((600,400), Image.LANCZOS)
        img=ImageTk.PhotoImage(img)

        canvas.img=img
        canvas.create_image(0,0,anchor=tk.NW,image=img)

faceCascade=cv2.CascadeClassifier('face_detector.xml')

root=tk.Tk()
root.title("Yüz Tanıma")

canvas=tk.Canvas(root,width=600,height=400)
canvas.pack()

openbutton=tk.Button(root,text="Dosya Seç",command=openFile)
openbutton.pack()



root.mainloop()