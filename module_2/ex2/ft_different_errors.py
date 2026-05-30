#!/usr/bin/env python3


def garden_operations(operation_number: int) -> None:
    """Run faulty code based on operation number (0-4)"""
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        _ = 10 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        _ = "garden" + 42  # type: ignore


def test_error_types() -> None:
    """Test every error type and print when caught"""
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
