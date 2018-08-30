################################################################################
# IMPORT LIBRARIES
################################################################################
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox
import time
import numpy as np

################################################################################
# GLOBAL VARIABLES
################################################################################
master = tk.Tk()
replaceType = tk.IntVar()
replaceType.set(2)
replaceList = [('First Only',1), ('All',2)]
target = ''
openfilename = []
mainString = []
lastPos = []
listFilename = './word_swap_list.txt'
step = 0

# ADJUSTABLE!
font_size = 12
typeface = 'times'
typeface = 'courier 10 pitch'

################################################################################
# HELPER FUNCTIONS
################################################################################
# ------------------------------------------------------------------------------
def OpenFile():
    global openfilename, mainString, Memory

    # Get the filename to open
    openfilename = tk.filedialog.askopenfilename()

    with open(openfilename, 'r') as myfile:
        mainString=myfile.read()

    # Insert the string to the text field
    T.insert(tk.END,mainString)
    T.configure(state=tk.DISABLED)
    #ipdb.set_trace()
    Memory = []
def Open():
    global openfilename, mainString

    with open(openfilename, 'r') as myfile:
        mainString=myfile.read()

    # Insert the string to the text field
    T.insert(tk.END,mainString)
    T.configure(state=tk.DISABLED)
# ------------------------------------------------------------------------------
def SaveFileAs():
    global mainString

    # Save as...
    f = tk.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    f.write(mainString)
    f.close()
# ------------------------------------------------------------------------------
def SaveFile():
    global mainString, openfilename, listFilename, newWord

    targetword = targetEntry.get()

    # Automatically save as a temporary file
    filename = openfilename+'_temp'
    with open(filename, "w") as text_file:
        print(mainString, file=text_file)

    f = open(listFilename,'a+')
    f.write(targetword+' | '+newWord+'\n')
    f.close()
# ------------------------------------------------------------------------------
def ShowInstructions():
    instructions = '''INSTRUCTIONS:
    Main Window:
        Open File: <Ctrl-O>
        Clear Hightlights: <Esc>
        Find a word: <Ctrl-F>
        Replace a word: <Ctrl-R>
    Find a word:
        - Ctrl-F will open an empty dialog
        - Select a string and <Ctrl-F> will open a filled dialog
        - Press <Enter> to highlight your words
    Choose the text to be replaced:
        - Double-Click and highlight a word will open a dialog
        - Highlight a set of words and <Ctrl-R> will open a dialog
    On the Replace Dialog:
        - (Optional) Choose the target string
        - Choose the new word(s)
        - You may choose to change all of the words or only the first one
        - Press <Enter>
    Note: Unfortunately I wasn\'t able to get the Text GUI to reset exactly at the same location, but if you press <Ctrl+/>, you will get restored back at your last spot '''
    #messagebox.showinfo("Information",instructions)
    w = tk.Toplevel(master)
    msg = tk.Message(w, text=instructions, width=2000)
    msg.pack()
# ------------------------------------------------------------------------------
def StoreTempVariables(previous_string):
    global Memory, step

    step += 1
    Memory.append(previous_string)
# ------------------------------------------------------------------------------
def Undo():
    global Memory, step, mainString
    step -= 1
    mainString = Memory[step]
    GetThisPosition()
    PutTextBackIn(Memory[step])
    ResetLastPosition()
    del Memory[-1]

# ------------------------------------------------------------------------------
def FindWord(event):
    global window, targetEntry
    print('Find word!')

    if T.tag_ranges("sel"):
        # If there is a text selection
        targetword = T.selection_get()
    else:
        # If there is no text selection
        # Get the target word
        targetword = ''

    # Open a new window
    window = tk.Toplevel(master)

    # Put in the entries
    targetEntry = tk.Entry(window,font=(14))
    targetEntry.insert(10,targetword)

    newEntry = tk.Entry(window,font=(14))

    # Make the <Return> key the activation key
    window.bind('<Return>', HighlightWord)
    window.bind('<Escape>', WindowCloseShortcut)

    tk.Label(window, text='Target').grid(row=0)
    #tk.Label(window, text='New Word').grid(row=1)

    # Set up the Layout
    targetEntry.grid(row=0,column=1)

    targetEntry.focus()

# ------------------------------------------------------------------------------
def HighlightWord(event):
    global window
    print("Highlight word!")
    targetword = targetEntry.get()
    T.highlight_pattern(targetword, "yellow")
    window.destroy()
# ------------------------------------------------------------------------------
def ClickOnWord():
    global newEntry, window, targetEntry

    if T.tag_ranges("sel"):
        # If there is a text selection
        targetword = T.selection_get()
    else:
        # If there is no text selection
        # Get the target word
        targetword = ''

    # Highlight the word ==> CustomText class
    T.highlight_pattern(targetword, "yellow")

    # Open a new window
    window = tk.Toplevel(master)

    # Put in the entries
    targetEntry = tk.Entry(window,font=(14))
    targetEntry.insert(10,targetword)

    newEntry = tk.Entry(window,font=(14))

    # Make the <Return> key the activation key
    window.bind('<Return>', ReplaceWord)

    tk.Label(window, text='Target').grid(row=0)
    tk.Label(window, text='New Word').grid(row=1)

    # Set up the Layout
    targetEntry.grid(row=0,column=1)
    newEntry.grid(row=1,column=1)
    tk.Radiobutton(window, text=replaceList[0][0], variable=replaceType, value=replaceList[0][1]).grid(row=0,column=2)
    tk.Radiobutton(window, text=replaceList[1][0], variable=replaceType, value=replaceList[1][1]).grid(row=1,column=2)

    window.protocol("WM_DELETE_WINDOW", WindowClose)
    # Set the newEntry as the focus
    newEntry.focus()
