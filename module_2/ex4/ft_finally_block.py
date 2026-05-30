#!/usr/bin/env python3


class GardenError(Exception):
    """Base exception for garden-related errors"""

    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Error for plant-related issues"""

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    """Water a plant if its name is capitalized"""
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(title: str, plants: list[str]) -> None:
    """Test the watering system with a list of plants"""

    print(f"Testing {title}...")
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")

    print()
    test_watering_system("valid plants", ["Tomato", "Lettuce", "Carrots"])

    print()
    test_watering_system("invalid plants", ["Tomato", "lettuce", "Carrots"])

    print()
    print("Cleanup always happens, even with errors!")
