import numpy as np

# Функція корисності
def utility(x):
    return ((x + 5) ** 2) / 15

# Прибутки за рішеннями (в десятках тисяч доларів)
profits = {
    'I': [10, -5, -5],
    'II': [-5, -5, 10],
    'III': [1.5, 1.5, 0],
    'IV': [0, 0, 0]
}

# Ймовірності для кожного варіанту прибутків
probabilities = [0.5, 0.1, 0.4]

# Розрахунок сподіваної корисності для кожного рішення
def expected_utility(profits, probabilities):
    return np.sum([p * utility(x) for p, x in zip(probabilities, profits)])

# Очікувана корисність для кожного рішення
expected_utilities = {key: expected_utility(value, probabilities) for key, value in profits.items()}

# Порівняння ефективності рішень
best_decision = max(expected_utilities, key=expected_utilities.get)  # Рішення з максимальною корисністю

# Виведення результатів
print("Сподівана корисність для кожного рішення:")
for decision, eu in expected_utilities.items():
    print(f"  Рішення {decision}: {eu:.4f}")

print(f"\nНайефективніше рішення за корисністю: {best_decision}")
