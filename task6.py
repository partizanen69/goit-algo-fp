# Завдання 6. Жадібні алгоритми та динамічне програмування
# Необхідно написати програму на Python, яка використовує два підходи — жадібний 
# алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору 
# їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.
# Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у
# вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.
# Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, 
# максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.
# Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, 
# яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.
# - Програмно реалізовано функцію, яка використовує принцип жадібного алгоритму. Код виконується і 
# повертає назви страв, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.
# - Програмно реалізовано функцію, яка використовує принцип динамічного
# програмування. Код виконується і повертає оптимальний набір страв для максимізації калорійності
# при заданому бюджеті.



items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items: dict[str, dict[str, int]], budget: int) -> tuple[list[str], int, int]:
    ratios = {
        item: data["calories"] / data["cost"] 
        for item, data in items.items()
    }
    
    sorted_items = sorted(ratios.items(), key=lambda x: x[1], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item, _ in sorted_items:
        item_cost = items[item]["cost"]
        if total_cost + item_cost <= budget:
            selected_items.append(item)
            total_cost += item_cost
            total_calories += items[item]["calories"]
            
    return selected_items, total_calories, total_cost

def dynamic_programming(items: dict[str, dict[str, int]], budget: int) -> tuple[list[str], int, int]:
    item_names = list(items.keys())
    n = len(items)
    
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item = item_names[i-1]
        cost = items[item]["cost"]
        calories = items[item]["calories"]
        
        for j in range(budget + 1):
            if cost <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + calories)
            else:
                dp[i][j] = dp[i-1][j]
    
    selected_items = []
    total_cost = 0
    curr_budget = budget
    
    for i in range(n, 0, -1):
        if dp[i][curr_budget] != dp[i-1][curr_budget]:
            item = item_names[i-1]
            selected_items.append(item)
            total_cost += items[item]["cost"]
            curr_budget -= items[item]["cost"]
    
    selected_items.reverse()
    return selected_items, dp[n][budget], total_cost


if __name__ == "__main__":
    budget = 100
    
    # Test greedy algorithm
    greedy_items, greedy_calories, greedy_cost = greedy_algorithm(items, budget)
    print("\nGreedy Algorithm Results:")
    print(f"Selected items: {greedy_items}")
    print(f"Total calories: {greedy_calories}")
    print(f"Total cost: {greedy_cost}")
    
    # Test dynamic programming
    dp_items, dp_calories, dp_cost = dynamic_programming(items, budget)
    print("\nDynamic Programming Results:")
    print(f"Selected items: {dp_items}")
    print(f"Total calories: {dp_calories}")
    print(f"Total cost: {dp_cost}")
