#!/usr/bin/env python3


class GardenError(Exception):
    """Base exception for garden-related errors"""

    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Error for plant-related issues"""

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Error for watering issues"""

    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant(plant_name: str) -> None:
    """Raise PlantError for wilting plant"""
    raise PlantError(f"The {plant_name} plant is wilting!")


def check_water(tank_level: int) -> None:
    """Raise WaterError if water is insufficient"""
    if tank_level < 10:
        raise WaterError("Not enough water in the tank!")


def test_errors() -> None:
    """Test all custom errors"""
    print("=== Custom Garden Errors Demo ===")

    print()
    print("Testing PlantError...")
    try:
        check_plant("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print()
    print("Testing WaterError...")
    try:
        check_water(0)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print()
    print("Testing catching all garden errors...")
    try:
        check_plant("tomato")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water(0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
