#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(
                f"{self.name.capitalize()}: "
                f"{self.height:.1f}cm, "
                f"{self.age} days old"
            )


def ft_plant_factory() -> None:
    """
    # Versao 1, sem otimizacao
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Oak", 200, 365)
    plant_3 = Plant("Cactus", 5, 90)
    plant_4 = Plant("Sunflower", 80, 45)
    plant_5 = Plant("Fern", 15, 120)

    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    plant_1.show()
    print("Created: ", end="")
    plant_2.show()
    print("Created: ", end="")
    plant_3.show()
    print("Created: ", end="")
    plant_4.show()
    print("Created: ", end="")
    plant_5.show()
    """

    plants: list[Plant] = [
            Plant("Rose", 25, 30),
            Plant("Oak", 200, 365),
            Plant("Cactus", 5, 90),
            Plant("Sunflower", 80, 45),
            Plant("Fern", 15, 120),
            ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


def main() -> None:
    ft_plant_factory()


if __name__ == "__main__":
    main()
