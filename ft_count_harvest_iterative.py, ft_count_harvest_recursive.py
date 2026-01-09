def ft_count_harvest_iterative():
    days_until_harvest = int(input("Enter the number of days until harvest: "))
    day = 1
    while day <= days_until_harvest:
        print(f"Day {day}")
        day += 1
    print("Harvest Day!")

if __name__ == "__main__":
    ft_count_harvest_iterative()

def ft_count_harvest_recursive(day=1, days_until_harvest=None):
    if days_until_harvest is None:
        days_until_harvest = int(input("Enter the number of days until harvest: "))
    if day > days_until_harvest:
        print("Harvest Day!")
    else:
        print(f"Day {day}")
        ft_count_harvest_recursive(day + 1, days_until_harvest)

if __name__ == "__main__":
