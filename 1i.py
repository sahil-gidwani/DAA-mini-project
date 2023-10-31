# Iterative (Non-Recursive) Approach to Calculate Fibonacci Numbers

def fibonacci_iterative(n):
    # Initialize an array to store Fibonacci numbers
    fib = [0, 1]

    # Calculate and store Fibonacci numbers up to n
    for i in range(2, n + 1):
        next_fib = fib[i - 1] + fib[i - 2]
        fib.append(next_fib)

    # Return the Fibonacci number for n
    return fib[n]

n = 10  # Change this to the desired Fibonacci number

# Calculate Fibonacci number using the iterative method
result = fibonacci_iterative(n)
print(f"Fibonacci({n}) using iterative method: {result}")

# Time Complexity Analysis:
# Time Complexity: O(n)
# The non-recursive approach calculates Fibonacci numbers in a loop that iterates n times.

# Space Complexity Analysis:
# Space Complexity: O(n)
# It stores all Fibonacci numbers up to n in a list, resulting in a linear space complexity.

"""
Recursion:

Method: Recursion is a programming technique where a function calls itself in order to solve a problem. It breaks a problem into smaller, similar subproblems.
Control Flow: It uses a function call stack to keep track of multiple recursive function calls. Each call is added to the stack, and the program returns from each call when a base case is met.
Termination: It requires a base case or a set of base cases to stop the recursive calls. Without a base case, recursion can result in an infinite loop.
Memory Usage: Recursive functions use memory to store intermediate results and function call information, which can lead to stack overflow errors if the recursion depth is too deep.
Readability: Recursive code can sometimes be more elegant and easier to understand, especially for problems that have a recursive structure.

Iteration:

Method: Iteration is a programming technique where a set of instructions is repeated in a loop. It involves explicit control structures like "for" and "while" loops.
Control Flow: It uses loops to repeat a block of code until a specific condition is met. There is no function call stack, and the flow of control is more explicit.
Termination: It relies on loop conditions or explicit exit conditions to stop execution. There is no need for a base case like in recursion.
Memory Usage: Iteration usually consumes less memory than recursion because there's no need to store function call information. It is less likely to lead to stack overflow errors.
Readability: Iterative code can be more verbose, especially for problems that have a repetitive structure. It may require more lines of code compared to recursive solutions.

Use Cases:

Recursion is often used when the problem can be naturally divided into smaller, similar subproblems (e.g., recursive algorithms for tree traversal or dynamic programming problems).

Iteration is commonly used when you need to perform a specific action repeatedly for a fixed number of times or as long as a certain condition is met (e.g., looping through an array or implementing iterative algorithms like sorting or searching).
"""
