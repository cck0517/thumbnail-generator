import tkinter as tk
from tkinter import filedialog
import os
import pathlib as pl

# setting up the basics of an User interface
root = tk.Tk()

root.title("Custom Video Thumbnail Generator")

canvas = tk.Canvas(root,height=500,width=500)
canvas.pack()

frame = tk.Frame(root,bg='white')
frame.place(relwidth=1.0,relheight=1.0)

#setting up the functions
parameters=[]

# This function get the file name using os, then using iteration to turn it into a path route available in ubuntu
def addvideo():
    drive = "c"
    linuxroot = "/mnt/"
    video = filedialog.askopenfile(mode='r', filetypes=[('video files','*.mp4')])
    if video:
      filepath = os.path.abspath(video.name)
      orgin_path = pl.PurePath(filepath)
      parts = list(orgin_path.parts)
      
      # decide which prefix to use because the video could be in c or in d
      if(parts[0]=='C:\\'):
        drive = "c"

      elif(parts[0]=='D:\\'):
        drive="d"
      
      else:
        linuxroot = "You should manually decide the hardrive file is in"
      
      # Using iteration, mutate the list to form an eligible path route in ubuntu
      parts=parts[1:]
      linuxroot+=drive
      while(parts):
        linuxroot+='/'
        linuxroot+=parts.pop(0)
      
      # Displays the root that is ultimately generated
      label = tk.Label(frame,text="chosen filepath :"+linuxroot,fg='blue')
      label.pack()

      # Get and display all the entries

      interval, width, height, output, column = entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get()
      parameters=[interval, width, height, output, column]
      p_label = tk.Label(frame,text = str(parameters))
      p_label.pack()

        

      
    else:
        print("No files found!")

#setting up the buttons and entries
Attachfile = tk.Button(root,text="Attach a video", padx=15, pady=10, fg = "white", bg="skyblue",command = addvideo)
Attachfile.place(x=190,y=400)

entry1 = tk.Entry(root,bg='skyblue')
canvas.create_window(360, 100, window=entry1)
label1 = tk.Label(frame,text="please input the interval (in seconds) ")
label1.place(x=50, y=88)

entry2 = tk.Entry(root,bg='skyblue')
canvas.create_window(360, 150, window=entry2)
label2 = tk.Label(frame,text="please input the width ")
label2.place(x=50, y=138)

entry3 = tk.Entry(root,bg='skyblue')
canvas.create_window(360, 200, window=entry3)
label3 = tk.Label(frame,text="please input the height ")
label3.place(x=50, y=188)

entry4 = tk.Entry(root,bg='skyblue')
canvas.create_window(360, 250, window=entry4)
label4 = tk.Label(frame,text="please input the name of the output ")
label4.place(x=50, y=238)

entry5 = tk.Entry(root,bg='skyblue')
canvas.create_window(360, 300, window=entry5)
label5 = tk.Label(frame,text="please input the number of columns ")
label5.place(x=50, y=288)

root.mainloop()