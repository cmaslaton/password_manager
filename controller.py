from main_view import MainView, LoginWindow
import math
from model import Model
from pass_generator_view import PasswordGenerator
# import pyperclip
import random
import tkinter as tk
from tkinter import messagebox
from tree_view import TreeView, PopUp


class Controller:

    def __init__(self):
        self.main_view = MainView(self)
        self.model = Model()
        self.password_generator = None
        self.tree_view = None
        self.pop_up = None

    def main(self):
        self.main_view.main()

    ############################################################
    ################# MÉTODOS - GENERADOR PASS #################
    ############################################################

    def create_pass_generator(self):
        """Llama al generador de passwords"""
        if self.password_generator is None:
            self.password_generator = PasswordGenerator(self)
            self.password_generator.protocol('WM_DELETE_WINDOW', self.close_password_generator)
        else:
            print('Mariano no te hagas el piola. Se abre sólo una ventana.')

    def generar_password(self):
        """Genera la password aleatoria"""

        def random_letters():
            return [random.choice(letras) for _ in (range(character_qty + remainder))]

        def random_numbers():
            return [random.choice(numeros) for _ in (range(character_qty))]

        def random_symbols():
            return [random.choice(simbolos) for _ in (range(character_qty))]

        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        pass_len = self.password_generator.scale_widget.get()
        shuffled_pass = ''

        if not self.password_generator.letters_boolvar.get() and not self.password_generator.numbers_boolvar.get() and not self.password_generator.symbols_boolvar.get():
            messagebox.showerror(message='Mariano no te hagas el vivo y marcá al menos una opción.',
                                 title='Error!')
        else:
            if self.password_generator.letters_boolvar.get() and self.password_generator.numbers_boolvar.get() and self.password_generator.symbols_boolvar.get():
                character_qty = math.floor(pass_len / 3)
                remainder = pass_len % 3
                rdm_let, rdm_num, rdm_symb = random_letters(), random_numbers(), random_symbols()
                shuffled_pass = [*rdm_let, *rdm_num, *rdm_symb]
                random.shuffle(shuffled_pass)

            elif self.password_generator.letters_boolvar.get() and self.password_generator.numbers_boolvar.get():
                character_qty = math.floor(pass_len / 2)
                remainder = pass_len % 2
                rdm_let, rdm_num = random_letters(), random_numbers()
                shuffled_pass = [*rdm_let, *rdm_num]
                random.shuffle(shuffled_pass)

            elif self.password_generator.letters_boolvar.get() and self.password_generator.symbols_boolvar.get():
                character_qty = math.floor(pass_len / 2)
                remainder = pass_len % 2
                rdm_let, rdm_symb = random_letters(), random_symbols()
                shuffled_pass = [*rdm_let, *rdm_symb]
                random.shuffle(shuffled_pass)

            elif self.password_generator.symbols_boolvar.get() and self.password_generator.numbers_boolvar.get():
                character_qty = math.floor(pass_len / 2)
                remainder = pass_len % 2
                rdm_symb, rdm_numb = random_symbols(), random_numbers()
                shuffled_pass = [*rdm_symb, *rdm_numb]
                random.shuffle(shuffled_pass)

            elif self.password_generator.letters_boolvar.get():
                character_qty, remainder = pass_len, 0
                shuffled_pass = [*random_letters()]
                random.shuffle(shuffled_pass)

            elif self.password_generator.numbers_boolvar.get():
                character_qty, remainder = pass_len, 0
                shuffled_pass = [*random_numbers()]
                random.shuffle(shuffled_pass)

            elif self.password_generator.symbols_boolvar.get():
                character_qty, remainder = pass_len, 0
                shuffled_pass = [*random_symbols()]
                random.shuffle(shuffled_pass)

            shuffled_pass = "".join(shuffled_pass)
            # pyperclip.copy(shuffled_pass)

            return shuffled_pass

    def close_password_generator(self):
        self.password_generator.destroy()
        self.password_generator = None

    def set_password(self):
        """Asigna la pass generada a los entrys del main_view y del pass_gen_view"""
        password = self.generar_password()
        self.password_generator.var_generated_password.set(password)
        self.main_view.var_password_entry.set(password)

    ############################################################
    ################### MÉTODOS - MAIN_VIEW ####################
    ############################################################

    def save_data(self):
        """obtiene la información del formulario, si está ok salva los datos"""
        # Chequea que los campos sean válidos
        if not self.main_view.var_website_entry.get():
            tk.messagebox.showerror(title='Error!', message='Hay campos sin completar')
        elif not self.main_view.var_email_username_entry.get():
            tk.messagebox.showerror(title='Error!', message='Hay campos sin completar')
        elif not self.main_view.var_password_entry.get():
            tk.messagebox.showerror(title='Error!', message='Hay campos sin completar')
        else:
            # Pide confirmación de alta
            msg_box = tk.messagebox.askquestion('Alta Password', 'Confirmás la carga de datos?',
                                                icon='warning')
            if msg_box == 'yes':
                data_dict = {
                    'website': self.main_view.var_website_entry.get(),
                    'username': self.main_view.var_email_username_entry.get(),
                    'password': self.main_view.var_password_entry.get(),
                }
                # Salva en el modelo
                self.model.save_data(data_dict=data_dict)
                self.clear_data()  # limpia el formulario de alta
                if self.tree_view is not None:
                    self.clean_and_show_treeview()

    def clear_data(self):
        """limpia los campos"""
        self.main_view.var_website_entry.set('')
        self.main_view.var_email_username_entry.set('')
        self.main_view.var_password_entry.set('')

    ############################################################
    ################### MÉTODOS - TREEVIEW #####################
    ############################################################

    def create_pop_up(self):
        """crea el pop"""
        if self.pop_up is None:
            self.pop_up = PopUp(self)
            self.pop_up.protocol('WM_DELETE_WINDOW', self.close_pop_up)
            try:
                row = self.selected_row()
                self.pop_up.var_website_entry.set(row[0])
                self.pop_up.var_usuario_entry.set(row[1])
                self.pop_up.var_password_entry.set(row[2])
            except:
                self.close_pop_up()
                tk.messagebox.showwarning(title='Pillín', message='Seleccioná los datos que quieras modificar!')
        else:
            print('Mariano no te hagas el piola. Se abre sólo una ventana.')

    def create_treeview(self):
        """crea el treeview"""
        if self.tree_view is None:
            self.tree_view = TreeView(self)
            self.tree_view.protocol('WM_DELETE_WINDOW', self.close_treeview)
            self.show_data()
        else:
            print('Mariano no te hagas el piola. Se abre sólo una ventana.')

    def clean_treeview(self):
        """limpia la vista del treeview"""
        self.tree_view.tree.delete(*self.tree_view.tree.get_children())

    def clean_and_show_treeview(self):
        self.clean_treeview()
        self.show_data()

    def close_pop_up(self):
        self.pop_up.destroy()
        self.pop_up = None

    def close_treeview(self):
        """cierra el treeview y establece el atributo treeview en None para que se puede volver a abrir"""
        self.tree_view.destroy()
        self.tree_view = None

    def delete_data(self):
        """borra la información seleccionada y hace refresh del treeview"""
        try:
            msg_box = tk.messagebox.askquestion('Eliminar Datos',
                                                'Confirmás la eliminación de los datos seleccionados?',
                                                icon='warning')
            if msg_box == 'yes':
                self.model.delete_data(self.selected_row())
                self.clean_and_show_treeview()
        except IndexError:
            print('Que hacés Marianito')

    def get_pop_up_data(self) -> list:
        """captura y devuelve los datos del pop up"""
        website = self.pop_up.var_website_entry.get()
        usuario = self.pop_up.var_usuario_entry.get()
        password = self.pop_up.var_password_entry.get()
        return [website, usuario, password]

    def search_data(self):
        """hace la búsqueda de la información en la db y la trae al treeview"""
        search_entry = self.tree_view.var_search_entry.get()
        self.clean_treeview()
        rows = self.model.search_data(website=search_entry)
        for row in rows:
            self.tree_view.tree.insert('', tk.END, values=row)

    def selected_row(self, *args) -> list:
        """devuelve la fila seleccionada"""
        if self.tree_view is not None:
            current_item = self.tree_view.tree.focus()
            row = self.tree_view.tree.item(current_item)['values']
            return row

    def show_data(self):
        """muestra los datos de la db en el view del treeview"""
        paswers = self.model.get_data()
        for paswer in paswers:
            self.tree_view.tree.insert('', tk.END, values=paswer)

    def update_data(self):
        if not self.pop_up.var_website_entry.get():
            tk.messagebox.showerror(title='Error!', message='Hay campos sin completar')
        elif not self.pop_up.var_usuario_entry.get():
            tk.messagebox.showerror(title='Error!', message='Hay campos sin completar')
        elif not self.pop_up.var_password_entry.get():
            tk.messagebox.showerror(title='Error!', message='Hay campos sin completar')
        else:
            msg_box = tk.messagebox.askquestion('Modificar Datos', 'Confirmás la modificación de los datos?',
                                                icon='warning')
            if msg_box == 'yes':
                self.model.update_data(old_data=self.selected_row(), new_data=self.get_pop_up_data())
                self.close_pop_up()
                self.clean_and_show_treeview()


if __name__ == '__main__':
    login = LoginWindow()
    login.mainloop()
    if login.password:
        controller = Controller()
        controller.main()
