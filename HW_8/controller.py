import view
import model

def run():
 view.grettings()
 while True:
  action = view.menu()
  if action == '1':
    name,surname,patronymic,phone_number=view.add_contact_view()
    model.add_contact(name,surname,patronymic,phone_number)
    view.add_contact_success()
  elif action == '2':
    search_query = view.delete_contact_view()
    model.delete_contact(search_query)
    view.delete_contact_success()
  elif action == '3':
    search_query=view.edit_contact_view()
    model.edit_contact(search_query)
    view.edit_contact_success()
  elif action == '4':
    contacts = model.show_contacts()
    view.show_contacts_view(contacts)
  elif action == '5':
    search_query = view.search_contact_view()
    result = model.search_contact(search_query)
    view.search_result_view(result)
  elif action == '6':
    file_name = view.export_data_view()
    model.export_data(file_name)
    view.export_data_success()
  elif action == '7':
    file_name = view.import_data_view()
    model.import_data(file_name)
    view.import_data_success()
  elif action == '8':
    view.exit_message()
    break    