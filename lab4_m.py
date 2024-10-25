import numpy as np 
from scipy.optimize import minimize

# Вихідні дані
m = np.array([0.10, 0.20, 0.50])  # Очікувані норми прибутку
sigma = np.array([0.02, 0.10, 0.20])  # Середньоквадратичні відхилення
correlation_matrix = np.array([
    [1, 0, 0],
    [0, 1, -0.6],
    [0, -0.6, 1]
])

# Ковариаційна матриця
cov_matrix = np.outer(sigma, sigma) * correlation_matrix

# Функція для обчислення ризику портфеля
def portfolio_risk(weights, cov_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

# Функція для обчислення прибутку портфеля
def portfolio_return(weights, m):
    return np.dot(weights, m)

# Обмеження суми ваг (ваги повинні складати 1)
def weight_sum_constraint(weights):
    return np.sum(weights) - 1

# a) Мінімізація ризику портфеля
def optimize_min_risk():
    num_assets = len(m)
    initial_weights = np.ones(num_assets) / num_assets
    bounds = [(0, 1)] * num_assets
    constraints = [{'type': 'eq', 'fun': weight_sum_constraint}]
    
    result = minimize(portfolio_risk, initial_weights, args=(cov_matrix), bounds=bounds, constraints=constraints)
    
    return result.x, portfolio_return(result.x, m), portfolio_risk(result.x, cov_matrix)

# б) Оптимізація для досягнення цільової прибутковості mC = 30%
def optimize_target_return(target_return=0.30):
    num_assets = len(m)
    initial_weights = np.ones(num_assets) / num_assets
    bounds = [(0, 1)] * num_assets
    constraints = [
        {'type': 'eq', 'fun': weight_sum_constraint},
        {'type': 'eq', 'fun': lambda weights: portfolio_return(weights, m) - target_return}
    ]
    
    result = minimize(portfolio_risk, initial_weights, args=(cov_matrix), bounds=bounds, constraints=constraints)
    
    return result.x, portfolio_return(result.x, m), portfolio_risk(result.x, cov_matrix)

# в) Оптимізація для досягнення цільового ризику σС = 15%
def optimize_target_risk(target_risk=0.15):
    num_assets = len(m)
    initial_weights = np.ones(num_assets) / num_assets
    bounds = [(0, 1)] * num_assets
    constraints = [
        {'type': 'eq', 'fun': weight_sum_constraint},
        {'type': 'ineq', 'fun': lambda weights: target_risk - portfolio_risk(weights, cov_matrix)}
    ]
    
    result = minimize(lambda weights: -portfolio_return(weights, m), initial_weights, bounds=bounds, constraints=constraints)
    
    return result.x, portfolio_return(result.x, m), portfolio_risk(result.x, cov_matrix)

# Розрахунок для кожного випадку
# а) Мінімальний ризик
weights_min_risk, return_min_risk, risk_min_risk = optimize_min_risk()
print("Мінімізація ризику:")
print(f"Ваги: {weights_min_risk}")
print(f"Очікувана норма прибутку: {return_min_risk:.2%}")
print(f"Ризик портфеля: {risk_min_risk:.2%}\n")

# б) Цільова прибутковість mC = 30%
weights_target_return, return_target_return, risk_target_return = optimize_target_return()
print("Цільова прибутковість (30%):")
print(f"Ваги: {weights_target_return}")
print(f"Очікувана норма прибутку: {return_target_return:.2%}")
print(f"Ризик портфеля: {risk_target_return:.2%}\n")

# в) Цільовий ризик σС = 15%
weights_target_risk, return_target_risk, risk_target_risk = optimize_target_risk()
print("Цільовий ризик (15%):")
print(f"Ваги: {weights_target_risk}")
print(f"Очікувана норма прибутку: {return_target_risk:.2%}")
print(f"Ризик портфеля: {risk_target_risk:.2%}")
