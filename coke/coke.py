def main():
    accepted_coins = [25, 10, 5]
    price = 50
    total_inserted = 0
    remaining_amount = 50

    while total_inserted < price:
        coin = int(input("Insert coin: "))
        if coin not in accepted_coins:
            print("Amount Due:", remaining_amount)
            continue

        total_inserted += coin
        remaining_amount = price - total_inserted

        if remaining_amount > 0:
            print(f"Amount Due: {remaining_amount}")

    if total_inserted > price:
        change = total_inserted - price
        print(f"Change Owed: {change}")
    else:
        print("Change Owed: 0")

if __name__ == "__main__":
    main()
