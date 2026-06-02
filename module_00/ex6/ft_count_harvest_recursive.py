def ft_count_harvest_recursive() -> None:
    harvest = int(input("Days until harvest: "))

    def ft_count_days(today):
        if today > harvest:
            return
        else:
            print(f"Day {today}")
            ft_count_days(today + 1)
    ft_count_days(1)
    print("Harvest time!")
