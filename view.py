import text


def main_menu():
    print(text.main_menu[0])
    for i in range(len(text.main_menu)):
        if i:
            print(f'{i:>3}.{text.main_menu[i]}')
    while True:
        choice = input(text.input_main_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return choice
        print(text.input_main_menu_error)


def print_message(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')


def show_contacts(book: dict, msg: str):
    if book:
        max_size = [len(max(field, key=len)) for field in zip(*list(book.values()))]
        print('\n' + '=' * (sum(max_size) + 10))
        for u_id, contact in book.items():
            contact = '   '.join([f'{contact[i]:<{max_size[0]}}' for i in range(len(contact))])
            print(f'{u_id:>3} {contact}')
        print('=' * (sum(max_size) + 10) + '\n')
    else:
        print_message(msg)


def input_new_contact(msg: list):
    contact = []
    for filed in msg:
        contact.append((input(filed)))
    return contact


def input_info(msg: str):
    return input(msg)
