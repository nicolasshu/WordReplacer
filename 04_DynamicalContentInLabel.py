import tkinter as tk


counter = 0
interval = 1000 # ms
def counter_label(label):
    def count():
        global counter
        global interval
        counter += 1
        label.config(text=str(counter))
        label.after(interval,count)
    count()

root = tk.Tk()
root.title("Counting Seconds")


label = tk.Label(root, fg = 'green')
label.pack()

counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()
