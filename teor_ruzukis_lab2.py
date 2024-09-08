import math

# обчислення математичного очікування
def expected_value(probabilities, values):
    return sum(p * v for p, v in zip(probabilities, values))

# обчислення дисперсії
def variance(probabilities, values, expected):
    return sum(p * (v - expected) ** 2 for p, v in zip(probabilities, values))


probabilities_1 = [0.7, 0.3]
values_1 = [9000, 7000]


probabilities_2 = [0.6, 0.4]
values_2 = [13000, 7500]


E1 = expected_value(probabilities_1, values_1)
Var1 = variance(probabilities_1, values_1, E1)
sigma1 = math.sqrt(Var1)


E2 = expected_value(probabilities_2, values_2)
Var2 = variance(probabilities_2, values_2, E2)
sigma2 = math.sqrt(Var2)


print(f"Перша угода: Математичне очікування = {E1:.2f} грн, Дисперсія = {Var1:.2f}, Середньоквадратичне відхилення = {sigma1:.2f}")
print(f"Друга угода: Математичне очікування = {E2:.2f} грн, Дисперсія = {Var2:.2f}, Середньоквадратичне відхилення = {sigma2:.2f}")


if sigma1 < sigma2:
    print("Найменш ризикована угода: Перша угода")
else:
    print("Найменш ризикована угода: Друга угода")
