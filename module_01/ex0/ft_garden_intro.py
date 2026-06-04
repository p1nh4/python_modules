#!/usr/bin/env python3
def ft_garden_intro() -> None:
    print("=== Welcome to My Garden ===")

    plant: str = "Rose"
    height: int = 25
    age: int = 30

    print(f"Plant: {plant}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")

    print("=== End of Program ===")


def main() -> None:
    ft_garden_intro()


if __name__ == "__main__":
    main()
