
def grettings():
     print('Добро пожаловать в телефонный справочник!')

def menu():
    print('===================Меню==================')
    print("1 - Добавить контакт")
    print("2 - Удалить контакт")
    print("3 - Изменить контакт")
    print("4 - Показать все контакты")
    print("5 - Найти контакт")
    print("6 - Экспортировать")
    print("7 - Импортировать")
    print("8 - Выйти из программы")
    action = input('Выберите действие: ')  
    return action

def add_contact_view():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    return name, surname, patronymic, phone_number

def delete_contact_view():
    search_query = input("Введите фамилию или имя для удаления контакта: ")
    return search_query

def edit_contact_view():
    search_query = input("Введите фамилию или имя для редактирования контакта: ")
    return search_query

def show_contacts_view(contacts):
    if not contacts:
        print("В справочнике нет контактов.")
    else:
       print("Список контактов:")
    for contact in contacts:
       print(contact)    

def search_contact_view():
    search_query = input("Введите фамилию или имя для поиска контакта: ")
    return search_query

def search_contacts(contacts):
    search_query = search_contact_view()
    result = [contact for contact in contacts if search_query in contact]
    if result:
        print("Контакт найден:")
        show_contacts_view(result)
    else:
         print("Контакт не найден.")
    return result
def search_result_view(result):
    if result:
        print("Контакт найден:")
        show_contacts_view(result)
    else:
        print("Контакт не найден.")

def exit_message():
    print("До свидания!")

def add_contact_success():
    print("Контакт добавлен.")

def delete_contact_success():
    print("Контакт удален.")

def edit_contact_success():
    print("Контакт изменен.")

def import_data_view():
    file_name = input("Введите имя файла .txt для импорта данных: ")
    return file_name


def export_data_view():
    file_name = input("Введите имя файла для экспорта данных: ")
    return file_name


def import_data_success():
    print("Данные импортированы.")


def export_data_success():
    print("Данные экспортированы.")

