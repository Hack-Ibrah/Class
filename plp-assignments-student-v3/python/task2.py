# Task 2: Loops & Conditionals
# Demonstrates for loops and if/else checks
def even_odd(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append((i, "even"))
        else:
            result.append((i, "odd"))
    return result

if __name__ == "__main__":
    for num, kind in even_odd(10):
        print(num, kind)
