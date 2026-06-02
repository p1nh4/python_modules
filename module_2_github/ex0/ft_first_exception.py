#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    """Convert temperature string to integer"""
    return int(temp_str)


def test_temperature() -> None:
    """Test input_temperature with valid and invalid inputs"""
    print("=== Garden Temperature ===")
    print()

    print("Input data is '25'")
    print(f"Temperature is now {input_temperature('25')}°C")

    print()
    print("Input data is 'abc'")
    try:
        input_temperature('abc')
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
