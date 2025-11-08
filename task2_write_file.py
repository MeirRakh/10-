def write_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        print("Мәтін файлға сәтті жазылды!")

file_name = input("Файл атын енгіз: ")
data = input("Файлға жазылатын мәтінді енгіз: ")

write_file(file_name, data)
