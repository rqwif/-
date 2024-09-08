import math

# обчислення математичного очікування
def expected_value(probabilities, values):
    return sum(p * v for p, v in zip(probabilities, values))

# обчислення дисперсії
def variance(probabilities, values, expected):
    return sum(p * (v - expected) ** 2 for p, v in zip(probabilities, values))

# обчислення коефіцієнта варіації
def coefficient_of_variation(sigma, expected):
    return sigma / expected

# Вхідні дані для першої угоди
probabilities_1 = [0.7, 0.3]
values_1 = [9000, 7000]

# Вхідні дані для другої угоди
probabilities_2 = [0.6, 0.4]
values_2 = [13000, 7500]

# Розрахунки для першої угоди
E1 = expected_value(probabilities_1, values_1)
Var1 = variance(probabilities_1, values_1, E1)
sigma1 = math.sqrt(Var1)
CV1 = coefficient_of_variation(sigma1, E1)

# Розрахунки для другої угоди
E2 = expected_value(probabilities_2, values_2)
Var2 = variance(probabilities_2, values_2, E2)
sigma2 = math.sqrt(Var2)
CV2 = coefficient_of_variation(sigma2, E2)

# Виведення результатів
print(f"Перша угода: Математичне очікування = {E1:.2f} грн, Дисперсія = {Var1:.2f}, "
      f"Середньоквадратичне відхилення = {sigma1:.2f}, Коефіцієнт варіації = {CV1:.4f}")

print(f"Друга угода: Математичне очікування = {E2:.2f} грн, Дисперсія = {Var2:.2f}, "
      f"Середньоквадратичне відхилення = {sigma2:.2f}, Коефіцієнт варіації = {CV2:.4f}")

# Висновок про ризик на основі коефіцієнта варіації
if CV1 < CV2:
    print("Найменш ризикована угода: Перша угода")
else:
    print("Найменш ризикована угода: Друга угода")
