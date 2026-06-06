#!/usr/bin/env python3

class GardenError(Exception):
    """Erros base"""
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):

    """Erros plantas"""
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):

    """Erros agua"""
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if (plant_name == plant_name.capitalize()):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plant_name: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_name:
            water_plant(plant)
    except (PlantError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    valid_plants: list = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(valid_plants)

    print("\nTesting invalid plants...")
    invalid_plants: list = ["Tomato", "lettuce", "Carrots"]
    test_watering_system(invalid_plants)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
