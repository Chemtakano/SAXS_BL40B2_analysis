import tkinter
from tkinter import filedialog
import pandas as pd

#ボタンがクリックされたら実行
def getdatadir():
    datadir_path = filedialog.askdirectory(
      title='select the data directory'
      )
    input_box1.insert(tkinter.END, datadir_path) #結果を表示

def getsavedir():
    savedir_path = filedialog.askdirectory(
        title='select the saving directory'
        )
    input_box2.insert(tkinter.END, savedir_path) 

def getLogfile():
    Logsheet_path = filedialog.askopenfilename(
        title='select the Logsheet',
        filetypes=[("Logsheet", ".xlsx")]
        )
    input_box3.insert(tkinter.END, Logsheet_path) 

def getICfile():
    ICfile_path = filedialog.askopenfilename(
        title='select the txt file ftom BL40B2',
        filetypes=[("text file from BL40B2 (*.txt)", ".txt")]
        )
    input_box4.insert(tkinter.END, ICfile_path)

def analysis():
    datapath=input_box1.get()
    savepath=input_box2.get()
    Logsheetfile=input_box3.get()
    ICfile=input_box4.get()

    Header = ['filename', 'time', 's', 'time2', 's2', 'Ex_time', 's3', 'IC', 'IC0', 'IC1', 'IC2']
    IC=pd.read_table(ICfile, header=None, names=Header, usecols = ['filename', 'time', 'Ex_time', 'IC0', 'IC1', 'IC2'], index_col = 'filename')
    LOG=pd.read_excel(Logsheetfile)
    samlist = LOG['sample']

    for i in samlist:
        df=LOG.loc[LOG['sample'] == i]
        samfile = df.iat[0,0]
        sol=df.iat[0,2]
        df2=LOG.loc[LOG['sample'] == sol]
        solfile = df2.iat[0,0]

        IC2_sol = IC.at[solfile, 'IC2']
        sol_file = datapath + '/' + solfile + '.chi'
        df_sol = pd.read_table(sol_file, skiprows = [0,1,2,3], header=None, sep = '\s+',  names = ('q', 'I(q)', 'noname'), usecols = ['q', 'I(q)'])
        df_sol['corrected_sol'] = df_sol['I(q)'] / IC2_sol 

        IC2_sam = IC.at[samfile, 'IC2']
        sam_file = datapath + '/' + samfile + '.chi'
        df_sam = pd.read_table(sam_file, skiprows = [0,1,2,3], header=None, sep = '\s+',  names = ('q', 'I(q)', 'noname'), usecols = ['q', 'I(q)'])
        df_sam['corrected_sam'] = df_sam['I(q)'] / IC2_sam

        df_sam[i] = df_sam['corrected_sam'] - df_sol['corrected_sol']
        df_fin = df_sam[['q', i]]
        df_fin2=df_fin.dropna()

        #抽出範囲
        df_fin3=df_fin2.query('0.02<q<1.8')

        df_fin3.to_csv(savepath + '/' + i + '.csv', index = False)  


#ウインドウの作成
root = tkinter.Tk()
root.title("Takano analysis app")
root.geometry("360x450")

#data--------
#入力欄の作成
input_box1 = tkinter.Entry(width=40)
input_box1.place(x=10, y=40)

#ラベルの作成
input_label = tkinter.Label(text="data directry")
input_label.place(x=10, y=10)

#ボタンの作成
button1 = tkinter.Button(text="参照",command=getdatadir)
button1.place(x=10, y=70)

#save--------
input_box2 = tkinter.Entry(width=40)
input_box2.place(x=10, y=140)

input_label = tkinter.Label(text="saving directry")
input_label.place(x=10, y=110)

button2 = tkinter.Button(text="参照",command=getsavedir)
button2.place(x=10, y=170)

#Log--------
input_box3= tkinter.Entry(width=40)
input_box3.place(x=10, y=240)

input_label = tkinter.Label(text="Logsheet")
input_label.place(x=10, y=210)

button3 = tkinter.Button(text="参照",command=getLogfile)
button3.place(x=10, y=270)

#ICfile--------
input_box4= tkinter.Entry(width=40)
input_box4.place(x=10, y=340)

input_label = tkinter.Label(text="text file from BL40B2")
input_label.place(x=10, y=310)

button4 = tkinter.Button(text="参照",command=getICfile)
button4.place(x=10, y=370)

#ボタンの作成
button = tkinter.Button(text="start analysis",command=analysis)
button.place(x=140, y=400)

#ウインドウの描画
root.mainloop()