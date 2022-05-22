from tkinter import filedialog

from matplotlib.pyplot import get

def getdatadir():
    datadir = filedialog.askdirectory(
        title='select the data directory'
        )

def getsavedir():
    savedir = filedialog.askdirectory(
        title='select the directory'
        )

def getLogfile():
    Logfile = filedialog.askopenfilename(
        title='select the directory',
        filetypes=("Logsheet", ".xlsx")
        )
def getICfile():
    ICfile = filedialog.askopenfilename(
        title='select the directory',
        filetypes=[("text file from BL40B2 (*.txt)", ".txt")]
        )
