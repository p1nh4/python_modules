#!/usr/bin/env python3


class Plant:
    """A class representing a plant with validation for height and age"""

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height if height >= 0 else 0.0
        self._age: int = age if age >= 0 else 0
        self.show()

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = float(height)
            print(f"Height updated: {height}cm")
        else:
            print(
                  f"{self._name.capitalize()}: Error, height can't be negative"
                 )
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days")
        else:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(
            f"Plant created: {self._name.capitalize()}: "
            f"{self._height}cm, {self._age} days old"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("rose", 15.0, 10)
    print()
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    plant.set_age(-3)
    print()
    print(
        f"Current state: {plant._name.capitalize()}: "
        f"{plant.get_height()}cm, {plant.get_age()} days old"
    )
