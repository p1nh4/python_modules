#!/usr/bin/env python3


class Plant:
    """A class representing a plant with name, height, and age"""

    def __init__(self, name: str, height: float, age: int) -> None:
        """Initialize a plant with name, height, and age"""
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def show(self) -> None:
        """Print plant information"""
        print(
            f"Created: {self.name.capitalize()}: "
            f"{self.height}cm, {self.age} days old"
        )


def main() -> None:
    """Create plants automatically and display their contents"""
    print("=== Plant Factory Output ===")

    plant_data: list[tuple[str, float, int]] = [
        ("rose", 25.0, 30),
        ("oak", 200.0, 365),
        ("cactus", 5.0, 90),
        ("sunflower", 80.0, 45),
        ("fern", 15.0, 120)
    ]

    for name, height, age in plant_data:
        plant: Plant = Plant(name, height, age)
        plant.show()


if __name__ == "__main__":
    main()
