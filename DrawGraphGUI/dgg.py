version = 2.0
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import drawgraph

win_width = 400
win_height = 150
size_str = "{}x{}".format(win_width, win_height)

window = tkinter.Tk()
window.title('DrawGraph ' + str(version))
window.geometry(size_str)
window.resizable(0, 0)
window.iconphoto(False, tkinter.PhotoImage(file='dgg.png'))

################################
PathLbl = tkinter.Label(window, text='Путь к файлу')
PathLbl.place(x=5, y=8)

PathEntryString = tkinter.StringVar()
PathEntry = tkinter.Entry(window, width=29, textvariable=PathEntryString)
PathEntry.place(x=110, y=8)

def GetFilePath():
    file_path = tkinter.filedialog.askopenfilename(title = "Выбор файла")
    if len(file_path) > 0:
        PathEntry.delete(0,'end')
        PathEntry.insert(0,file_path)

GetPathBtn = tkinter.Button(window, text='...', command=GetFilePath)
GetPathBtn.place(x=win_width - 45, y=5)
###################################
Col_1Lbl = tkinter.Label(window, text='Колонка 1')
Col_1Lbl.place(x=30, y=45)

Col1EntryString = tkinter.StringVar()
Col_1Entry = tkinter.Entry(window, width=6, textvariable=Col1EntryString)
Col_1Entry.place(x=110, y=45)
####################################
def CheckState():
    if CheckFlag.get():
        Col_2Lbl.config(state='active')
        Col_2Entry.config(state='normal')
        OffsetLbl.config(state='active')
        OffsetEntry.config(state='normal')
    else:
        Col_2Lbl.config(state='disabled')
        Col_2Entry.config(state='disabled')
        OffsetLbl.config(state='disabled')
        OffsetEntry.config(state='disabled')

CheckFlag = tkinter.IntVar()
Col_2Check = tkinter.Checkbutton(window, variable=CheckFlag, command=CheckState)
Col_2Check.place(x=5, y=80)


Col_2Lbl = tkinter.Label(window, text='Колонка 2')
Col_2Lbl.place(x=30, y=82)
Col_2Lbl.config(state='disabled')

Col2EntryString = tkinter.StringVar()
Col_2Entry = tkinter.Entry(window, width=6, textvariable=Col2EntryString)
Col_2Entry.place(x=110, y=82)
Col_2Entry.config(state='disabled')

OffsetLbl = tkinter.Label(window, text='Смещение')
OffsetLbl.place(x=30, y=119)
OffsetLbl.config(state='disabled')

OffsetEntryString = tkinter.StringVar()
OffsetEntry = tkinter.Entry(window, width=6, textvariable=OffsetEntryString)
OffsetEntry.place(x=110, y=119)
OffsetEntry.config(state='disabled')
################################
def ConstructGraph():
    path = PathEntryString.get()
    if len(path) == 0:
        tkinter.messagebox.showerror('Ошибка!!!', 'Необходимо указать файл!')
        return
    col_1 = Col1EntryString.get()
    if len(col_1) == 0:
        tkinter.messagebox.showerror('Ошибка!!!', 'Необходимо задать номер колонки 1!')
        return
    if col_1.isdigit() is False:
        tkinter.messagebox.showerror('Ошибка!!!', 'Номер колонки должен быть числом')
        return

    if CheckFlag.get():
        col_2 = Col2EntryString.get()
        if len(col_2) == 0:
            tkinter.messagebox.showerror('Ошибка!!!', 'Необходимо задать номер колонки 2!')
            return
        if col_2.isdigit() is False:
            tkinter.messagebox.showerror('Ошибка!!!', 'Номер колонки должен быть числом')
            return

        offset = OffsetEntryString.get()
        if len(offset) != 0:
            if offset.isdigit() is False:
                tkinter.messagebox.showerror('Ошибка!!!', 'Смещение должено быть числом')
                return
        else:
            offset = '0'
        result = drawgraph.drawgraph(path, int(col_1), True, int(col_2), int(offset))
    else:
        result = drawgraph.drawgraph(path, int(col_1))

    if result[0] is False:
        tkinter.messagebox.showerror('Ошибка!!!', result[1])
    else:
        tkinter.messagebox.showinfo('Успешно', result[1])

ConstructBtn = tkinter.Button(window, text='Построить', height = 5, width = 24, command=ConstructGraph)
ConstructBtn.place(x=174, y=44)
###############################

window.mainloop()
