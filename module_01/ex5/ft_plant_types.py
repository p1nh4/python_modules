#!/usr/bin/env python3
class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, n_height: float) -> None:
        if n_height < 0:
            print(
                    f"{self._name.capitalize()}: "
                    "Error, height can't be negative"
                 )
            print("Height update rejected")
        else:
            self._height = n_height
            print(f"Height updated: {int(self._height)}cm")

    def set_age(self, n_age: int) -> None:
        if n_age < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = n_age
            print(f"Age updated: {self._age} days")

    def grow(self, grow_week: float) -> None:
        self._height += grow_week

    def age(self, days: int) -> None:
        self._age += days

    def show(self) -> None:
        print(
                f"{self._name.capitalize()}: "
                f"{self._height:.1f}cm, "
                f"{self._age} days old"
            )


class Flower(Plant):
    _color: str
    _is_bloomed: bool

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._is_bloomed = False

    def bloom(self) -> None:
        self._is_bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._is_bloomed:
            print(f" {self._name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")


class Tree(Plant):
    _trunk_diameter: float

    def __init__(
            self, name: str, height: float, age: int, trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name.capitalize()} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    _harvest_season: str
    _nutritional_value: int

    def __init__(
            self, name: str, height: float, age: int,
            harvest_season: str, nutritional_value: int
            ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += days

    def grow(self, grow_amount: float) -> None:
        super().grow(grow_amount)

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season.capitalize()}")
        print(f" Nutritional value: {self._nutritional_value}")


def ft_plant_types() -> None:

    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("rose", 15, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("oak", 200, 365, 5)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("tomato", 5, 10, "april", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42)
    tomato.age(20)
    tomato.show()


def main() -> None:
    ft_plant_types()


if __name__ == "__main__":
    main()
