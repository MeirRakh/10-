class AgeError(Exception):
    pass
try:
    age = int(input("Жасыңызды енгізіңіз: "))
    if age < 0:
        raise AgeError("Жас теріс болмауы керек!")
    print("Сіз қабылдандыңыз.")
except AgeError as e:
    print("Қате:", e)
