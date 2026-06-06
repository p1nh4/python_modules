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


def ft_check_plant(status: str):
    if status == "wilting":
        raise PlantError("The tomato plant is wilting!")


def ft_check_water(status: str):
    if status == "tank":
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        ft_check_plant("wilting")
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("\nTesting WaterError...")
    try:
        ft_check_water("tank")
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("\nTesting catching all garden errors...")
    try:
        ft_check_plant("wilting")
    except GardenError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    try:
        ft_check_water("tank")
    except GardenError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("\nAll custom error types work correctly!")


def main() -> None:
    test_custom_errors()


if __name__ == "__main__":
    main()
