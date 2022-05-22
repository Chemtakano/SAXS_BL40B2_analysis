import tkinter
from tkinter import filedialog

class Application(tkinter.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=380, height=280, borderwidth=1, relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()
    
    def create_widgets(self):
        quit_btn=tkinter.Button(self)
        quit_btn['text']='exit'
        quit_btn['command']=self.root.destroy
        quit_btn.pack(side='bottom')

        data_btn=tkinter.Button(self)
        data_btn['text']='set the data directry'
        data_btn['command']=filedialog.askdirectory(
            title='select the data directory'
            )
        data_btn.pack()





root=tkinter.Tk()
root.title('takano')
app=Application(root=root)
app.mainloop()


