menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def get_order():
    total_cost = 0
    while True:
        try:
            order = input("Item: ").title()
            price = float(menu[order])
            total_cost += price
            print(f'Total: ${total_cost:.2f}')
            continue
        except (ValueError, KeyError):
            continue
        except EOFError:
            print("")
            break


if __name__ == "__main__":
    get_order()


