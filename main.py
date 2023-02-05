import customtkinter as Ctk
import password
import tkinter

from PIL import Image
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


# Шаблон программы
class App(Ctk.CTk):
    def __init__(self):
        super().__init__()

        # Настройки окна
        self.geometry('460x370')
        self.title('Password generator')
        self.resizable(False, False)

        # Логотип
        self.logo = Ctk.CTkImage(
            dark_image=Image.open('img.png'),
            size=(460, 150)
        )
        # Для того, чтобы отобразить логотип помещаем его в виджет Label,
        # master=self
        # размещает на основном окне программы
        self.logo_label = Ctk.CTkLabel(master=self, text='', image=self.logo)
        # С помощью метода упаковки grid размещаем виджет в 0 строке и
        # 0 столбце основного окна
        self.logo_label.grid(row=0, column=0)

        # Фрейм для вывода пароля
        self.password_frame = Ctk.CTkFrame(master=self, fg_color='transparent')
        self.password_frame.grid(row=1, column=0, padx=(20, 20), sticky='nsew')

        self.entry_password = Ctk.CTkEntry(
            master=self.password_frame,
            width=300
        )
        self.entry_password.grid(row=0, column=0, padx=(0, 20))

        # Кнопка генерации пароля
        self.btn_generate = Ctk.CTkButton(
            master=self.password_frame,
            text='Generate', width=100,
            command=self.set_password
        )
        self.btn_generate.grid(row=0, column=1)

        # Фрейм настроек изменения сложности пароля
        self.settings_frame = Ctk.CTkFrame(master=self)
        self.settings_frame.grid(
            row=2, column=0,
            padx=(20, 20),
            pady=(20, 0),
            sticky='nsew'
        )

        # Слайдер для установки длины пароля
        self.password_length_slider = Ctk.CTkSlider(
            master=self.settings_frame,
            from_=0,
            to=100,
            number_of_steps=100,
            command=self.slider_event
        )
        self.password_length_slider.grid(
            row=1,
            column=0,
            columnspan=3,
            pady=(20, 20),
            sticky='ew'
        )

        # Виджет для вывода длины пароля, установленной слайдером
        self.password_length_entry = Ctk.CTkEntry(
            master=self.settings_frame,
            width=50
        )
        self.password_length_entry.grid(
            row=1,
            column=3,
            padx=(20, 10),
            sticky='we'
        )

        # Чек-боксы для установки сложности пароля
        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = Ctk.CTkCheckBox(
            master=self.settings_frame,
            text='0-9',
            variable=self.cb_digits_var,
            onvalue=digits,
            offvalue=''
        )
        self.cb_digits.grid(row=2, column=0, padx=10)

        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = Ctk.CTkCheckBox(
            master=self.settings_frame,
            text='a-z',
            variable=self.cb_lower_var,
            onvalue=ascii_lowercase,
            offvalue=''
        )
        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = Ctk.CTkCheckBox(
            master=self.settings_frame,
            text='A-Z',
            variable=self.cb_upper_var,
            onvalue=ascii_uppercase,
            offvalue=''
        )
        self.cb_upper.grid(row=2, column=2)

        self.cb_symbol_var = tkinter.StringVar()
        self.cb_symbol = Ctk.CTkCheckBox(
            master=self.settings_frame,
            text='@#$%',
            variable=self.cb_symbol_var,
            onvalue=punctuation,
            offvalue=''
        )
        self.cb_symbol.grid(row=2, column=3)

        # Выбор цветового оформления
        self.appearance_mode_option_menu = Ctk.CTkOptionMenu(
            master=self.settings_frame,
            values=['Light', 'Dark', 'System'],
            command=self.appearance_mode_option_event
        )
        self.appearance_mode_option_menu.grid(
            row=3,
            column=0,
            columnspan=4,
            pady=(10, 10)
        )

        # Значения по умолчанию
        self.password_length_slider.set(12)
        self.password_length_entry.insert(0, 12)
        self.appearance_mode_option_menu.set('System')

    def get_characters(self):
        chars = ''.join(
            self.cb_digits_var.get() +
            self.cb_lower_var.get() +
            self.cb_upper_var.get() +
            self.cb_symbol_var.get()
        )

        return chars

    # Функция генерации пароля
    def set_password(self):
        self.entry_password.delete(0, 'end')
        self.entry_password.insert(0, password.create_new(
            length=int(self.password_length_slider.get()),
            characters=self.get_characters()
        ))

    # Функция для обработки изменения значений слайдера
    def slider_event(self, value):
        self.password_length_entry.delete(0, 'end')
        self.password_length_entry.insert(0, int(value))

    # Функция изменения цветового оформления
    def appearance_mode_option_event(self, new_appearance_mode):
        Ctk.set_appearance_mode(new_appearance_mode)


if __name__ == '__main__':
    app = App()
    app.mainloop()
