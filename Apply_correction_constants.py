import tkinter
from tkinter import filedialog
import pandas as pd


def work():
    datas=input_box1.get().split(',')
    datas=datas[:-1]
    savepath=input_box2.get()
    F=float(input_box3.get())

    for i in datas:
        df=pd.read_csv(i, header=None)
        df2=pd.read_csv(i)
        name=df2.columns[1]
        df[1]=df[1]*F
        df.to_csv(savepath + '/' + name + '_abs.csv', index = False)

def getfiles():
    files = filedialog.askopenfilenames(
      title='select the files',
      filetypes=[("csvfile (*.csv)", ".csv")]
      )
    for i in files:
        input_box1.insert(tkinter.END, str(i)+',') 

def getsavedir():
    savedir_path = filedialog.askdirectory(
        title='select the saving directory'
        )
    input_box2.insert(tkinter.END, savedir_path) 


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
input_label = tkinter.Label(text="sample files")
input_label.place(x=10, y=10)

#ボタンの作成
button1 = tkinter.Button(text="参照",command=getfiles)
button1.place(x=10, y=70)

#save--------
input_box2 = tkinter.Entry(width=40)
input_box2.place(x=10, y=140)

input_label = tkinter.Label(text="saving directry")
input_label.place(x=10, y=110)

button2 = tkinter.Button(text="参照",command=getsavedir)
button2.place(x=10, y=170)

#constant--------
input_box3 = tkinter.Entry(width=40)
input_box3.insert(0, '1')
input_box3.place(x=10, y=240)

input_label = tkinter.Label(text="correction constance (1.00 default)")
input_label.place(x=10, y=210)

#plot--------
button = tkinter.Button(text="start", font=7, bg='yellow', command=work)
button.place(x=300, y=140)

#ウインドウの描画
root.mainloop()
