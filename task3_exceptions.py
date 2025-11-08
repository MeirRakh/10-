try:
    number = int(input("Сан енгіз: "))
    result = 10 / number
    print("Нәтиже:", result)

except ValueError:
    print("Қате: Сан енгізу керек!")

except ZeroDivisionError:
    print("Қате: Нөлге бөлу мүмкін емес!")
