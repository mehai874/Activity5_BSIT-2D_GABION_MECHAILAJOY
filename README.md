# Stacks and Queues: Array vs. Linked List

## Description
This Python project demonstrates stacks and queues implemented using arrays and linked lists. It also includes a parentheses balance checker and a print queue simulation.

- A stack follows LIFO (Last In, First Out).
- A queue follows FIFO (First In, First Out).

## Files
- `node.py` — node class used by linked structures.
- `array_stack.py` — fixed-capacity array stack.
- `linked_stack.py` — linked-list stack.
- `array_queue.py` — circular array queue.
- `linked_queue.py` — linked-list queue with front and rear references.
- `applications.py` — parentheses balance checker and print queue simulation.
- `main.py` — menu-driven program for testing the structures and applications.
- `analysis.md` — answer to the analysis question.
- `sample_runs.txt` — sample output for normal operations and error handling.

## Requirements
Python 3. No additional packages are required.

## How to Run
Open a terminal in this folder and run:

`python main.py`

If your system uses the `python3` command, run:

`python3 main.py`

Use the menu to select an implementation or application and follow the prompts.

To run the two application demonstrations directly, use:

`python applications.py`

## Stack Operations
- `push(value)` — add a value to the top.
- `pop()` — remove and return the top value.
- `peek()` — view the top value without removing it.
- `is_empty()` — check whether the stack is empty.
- `is_full()` — check whether the fixed-size array stack is full.

## Queue Operations
- `enqueue(value)` — add a value at the rear.
- `dequeue()` — remove and return the front value.
- `peek_front()` — view the front value without removing it.
- `is_empty()` — check whether the queue is empty.
- `is_full()` — check whether the fixed-size array queue is full.

## Error Handling
The array implementations raise `OverflowError` if an insertion is attempted while full. Stack and queue removal or peek operations raise `IndexError` when the structure is empty. The menu catches these errors and displays a message.

## Applications
1. The parentheses balance checker checks matching pairs of `()`, `[]`, and `{}` using a stack.
2. The print queue simulation demonstrates jobs being processed in first-in, first-out order.

## Sample Runs
See `sample_runs.txt` for examples of normal behavior, underflow, and overflow.
