def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print("Файл мазмұны:")
            print(file.read())
    except FileNotFoundError:
        print("Қате: Файл табылмады!")

file_name = input("Оқылатын файл атын енгіз: ")
read_file(file_name)
