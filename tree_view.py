import tkinter as tk
from tkinter import ttk
from tkinter import StringVar


class TreeView(tk.Toplevel):
    BACKGROUND_COLOR = '#3E065F'
    WIDGET_BG_COLOR = '#a645d9'
    ACTIVE_BACKGROUND_COLOR = '#916BBF'

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title('Password Manager')
        self.config(bg=self.BACKGROUND_COLOR)
        self.resizable(False, False)
        self.geometry('350x270+460+450')
        self._app_interface()

    def _app_interface(self):
        self.var_search_entry = StringVar()
        self.search_entry = ttk.Entry(self,
                                      textvariable=self.var_search_entry,
                                      width=25)
        self.search_entry.place(x=5, y=5, height=25)
        self.search_button = tk.Button(self,
                                       activebackground=self.WIDGET_BG_COLOR,
                                       bg=self.WIDGET_BG_COLOR,
                                       command=self.controller.search_data,
                                       fg='white',
                                       text='Buscar',
                                       width=12)
        self.search_button.place(x=165, y=5)
        self.refresh_button = tk.Button(self,
                                        activebackground=self.WIDGET_BG_COLOR,
                                        bg=self.WIDGET_BG_COLOR,
                                        command=self.controller.clean_and_show_treeview,
                                        fg='white',
                                        text='Reiniciar',
                                        width=11)
        self.refresh_button.place(x=260, y=5)
        self.columns = ('website', 'user', 'password')
        self.tree = ttk.Treeview(self, columns=self.columns, show='headings')
        self.tree.column('# 1', anchor=tk.CENTER, stretch=tk.NO, width=112)
        self.tree.heading('# 1', text="Website")
        self.tree.column('# 2', anchor=tk.CENTER, stretch=tk.NO, width=112)
        self.tree.heading('# 2', text="Usuario")
        self.tree.column('# 3', anchor=tk.CENTER, stretch=tk.NO, width=115)
        self.tree.heading('# 3', text="Password")
        self.tree.place(relx=0.01, rely=0.13, width=342, height=200)

        self.modify_button = tk.Button(self,
                                       activebackground=self.WIDGET_BG_COLOR,
                                       bg=self.WIDGET_BG_COLOR,
                                       command=self.controller.create_pop_up,
                                       fg='white',
                                       text='Modificar',
                                       width=23)
        self.modify_button.place(x=5, y=240)

        self.delete_button = tk.Button(self,
                                       activebackground=self.WIDGET_BG_COLOR,
                                       bg=self.WIDGET_BG_COLOR,
                                       command=self.controller.delete_data,
                                       fg='white',
                                       text='Eliminar',
                                       width=22)

        self.delete_button.place(x=182, y=240)

        self.tree.bind('<ButtonRelease-1>', self.controller.selected_row)


class PopUp(tk.Toplevel):
    BACKGROUND_COLOR = '#3E065F'
    WIDGET_BG_COLOR = '#a645d9'
    ACTIVE_BACKGROUND_COLOR = '#916BBF'

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title('Modificar Datos')
        self.config(bg=self.BACKGROUND_COLOR)
        self.resizable(False, False)
        self.geometry('305x135+650+350')
        self._pop_up_interface()

    def _pop_up_interface(self):
        self.website_label = tk.Label(self,
                                      bg=self.BACKGROUND_COLOR,
                                      fg='white',
                                      text='Website:')
        self.website_label.place(x=10, y=10)

        self.var_website_entry = StringVar()
        self.website_entry = ttk.Entry(self,
                                       state='disabled',
                                       textvariable=self.var_website_entry,
                                       width=35)
        self.website_entry.place(x=75, y=10)

        self.usuario_label = tk.Label(self,
                                      bg=self.BACKGROUND_COLOR,
                                      fg='white',
                                      text='Usuario:')
        self.usuario_label.place(x=10, y=40)

        self.var_usuario_entry = StringVar()
        self.usuario_entry = ttk.Entry(self,
                                       textvariable=self.var_usuario_entry,
                                       width=35)
        self.usuario_entry.place(x=75, y=40)

        self.password_label = tk.Label(self,
                                       bg=self.BACKGROUND_COLOR,
                                       fg='white',
                                       text='Password:')
        self.password_label.place(x=10, y=70)

        self.var_password_entry = StringVar()
        self.password_entry = ttk.Entry(self,
                                        textvariable=self.var_password_entry,
                                        width=35)
        self.password_entry.place(x=75, y=70)

        self.modify_button = tk.Button(self,
                                       activebackground=self.WIDGET_BG_COLOR,
                                       bg=self.WIDGET_BG_COLOR,
                                       command=self.controller.update_data,
                                       fg='white',
                                       text='Modificar',
                                       width=39)
        self.modify_button.place(x=10, y=100)
