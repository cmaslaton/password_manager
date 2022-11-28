import tkinter as tk
from tkinter import StringVar
from tkinter import ttk


class MainView(tk.Tk):
    BACKGROUND_COLOR = '#3E065F'
    WIDGET_BG_COLOR = '#a645d9'
    ACTIVE_BACKGROUND_COLOR = '#916BBF'

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title('Password Manager')
        self.config(bg=self.BACKGROUND_COLOR)
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')
        self.geometry('350x250+460+160')
        self._main_interface()

    def _main_interface(self):
        self.canvas = tk.Canvas(self,
                                bg=self.BACKGROUND_COLOR,
                                height=160,
                                highlightthickness=0,
                                width=300)
        self.logo_img = tk.PhotoImage(file='logo.png')
        self.canvas.create_image(150, 60, image=self.logo_img)  # X, Y
        self.canvas.place(x=25, y=1)

        self.website_label = tk.Label(self,
                                      bg=self.BACKGROUND_COLOR,
                                      fg='white',
                                      text='Website:')
        self.website_label.place(x=5, y=130)
        self.var_website_entry = StringVar()
        self.website_entry = ttk.Entry(textvariable=self.var_website_entry,
                                       width=45)
        self.website_entry.place(x=69, y=130)
        self.website_entry.focus()  # Para que por defecto se pueda escribir acá cuando abre la app

        self.email_username_label = tk.Label(self,
                                             bg=self.BACKGROUND_COLOR,
                                             fg='white',
                                             text='Usuario:')
        self.email_username_label.place(x=5, y=160)
        self.var_email_username_entry = StringVar()
        self.email_username_entry = ttk.Entry(textvariable=self.var_email_username_entry,
                                              width=45)
        self.email_username_entry.place(x=69, y=160)

        self.password_label = tk.Label(self,
                                       bg=self.BACKGROUND_COLOR,
                                       fg='white',
                                       text='Password:')
        self.password_label.place(x=5, y=190)

        self.var_password_entry = StringVar()
        self.password_entry = ttk.Entry(textvariable=self.var_password_entry,
                                        width=45)
        self.password_entry.place(x=69, y=190)

        self.consulta_button = tk.Button(self,
                                         activebackground=self.WIDGET_BG_COLOR,
                                         bg=self.WIDGET_BG_COLOR,
                                         command=self.controller.create_treeview,
                                         fg='white',
                                         text='Consultas',
                                         width=15)
        self.consulta_button.place(x=5, y=220)

        self.generate_button = tk.Button(self,
                                         activebackground=self.WIDGET_BG_COLOR,
                                         bg=self.WIDGET_BG_COLOR,
                                         command=self.controller.create_pass_generator,
                                         fg='white',
                                         text='Generador de Pass',
                                         width=15)
        self.generate_button.place(x=122, y=220)

        self.save_button = tk.Button(self,
                                     activebackground=self.WIDGET_BG_COLOR,
                                     bg=self.WIDGET_BG_COLOR,
                                     command=self.controller.save_data,
                                     fg='white',
                                     text='Guardar',
                                     width=14)
        self.save_button.place(x=239, y=220)

    def main(self):
        self.mainloop()


class LoginWindow(tk.Tk):
    BACKGROUND_COLOR = '#3E065F'
    WIDGET_BG_COLOR = '#a645d9'
    ACTIVE_BACKGROUND_COLOR = '#916BBF'

    def __init__(self):
        super().__init__()
        self.title('Ingresar Clave Maestra')
        self.config(bg=self.BACKGROUND_COLOR)
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')
        self.geometry('305x73+650+350')
        self.password = False

        self.clave_label = tk.Label(self,
                                    bg=self.BACKGROUND_COLOR,
                                    fg='white',
                                    text='Clave:')
        self.clave_label.place(x=10, y=10)

        self.var_clave_entry = StringVar()
        self.clave_entry = ttk.Entry(self,
                                     show='*',
                                     textvariable=self.var_clave_entry,
                                     width=35)
        self.clave_entry.place(x=75, y=10)

        self.modify_button = tk.Button(self,
                                       activebackground=self.WIDGET_BG_COLOR,
                                       bg=self.WIDGET_BG_COLOR,
                                       command=self.clave_maestra,
                                       fg='white',
                                       text='Ingresar',
                                       width=39)
        self.modify_button.place(x=10, y=40)

    def clave_maestra(self):
        # if (self.var_clave_entry.get() == 'reshpirau_hoteu') or (self.var_clave_entry.get() == '24x7'):
            self.password = True
            self.destroy()
