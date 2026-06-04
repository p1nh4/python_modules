#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    t_age: int
    t_week_grow: float

    def __init__(self) -> None:
        self.t_week_grow = 0.00

    def grow(self, grow_week: float) -> None:
        self.height += grow_week
        self.t_week_grow += grow_week

    def age(self, days: int) -> None:
        self.t_age += days

    def show(self) -> None:
        print(
                f"{self.name.capitalize()}: "
                f"{self.height:.1f}cm, "
                f"{self.t_age} days old"
            )


def ft_plant_grow() -> None:
    plant_1 = Plant()
    plant_1.name = "Rose"
    plant_1.height = 25
    plant_1.t_age = 30

    print("=== Garden Plant Growth ===")
    plant_1.show()
    for i in range(1, 8):
        plant_1.grow(0.8)
        plant_1.age(1)
        print(f"=== Day {i} ===")
        plant_1.show()

    print(f"Growth this week: {plant_1.t_week_grow:.1f}cm")


def main() -> None:
    ft_plant_grow()


if __name__ == "__main__":
    main()
