# -*- coding: utf-8 -*-
import os
from typing import Any, Final

from tkinter import *
from tkinter import messagebox, ttk
from tkinter.filedialog import askopenfilename, askdirectory

from PIL import Image as imagen, ImageTk as imagenTk
from pyzbar.pyzbar import decode
import qrcode


PNG = ".png"
correction_dict: Final[dict[str, Any]]  = {
    'L7%': qrcode.constants.ERROR_CORRECT_L,
    'M15%': qrcode.constants.ERROR_CORRECT_M,
    'Q25%': qrcode.constants.ERROR_CORRECT_Q,
    'H30%': qrcode.constants.ERROR_CORRECT_H}
color_choose: Final[dict[str, list[str]]] = {
    'Blanco&Negro': ['white', 'black'],
    'Blanco&Azul': ['white', 'blue'],
    'Blanco&Rojo': ['white', 'red'],
    'Negro&Amarillo': ['yellow', 'black'],
    'Amarillo&Azul': ['yellow', 'blue'],
    'Amarillo&Rojo': ['yellow', 'red'],
    'Blanco&Verde': ['white', 'green'],
    'Amarillo&Verde': ['yellow', 'green']}
OUTPUT_DIR: Final[str] = ''
file_name = 'qrcode.png'

root = Tk()
root.title('Codificador y decodificador de QR')


# ---------------- Star Image ------------------

frame_1 = Frame(root)
frame_1.pack()


# ---------------- Init func ------------------
def create_qr_image(qr_file_name: str) -> None:
    global selected_image
    global photo_image
    global photo

    # output path ie "C:/Users/User_Name/Downloads/qrcode.png"
    selected_image = imagen.open(qr_file_name)
    selected_image = selected_image.resize((150, 150), imagen.ADAPTIVE)
    photo_image = imagenTk.PhotoImage(selected_image)

    photo = Label(frame_1, image=photo_image)
    # place(x=0, y=0, relwidth=1, relheight=1) #pack
    photo.grid(row=0, column=0, padx=10, pady=10)


def create_qr(qr_file_name, msg, data_capacity, correct_lvl,
              selected_color, selected_color_2):
    qr = qrcode.QRCode(
        version=data_capacity,
        # error percentage L 7%, M 15%, Q 25%, H 30%
        error_correction=correct_lvl,
        # choose array size or pixels per row and column
        box_size=5,
        border=4,
    )

    qr.add_data(msg)  # https://medium.com/@ngwaifoong92
    qr.make(fit=True)

    imag = qr.make_image(fill_color=selected_color,
                         back_color=selected_color_2)
    imag.save(qr_file_name)


def exit_app():
    value = messagebox.askokcancel(
        "Salir", "¿Deseas salir de la aplicación?")  # True or False
    if value is True:
        root.destroy()


def show_info():
    messagebox.showinfo("Taller3", "Codificar y decodificar código QR")


def show_licence():
    messagebox.showwarning(
        "Licencia", "producto bajo licencia GNU - Software libre")


def validate_input(input_arg, default_value):
    if input_arg == "" or input_arg.strip() == "":
        return default_value
    else:
        return input_arg


def qr_create() -> None:
    selected_dir = select_dir()
    directory = selected_dir if selected_dir else OUTPUT_DIR
    file_name = validate_input(file_name_var.get(), "qrcode.png")
    msg = validate_input(txt_msg.get('1.0', END), "testing 123@789?")
    data_capacity = validate_input(data_capacity_dd.get(), "1")
    correct_lvl = validate_input(correct_lvl_dd.get(), "L7%")
    new_color = validate_input(color_change_dd.get(), "Blanco&Negro")
    if PNG in file_name:
        file_name = directory + file_name
    else:
        file_name = directory + file_name + PNG

    create_qr(file_name, msg, data_capacity,
              correction_dict[correct_lvl],
              color_choose[new_color][1],
              color_choose[new_color][0])
    create_qr_image(file_name)

    messagebox.showinfo("Registro QR", f"QR generado con éxito: {file_name}")


def select_dir() -> str:
    tmp_dir = askdirectory()
    if tmp_dir:
        return tmp_dir + os.path.sep
    return ''


def load_qr_file() -> None:
    # Tk().withdraw()
    # we don't want a full GUI, so keep the root
    # window from appearing
    # show an "Open" dialog box and return the path to the selected file
    file_name = askopenfilename(filetypes=(
        ('imagenes', '*.png'), ('todos', '*.*')))
    create_qr_image(file_name)
    messagebox.showinfo(
            "Registro QR", "Archivo cargado con éxito: " + file_name)


