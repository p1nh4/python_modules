#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)
    return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    print("\nInput data is '25'")
    try:
        print(f"Temperature is now {input_temperature('25')}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nInput data is 'abc'")
    try:
        print(f"Temperature is now {input_temperature('abc')}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
