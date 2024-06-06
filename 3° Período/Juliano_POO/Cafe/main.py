from cafe_class import Cafe

pequeno = Cafe("Pequeno", 5)
medio = Cafe("Medio", 8)
grande = Cafe("Grande", 10)

try:
    user_budget = float(input("Quanto você tem? "))
except ValueError:
    exit ("Por favor, coloque um número: ")

for cafe in [grande, medio, pequeno]:
    cafe.vender(user_budget)