def import_data(file_name):
   #  file_name = input("Введите имя файла .txt для импорта данных: ")
    with open(file_name, 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
    with open('phonebook.txt', 'a', encoding = 'utf-8') as file:
        for line in lines:
            file.write(line)
    print("Данные импортированы.")

def export_data(file_name):
   #  file_name = input("Введите имя файла для экспорта данных: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    with open('phonebook.txt', 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
    with open(file_name, 'w') as file:
        for line in lines:
            file.write(line)
    print("Данные экспортированы.")

def add_contact(name, surname, patronymic, phone_number):
    with open('phonebook.txt', 'a', encoding = 'utf-8') as file:
        file.write(f"{surname} {name} {patronymic} {phone_number}\n")

def delete_contact(search_query):
    with open('phonebook.txt', 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
    with open('phonebook.txt', 'w', encoding = 'utf-8') as file:
        for line in lines:
            if search_query not in line.strip("\n"):
                file.write(line)

def edit_contact(search_query):
    with open('phonebook.txt', 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
    with open('phonebook.txt', 'w', encoding = 'utf-8') as file:
        for line in lines:
            if search_query in line.strip("\n"):
                name = input("Введите новое имя: ")
                surname = input("Введите новую фамилию: ")
                patronymic = input("Введите новое отчество: ")
                phone_number = input("Введите новый номер телефона: ")
                file.write(f"{surname} {name} {patronymic} {phone_number}\n")
            else:
                file.write(line)

def show_contacts():
  contacts = []
  with open('phonebook.txt', 'r', encoding = 'utf-8') as file:
      lines = file.readlines()
      for line in lines:
          contacts.append(line.strip())
  return contacts
def search_contact(search_query):
    result = []
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if search_query in line.strip("\n"):
                result.append(line.strip())
    return result