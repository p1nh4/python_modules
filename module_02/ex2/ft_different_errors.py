#!/usr/bin/env python3


"""
raise serve para modificar a saida, quando envolve regras de negocio
(erros que o ptyhon3 nao conhece), em outros casos python3 devolve
erro de fabrica
"""


def garden_operations(operation_number: int) -> None:

    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "string" + 5
    else:
        4


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    print("Testing operation 0...")
    try:
        garden_operations(0)
        print("Operation completed successfully!")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("Testing operation 1...")
    try:
        garden_operations(1)
        print("Operation completed successfully!")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("Testing operation 2...")
    try:
        garden_operations(2)
        print("Operation completed successfully!")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("Testing operation 3...")
    try:
        garden_operations(3)
        print("Operation completed successfully!")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("Testing operation 4...")
    try:
        garden_operations(4)
        print("Operation completed successfully!")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("\nAll error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
