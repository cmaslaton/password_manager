import tkinter as tk
from tkinter import StringVar, BooleanVar


class PasswordGenerator(tk.Toplevel):
    BACKGROUND_COLOR = '#3E065F'
    WIDGET_BG_COLOR = '#a645d9'
    ACTIVE_BACKGROUND_COLOR = '#916BBF'

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.config(bg=self.BACKGROUND_COLOR)
        self.geometry('305x560+820+160')
        self.resizable(False, False)
        self.title('Password Generator')
        self._pass_generator_interface()

    def _pass_generator_interface(self):
        self.canvas = tk.Canvas(self,  # Hay que indicar a qué ventana corresponden los widgets
                                bg=self.BACKGROUND_COLOR,
                                height=110,
                                highlightthickness=0,
                                width=306)
        self.logo_img = tk.PhotoImage(file='logo.png')
        self.canvas.create_image(153, 55, image=self.logo_img)
        self.canvas.grid(column=0, row=0)

        # Título
        tk.Label(self,
                 bg=self.BACKGROUND_COLOR,
                 fg='white',
                 font=('Arial', 15, 'bold'),
                 height=2,
                 text='Generador de Password xD').grid(column=0, row=1)

        self.generated_password_label_1 = tk.Label(self,
                                                   bg=self.BACKGROUND_COLOR,
                                                   fg='white',
                                                   padx=17,
                                                   text='Password Generada:')
        self.generated_password_label_1.grid(column=0, row=2, sticky='W')

        self.var_generated_password = StringVar()
        self.generated_password_label_2 = tk.Label(self,
                                                   bg=self.WIDGET_BG_COLOR,
                                                   fg='black',
                                                   width=29,
                                                   font=('Arial', 11, 'bold'),
                                                   textvariable=self.var_generated_password)
        self.generated_password_label_2.grid(column=0, row=3)

        tk.Label(self, text='', pady=2, bg=self.BACKGROUND_COLOR).grid(column=0, row=4)

        self.password_options_label = tk.Label(self,
                                               bg=self.BACKGROUND_COLOR,
                                               fg='white',
                                               padx=17,
                                               text='Longitud de la Password:')
        self.password_options_label.grid(column=0, row=5, sticky='W')

        self.scale_widget = tk.Scale(self,
                                     activebackground=self.ACTIVE_BACKGROUND_COLOR,
                                     bg=self.WIDGET_BG_COLOR,
                                     from_=4,
                                     highlightbackground=self.WIDGET_BG_COLOR,
                                     length=263,
                                     orient='horizontal',
                                     to=24,
                                     troughcolor=self.WIDGET_BG_COLOR)
        self.scale_widget.grid(column=0, row=6)

        tk.Label(self, text='', pady=2, bg=self.BACKGROUND_COLOR).grid(column=0, row=7)

        self.password_options_label = tk.Label(self,
                                               bg=self.BACKGROUND_COLOR,
                                               fg='white',
                                               padx=17,
                                               text='Opciones:')
        self.password_options_label.grid(column=0, row=8, sticky='W')

        self.numbers_boolvar = BooleanVar()
        self.numbers_boolvar.set(True)
        self.include_numbers = tk.Checkbutton(self,
                                              activebackground=self.WIDGET_BG_COLOR,
                                              anchor='w',
                                              bg=self.WIDGET_BG_COLOR,
                                              height=2,
                                              text='Incluir números (0-9)',
                                              variable=self.numbers_boolvar,
                                              width=34)
        self.include_numbers.grid(column=0, row=9)

        self.letters_boolvar = BooleanVar()
        self.letters_boolvar.set(True)
        self.include_letters = tk.Checkbutton(self,
                                              activebackground=self.WIDGET_BG_COLOR,
                                              anchor='w',
                                              bg=self.WIDGET_BG_COLOR,
                                              height=2,
                                              text='Incluir letras (Aa-Zz)',
                                              variable=self.letters_boolvar,
                                              width=34)
        self.include_letters.grid(column=0, row=10, pady=5)

        self.symbols_boolvar = BooleanVar()
        self.symbols_boolvar.set(True)
        self.include_symbols = tk.Checkbutton(self,
                                              activebackground=self.WIDGET_BG_COLOR,
                                              anchor='w',
                                              bg=self.WIDGET_BG_COLOR,
                                              height=2,
                                              text='Incluir Símbolos (!, #, $, %, &, (, ), *, +)',
                                              variable=self.symbols_boolvar,
                                              width=34)
        self.include_symbols.grid(column=0, row=11)

        tk.Label(self, text='', pady=10, bg=self.BACKGROUND_COLOR).grid(column=0, row=12)

        self.generate_button = tk.Button(self,
                                         activebackground=self.WIDGET_BG_COLOR,
                                         bg=self.WIDGET_BG_COLOR,
                                         command=self.controller.set_password,
                                         fg='white',
                                         # font=('Arial', 16, 'bold'),
                                         text='Generar Password',
                                         width=37)
        # self.generate_button.grid(column=0, row=13)
        self.generate_button.place(x=19, y=530)
