#!/usr/bin/env python3

class Plant:
    _name: str
    _height: float
    _age: int
    _is_tree: bool
    _stats: 'History'

    class History:
        _grow_count: int
        _age_count: int
        _show_count: int
        _shade_count: int

        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0
            self._shade_count = 0

        def show(self, is_tree: bool = False) -> None:
            print(
                    f"Stats: {self._grow_count} grow, "
                    f"{self._age_count} age, "
                    f"{self._show_count} show"
                    )
            if is_tree:
                print(f" {self._shade_count} shade")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._is_tree = False
        self._stats = self.History()

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

    @staticmethod
    def is_older(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous_plant(cls) -> 'Plant':
        return cls("Unknown plant", 0, 0)

    def grow(self, grow_week: float) -> None:
        self._height += grow_week
        self._stats._grow_count += 1

    def age(self, days: int) -> None:
        self._age += days
        self._stats._age_count += 1

    def show(self) -> None:
        print(
                f"{self._name.capitalize()}: "
                f"{self._height:.1f}cm, "
                f"{self._age} days old"
            )
        self._stats._show_count += 1


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


class Seed(Flower):
    _num_seed: int

    def __init__(
                 self, name: str, height: float,
                 age: int, color: str
                 ) -> None:
        super().__init__(name, height, age, color)
        self._num_seed = 0

    def bloom(self):
        super().bloom()
        self._num_seed += 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._num_seed}")


class Tree(Plant):
    _trunk_diameter: float

    def __init__(
            self, name: str, height: float, age: int, trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self._is_tree = True
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name.capitalize()} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )
        self._stats._shade_count += 1

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


def ft_show_plant_analytics(plant: Plant) -> None:
    print(f"[statistics for {plant._name.capitalize()}]")
    plant._stats.show(plant._is_tree)


def ft_plant_analytics() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    days: int = 30
    age = Plant.is_older(days)
    print(f"Is {days} days more than a year? -> {age}")
    days = 400
    age = Plant.is_older(days)
    print(f"Is {days} days more than a year? -> {age}")

    print("\n=== Flower")
    rose = Flower("rose", 15, 10, "red")
    rose.show()
    ft_show_plant_analytics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    ft_show_plant_analytics(rose)

    print("\n=== Tree")
    oak = Tree("oak", 200, 365, 5)
    oak.show()
    ft_show_plant_analytics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    ft_show_plant_analytics(oak)

    print("\n=== Seed")
    seed = Seed("sunflower", 80, 45, "yellow")
    seed.show()
    seed.bloom()
    print("[make sunflower grow, age and bloom]")
    seed.grow(30)
    seed.age(20)
    seed.show()
    ft_show_plant_analytics(seed)

    print("\n=== Anonymous")
    anon = Plant.anonymous_plant()
    anon.show()
    ft_show_plant_analytics(anon)


def main() -> None:
    ft_plant_analytics()


if __name__ == "__main__":
    main()
