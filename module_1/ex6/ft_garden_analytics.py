#!/usr/bin/env python3


class Plant:
    """A base class representing a plant"""

    class Stats:
        """Nested class for tracking plant statistics"""

        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0

        def display(self) -> None:
            """Display plant statistics"""
            print(
                f"Stats: {self._grow_count} grow,"
                f" {self._age_count} age,"
                f" {self._show_count} show"
            )

    def __init__(
        self, name: str, height: float,
        age: int, growth_rate: float = 2.1
    ) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self._growth_rate: float = growth_rate
        self._stats: Plant.Stats = Plant.Stats()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        """Check if given age is more than a year"""
        return age > 365

    @classmethod
    def anonymous(cls) -> 'Plant':
        """Create an anonymous plant with default values"""
        return cls("Unknown plant", 0.0, 0)

    def grow(self) -> None:
        """Grow the plant by its growth rate"""
        self._height = round(self._height + self._growth_rate, 1)
        self._stats._grow_count += 1

    def grow_older(self, amount: int = 1) -> None:
        """Age the plant by the given amount of days"""
        self._age += amount
        self._stats._age_count += 1

    def show(self) -> None:
        """Display plant information"""
        print(
            f"{self._name.capitalize()}: {self._height}cm,"
            f" {self._age} days old"
        )
        self._stats._show_count += 1


class Flower(Plant):
    """A flower with color and bloom ability"""

    def __init__(
        self, name: str, height: float,
        age: int, color: str, growth_rate: float = 2.1
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        """Set the flower as bloomed"""
        self._bloomed = True

    def show(self) -> None:
        """Display flower information"""
        super().show()
        print(f" Color: {self._color}")
        if self._bloomed:
            print(
                f" {self._name.capitalize()} is blooming beautifully!"
            )
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")


class Tree(Plant):
    """A tree with trunk diameter and shade production"""

    class Stats(Plant.Stats):
        """Extended stats for trees including shade count"""

        def __init__(self) -> None:
            super().__init__()
            self._shade_count: int = 0

        def display(self) -> None:
            """Display tree statistics"""
            super().display()
            print(f" {self._shade_count} shade")

    def __init__(
        self, name: str, height: float,
        age: int, trunk_diameter: float,
        growth_rate: float = 2.1
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter: float = trunk_diameter
        self._stats: Tree.Stats = Tree.Stats()

    def produce_shade(self) -> None:
        """Display shade production message"""
        print(
            f"Tree {self._name.capitalize()} now produces a shade of "
            f"{self._height}cm long and {self._trunk_diameter}cm wide."
        )
        self._stats._shade_count += 1

    def show(self) -> None:
        """Display tree information"""
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    """A vegetable with harvest season and nutritional value"""

    def __init__(
        self, name: str, height: float,
        age: int, harvest_season: str,
        growth_rate: float = 2.1
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = 0

    def grow(self) -> None:
        """Grow the vegetable and increase nutritional value"""
        super().grow()
        self._nutritional_value += 1

    def show(self) -> None:
        """Display vegetable information"""
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


class Seed(Flower):
    """A seed that inherits from Flower and tracks seed count"""

    def __init__(
        self, name: str, height: float, age: int,
        color: str, max_seeds: int, growth_rate: float = 2.1
    ) -> None:
        super().__init__(name, height, age, color, growth_rate)
        self._max_seeds: int = max_seeds
        self._seeds: int = 0

    def bloom(self) -> None:
        """Bloom the seed and set seed count"""
        super().bloom()
        self._seeds = self._max_seeds

    def show(self) -> None:
        """Display seed information"""
        super().show()
        print(f" Seeds: {self._seeds}")


def display_stats(plant: Plant) -> None:
    """Display statistics for any kind of plant"""
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        f"Is 30 days more than a year?"
        f" -> {Plant.is_older_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year?"
        f" -> {Plant.is_older_than_year(400)}"
    )

    print()
    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red", 8.0)
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)

    print()
    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)

    print()
    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow", 42, 30.0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.grow_older(20)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)

    print()
    print("=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    print("[statistics for Unknown plant]")
    display_stats(anon)
