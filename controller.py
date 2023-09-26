import text
import view
import model


def search_func(msg: str):
    word = view.input_info(msg)
    result = model.search(word)
    view.show_contacts(result, text.search_contact_error(word))


def start():
    while True:
        choice = view.main_menu()
        match choice:
            case '1':
                model.open_file()
                view.print_message(text.open_successful)
            case '2':
                model.save_file()
                view.print_message(text.save_successful)
            case '3':
                view.show_contacts(model.phone_book, text.empty_phone_book_error)
            case '4':
                contact = view.input_new_contact(text.input_new_contact)
                model.new_contact(contact)
                view.print_message(text.contact_successful_result(contact[0], 0))
            case '5':
                search_func(text.input_search_word)
            case '6':
                search_func(text.input_edit_word)
                u_id = view.input_info(text.input_edit_id)
                new_contact = view.input_new_contact(text.input_edit_contact)
                name = model.edit(int(u_id), new_contact)
                view.print_message(text.contact_successful_result(name, 1))

            case '7':
                search_func(text.input_delete_word)
                u_id = view.input_info(text.input_delete_id)
                name = model.delete(int(u_id))
                view.print_message(text.contact_successful_result(name, 2))

            case '8':
                view.print_message(text.good_bay)
                break
