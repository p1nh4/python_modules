#!/usr/bin/env python3

class Plant:
    """A class representing a plant."""

    def __init__(
        self, name: str, height: float,
        age: int, growth_rate: float
    ) -> None:
        self.name: str = name
        self.height: float = height
        self.plant_age: int = age
        self.growth_rate: float = growth_rate

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.plant_age += 1

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm,"
              f" {self.plant_age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    plant = Plant("rose", 25.0, 30, 0.8)
    plant.show()
    initial = plant.height
    for day in range(1, 8):
        plant.grow()
        plant.age()
        print(f"=== Day {day} ===")
        plant.show()
    growth = round(plant.height - initial, 1)
    print(f"Growth this week: {growth}cm")
