# Завдання 7. Використання методу Монте-Карло
# Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, 
# і визначає ймовірність кожної можливої суми.
# Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на 
# обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи 
# ці дані, обчисліть імовірність кожної суми.
# На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.
# Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.
# Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.

# - Програмно реалізовано алгоритм для моделювання кидання двох ігрових кубиків і побудови таблиці сум та їх імовірностей 
# за допомогою методу Монте-Карло.
# - Код виконується та імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, підраховує, 
# скільки разів кожна можлива сума з’являється у процесі симуляції, і визначає ймовірність кожної можливої суми.
# - Створено таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.
# - Зроблено висновки щодо правильності розрахунків шляхом порівняння отриманих за допомогою методу Монте-Карло результатів та
# результатів аналітичних розрахунків. Висновки оформлено у вигляді файлу readme.md фінального завдання.

import random
import matplotlib.pyplot as plt
from collections import defaultdict
from typing import Dict, Tuple

def monte_carlo_simulation(num_rolls: int = 1000000) -> Dict[int, float]:
    counts = defaultdict(int)
    
    for _ in range(num_rolls):
        total = random.randint(1, 6) + random.randint(1, 6)
        counts[total] += 1
        
    probabilities = {
        sum_val: count/num_rolls 
        for sum_val, count in counts.items()
    }
    
    return dict(sorted(probabilities.items()))

def plot_probabilities(monte_carlo: Dict[int, float]) -> None:
    plt.figure(figsize=(10, 6))
    
    x = list(monte_carlo.keys())
    mc_probs = [monte_carlo[k] for k in x]
    
    width = 0.35
    plt.bar([i-width/2 for i in x], mc_probs, width, label='Monte Carlo', color='skyblue')
    
    plt.xlabel('Sum of Dice')
    plt.ylabel('Probability')
    plt.title('Dice Roll Probabilities: Monte Carlo')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    monte_carlo_probs = monte_carlo_simulation()
    
    print("\nMonte Carlo Probabilities:")
    for sum_val, prob in monte_carlo_probs.items():
        print(f"Sum {sum_val}: {prob:.4f}")
        
    
    plot_probabilities(monte_carlo_probs)
