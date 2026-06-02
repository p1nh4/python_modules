#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    """Ask user for 3D coordinates, retry until valid"""
    while True:
        coord_str: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parts: list[str] = coord_str.split(',')
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x: float = float(parts[0])
            y: float = float(parts[1])
            z: float = float(parts[2])
            return (x, y, z)
        except ValueError:
            for part in parts:
                try:
                    float(part.strip())
                except ValueError as ve:
                    print(f"Error on parameter '{part.strip()}': {ve}")
                    break


def calc_distance(
    p1: tuple[float, float, float],
    p2: tuple[float, float, float]
) -> float:
    """Calculate Euclidean distance between two 3D points"""
    return round(math.sqrt(
        (p2[0] - p1[0])**2 +
        (p2[1] - p1[1])**2 +
        (p2[2] - p1[2])**2
    ), 4)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()

    center: tuple[float, float, float] = (0.0, 0.0, 0.0)
    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()

    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    print(f"Distance to center: {calc_distance(center, pos1)}")

    print()
    print("Get a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()
    dist: float = calc_distance(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: {dist}")
