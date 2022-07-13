import pandas as pd
import matplotlib.pyplot as plt
import tkinter
from tkinter import filedialog

###main---------------------------------------------------------
def main():
    minq_s=float(input_box4.get())
    maxq_s=float(input_box5.get())
    maxq_w=float(input_box6.get())
    datas=input_box1.get()
    Listdata=input_box2.get()
    saving_dir=input_box3.get()

    df=pd.read_excel(Listdata)
    
    for i in range(len(df['small q'])):
        data_s=df["small q"][i]
        data_w=df['wide q'][i]
        name=df['name'][i]

        df_s=pd.read_csv(datas+'//'+data_s+'.csv', names =['q', 'Iq'], skiprows=1)
        df_w=pd.read_csv(datas+'//'+data_w+'.csv', names =['q', 'Iq'], skiprows=1)

        df_s=df_s.query('@minq_s< q <@maxq_s')
        df_w=df_w.query('@maxq_s<= q <@maxq_w')

        a=df_s.tail(1).iat[0,1] / df_w.head(1).iat[0,1]

        df_w['Iq']=df_w['Iq']*a

        df_fin=pd.concat([df_s, df_w])

        df_fin.to_csv(saving_dir+'//'+name+'.csv', index=False)



###ファイルの取得のdef--------------------------------------------
def getdatadir():
    datadir_path = filedialog.askdirectory(
      title='select the data directory'
      )
    input_box1.insert(tkinter.END, datadir_path) #結果を表示

def getListfile():
    Logsheet_path = filedialog.askopenfilename(
        title='select the saving directory',
        filetypes=[("List", ".xlsx")]
        )
    input_box2.insert(tkinter.END, Logsheet_path) 

def getsavedir():
    savedir_path = filedialog.askdirectory(
        title='select the saving directory'
        )
    input_box3.insert(tkinter.END, savedir_path) 

##Apprication--------------------------------------------------
#ウインドウの作成
root = tkinter.Tk()
root.title("concat q range")
root.geometry("360x450")

#data--------
#入力欄の作成
input_box1 = tkinter.Entry(width=40)
input_box1.place(x=10, y=40)

#ラベルの作成
input_label = tkinter.Label(text="data directory")
input_label.place(x=10, y=10)

#ボタンの作成
button1 = tkinter.Button(text="参照",command=getdatadir)
button1.place(x=10, y=70)

#List--------
input_box2 = tkinter.Entry(width=40)
input_box2.place(x=10, y=140)

input_label = tkinter.Label(text="sample list")
input_label.place(x=10, y=110)

button2 = tkinter.Button(text="参照",command=getListfile)
button2.place(x=10, y=170)

#save--------
input_box3 = tkinter.Entry(width=40)
input_box3.place(x=10, y=240)

input_label = tkinter.Label(text="directory for saving")
input_label.place(x=10, y=210)

button2 = tkinter.Button(text="参照",command=getsavedir)
button2.place(x=10, y=270)

#min&max--------
input_box4 = tkinter.Entry(width=10)
input_box4.insert(0, '0.025')
input_box4.place(x=10, y=340)

input_label = tkinter.Label(text="minimum q")
input_label.place(x=10, y=310)

input_box5 = tkinter.Entry(width=10)
input_box5.insert(0, '0.5')
input_box5.place(x=110, y=340)

input_label = tkinter.Label(text="Link point")
input_label.place(x=110, y=310)

input_box6 = tkinter.Entry(width=10)
input_box6.insert(0, '2')
input_box6.place(x=210, y=340)

input_label = tkinter.Label(text="maximum q")
input_label.place(x=210, y=310)

#start--------
button = tkinter.Button(text="start", font=7, bg='white', command=main)
button.place(x=300, y=170)


#ウインドウの描画
root.mainloop()
