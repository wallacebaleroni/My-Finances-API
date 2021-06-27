from src.controller.controller import *

COLUMN_DATE_SIZE = 12
COLUMN_CATEGORY_SIZE = 11
COLUMN_DESCRIPTION_SIZE = 11
COLUMN_COMMENTARY_SIZE = 12
COLUMN_ACCOUNT_SIZE = 9


def print_header():
    print("CONTROLE FINANCEIRO")
    print("|{0}|{1}|{2}|{3}|{4}|".format(pad_center("Data", COLUMN_DATE_SIZE),
                                         pad_center("Categoria", COLUMN_CATEGORY_SIZE),
                                         pad_center("Descrição", COLUMN_DESCRIPTION_SIZE),
                                         pad_center("Comentário", COLUMN_COMMENTARY_SIZE),
                                         pad_center("NuConta", COLUMN_ACCOUNT_SIZE)))


def print_entries(entries):
    if entries is not None:
        for entry in entries:
            print("|{0}|{1}|{2}|{3}|{4}|".format(pad_center(entry.date, COLUMN_DATE_SIZE),
                                                 pad_center(entry.category, COLUMN_CATEGORY_SIZE),
                                                 pad_center(entry.description, COLUMN_DESCRIPTION_SIZE),
                                                 pad_center(entry.commentary, COLUMN_COMMENTARY_SIZE),
                                                 pad_center("R$ " + entry.get_formatted_value(), COLUMN_ACCOUNT_SIZE)))


def print_footer(entries):
    print("footer")


def print_table():
    controller = Controller()
    entries = controller.get_all_entries()

    print_header()
    print_entries(entries)
    print_footer(entries)


def pad_center(string, size, padding=" ", truncate=True):
    if len(string) == size:
        return string
    elif len(string) < size:
        pad_size = size - len(string)
        if pad_size % 2 == 0:
            left_pad = pad_size // 2
            right_pad = pad_size // 2
        else:
            left_pad = pad_size // 2
            right_pad = pad_size // 2 + 1
        return padding * left_pad + string + padding * right_pad
    else:
        if truncate:
            return string[:size]
        else:
            return string


def start():
    print_table()
