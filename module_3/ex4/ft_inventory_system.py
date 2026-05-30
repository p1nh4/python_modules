#!/usr/bin/env python3
import sys


def main() -> None:
    """Process inventory from command-line and display analytics"""
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for i in range(1, len(sys.argv)):
        item_arg: str = sys.argv[i]
        if ':' not in item_arg:
            print(f"Error - invalid parameter '{item_arg}'")
            continue
        parts: list[str] = item_arg.split(':', 1)
        key: str = parts[0]
        val: str = parts[1]
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            inventory[key] = int(val)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
    total: int = sum(inventory.values())
    items: list[str] = list(inventory.keys())
    print(f"Got inventory: {inventory}")
    print(f"Item list: {items}")
    print(f"Total quantity of the {len(items)} items: {total}")

    for key, value in inventory.items():
        pct: float = round(value / total * 100, 1)
        print(f"Item {key} represents {pct}%")
    most: str = max(inventory, key=lambda k: inventory[k])
    least: str = min(inventory, key=lambda k: inventory[k])
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
