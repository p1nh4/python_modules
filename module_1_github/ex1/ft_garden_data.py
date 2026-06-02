#!/usr/bin/env python3

class Plant:
    """A class representing a plant with name, height, and age"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with name, height, and age"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: {self.height}cm, {self.age} days old"
            )


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("rose", 25, 30)
    plant2 = Plant("sunflower", 80, 45)
    plant3 = Plant("cactus", 15, 120)
    plant1.show()
    plant2.show()
    plant3.show()
