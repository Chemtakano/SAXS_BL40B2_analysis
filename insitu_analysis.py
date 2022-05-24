from matplotlib import markers
import pandas as pd
import tkinter
from tkinter import filedialog
import matplotlib.pyplot as plt

def getsamfile():
    sam_path = filedialog.askopenfilename(
        title='select the saving directory',
        filetypes=[("sample", ".chi")]
        )
    input_box1.insert(tkinter.END, sam_path) 

def getsolfile():
    sol_path = filedialog.askopenfilename(
        title='select the saving directory',
        filetypes=[("solvent", ".chi")]
        )
    input_box2.insert(tkinter.END, sol_path) 

def chi(file):
    return pd.read_table(
        file,
        skiprows = [0,1,2,3],
        header=None,
        sep = '\s+',
        names = ('q', 'I(q)', 'noname'),
        usecols = ['q', 'I(q)']
    )

def plot():
    dfsam=chi(input_box1.get())
    dfsol=chi(input_box2.get())
    cons=float(input_box3.get())

    dfcal=dfsam['I(q)']-dfsol['I(q)']*cons
    
    fig = plt.figure(figsize=(8, 6))
    ax1 = fig.add_subplot(121, title='result', ylabel='$I$($q$)', xlabel='$q$ / nm$^{-1}$')
    ax2 = fig.add_subplot(122, title='sample & solvent', xlabel='$q$ / nm$^{-1}$')

    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlim(0.02,0.5)
  
    ax1.plot(dfsam['q'], dfcal, color='k', linewidth = 0, marker='o',markersize=4, label='result')

    ax2.set_xscale('log')
    ax2.set_yscale('log')
    
    ax2.plot(dfsam['q'], dfsam['I(q)'], color='green', label='sample')
    ax2.plot(dfsol['q'], dfsol['I(q)']*cons, color='blue', label='solvent')
    ax2.legend()

    plt.show()

##Apprication--------------------------------------------------
#ウインドウの作成
root = tkinter.Tk()
root.title("Takano in situ analysis app")
root.geometry("360x450")

#sample--------
#入力欄の作成
input_box1 = tkinter.Entry(width=40)
input_box1.place(x=10, y=40)

#ラベルの作成
input_label = tkinter.Label(text="sample file")
input_label.place(x=10, y=10)

#ボタンの作成
button1 = tkinter.Button(text="参照",command=getsamfile)
button1.place(x=10, y=70)

#solvent--------
input_box2 = tkinter.Entry(width=40)
input_box2.place(x=10, y=140)

input_label = tkinter.Label(text="solvent file")
input_label.place(x=10, y=110)

button2 = tkinter.Button(text="参照",command=getsolfile)
button2.place(x=10, y=170)

#constant--------
input_box3 = tkinter.Entry(width=40)
input_box3.insert(0, '1')
input_box3.place(x=10, y=240)

input_label = tkinter.Label(text="constant (1.00 default)")
input_label.place(x=10, y=210)

#plot--------
button = tkinter.Button(text="plot", font=7, bg='yellow', command=plot)
button.place(x=300, y=140)

#ウインドウの描画
root.mainloop()