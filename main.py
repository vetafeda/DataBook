import random
import string
import sys
import tkinter as tkin # встроенная библиотека для графического интерфейса
from random import randint
from tkinter import ttk
from PIL import ImageTk
import tkinter.messagebox as mb
import pymysql
from config import host, user, password, db_name
import datetime
import hashlib

telephone_number = 1
id_of_employee = randint(1, 4)
id_order = 0
id_client = 0
id_order_for_element = 0
all_sum_order = 0
discount_card = 0


class Main_one(tkin.Frame): # класс начального главного окна
    # (frame - контейнер, отвечающий за расположение других виджетов. базовый класс для реализации сложных виджетов)
    def __init__(self, root):
        super().__init__(root)
        self.init_main_one()

    def init_main_one(self): # для инициализации всех объектов окна
        btn_client_sign_up = tkin.Button(text='Регистрация', bg='white', bd=2, height=1, cursor='sizing', width=20, command=self.open_dops)
        btn_client_sign_up.pack(padx=50, pady=5, side=tkin.BOTTOM)
        btn_client_login = tkin.Button(text='Войти', bg='white', bd=2, height=1, cursor='sizing', width=20, command=self.open_dop)
        btn_client_login.pack(padx=10, pady=5, side=tkin.BOTTOM)
        btn_client_exit = tkin.Button(text='Выйти', cursor='sizing')
        btn_client_exit.pack(padx=50, pady=5, side=tkin.BOTTOM)
        btn_client_exit.bind('<Button-1>', lambda event: [sys.exit(), db.connection.close()])

    def open_dop(self):
        Child_one()

    def open_dops(self):
        Child_two()

    def into_second(self):
        gui_one.destroy()