# ------------------------------------------------------------------------------
def ReplaceWord(event):
    global newEntry, window, mainString, lastPos, newWord, targetEntry
    print('Replace Word')
    StoreTempVariables(mainString)

    targetword = targetEntry.get()
    # Get the new word
    newWord = newEntry.get()

    # Get the old word
    chosenOne = replaceType.get()

    # Replace accordingly
    if chosenOne == 1:
        tempString = mainString.replace(targetword,newWord,1)
        mainString = tempString
    else:
        tempString = mainString.replace(targetword,newWord)
        mainString = tempString

    GetThisPosition()
    PutTextBackIn(mainString)
    SaveFile()
    window.destroy()
    ResetLastPosition()

# ------------------------------------------------------------------------------
class CustomText(tk.Text):
    '''A text widget with a new method, highlight_pattern()

    example:

    text = CustomText()
    text.tag_configure("red", foreground="#ff0000")
    text.highlight_pattern("this should be red", "red")

    The highlight_pattern method is a simplified python
    version of the tcl code at http://wiki.tcl.tk/3246
    '''
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end",
                          regexp=False):
        '''Apply the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular
        expression according to Tcl's regular expression syntax.
        '''

        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = tk.IntVar()
        while True:
            index = self.search(pattern, "matchEnd","searchLimit",
                                count=count, regexp=regexp)
            if index == "": break
            if count.get() == 0: break # degenerate pattern which matches zero-length strings
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")
# ------------------------------------------------------------------------------
def WindowClose():
    window.destroy()
    GetThisPosition()
    PutTextBackIn()
    ResetLastPosition()
# ------------------------------------------------------------------------------
def GetThisPosition():
    global lastPos
    #lastPos = S.get()
    print('This position: ',end='')
    print(T.index('current'))
    lastPos = T.index('current')
    print("GetThisPosition: "+str(lastPos))
# ------------------------------------------------------------------------------
def PutTextBackIn(string=mainString):
    T.configure(state=tk.NORMAL)
    T.delete(0.0,tk.END)
    T.insert(0.0,string)
    T.configure(state=tk.DISABLED)
# ------------------------------------------------------------------------------
def ResetLastPosition():
    #T.yview_moveto(np.mean(lastPos))
    T.see(lastPos)
    #T.config(yscrollcommand=S.set)


################################################################################
# KEYBINDED FUNCTIONS
################################################################################
# ------------------------------------------------------------------------------
def Debug(event):
    global Memory,step
    # Get the line number
    print('Step: '+str(step))
    print('Memory: ',end='')
    print(Memory)
    print('mainString: '+mainString)
# ------------------------------------------------------------------------------
def ClickOnWordShortcut(event):
    ClickOnWord()
# ------------------------------------------------------------------------------
def ClearHighlights(event):
    GetThisPosition()
    PutTextBackIn()
    ResetLastPosition()
# ------------------------------------------------------------------------------
def ResetLastPositionShortcut(event):
    ResetLastPosition()
# ------------------------------------------------------------------------------
def OpenFileShortcut(event):
    OpenFile()
# ------------------------------------------------------------------------------
def WindowCloseShortcut(event):
    WindowClose()
# ------------------------------------------------------------------------------
def UndoShortcut(event):
    try:
        Undo()
    except:
        print('This is the original! Can\'t Undo!')
################################################################################
# GRAPHIC USER INTERFACE
################################################################################
# Initialize the window class --------------------------------------------------
master.title('Chris\'s Word Searcher')

# Menu Widget ------------------------------------------------------------------
menu = tk.Menu(master)
master.config(menu=menu)
filemenu = tk.Menu(menu)
aboutmenu = tk.Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
menu.add_cascade(label='About',menu=aboutmenu)
menu.add_cascade(label='Undo',menu=aboutmenu)
filemenu.add_command(label='Open File', command=OpenFile)
filemenu.add_command(label='Save File', command=SaveFileAs)
filemenu.add_command(label='Undo', command=Undo)
aboutmenu.add_command(label='Instructions', command=ShowInstructions)

# Shortcuts --------------------------------------------------------------------
master.bind('<Double-1>',ClickOnWordShortcut)
master.bind('<Control-Key-r>',ClickOnWordShortcut)
master.bind('<Control-Key-R>',ClickOnWordShortcut)
master.bind('<Control-Key-f>',FindWord)
master.bind('<Control-Key-F>',FindWord)
master.bind('<Control-slash>',ResetLastPositionShortcut)
master.bind('<Control-Key-o>',OpenFileShortcut)
master.bind('<Control-Key-O>',OpenFileShortcut)
master.bind('<Return>',Debug)
master.bind('<Escape>',ClearHighlights)
master.bind('<Control-Key-z>',UndoShortcut)
# Text Widget ------------------------------------------------------------------
T = CustomText(master, height=50, width=60, font=(typeface,font_size),exportselection=True)
T.pack(side=tk.LEFT,expand=True,fill='both')

# Scroll Widget ----------------------------------------------------------------
S = tk.Scrollbar(master)
S.pack(side=tk.LEFT, fill=tk.Y)

# Synchronize the scroll bar and the text
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

# Choose the highlighting
T.tag_configure("yellow", background="yellow")

# Main Loop --------------------------------------------------------------------
tk.mainloop()
