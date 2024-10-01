import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#init
window=tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("oi")

#variable dan fungsi
NAMA_DEPAN=tk.StringVar()
NAMA_BELAKANG=tk.StringVar()

def tombol_click():
    '''fungsi ini dipanggil oleh tombol'''
    pesan=f"{NAMA_DEPAN.get()},{NAMA_BELAKANG.get()}"
    showinfo(tittle="oi",message=pesan)

#frame input
input_frame=ttk.Frame(window)
#penempatan: grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

#komponen komponen
#1.label nama depan
nama_label_depan=ttk.Label(input_frame,text="Nama Depan:")
nama_label_depan.pack(padx=10,fill="x",expand=True)
#2.entry nama depan
nama_depan_entry=ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)
#3.label nama belakang
nama_label_belakang=ttk.Label(input_frame,text="Nama Belakang:")
nama_label_belakang.pack(padx=10,fill="x",expand=True)
#4.entry nama belakang
nama_belakang_entry=ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)
#5.tombol
tombol=ttk.Button(input_frame,text="pencet",command=tombol_click)
tombol.pack(padx=10,pady=10,fill="x",expand=True)

#mainloop window
window.mainloop()