class Child_one(tkin.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_child_one()

    def init_child_one(self):
        self.title('Вы были раньше в нашем магазине')
        self.geometry('400x220+150+300')
        self.resizable(False, False)
        label_phone = tkin.Label(self, text='Номер телефона:', font='Verdana 10')
        label_phone.place(x=50, y=50)
        label_format_tele = tkin.Label(self, text='Формат: +7(ххх)ххх-хх-хх', font='Verdana 8')
        label_format_tele.place(x=70, y=70)
        label_pass = tkin.Label(self, text='Пароль:', font='Verdana 10')
        label_pass.place(x=50, y=110)
        self.entry_phone = ttk.Entry(self)
        self.entry_phone.place(x=200, y=50)
        self.entry_pass = ttk.Entry(self)
        self.entry_pass.place(x=200, y=110)
        btn_cancel = ttk.Button(self, text='Закрыть', cursor='sizing', command=self.destroy)
        btn_cancel.place(x=300, y=170)
        btn_ok = ttk.Button(self, text='Ввести', cursor='sizing', command=lambda: [self.check_pass(self.entry_phone.get(), self.entry_pass.get())])
        btn_ok.place(x=220, y=170)
        self.grab_set()
        self.focus_set()

    def show_error(self):
        msg = "Неправильный номер телефона или пароль!"
        mb.showerror("Ошибка", msg)

    def check_pass(self, number_phone, password):
        number_phone = self.format_numbers(number_phone)
        if (number_phone) and (password):
            main_o = Main_one(gui_one)
            dicti_pass = db.cursor.execute('''SELECT PasswordOfClient FROM client WHERE ClientPhoneNumber = %s''', number_phone)
            if (dicti_pass):
                global telephone_number
                telephone_number = number_phone
                password_of_user = db.cursor.fetchone()
                all_password = db.for_fetchone(password_of_user)

                password = hashlib.md5(password.encode())
                # берет строку и преобразует ее в байтовый эквивалент с помощью encode(), чтобы она могла быть принята хеш-функцией
                # затем hashlib.md5() хеш-функция принимает последовательность байтов, кодирует, и возвращает 128-битное хэш-значение
                password2 = password.hexdigest()
                # возвращает закодированные данные в шестнадцатеричном формате (Шестнадцатеричный эквивалент хеша - закодированной строки)

                if (password2 != all_password):
                    self.show_error()
                else:
                    main_o.into_second()
            else:
                self.show_error()
        else:
            self.show_error()

    def format_numbers(self, phone_number: str) -> str:
        numbers = list(filter(str.isdigit, phone_number))[1:]
        if ((numbers) and (len(numbers) == 10)):
            return "+7({}{}{}){}{}{}-{}{}-{}{}".format(*numbers)
        else:
            return 0


class Child_two(tkin.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_child_two()

    def init_child_two(self):
        self.title('Вы не были раньше в нашем магазине')
        self.geometry('400x220-185-300')
        self.resizable(False, False)
        label_name = tkin.Label(self, text='ФИО пользователя:', font='Verdana 10')
        label_name.place(x=50, y=30)
        label_tphone = tkin.Label(self, text='Номер телефона:', font='Verdana 10')
        label_tphone.place(x=50, y=50)
        label_format_tele = tkin.Label(self, text='Формат: +7(ххх)ххх-хх-хх', font='Verdana 8')
        label_format_tele.place(x=70, y=70)
        label_addr = tkin.Label(self, text='Адрес:', font='Verdana 10')
        label_addr.place(x=50, y=90)
        label_email = tkin.Label(self, text='Email:', font='Verdana 10')
        label_email.place(x=50, y=110)
        label_npass = tkin.Label(self, text='Пароль:', font='Verdana 10')
        label_npass.place(x=50, y=130)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=30)
        self.entry_tphone = ttk.Entry(self)
        self.entry_tphone.place(x=200, y=50)
        self.entry_addr = ttk.Entry(self)
        self.entry_addr.place(x=200, y=110)
        self.entry_email = ttk.Entry(self)
        self.entry_email.place(x=200, y=90)
        self.entry_npass = ttk.Entry(self)
        self.entry_npass.place(x=200, y=130)
        btn_cancel = ttk.Button(self, text='Закрыть', cursor='sizing', command=self.destroy)
        btn_cancel.place(x=300, y=170)
        btn_oks = ttk.Button(self, text='Добавить', cursor='sizing', command=lambda: [
            self.check_errors(self.entry_name.get(), self.entry_tphone.get(), self.entry_addr.get(),
                                  self.entry_email.get(), self.entry_npass.get())])
        btn_oks.place(x=220, y=170)
        self.grab_set()
        self.focus_set()

    def show_errors(self):
        msg = "Не все поля заполнены!"
        mb.showerror("Ошибка", msg)

    def check_errors(self, name, phone, addr, email, npass):
        spisok_tele = db.select_tele_of_client()
        dopv = 0
        for i in spisok_tele:
            if phone == i:
                dopv = 1
        if (dopv==1):
            self.show_error_tele_not_new()
        else:
            phone = self.format_numbers(phone)
            if (phone) and (dopv == 0):
                if (name) and (phone) and (addr) and (email) and (npass):
                    db.insert_data_client(name, phone, addr, email, npass)
                    main_o = Main_one(gui_one)
                    main_o.into_second()
                else:
                    self.show_errors()
            else:
                self.show_error_tele()

    def show_error_tele(self):
        msg = "Неправильно указан номер телефона!"
        mb.showerror("Ошибка", msg)

    def show_error_tele_not_new(self):
        msg = "Пользователь с таким номером телефона уже существует!"
        mb.showerror("Ошибка", msg)

    def format_numbers(self, phone_number: str) -> str:
        numbers = list(filter(str.isdigit, phone_number))[1:]
        if ((numbers) and (len(numbers)==10)):
            return "+7({}{}{}){}{}{}-{}{}-{}{}".format(*numbers)
        else:
            return 0


class Main_new(tkin.Frame): # класс основного главного окна
    def __init__(self, root):
        super().__init__(root)
        self.db = db
        self.init_main_new()
        self.view_records()

    def init_main_new(self):
        toolbar = tkin.Frame(bg='#F0FFF0', bd=4, height=50, width=20)
        toolbar.pack(side=tkin.TOP, fill=tkin.X)
        self.search_book = tkin.PhotoImage(file='search_book.png')
        btn_search = tkin.Button(toolbar, text='Каталог', font='Verdana 9', width=121, bg='#cceade', bd=0, cursor='sizing', image=self.search_book,
                                 compound=tkin.TOP, command=self.open_catalog)
        btn_search.pack(side=tkin.LEFT)
        self.add_book = tkin.PhotoImage(file='add_book2.png')
        btn_add_book = tkin.Button(toolbar, text='Добавить книгу', font='Verdana 9',  width=121, bg='#cceade', bd=0, cursor='sizing', compound=tkin.TOP, image=self.add_book, command=self.open_add)
        btn_add_book.pack(side=tkin.LEFT)
        self.update_book = tkin.PhotoImage(file='update_book.png')
        btn_edit = tkin.Button(toolbar, text='Редактировать', font='Verdana 9', width=121, bg='#cceade', bd=0, cursor='sizing', image=self.update_book,
                                    compound=tkin.TOP, command=self.open_update_dia)
        btn_edit.pack(side=tkin.LEFT)
        self.delete_book = tkin.PhotoImage(file='delete_book.png')
        btn_delete = tkin.Button(toolbar, text='Удалить книгу', font='Verdana 9', width=121, bg='#cceade', bd=0, cursor='sizing', image=self.delete_book, compound=tkin.TOP, command=self.delete_records)
        btn_delete.pack(side=tkin.LEFT)
        # #0B9B4B #0A9447 #14905A #0F7347
        self.my_order_book = tkin.PhotoImage(file='orderbook.png')
        btn_order = tkin.Button(toolbar, text='Мои заказы', font='Verdana 9', width=121, bg='#cceade', bd=0,
                                cursor='sizing', image=self.my_order_book,
                                compound=tkin.TOP, command=self.open_user_orders)
        btn_order.pack(side=tkin.LEFT)
        self.info_book = tkin.PhotoImage(file='info_book.png')
        btn_info = tkin.Button(toolbar, text='Информация', font='Verdana 9', width=121, bg='#cceade', bd=0, cursor='sizing', image=self.info_book,
                                 compound=tkin.TOP, command=self.open_info)
        btn_info.pack(side=tkin.LEFT)
        self.func_book = tkin.PhotoImage(file='disc.png')
        btn_func = tkin.Button(toolbar, text='Расчет со %', font='Verdana 9', width=121, bg='#cceade', bd=0,
                               cursor='sizing', image=self.func_book,
                               compound=tkin.TOP, command=self.open_func)
        btn_func.pack(side=tkin.LEFT)

        db.insert_orderbook(telephone_number)
        db.id_order_book(telephone_number)
        print(id_order, id_client, telephone_number, id_of_employee)

        self.tree = ttk.Treeview(self, height=15, show='headings')
        scroll = tkin.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tkin.LEFT, fill=tkin.Y)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree['columns'] = ['ID', 'BookName', 'Product_idBook', 'QuantityOfProducts', 'BookPrice']
        self.tree.column('ID', width=50, anchor=tkin.CENTER)
        self.tree.column('BookName', width=250, anchor=tkin.CENTER)
        self.tree.column('Product_idBook', width=200, anchor=tkin.CENTER)
        self.tree.column('QuantityOfProducts', width=100, anchor=tkin.CENTER)
        self.tree.column('BookPrice', width=250, anchor=tkin.CENTER)
        self.tree.heading('ID', text='ID')
        self.tree.heading('BookName', text='Книга')
        self.tree.heading('Product_idBook', text='ID книги')
        self.tree.heading('QuantityOfProducts', text='Количество')
        self.tree.heading('BookPrice', text='Цена за книгу')
        self.tree.pack(expand=tkin.YES, fill=tkin.BOTH)

        toolbar_btm = tkin.Frame(bg='#F0FFF0', bd=6, height=120, width=25)
        toolbar_btm.pack(side=tkin.BOTTOM, fill=tkin.X)
        btn_delivery = tkin.Button(toolbar_btm, text="Доставка", cursor='sizing', command=self.open_delivery)
        btn_delivery.pack(side=tkin.LEFT)
        btn_toorder = tkin.Button(toolbar_btm, text="Оформить заказ", cursor='sizing')
        btn_toorder.bind('<Button-1>', lambda event: self.price_each_order(self.view_records()))
        btn_toorder.pack(side=tkin.RIGHT)

    def records(self, bookname, quantity):
        if (bookname) and (quantity):
            db.insert_order_element(bookname, quantity)
            self.view_records()
        else:
            msg = "Не все поля заполнены!"
            mb.showerror("Ошибка", msg)

    def view_records(self):
        self.db.cursor.execute(
            '''SELECT idOrderElement, BookName, Product_idBook, QuantityOfProducts, BookPrice FROM orderelement JOIN product ON orderelement.Product_idBook = product.idBook WHERE orderelement.OrderBook_idOrderBook = %s''',
            id_order)
        for i in self.tree.get_children(): # очистка содержимого виджета, чтобы не дублировалось
            self.tree.delete(i)
        all_row = self.db.cursor.fetchall()  # каждая строка в виде словаря
        all_row_books = []
        for row in all_row:
            dops = list(row.values())
            all_row_books.append(dops)
        for row in all_row_books: # список кортежей
            self.tree.insert("", 'end', values=row)
        return (all_row_books)

    def price_each_order(self, all_row_books):
        global all_sum_order
        all_sum_order = 0
        for row in all_row_books:
            all_sum_order += (row[4]*row[3])
        self.open_set_of_order()

    def update_record(self, bookname, quantity):
        self.db.cursor.execute('''SELECT NumberOfCopies FROM product WHERE BookName = %s''', bookname)
        quantitity_book = self.db.cursor.fetchone()
        number_copies = int(self.db.for_fetchone(quantitity_book))
        if (bookname) and (quantity):
            if (number_copies >= int(quantity)):
                self.db.cursor.execute('''UPDATE orderelement SET QuantityOfProducts=%s, Product_idBook=%s WHERE idOrderElement=%s''',
                                          (quantity, self.db.select_id_book(bookname), self.tree.set(self.tree.selection()[0], '#1')))
                self.db.connection.commit()
                self.view_records()
            else:
                msg = "Не хватает копий книг!"
                mb.showerror("Ошибка", msg)
        else:
            msg = "Не все поля заполнены!"
            mb.showerror("Ошибка", msg)

    def show_warning_update(self):
        msg = "Не выбран элемент заказа!"
        mb.showwarning("Предупреждение", msg)

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cursor.execute('''DELETE FROM orderelement WHERE idOrderElement=%s''', (self.tree.set(selection_item, '#1'),))
        self.db.connection.commit()
        self.view_records()

    def open_add(self):
        Child_order()

    def open_update_dia(self):
        currItem = self.tree.item(self.tree.focus())
        if (currItem['values'] != ''):
            Update()
        else:
            self.show_warning_update()

    def open_catalog(self):
        Child_catalog()

    def open_user_orders(self):
        Child_user_order()

    def open_info(self):
        Info_user()

    def open_delivery(self):
        Child_delivery()

    def open_func(self):
        Child_func()

    def open_set_of_order(self):
        Child_set_order()


