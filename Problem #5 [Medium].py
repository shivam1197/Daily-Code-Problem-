"""cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr."""

#This problem was asked by Jane Street.

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    # Pass a function to get the first element from the pair
    def get_first(a, b):
        return a
    return pair(get_first)

def cdr(pair):
    # Pass a function to get the last element from the pair
    def get_last(a, b):
        return b
    return pair(get_last)

# Example usage:
pair = cons(3, 4)
result_car = car(pair)
result_cdr = cdr(pair)

print(result_car)  # Output: 3
print(result_cdr)  # Output: 4
