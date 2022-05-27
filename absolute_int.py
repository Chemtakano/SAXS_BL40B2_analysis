from sunau import AUDIO_FILE_ENCODING_LINEAR_32
import tkinter
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

def getdir():
    dirchi = filedialog.askdirectory(
        title='select the directory storing chifiles'
        )
    input_box1.insert(tkinter.END, dirchi) 

def ana():
    water = input_box3.get()
    empty = input_box4.get()
    datapath= input_box1.get()
    txtfile= input_box2.get()

    def readchi(filename):
        df = pd.read_table(datapath+'/'+filename+'.chi', sep='\s+', skiprows=4, usecols = [0,1], names=['q', 'Iq'])
        return df
    
    def IC2(filename):
        Header = ['filename', 'time', 's', 'time2', 's2', 'Ex_time', 's3', 'IC', 'IC0', 'IC1', 'IC2']
        IC = pd.read_table(datapath+'/'+txtfile+'.txt', names=Header, index_col = 'filename')
        return IC.at[filename, 'IC2']

    def corrected_data(filename):
        df = readchi(filename)['Iq']/IC2(filename)
        return pd.concat([readchi(filename)['q'], df], axis=1)
    
    x=corrected_data(water)['q']
    ywater=corrected_data(water)['Iq']
    ycapi=corrected_data(empty)['Iq']
    subs=ywater-ycapi

    #plot
    fig, ax = plt.subplots()
    ax.plot(x, ywater, label='water')
    ax.plot(x, ycapi, label='empty')
    ax.plot(x, subs, label='water-empty')
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.legend()
    plt.show()

    
def ana2():
    water = input_box3.get()
    empty = input_box4.get()
    datapath = input_box1.get()
    txtfile = input_box2.get()
    minq = float(input_box5.get())
    maxq = float(input_box6.get())

    def readchi(filename):
        df = pd.read_table(datapath+'/'+filename+'.chi', sep='\s+', skiprows=4, usecols = [0,1], names=['q', 'Iq'])
        return df
    
    def IC2(filename):
        Header = ['filename', 'time', 's', 'time2', 's2', 'Ex_time', 's3', 'IC', 'IC0', 'IC1', 'IC2']
        IC = pd.read_table(datapath+'/'+txtfile+'.txt', names=Header, index_col = 'filename')
        return IC.at[filename, 'IC2']

    def corrected_data(filename):
        df = readchi(filename)['Iq']/IC2(filename)
        return pd.concat([readchi(filename)['q'], df], axis=1)

    x=corrected_data(water)['q']
    ywater=corrected_data(water)['Iq']
    ycapi=corrected_data(empty)['Iq']
    subs=ywater-ycapi

    df=pd.concat([x, ywater, ycapi, subs], axis=1)
    df2=df.set_axis(['q', 'water', 'empty', 'water-empty'], axis='columns')
    df3=df2.query('@minq < q < @maxq')

    x2=df3['q']
    ywater2=df3['water']
    ycapi2=df3['empty']
    subs2=df3['water-empty']
    F=0.01632 / df3['water-empty'].mean()
    
    fig, ax = plt.subplots()
    ax.plot(x2, ywater2, label='water')
    ax.plot(x2, ycapi2, label='empty')
    ax.plot(x2, subs2, label='water-empty')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_title('F = 0.01632/{} = {}'.format(df3['water-empty'].mean(),F))
    plt.legend()
    plt.show()





##App----------------------------------------------
root = tkinter.Tk()
root.title("Takano marge app")
root.geometry("550x330")

#text data--------
#入力欄の作成
input_box1 = tkinter.Entry(width=40)
input_box1.place(x=10, y=40)

#ラベルの作成
input_label = tkinter.Label(text="select the text files")
input_label.place(x=10, y=10)

#ボタンの作成
button1 = tkinter.Button(text="参照",command=getdir)
button1.place(x=10, y=70)

#txt--------
input_box2 = tkinter.Entry(width=20)
input_box2.place(x=260, y=40)

input_label = tkinter.Label(text="text file without extention")
input_label.place(x=260, y=10)

#water--------
input_box3 = tkinter.Entry(width=20)
input_box3.place(x=260, y=100)

input_label = tkinter.Label(text="file name without extention (water)")
input_label.place(x=260, y=70)

#capi--------
input_box4 = tkinter.Entry(width=20)
input_box4.place(x=260, y=160)

input_label = tkinter.Label(text="file name without extention (empty)")
input_label.place(x=260, y=130)

#testplot--------
button3 = tkinter.Button(text="start 1st run",command=ana)
button3.place(x=200, y=200)

#minq--------
input_box5 = tkinter.Entry(width=10)
input_box5.place(x=160, y=250)
input_label = tkinter.Label(text="minq")
input_label.place(x=120, y=250)

#maxq--------
input_box6 = tkinter.Entry(width=10)
input_box6.place(x=290, y=250)
input_label = tkinter.Label(text="maxq")
input_label.place(x=250, y=250)

#final
button4 = tkinter.Button(text="start 2nd run",command=ana2)
button4.place(x=200, y=290)

root.mainloop()