class Child_order(tkin.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_child_order()
        self.view = app

    def init_child_order(self):
        self.title('Добавить элемент заказа')
        self.geometry('400x220+550+350')
        self.resizable(False, False)

        label_select = tkin.Label(self, text='Книга:')
        label_select.place(x=50, y=50)
        label_qua = tkin.Label(self, text='Количество:')
        label_qua.place(x=50, y=110)
        all_books = db.select_all_book()
        self.combobox = ttk.Combobox(self, values=all_books)
        self.combobox.current(0)
        self.combobox.place(x=200, y=50)
        self.entry_qua = ttk.Entry(self)
        self.entry_qua.place(x=200, y=110)
        btn_cancel = tkin.Button(self, text='Закрыть', cursor='sizing', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = tkin.Button(self, text='Добавить', cursor='sizing')
        btn_ok.place(x=220, y=170)
        btn_ok.bind('<Button-1>', lambda event: self.view.records(self.combobox.get(), self.entry_qua.get()))

        self.grab_set()
        self.focus_set()


class Child_func(tkin.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_child_func()
        self.view = app

    def init_child_func(self):
        self.title('Расчет стоимости со скидкой')
        self.geometry('400x220+550+350')
        self.resizable(False, False)

        label_select_bo = tkin.Label(self, text='Книга:')
        label_select_bo.place(x=50, y=50)
        label_qua_bo = tkin.Label(self, text='Количество:')
        label_qua_bo.place(x=50, y=80)
        label_qua_disc = tkin.Label(self, text='Скидка:')
        label_qua_disc.place(x=50, y=110)
        all_bookss = db.select_all_book()
        self.combobox_disc = ttk.Combobox(self, values=all_bookss)
        self.combobox_disc.current(0)
        self.combobox_disc.place(x=200, y=50)
        self.entry_qua_bo = ttk.Entry(self)
        self.entry_qua_bo.place(x=200, y=80)
        self.entry_qua_discount = ttk.Entry(self)
        self.entry_qua_discount.place(x=200, y=110)
        btn_cancels = tkin.Button(self, text='Закрыть', cursor='sizing', command=self.destroy)
        btn_cancels.place(x=300, y=170)

        btn_okeys = tkin.Button(self, text='Рассчитать', cursor='sizing')
        btn_okeys.place(x=220, y=170)
        btn_okeys.bind('<Button-1>',
                       lambda event: self.card_calculate(self.combobox_disc.get(), self.entry_qua_bo.get(),
                                                         self.entry_qua_discount.get()))

        self.grab_set()
        self.focus_set()

    def card_calculate(self, book, number_of_book, discount_amount_var):
        if (book) and (number_of_book) and (discount_amount_var):
            id_book = db.select_id_book(book)
            discount_amount_var = int(discount_amount_var)
            number_of_book = int(number_of_book)
            db.cursor.execute('''SELECT price_discount(%s, %s, %s) AS rez''', (discount_amount_var, number_of_book, id_book))
            pr_d = db.cursor.fetchone()
            res_sum = float(db.for_fetchone(pr_d))
            res_sum = round(res_sum, 2)
            self.show_info_discount_card(res_sum)
        else:
            msg = "Не все поля заполнены!"
            mb.showerror("Ошибка", msg)

    def show_info_discount_card(self, res):
        msg = "Итоговая сумма: " + str(res)
        mb.showinfo("Информация", msg)


class Child_set_order(tkin.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_child_set_order()
        self.view = app

    def init_child_set_order(self):
        self.title('Оформить заказ')
        self.geometry('400x220+550+350')
        self.resizable(False, False)

        label_price_order_user = tkin.Label(self, text='Цена заказа:')
        label_price_order_user .place(x=50, y=40)
        label_price_order_user_disc = tkin.Label(self, text='Цена заказа со скидкой:')
        label_price_order_user_disc.place(x=50, y=70)
        label_price_order_delivery = tkin.Label(self, text='Цена доставки:')
        label_price_order_delivery.place(x=50, y=100)
        btn_cancel_del = tkin.Button(self, text='Отменить доставку', cursor='sizing', command=self.destroy_del)
        btn_cancel_del.place(x=270, y=100)
        label_price_order_uall = tkin.Label(self, text='Итоговая цена:')
        label_price_order_uall.place(x=50, y=130)

        answer_price_order_user = tkin.Label(self, text=str(all_sum_order) + " РУБ.")
        answer_price_order_user.place(x=200, y=40)

        price_with_discount = float(all_sum_order) * (100 - float(discount_card)) / 100
        price_with_discount = round(price_with_discount, 2)
        answer_price_order_user_disc = tkin.Label(self, text=str(price_with_discount) + " РУБ.")
        answer_price_order_user_disc.place(x=200, y=70)

        db.cursor.execute('''SELECT DeliveryPrice FROM delivery INNER JOIN orderbook ON delivery.TrackNumberDelivery = orderbook.Delivery_TrackNumberDelivery WHERE idOrderBook=%s''', id_order)
        d_price = db.cursor.fetchone()
        deliver_price = db.for_fetchone(d_price)

        answer_price_order_delivery = tkin.Label(self, text=str(deliver_price) + " РУБ.")
        answer_price_order_delivery.place(x=200, y=100)

        deliver_price = float(deliver_price)
        price_order_uall = float(price_with_discount) + deliver_price

        answer_price_order_uall = tkin.Label(self, text=str(price_order_uall) + " РУБ.")
        answer_price_order_uall.place(x=200, y=130)

        btn_cancel_or = tkin.Button(self, text='Закрыть', cursor='sizing', command=self.destroy)
        btn_cancel_or.place(x=300, y=170)
        btn_oki = tkin.Button(self, text='Оформить', cursor='sizing')
        btn_oki.place(x=220, y=170)
        btn_oki.bind('<Button-1>', lambda event: self.add_order(price_order_uall))
        self.grab_set()
        self.focus_set()

    def add_order(self, sum):
        self.destroy()
        msg = "Заказ оформлен!"
        mb.showinfo("Информация", msg)
        db.new_order()
        global all_sum_order
        all_sum_order = 0
        global id_order
        id_order = int(id_order) + 1
        db.insert_orderbook(telephone_number)
        self.view.view_records()

    def destroy_del(self):
        self.destroy()
        msg = "Доставка отменена!"
        mb.showinfo("Информация", msg)
        db.cursor.execute('''UPDATE orderbook SET Delivery_TrackNumberDelivery = '000000', availability_of_delivery=0 WHERE idOrderBook=%s''', id_order)
        db.cursor.connection.commit()


class Update(Child_order):
    def __init__(self):
        super().__init__()
        self.init_update()
        self.view = app

    def init_update(self):
        self.title('Редактировать заказ')
        btn_edit = ttk.Button(self, text='Редактировать', cursor='sizing')
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.combobox.get(), self.entry_qua.get()))


class Info_user(tkin.Toplevel):
    def __init__(self):
        super().__init__()
        self.id_discount_card = 0
        self.db = DB()
        self.init_child_user_info()
        self.view_info()

    def init_child_user_info(self):
        self.title('Информация о клиенте')
        self.geometry('800x200+360+330')
        self.resizable(False, False)

        toolbar_info = tkin.Frame(self, bg='#cceade', bd=4, height=20)
        toolbar_info.pack(side=tkin.TOP, fill=tkin.X)
        self.discount = tkin.PhotoImage(file='discount.png')

        btn_card = tkin.Button(toolbar_info, text='Запросить скидочную карту', font='Verdana 8', width=790, bg='#cceade', bd=1,
                              cursor='sizing', image=self.discount, compound=tkin.TOP)
        btn_card.pack(side=tkin.LEFT)
        btn_card.bind('<Button-1>', lambda event: self.discount_card_user())

        self.tree_user = ttk.Treeview(self, height=50, show='headings')
        self.tree_user['columns'] = ['idClient', 'ClientFIO', 'ClientPhoneNumber', 'AddressOfClient', 'EmailOfClient', 'idDiscountCard', 'DiscountAmount']
        self.tree_user.column('idClient', width=5, anchor=tkin.CENTER)
        self.tree_user.column('ClientFIO', width=110, anchor=tkin.CENTER)
        self.tree_user.column('ClientPhoneNumber', width=60, anchor=tkin.CENTER)
        self.tree_user.column('AddressOfClient', width=130, anchor=tkin.CENTER)
        self.tree_user.column('EmailOfClient', width=50, anchor=tkin.CENTER)
        self.tree_user.column('idDiscountCard', width=30, anchor=tkin.CENTER)
        self.tree_user.column('DiscountAmount', width=30, anchor=tkin.CENTER)

        self.tree_user.heading('idClient', text='ID')
        self.tree_user.heading('ClientFIO', text='ФИО')
        self.tree_user.heading('ClientPhoneNumber', text='Номер телефона')
        self.tree_user.heading('AddressOfClient', text='Адрес')
        self.tree_user.heading('EmailOfClient', text='Email')
        self.tree_user.heading('idDiscountCard', text='Карта')
        self.tree_user.heading('DiscountAmount', text='Скидка %')
        self.tree_user.pack(expand=tkin.YES, fill=tkin.BOTH)

        self.grab_set()
        self.focus_set()

    def view_info(self):
        self.db.cursor.execute('''SELECT idClient, ClientFIO, ClientPhoneNumber, AddressOfClient, EmailOfClient FROM client WHERE idClient = %s''', id_client)
        that_user = self.db.cursor.fetchall()
        all_info_user = []
        for row in that_user:
            dops = list(row.values())
            all_info_user.append(dops)
        flat_new = [*all_info_user[0]]
        res_show_info = []
        res_show_info.append(flat_new)
        self.db.cursor.execute(
            '''SELECT idDiscountCard FROM client JOIN discountcard ON client.idClient = discountcard.Client_idClient WHERE idClient = %s''',
            id_client)
        row_discount = self.db.cursor.fetchall()
        if (row_discount):
            all_card = self.db.for_fetchall(row_discount)
            self.id_discount_card = all_card[0]
            self.id_discount_card = self.id_discount_card[0]
            flat_new.append(all_card)
            self.db.cursor.execute(
                '''SELECT DiscountAmount FROM client JOIN discountcard ON client.idClient = discountcard.Client_idClient WHERE idClient = %s''',
                id_client)
            row_number_dic = self.db.cursor.fetchall()
            all_number_card = self.db.for_fetchall(row_number_dic)
            global discount_card
            discount_card = all_number_card[0]
            flat_new.append(all_number_card)
            res_show_info = []
            res_show_info.append(flat_new)
        for row in res_show_info:
            self.tree_user.insert("", 'end', values=row)

    def discount_card_user(self):
        if (self.id_discount_card != 0):
            self.destroy()
            self.show_warning()
        else:
            self.id_discount_card = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
            global discount_card
            discount_card = 7
            self.db.cursor.execute('''INSERT INTO discountcard VALUES (%s, %s, %s)''', (self.id_discount_card, discount_card, id_client))
            self.db.connection.commit()
            self.destroy()
            self.show_info()

    def show_info(self):
        msg = "Скидочная карта добавлена!"
        mb.showinfo("Информация", msg)

    def show_warning(self):
        msg = "У Вас уже есть скидочная карта!"
        mb.showwarning("Предупреждение", msg)


class Child_catalog(tkin.Toplevel):
    def __init__(self):
        super().__init__()
        self.db = DB()
        self.init_child_catalog()
        self.view = app
        self.view_catalog()

    def init_child_catalog(self):
        self.title('Каталог доступных книг')
        self.geometry('800x400+360+330')
        self.resizable(False, False)
        toolbar_new = tkin.Frame(self, bg='#cceade', bd=4, height=20)
        toolbar_new.pack(side=tkin.TOP, fill=tkin.X)

        self.tree_new = ttk.Treeview(self, height=10, show='headings')
        scroll_new = ttk.Scrollbar(self, orient ="vertical", command=self.tree_new.yview)
        scroll_new.pack(side=tkin.LEFT, fill=tkin.Y)
        self.tree_new.configure(yscrollcommand=scroll_new.set)
        self.tree_new['columns'] = ['idBook', 'BookName', 'BookAuthor', 'NumberOfPages', 'BookPrice', 'NumberOfCopies', 'Rating']
        self.tree_new.column('idBook', width=50, anchor=tkin.CENTER)
        self.tree_new.column('BookName', width=100, anchor=tkin.CENTER)
        self.tree_new.column('BookAuthor', width=100, anchor=tkin.CENTER)
        self.tree_new.column('NumberOfPages', width=70, anchor=tkin.CENTER)
        self.tree_new.column('BookPrice', width=80, anchor=tkin.CENTER)
        self.tree_new.column('NumberOfCopies', width=60, anchor=tkin.CENTER)
        self.tree_new.column('Rating', width=30, anchor=tkin.CENTER)

        self.tree_new.heading('idBook', text='ID книги')
        self.tree_new.heading('BookName', text='Название')
        self.tree_new.heading('BookAuthor', text='Автор')
        self.tree_new.heading('NumberOfPages', text='Кол-во страниц')
        self.tree_new.heading('BookPrice', text='Цена')
        self.tree_new.heading('NumberOfCopies', text='В наличии (шт.)')
        self.tree_new.heading('Rating', text='Рейтинг')
        self.tree_new.pack(expand=tkin.YES, fill=tkin.BOTH)

        btn_sea = tkin.Label(toolbar_new, text='Поиск', font='Verdana 10', bg='#b6decb', bd=1, cursor='sizing')
        btn_sea.pack(side=tkin.TOP)
        self.combobox_search = ttk.Combobox(toolbar_new, values=[u'По автору', u'По названию'])
        self.combobox_search.current(0)
        self.combobox_search.pack(side=tkin.TOP)
        self.entry_sea = ttk.Entry(toolbar_new)
        self.entry_sea.pack(side=tkin.TOP)
        btn_sea.bind('<Button-1>', lambda event: self.search_cat(self.entry_sea.get(), self.combobox_search.get()))

        self.grab_set()
        self.focus_set()

    def view_catalog(self):
        self.db.cursor.execute('''SELECT idBook FROM product''')
        book_id_last = self.db.cursor.fetchall()
        all_catalog = self.db.for_fetchall(book_id_last)
        for it in all_catalog:
            self.db.cursor.execute(
                 '''SELECT idBook, BookName, BookAuthor, NumberOfPages, BookPrice, NumberOfCopies, Rating FROM product WHERE idBook = %s''', str(it))
            all_rows = self.db.cursor.fetchall()
            all_rows_books = []
            for row in all_rows:
                dops = list(row.values())
                all_rows_books.append(dops)
            for row in all_rows_books:
                self.tree_new.insert("", 'end', values=row)

    def search_cat(self, search_word, choice_search):
        if (search_word) and (choice_search):
            search_word = str(search_word)
            choice_search = str(choice_search)
            s = Search(search_word, choice_search)
        else:
            msg = "Не все поля заполнены!"
            mb.showerror("Ошибка", msg)


class Search(tkin.Toplevel):
    def __init__(self, sea, choice_search):
        super().__init__()
        self.db = DB()
        self.sea = sea
        self.choice_search = choice_search
        self.init_search_catalog()
        self.search_author_or_name(self.choice_search)

    def init_search_catalog(self):
        self.title('Результат поиска')
        self.geometry('800x280+360+60')
        self.resizable(False, False)

        toolbar_search = tkin.Frame(self, bg='#cceade', bd=4, height=20)
        toolbar_search.pack(side=tkin.TOP, fill=tkin.X)

        self.tree_search = ttk.Treeview(self, height=10, show='headings')
        scroll_search = ttk.Scrollbar(self, orient ="vertical", command=self.tree_search.yview)
        scroll_search.pack(side=tkin.LEFT, fill=tkin.Y)
        self.tree_search.configure(yscrollcommand=scroll_search.set)
        self.tree_search['columns'] = ['idBook', 'BookName', 'BookAuthor', 'NumberOfPages', 'BookPrice', 'NumberOfCopies', 'Rating']
        self.tree_search.column('idBook', width=50, anchor=tkin.CENTER)
        self.tree_search.column('BookName', width=100, anchor=tkin.CENTER)
        self.tree_search.column('BookAuthor', width=100, anchor=tkin.CENTER)
        self.tree_search.column('NumberOfPages', width=70, anchor=tkin.CENTER)
        self.tree_search.column('BookPrice', width=80, anchor=tkin.CENTER)
        self.tree_search.column('NumberOfCopies', width=60, anchor=tkin.CENTER)
        self.tree_search.column('Rating', width=30, anchor=tkin.CENTER)

        self.tree_search.heading('idBook', text='ID книги')
        self.tree_search.heading('BookName', text='Название')
        self.tree_search.heading('BookAuthor', text='Автор')
        self.tree_search.heading('NumberOfPages', text='Кол-во страниц')
        self.tree_search.heading('BookPrice', text='Цена')
        self.tree_search.heading('NumberOfCopies', text='В наличии (шт.)')
        self.tree_search.heading('Rating', text='Рейтинг')
        self.tree_search.pack(expand=tkin.YES, fill=tkin.BOTH)

        self.grab_set()
        self.focus_set()

    def search_author_or_name(self, choice):
        self.sea = str(self.sea)
        if (choice == 'По автору'):
            self.db.cursor.execute('''SELECT idBook FROM product WHERE BookAuthor LIKE %s''', ("%" + self.sea + "%",))
        else:
            self.db.cursor.execute('''SELECT idBook FROM product WHERE BookName LIKE %s''', ("%" + self.sea + "%",))
        book_id_last = self.db.cursor.fetchall()
        all_catalog = self.db.for_fetchall(book_id_last)
        if (all_catalog):
            for it in all_catalog:
                self.db.cursor.execute(
                    '''SELECT idBook, BookName, BookAuthor, NumberOfPages, BookPrice, NumberOfCopies, Rating FROM product WHERE idBook = %s''',
                    str(it))
                all_rows = self.db.cursor.fetchall()
                all_rows_books = []
                for row in all_rows:
                    dops = list(row.values())
                    all_rows_books.append(dops)
                for row in all_rows_books:
                    self.tree_search.insert("", 'end', values=row)
        else:
            self.destroy()
            msg = "Результаты не найдены!"
            mb.showwarning("Предупреждение", msg)


class Child_user_order(tkin.Toplevel):
    def __init__(self):
        super().__init__()
        self.db = DB()
        self.init_child_user_order()
        self.view_my_orders()

    def init_child_user_order(self):
        self.title('Мои заказы')
        self.geometry('800x400+360+330')
        self.resizable(False, False)
        toolbar_my_order = tkin.Frame(self, bg='#cceade', bd=4, height=20)
        toolbar_my_order.pack(side=tkin.TOP, fill=tkin.X)

        self.tree_my_order = ttk.Treeview(self, height=10, show='headings')
        scroll_new = tkin.Scrollbar(self, command=self.tree_my_order.yview)
        scroll_new.pack(side=tkin.LEFT, fill=tkin.Y)
        self.tree_my_order.configure(yscrollcommand=scroll_new.set)
        self.tree_my_order['columns'] = ['idOrderBook', 'OrderBookPrice', 'ContractDate', 'OrderStatus', 'Delivery_TrackNumberDelivery', 'DeliveryPrice', 'DateOfDelivery']
        self.tree_my_order.column('idOrderBook', width=50, anchor=tkin.CENTER)
        self.tree_my_order.column('OrderBookPrice', width=70, anchor=tkin.CENTER)
        self.tree_my_order.column('ContractDate', width=50, anchor=tkin.CENTER)
        self.tree_my_order.column('OrderStatus', width=70, anchor=tkin.CENTER)
        self.tree_my_order.column('Delivery_TrackNumberDelivery', width=80, anchor=tkin.CENTER)
        self.tree_my_order.column('DeliveryPrice', width=80, anchor=tkin.CENTER)
        self.tree_my_order.column('DateOfDelivery', width=50, anchor=tkin.CENTER)

        self.tree_my_order.heading('idOrderBook', text='ID заказа')
        self.tree_my_order.heading('OrderBookPrice', text='Цена')
        self.tree_my_order.heading('ContractDate', text='Дата')
        self.tree_my_order.heading('OrderStatus', text='Статус')
        self.tree_my_order.heading('Delivery_TrackNumberDelivery', text='Трек-номер доставки')
        self.tree_my_order.heading('DeliveryPrice', text='Цена доставки')
        self.tree_my_order.heading('DateOfDelivery', text='Дата доставки')
        self.tree_my_order.pack(expand=tkin.YES, fill=tkin.BOTH)
        self.tree_my_order.bind('<<TreeviewSelect>>', self.open_show_orders)

        self.grab_set()
        self.focus_set()

    def view_my_orders(self):
        self.db.cursor.execute('''SELECT idOrderBook FROM orderbook WHERE Client_idClient = %s''', id_client)
        book_user = self.db.cursor.fetchall()
        all_users_id_order = self.db.for_fetchall(book_user)
        for it in all_users_id_order:
            self.db.cursor.execute(
                '''SELECT idOrderBook, OrderBookPrice, ContractDate, OrderStatusName, Delivery_TrackNumberDelivery FROM orderbook JOIN orderstatus ON orderbook.OrderStatus_idOrderStatus = orderstatus.idOrderStatus WHERE idOrderBook = %s''', it)
            all_rows_user = self.db.cursor.fetchall()
            orders_books = []
            for row in all_rows_user:
                dooops = list(row.values())
                orders_books.append(dooops)
            flat_2 = [*orders_books[0]]
            self.db.cursor.execute(
                '''SELECT DeliveryPrice FROM delivery JOIN orderbook ON delivery.TrackNumberDelivery = orderbook.Delivery_TrackNumberDelivery WHERE orderbook.idOrderBook = %s''',
                it)
            row_last_price = self.db.cursor.fetchone()
            order_price_delivery = self.db.for_fetchone(row_last_price)
            flat_2.append(order_price_delivery)
            self.db.cursor.execute(
                '''SELECT DateOfDelivery FROM delivery JOIN orderbook ON delivery.TrackNumberDelivery = orderbook.Delivery_TrackNumberDelivery WHERE orderbook.idOrderBook = %s''',
                it)
            row_date_del = self.db.cursor.fetchone()
            order_date_delivery = self.db.for_fetchone(row_date_del)
            flat_2.append(order_date_delivery)
            res_show_row = []
            res_show_row.append(flat_2)
            for row in res_show_row:
                self.tree_my_order.insert("", 'end', values=row)

    def open_show_orders(self, event):
        selected_item = self.tree_my_order.selection()[0]
        global id_order_for_element
        id_order_for_element = self.tree_my_order.item(selected_item, option="values")[0]
        Child_orderelement()


class Child_orderelement(tkin.Toplevel):
    def __init__(self):
        super().__init__()
        self.db = DB()
        self.init_child_orderelement()
        self.view_my_orderelement()

    def init_child_orderelement(self):
        self.title('Просмотр заказа')
        self.geometry('600x180+460+490')
        self.resizable(False, False)
        toolbar_my_orderelement = tkin.Frame(self, bg='#cceade', bd=4, height=20)
        toolbar_my_orderelement.pack(side=tkin.TOP, fill=tkin.X)

        self.tree_my_orderelement = ttk.Treeview(self, height=10, show='headings')
        scroll_new = tkin.Scrollbar(self, command=self.tree_my_orderelement.yview)
        scroll_new.pack(side=tkin.LEFT, fill=tkin.Y)
        self.tree_my_orderelement.configure(yscrollcommand=scroll_new.set)
        self.tree_my_orderelement['columns'] = ['idOrderElement', 'QuantityOfProducts', 'ProductID', 'Product']
        self.tree_my_orderelement.column('idOrderElement', width=50, anchor=tkin.CENTER)
        self.tree_my_orderelement.column('QuantityOfProducts', width=50, anchor=tkin.CENTER)
        self.tree_my_orderelement.column('ProductID', width=50, anchor=tkin.CENTER)
        self.tree_my_orderelement.column('Product', width=150, anchor=tkin.CENTER)

        self.tree_my_orderelement.heading('idOrderElement', text='ID элемента')
        self.tree_my_orderelement.heading('QuantityOfProducts', text='Количество')
        self.tree_my_orderelement.heading('ProductID', text='ID книги')
        self.tree_my_orderelement.heading('Product', text='Название книги')
        self.tree_my_orderelement.pack(expand=tkin.YES, fill=tkin.BOTH)

        self.grab_set()
        self.focus_set()

    def view_my_orderelement(self):
        self.db.cursor.execute('''SELECT idOrderElement, QuantityOfProducts, Product_idBook, BookName FROM orderelement JOIN product ON orderelement.Product_idBook = product.idBook WHERE orderelement.OrderBook_idOrderBook = %s''', id_order_for_element)
        orderelement_user = self.db.cursor.fetchall()
        element_row_books = []
        for row in orderelement_user:
            dops = list(row.values())
            element_row_books.append(dops)
        for row in element_row_books:
            self.tree_my_orderelement.insert("", 'end', values=row)


class Child_delivery(tkin.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_child_delivery()

    def init_child_delivery(self):
        self.title('Доставка')
        self.geometry('400x220+550+350')
        self.resizable(False, False)

        label_delivery_addr = tkin.Label(self, text='Адрес:')
        label_delivery_addr.place(x=50, y=50)
        label_data_del = tkin.Label(self, text='Дата:')
        label_data_del.place(x=50, y=110)
        label_format_data = tkin.Label(self, text='Формат даты: год-месяц-число', font='Verdana 8')
        label_format_data.place(x=50, y=130)
        self.entry_delivery_addr = ttk.Entry(self)
        self.entry_delivery_addr.place(x=200, y=50)
        self.entry_data_del = ttk.Entry(self)
        self.entry_data_del.place(x=200, y=110)
        btn_cancel_del = tkin.Button(self, text='Закрыть', cursor='sizing', command=self.destroy)
        btn_cancel_del.place(x=300, y=170)

        btn_okew = tkin.Button(self, text='Добавить', cursor='sizing')
        btn_okew.place(x=220, y=170)
        btn_okew.bind('<Button-1>', lambda event: self.add_delivery(self.entry_delivery_addr.get(), self.entry_data_del.get()))

        self.grab_set()
        self.focus_set()
        
    def add_delivery(self, address, date):
        if (address) and (date):
            self.destroy()
            db.insert_delivery(address, date)
        else:
            msg = "Не все поля заполнены!"
            mb.showerror("Ошибка", msg)


class DB:
    def __init__(self):
        try:
            self.connection = pymysql.connect(  # подключение к БД
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Успешное соединение с БД.")
            self.cursor = self.connection.cursor() # объект, который содержит различные методы для mysql-команд
        except Exception as ex:
            print("Соединение не установлено!")
            print(ex)
            sys.exit()

    def insert_data_client(self, ClientFIO, ClientPhoneNumber, AddressOfClient, EmailOfClient, PasswordOfClient):
        global telephone_number
        telephone_number = ClientPhoneNumber

        hash_password = hashlib.md5(PasswordOfClient.encode())
        password_user_hash = hash_password.hexdigest()

        self.cursor.execute('''INSERT INTO client(ClientFIO, ClientPhoneNumber, EmailOfClient, AddressOfClient, PasswordOfClient) VALUES (%s, %s, %s, %s, %s)''', (ClientFIO, ClientPhoneNumber, AddressOfClient, EmailOfClient, password_user_hash))
        self.connection.commit() # чтобы данные сохранились в бд

    def select_all_book(self):
        self.cursor.execute('''SELECT BookName FROM product ORDER BY BookName''')
        books = self.cursor.fetchall()
        all_our_books = self.for_fetchall(books)
        return list(all_our_books)

    def id_order_book(self, telephns):
        self.cursor.execute('''SELECT MAX(idOrderBook) FROM orderbook''')
        book_last = db.cursor.fetchone()
        all_order_id = self.for_fetchone(book_last)
        global id_order
        id_order = all_order_id

    def insert_orderbook(self, telephone_of_user):
        orderbook = self.cursor.execute('''INSERT INTO orderbook(ContractDate, Client_idClient, Employee_idEmployee) VALUES (%s, %s, %s)''',
                                        (datetime.date.today(), self.select_id_client(telephone_of_user), id_of_employee))
        self.connection.commit()

    def insert_order_element(self, BookName, QuantityOfProducts):
        self.cursor.execute('''SELECT NumberOfCopies FROM product WHERE BookName = %s''', BookName)
        quantitity_book = self.cursor.fetchone()
        number_copies = int(self.for_fetchone(quantitity_book))
        if (number_copies >= int(QuantityOfProducts)):
            self.cursor.execute('''INSERT INTO orderelement(QuantityOfProducts, OrderBook_idOrderBook, OrderBook_Client_idClient, OrderBook_Employee_idEmployee, Product_idBook) 
                VALUES (%s, %s, %s, %s, %s)''', (QuantityOfProducts, id_order, id_client, id_of_employee, self.select_id_book(BookName)))
            self.connection.commit()
        else:
            msg = "Не хватает копий книг!"
            mb.showerror("Ошибка", msg)

    def insert_delivery(self, AddressOfDelivery, DateOfDelivery):
        db.cursor.execute('''SELECT DateOfDelivery FROM delivery JOIN orderbook ON delivery.TrackNumberDelivery=orderbook.Delivery_TrackNumberDelivery WHERE orderbook.idOrderBook=%s''', id_order)
        data_deli = db.cursor.fetchone()
        data_delivery = db.for_fetchone(data_deli)
        id_delivery_list = self.select_id_del(DateOfDelivery)
        if (id_delivery_list != 0):
            id_delivery = random.choice(id_delivery_list)
            self.cursor.execute('''UPDATE orderbook SET Delivery_TrackNumberDelivery = %s, AddressOfDelivery = %s, availability_of_delivery=1 WHERE idOrderBook = %s''', (id_delivery, AddressOfDelivery, id_order))
            self.connection.commit()
            msg = "Доставка оформлена!"
            mb.showinfo("Информация", msg)

    def select_id_del(self, DateOfDelivery):
        self.cursor.execute('''SELECT TrackNumberDelivery FROM delivery WHERE DeliveryPrice != 0 AND DateOfDelivery >= %s''', DateOfDelivery)
        tracknum = self.cursor.fetchall()
        if (tracknum):
            all_track = self.for_fetchall(tracknum)
            return list(all_track)
        else:
            msg = "На эту дату доставки нет!"
            mb.showwarning("Предупреждение", msg)
            return 0

    def select_id_book(self, bookname):
        self.cursor.execute('''SELECT idBook FROM product WHERE BookName= %s''', bookname)
        one_id = db.cursor.fetchone()
        id_of_book = self.for_fetchone(one_id)
        return id_of_book

    def select_id_client(self, phonenumber):
        idclients = self.cursor.execute('''SELECT idClient FROM client WHERE ClientPhoneNumber= %s''', phonenumber)
        if (idclients):
            teleph = db.cursor.fetchone()
            id_of_client = self.for_fetchone(teleph)
            global id_client
            id_client = id_of_client
        return id_client

    def select_tele_of_client(self):
        self.cursor.execute('''SELECT ClientPhoneNumber FROM client''')
        telephns = self.cursor.fetchall()
        all_tpn = self.for_fetchall(telephns)
        return list(all_tpn)

    def new_order(self):
        self.cursor.execute('''UPDATE orderbook SET OrderBookPrice=%s WHERE idOrderBook=%s''', (all_sum_order, id_order))
        self.cursor.connection.commit()

    def delete_for_copies(self):
        self.cursor.execute(
            '''SELECT idOrderElement FROM orderelement INNER JOIN orderbook ON orderelement.OrderBook_idOrderBook = orderbook.idOrderBook WHERE orderbook.OrderBookPrice=0.00''')
        order_for_delete = db.cursor.fetchall()
        element_for_delete = db.for_fetchall(order_for_delete)
        for r in element_for_delete:
            self.cursor.execute('''SELECT QuantityOfProducts FROM orderelement WHERE idOrderElement = %s''', r)
            dp = self.cursor.fetchone()
            quan = self.for_fetchone(dp)
            self.cursor.execute('''SELECT Product_idBook FROM orderelement WHERE idOrderElement = %s''', r)
            do_bo = self.cursor.fetchone()
            prod_bo = self.for_fetchone(do_bo)
            self.cursor.execute('''UPDATE product SET NumberOfCopies = NumberOfCopies + %s WHERE idBook=%s''',
                              (quan, prod_bo))
            self.cursor.connection.commit()

    def for_fetchone(self, dicti):
        for_fone = list(dicti.values())
        result_need = ""
        for i in for_fone:
            result_need += str(i)
        return result_need

    def for_fetchall(self, dictio):
        all_res = []
        for d in dictio:
            dop_var = list(d.values())
            need_result = ""
            for g in dop_var:
                need_result += str(g)
            all_res.append(need_result)
        return all_res


if __name__ == "__main__":
    db = DB()
    gui_one = tkin.Tk()  # корневое окно программы
    app = Main_one(gui_one)
    gui_one.overrideredirect(1)
    gui_one.lift()
    gui_one.attributes('-topmost', True)
    gui_one.after_idle(gui_one.attributes, '-topmost', True)
    app.pack()  # чтобы отобразить содержимое окна, нужно упаковать
    gui_one.title("Книжный магазин")
    w = gui_one.winfo_screenwidth()
    h = gui_one.winfo_screenheight()
    w = w // 2  # середина экрана
    h = h // 2
    w = w - 200  # смещение от середины
    h = h - 200
    gui_one.geometry('350x350+{}+{}'.format(w, h))  # размер окна и точка, где оно появляется
    gui_one.configure(bg='#cceade')
    gui_one.resizable(False, False)  # окно не изменяется в размерах (по верт и по гор)
    begin_logo = ImageTk.PhotoImage(file='./pic_begin.png')
    label1 = tkin.Label(image=begin_logo, text='Добро пожаловать!', font='Verdana 18', bg='white',
                                    fg='black', compound='bottom')
    label1.pack(ipadx=50, ipady=50)
    gui_one.mainloop()  # запускает главный цикл обработки событий (само отображение окна с виджетами)
    gui_second = tkin.Tk()
    app = Main_new(gui_second)
    app.pack()
    gui_second.title("Книжный магазин")
    x = (gui_second.winfo_screenwidth() - gui_second.winfo_reqwidth()) / 2 - 350
    y = (gui_second.winfo_screenheight() - gui_second.winfo_reqheight()) / 2 - 180
    gui_second.wm_geometry("885x450+%d+%d" % (x, y))
    gui_second.configure(bg='#fffefb')
    gui_second.resizable(False, False)
    gui_second.mainloop()
    db.delete_for_copies()
    db.cursor.callproc('delete_zero')
    db.connection.commit()
    db.connection.close()
    print('Успешное отключение от БД.')
