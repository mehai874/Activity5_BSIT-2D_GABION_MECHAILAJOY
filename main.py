from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue
from applications import is_balanced, print_queue_simulation


def choose_structure():
    print("\n=== STACKS AND QUEUES ===")
    print("1. Array Stack")
    print("2. Linked List Stack")
    print("3. Circular Array Queue")
    print("4. Linked List Queue")
    print("5. Parentheses Balance Checker")
    print("6. Print Queue Simulation")
    print("0. Exit")
    return input("Choose an option: ").strip()


def run_structure(choice):
    if choice == "1":
        structure, kind = ArrayStack(3), "stack"
    elif choice == "2":
        structure, kind = LinkedStack(), "stack"
    elif choice == "3":
        structure, kind = ArrayQueue(3), "queue"
    elif choice == "4":
        structure, kind = LinkedQueue(), "queue"
    else:
        print("Invalid choice.")
        return

    while True:
        print("\nOperations:")
        if kind == "stack":
            print("1. Push  2. Pop  3. Peek")
        else:
            print("1. Enqueue  2. Dequeue  3. Peek front")
        print("4. Check empty  5. Check full  6. Display  0. Back")
        operation = input("Choose an operation: ").strip()

        try:
            if operation == "1":
                value = input("Enter a value: ")
                if kind == "stack":
                    structure.push(value)
                else:
                    structure.enqueue(value)
                print("Value added.")
            elif operation == "2":
                print("Removed:", structure.pop() if kind == "stack" else structure.dequeue())
            elif operation == "3":
                print("Value:", structure.peek() if kind == "stack" else structure.peek_front())
            elif operation == "4":
                print("Empty:", structure.is_empty())
            elif operation == "5":
                print("Full:", structure.is_full())
            elif operation == "6":
                structure.display()
            elif operation == "0":
                break
            else:
                print("Invalid operation. Please try again.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)

        structure.display()


def main():
    while True:
        choice = choose_structure()
        if choice == "0":
            print("Program ended.")
            break
        elif choice in {"1", "2", "3", "4"}:
            run_structure(choice)
        elif choice == "5":
            expression = input("Enter an expression with (), [], or {}: ")
            print("Balanced." if is_balanced(expression) else "Not balanced.")
        elif choice == "6":
            print_queue_simulation()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
