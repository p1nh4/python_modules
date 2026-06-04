#!/usr/bin/env python3

class Plant:
    name: str
    height: int
    age: int

    # def __init__(self) -> None
    #    pass -- python cria un __init__ vazio por padrao

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: {self.height}cm, {self.age} days old"
            )


def ft_garden_data() -> None:
    plant_1 = Plant()
    plant_1.name = "Rose"
    plant_1.height = 25
    plant_1.age = 30

    plant_2 = Plant()
    plant_2.name = "Sunflower"
    plant_2.height = 80
    plant_2.age = 45

    plant_3 = Plant()
    plant_3.name = "Cactus"
    plant_3.height = 15
    plant_3.age = 120

    print("=== Garden Plant Registry ===")
    plant_1.show()
    plant_2.show()
    plant_3.show()


def main() -> None:
    ft_garden_data()


if __name__ == "__main__":
    main()
