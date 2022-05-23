import tkinter
from tkinter import filedialog
import pandas as pd

def getfiles():
    files = filedialog.askopenfilenames(
      title='select the files',
      filetypes=[("csvfile (*.csv)", ".csv")]
      )
    input_box1.insert(tkinter.END, files) 

def getsavedir():
    savedir_path = filedialog.askdirectory(
        title='select the saving directory'
        )
    input_box2.insert(tkinter.END, savedir_path) 


def merge():
    files2=input_box1.get().split()
    savepath=input_box2.get()
    name=input_box3.get()

    li = []
    for file in files2:
        df = pd.read_csv(file, usecols = [1])
        li.append(df)
        Iqdata = pd.concat(li, axis=1)
        #qデータの取得
        df2 = pd.read_csv(files2[0], usecols = [0])
        #qデータを合わせる
        merged_data = pd.concat([df2,Iqdata], axis=1)
        merged_data.to_excel(savepath + '/'+ name +'.xlsx', index = False)

root = tkinter.Tk()
root.title("Takano marge app")
root.geometry("550x300")

#data--------
#入力欄の作成
input_box1 = tkinter.Entry(width=40)
input_box1.place(x=10, y=40)

#ラベルの作成
input_label = tkinter.Label(text="data directry")
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

#filename--------
input_box3 = tkinter.Entry(width=20)
input_box3.place(x=260, y=140)
input_label = tkinter.Label(text="enter export file name")
input_label.place(x=260, y=110)
input_label = tkinter.Label(text="/")
input_label.place(x=250, y=140)
input_label = tkinter.Label(text=".xlsx")
input_label.place(x=380, y=140)

#ボタンの作成
button = tkinter.Button(text="start analysis",command=merge)
button.place(x=140, y=240)


root.mainloop()