def qr_read() -> None:
    imag = imagen.open(file_name)
    result = decode(imag)
    decoded = ''
    for i in result:
        decoded += i.data.decode("utf-8")

    txt_comment.delete(1.0, END)
    txt_comment.insert(1.0, decoded)
    messagebox.showinfo("Registro QR", f"Archivo leido con éxito: {file_name}")


# ---------------- Menu bar ------------------

bar_menu = Menu(root)
root.config(menu=bar_menu, width=300, height=300)

exit_menu = Menu(bar_menu, tearoff=0)
exit_menu.add_command(label="Salir", command=exit_app)

help_menu = Menu(bar_menu, tearoff=0)
help_menu.add_command(label="Licencia", command=show_licence)
help_menu.add_command(label="Acerca de...", command=show_info)

bar_menu.add_cascade(label="File", menu=exit_menu)
bar_menu.add_cascade(label="Ayuda", menu=help_menu)


# ---------------- Init fields ------------------

frame_2 = Frame()
frame_2.pack()

file_name_var = StringVar()


# ---------------- second column ------------------

txt_msg = Text(frame_2, width=16, height=5)
txt_msg.grid(row=0, column=1, padx=10, pady=10)
y_scroll = Scrollbar(frame_2, command=txt_msg.yview)
y_scroll.grid(row=0, column=2, sticky="nsew")
txt_msg.config(yscrollcommand=y_scroll.set)

data_capacity_opt = [i for i in range(1, 41)]
data_capacity_dd = ttk.Combobox(
    frame_2, width=16, state='readonly', values=data_capacity_opt)
data_capacity_dd.grid(row=1, column=1, padx=10, pady=10)
data_capacity_dd.current(0)

correct_lvl_opt = ['L7%', 'M15%', 'Q25%', 'H30%']
correct_lvl_dd = ttk.Combobox(
    frame_2, width=16, state='readonly', values=correct_lvl_opt)
correct_lvl_dd.grid(row=2, column=1, padx=10, pady=10)
correct_lvl_dd.current(0)

color_change_opt = ['Blanco&Negro', 'Blanco&Azul',
                    'Blanco&Rojo', 'Negro&Amarillo',
                    'Amarillo&Azul', 'Amarillo&Rojo',
                    'Blanco&Verde', 'Amarillo&Verde']
color_change_dd = ttk.Combobox(
    frame_2, width=16, state='readonly', values=color_change_opt)
color_change_dd.grid(row=3, column=1, padx=10, pady=10)
color_change_dd.current(0)

file_name_entry = Entry(frame_2, textvariable=file_name_var)
file_name_entry.grid(row=4, column=1, padx=10, pady=10)


# ---------------- first column ------------------

msg_label = Label(frame_2, text="Mensaje: ")
msg_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

capacity_label = Label(frame_2, text="Conf capacidad de datos: ")
capacity_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

correct_lvl_label = Label(frame_2, text="Nivel de correción de errores: ")
correct_lvl_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

color_label = Label(frame_2, text="Cambiar colores QR: ")
color_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)

file_name_label = Label(frame_2, text="Nombre Archivo: ")
file_name_label.grid(row=4, column=0, sticky="e", padx=10, pady=10)


# ---------------- Bottom buttons ------------------

frame_3 = Frame(root)
frame_3.pack()

create_button = Button(frame_3, text="Codificar",
                       width="10", height="1", command=qr_create)
create_button.grid(row=0, column=0, padx=10, pady=10)
load_button = Button(frame_3, text="Cargar archivo QR",
                     width="15", height="1", command=load_qr_file)
load_button.grid(row=0, column=1, padx=10, pady=10)
decypher_button = Button(frame_3, text="Leer QR",
                         width="10", height="1", command=qr_read)
decypher_button.grid(row=0, column=2, padx=10, pady=10)


# ---------------- Read Msg ------------------

frame_4 = Frame()
frame_4.pack()

txt_comment = Text(frame_4, width=40, height=3)
txt_comment.grid(row=0, column=1, padx=10, pady=10)
y_scroll = Scrollbar(frame_4, command=txt_comment.yview)
y_scroll.grid(row=0, column=2, sticky="nsew")
txt_comment.config(yscrollcommand=y_scroll.set)


# ---------------- Init Values ------------------

create_qr(file_name, "testing 123@789?", 1,
          qrcode.constants.ERROR_CORRECT_L, 'black', 'white')
create_qr_image(file_name)

root.mainloop()
