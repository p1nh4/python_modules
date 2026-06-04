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

    def show(self) -> None:
        print(
                f"{self._name}: "
                f"{self._height:.1f}cm, "
                f"{self._age} days old"
            )


def ft_garden_security() -> None:
    plant_1 = Plant("Rose", 15, 10)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    plant_1.show()
    print()

    plant_1.set_height(25)
    plant_1.set_age(30)
    print()

    plant_1.set_height(-5)
    plant_1.set_age(-5)
    print()

    print("Current state: ", end="")
    plant_1.show()


def main() -> None:
    ft_garden_security()


if __name__ == "__main__":
    main()
