from tkinter import *

canvas_width = 200
canvas_height= 100

colors = ('#476042','yellow')
box = []

for ratio in (0.2,0.35):
    box.append(
                (canvas_width*ratio,
                 canvas_height*ratio,
                 canvas_width*(1-ratio),
                 canvas_height*(1-ratio)
                )
    )
master = Tk()
w = Canvas(master, width = canvas_width, height=canvas_height)
w.pack()

for i in range(2):
    w.create_rectangle(box[i][0], box[i][1], box[i][2], box[i][3], fill=colors[i])
w.create_line(0,0,box[0][0],box[0][1], fill=colors[0], width=3)
w.create_line(0, canvas_height,     # lower left corner of canvas
          box[0][0], box[0][3], # lower left corner of box[0]
          fill=colors[0],
          width=3)
w.create_line(box[0][2],box[0][1],  # right upper corner of box[0]
          canvas_width, 0,      # right upper corner of canvas
          fill=colors[0],
          width=3)
w.create_line(box[0][2], box[0][3], # lower right corner pf box[0]
          canvas_width, canvas_height, # lower right corner of canvas
          fill=colors[0], width=3)

w.create_text(canvas_width / 2,
          canvas_height / 2,
          text="Python")

mainloop()
