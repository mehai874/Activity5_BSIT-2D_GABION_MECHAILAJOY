from array_stack import ArrayStack


def is_balanced(expression):
    """Return True if (), [], and {} are correctly balanced."""
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = ArrayStack(max(1, len(expression)))

    for character in expression:
        if character in "([{":
            stack.push(character)
        elif character in ")]}":
            if stack.is_empty():
                return False
            if stack.pop() != pairs[character]:
                return False

    return stack.is_empty()


def print_queue_simulation():
    """Demonstrate a print queue processed in FIFO order."""
    jobs = [
        {"id": "JOB-101", "pages": 3},
        {"id": "JOB-102", "pages": 5},
        {"id": "JOB-103", "pages": 2},
    ]

    print("\nPrint Queue Simulation")
    print("Jobs arrive in this order:")
    for job in jobs:
        print(f"Enqueue {job['id']} ({job['pages']} pages)")

    print("\nProcessing jobs in FIFO order:")
    while jobs:
        job = jobs.pop(0)
        print(f"Printing {job['id']} - {job['pages']} pages")


def parentheses_demo():
    print("\nParentheses Balance Checker")
    examples = ["([]{})", "([)]", "((())", "{a + [b * (c + d)]}"]
    for expression in examples:
        print(f"{expression!r}: {'Balanced' if is_balanced(expression) else 'Not balanced'}")


if __name__ == "__main__":
    parentheses_demo()
    print_queue_simulation()
