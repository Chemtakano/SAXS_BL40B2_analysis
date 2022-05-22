import tkinter
from tkinter import filedialog

def getdatadir():
    datadir = filedialog.askdirectory(
        title='select the data directory'
        )

def getsavedir():
    savedir = filedialog.askdirectory(
        title='select the saving directory'
        )

def getLogfile():
    Logfile = filedialog.askopenfilename(
        title='select the Logsheet',
        filetypes=("Logsheet", ".xlsx")
        )
def getICfile():
    ICfile = filedialog.askopenfilename(
        title='select the directory',
        filetypes=[("text file from BL40B2 (*.txt)", ".txt")]
        )

root = tkinter.Tk()
root.title("SAXS data analysis")
root.geometry("400x300")

frame = tkinter.Frame(root, bg="red")

#button1
btn1 = tkinter.Button()
btn1["text"] = "(1)select the data directory"
btn1["command"] = getdatadir
btn1.grid(column=0, row=1, sticky="NSEW")

#button2
btn2 = tkinter.Button()
btn2["text"] = "(2)select the saving directory"
btn2["command"] = getsavedir
btn2.grid(column=0, row=2, sticky="NSEW")

#button3
btn3 = tkinter.Button()
btn3["text"] = "(3)select the Log sheet"
btn3["command"] = getLogfile
btn3.grid(column=0, row=3, sticky="NSEW")

#button4
btn4 = tkinter.Button()
btn4["text"] = "(4)select IC file"
btn4["command"] = getICfile
btn4.grid(column=0, row=4, sticky="NSEW")

#button5
btn5 = tkinter.Button()
btn5["text"] = "start analysis"
btn5["command"] = root.destroy
btn5.grid(column=0, row=5, sticky="NSEW")

#button6
btn6 = tkinter.Button()
btn6["text"] = "exit"
btn6["command"] = root. destroy
btn6.grid(column=0, row=6, sticky="NSEW")

root.mainloop()
