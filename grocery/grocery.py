def get_grocery():
    groceries = dict()
    while True:
        times = 1
        try:
            grocery = input("").upper()
            if grocery not in groceries:
                groceries[grocery] = times
            else:
                times += 1
                groceries[grocery] = times
        except (ValueError, KeyError):
            continue
        except EOFError:
            print("")
            break
    return groceries

def print_grocery():
    # groceries = get_grocery()
    groceries = dict(sorted(get_grocery().items()))
    for key, value in groceries.items():
        print(f'{value} {key}')


if __name__ == "__main__":
    print_grocery()