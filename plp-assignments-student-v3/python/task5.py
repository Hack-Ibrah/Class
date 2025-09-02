# Task 5: Error Handling
# Example showing try/except and proper error messages

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Error: Division by zero')
        return None
    except TypeError:
        print('Error: Invalid types provided')
        return None

if __name__ == '__main__':
    print('10 / 2 =', safe_divide(10, 2))
    print('10 / 0 =', safe_divide(10, 0))
    print("'10' / 2 =", safe_divide('10', 2))
