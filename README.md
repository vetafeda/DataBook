# Проект по деятельности книжного магазина
Предметная область охватывает деятельность книжного магазина, в особенности — реализацию продажи товаров. Сам магазин предоставляет клиентам широкий выбор книжной продукции, с возможностью совершать покупки как офлайн, так и онлайн. Человек может выбрать способ доставки оплаченного товара: курьерской службой либо самовывозом. Ещё одним преимуществом является возможность постоянным покупателям приобрести скидку на интересующие их товары. Книжный магазин также заключает договоры с поставщиками, что расширяет ассортимент, и обрабатывает полученные поставки. Для учёта всех книг необходимо оформлять и вести довольно большое количество отчетов, этим занимается администрация и сотрудники книжного магазина. Базы данных книг, клиентов, сотрудников и документации значительно облегчит управление книжным магазином и послужит отличной опорой для дальнейшей, более эффективной, работы.

Для проекта реализованы:
1. IDEF0

Контекстная диаграмма в методологии IDEF0:
![image](https://github.com/vetafeda/DataBook/assets/124678022/d0ada5bd-88e5-4543-ac78-08b4cfde27c9)
Декомпозиция контекстной диаграммы:
![image](https://github.com/vetafeda/DataBook/assets/124678022/5e6ff909-d530-4c60-89ed-bf5553d711d3)
Декомпозиция блока «Реализация продажи нужных товаров клиентам»:
![image](https://github.com/vetafeda/DataBook/assets/124678022/35a3899b-dd49-4e82-9dca-9b0a78029909)
Декомпозиция блока «Продажа через интернет-магазин»:
![image](https://github.com/vetafeda/DataBook/assets/124678022/ba2a2f00-0479-4553-85da-990b165ae5e5)

2. DFD

Контекстная диаграмма в методологии DFD:
![image](https://github.com/vetafeda/DataBook/assets/124678022/5aa81364-712b-4468-a431-b997c0c97136)
Декомпозиция контекстной диаграммы:
![image](https://github.com/vetafeda/DataBook/assets/124678022/b5896c44-06e2-49a1-a521-6699a949237a)
Декомпозиция процесса «Реализация продажи товаров клиентам» DFD:
![image](https://github.com/vetafeda/DataBook/assets/124678022/4a3090ae-d8a7-41d1-aeca-eb3279959c54)

3. IDEF3

Контекстная диаграмма в методологии IDEF3:
![image](https://github.com/vetafeda/DataBook/assets/124678022/7ced4344-54d0-44a3-850a-5d0494bc6440)
Диаграмма декомпозиции активности «Обработка поставок»:
![image](https://github.com/vetafeda/DataBook/assets/124678022/92cac25f-c0c5-49bd-9c06-4b21e69d8250)
Диаграмма декомпозиции активности «Продажа клиентам товаров»:
![image](https://github.com/vetafeda/DataBook/assets/124678022/896e9641-ae56-4d78-bc47-dc738ce57477)

4. UML диаграмма вариантов использования Use Case
![image](https://github.com/vetafeda/DataBook/assets/124678022/60c5bd60-32eb-4393-b295-3ad487d03180)
![image](https://github.com/vetafeda/DataBook/assets/124678022/c0a28b3e-788e-4bc7-af28-888884ed2b5c)
![image](https://github.com/vetafeda/DataBook/assets/124678022/3896eea0-67b1-42db-a937-76a9394f5241)
![image](https://github.com/vetafeda/DataBook/assets/124678022/27edf0bc-a5b2-40fc-945c-29ffce5d28a9)

5. UML диаграмма классов (процесса выбора товара онлайн)
![image](https://github.com/vetafeda/DataBook/assets/124678022/a2c78445-d4c7-46d3-b8ba-3b98dff05101)

6. ER-диаграмма

Физическая модель:
![image](https://github.com/vetafeda/DataBook/assets/124678022/18062697-63f8-4cde-b4b8-ec17aabe6888)
В MySQL Workbench:
![image](https://github.com/vetafeda/DataBook/assets/124678022/e4274a31-7571-424a-bcc3-390ca2834cf0)

В качестве оболочки для работы с сервером MySQL был использован программный пакет MySQL Workbench. 

Также был реализован пользовательский интерфейс базы данных на языке программирования Python. На рисунках ниже представлено главное окно при открытии программы, а также окна входа и регистрации с шифрованием пароля, окна взаимодействия с БД. Когда происходят изменения в интерфейсе, меняется и сама база данных.

Главное окно
![image](https://github.com/vetafeda/DataBook/assets/124678022/bc5e7f84-4623-4224-8788-2545f251359d)

Окно входа
![image](https://github.com/vetafeda/DataBook/assets/124678022/91e55278-5198-4ac9-bf5e-83dcd3f28f6e)

Окно регистрации
![image](https://github.com/vetafeda/DataBook/assets/124678022/01c4f015-2ffb-43df-872e-d989b43ff567)

Основное окно взаимодействия с БД
![image](https://github.com/vetafeda/DataBook/assets/124678022/a9c6dc02-8e3e-48ce-bd64-5f4524ab763b)

Окно при нажатии кнопки «Каталог» 
![image](https://github.com/vetafeda/DataBook/assets/124678022/e0e75dc5-1174-493a-9d18-7b0e4fc8653b)

Поиск
![image](https://github.com/vetafeda/DataBook/assets/124678022/a33e68e6-eabd-4119-bc6a-7a4767bff272)

Окно добавления книги
![image](https://github.com/vetafeda/DataBook/assets/124678022/ad96a0df-2ca2-448c-a8c7-d2d1893065c3)

Окно редактирования книги
![image](https://github.com/vetafeda/DataBook/assets/124678022/e371d91e-057a-435e-a488-593431099f1b)

Окно после нажатия кнопки «Мои заказы»
![image](https://github.com/vetafeda/DataBook/assets/124678022/911191e9-59c8-45f7-8dfb-67965162fd84)

Просмотр оформленного заказа в окне «Мои заказы»
![image](https://github.com/vetafeda/DataBook/assets/124678022/8dcf6272-7c67-4d67-8fcd-256664e153ba)

Окно после нажатия кнопки «Информация» с возможностью запросить скидочную карту тем клиентам, у кого ее нет
![image](https://github.com/vetafeda/DataBook/assets/124678022/36f7b145-1788-400e-bef0-7fe7944134a1)

Окно после нажатия кнопки «Расчет со %»
![image](https://github.com/vetafeda/DataBook/assets/124678022/7870e473-e30b-427a-81b4-07d9d391624f)

Окно после нажатия кнопки «Доставка»
![image](https://github.com/vetafeda/DataBook/assets/124678022/5fa6dc44-3cef-496f-8473-0df681ffe439)

Окно после нажатия кнопки «Оформить заказ»
![image](https://github.com/vetafeda/DataBook/assets/124678022/9bcb5766-1f17-46a3-90b1-936c37f55cec)
