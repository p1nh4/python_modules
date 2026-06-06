#!/usr/bin/env python3

def garden_operations(operation_number: str) -> None:
    temp_int: int = int(operation_number)

    if operation_number == 0:
        int("abc")
    elif operation_number == 1
        result = 1 / 0
    elif
    raise ValueError("")

    raise ZeroDivisionError

    raise FileNotFoundError ()

    raise TypeError

    return

def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    print("Testing Operation 0...") 
    try:
        garden_operations('0')
        print(f"Operation completed successfully!")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")
    
    print("Testing Operation 1...") 
    try:
        garden_operations('1')
        print(f"Operation completed successfully!")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")
    
    print("Testing Operation 2...") 
    try:
        garden_operations('2')
        print(f"Operation completed successfully!")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")
    
    print("Testing Operation 3...") 
    try:
        garden_operations('3')
        print(f"Operation completed successfully!")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")
   
   print("Testing Operation 4...") 
    try:
        garden_operations('4')
        print(f"Operation completed successfully!")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")

    print("All error types testes sucessfully!")

def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
     

