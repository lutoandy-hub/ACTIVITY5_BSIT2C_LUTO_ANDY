"""Menu-driven test driver for all four data structures and the applications."""

import sys

from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue
from balanced_parentheses import is_balanced
from print_queue import run_print_queue


def ask(prompt):
    """input() that also echoes the answer when input is piped (for sample runs)."""
    value = input(prompt)
    if not sys.stdin.isatty():
        print(value)
    return value.strip()


def ask_int(prompt):
    while True:
        try:
            return int(ask(prompt))
        except ValueError:
            print("Please enter a whole number.")


def run_structure(name, ds, is_stack):
    add, remove, look = ("push", "pop", "peek") if is_stack else ("enqueue", "dequeue", "peek_front")
    while True:
        print(f"\n--- {name} ---")
        print(f"1. {add}   2. {remove}   3. {look}   4. is_empty   5. is_full   0. Back")
        choice = ask("Choose: ")
        try:
            if choice == "1":
                getattr(ds, add)(ask("Value: "))
                print(f"{add} OK")
            elif choice == "2":
                print(f"{remove} returned:", getattr(ds, remove)())
            elif choice == "3":
                print(f"{look} returned:", getattr(ds, look)())
            elif choice == "4":
                print("is_empty:", ds.is_empty())
            elif choice == "5":
                print("is_full:", ds.is_full())
            elif choice == "0":
                return
            else:
                print("Invalid choice.")
                continue
        except (IndexError, OverflowError) as err:
            print("Error:", err)
        print("State:", ds)


def main():
    while True:
        print("\n===== Stacks and Queues =====")
        print("1. ArrayStack   2. LinkedStack   3. ArrayQueue   4. LinkedQueue")
        print("5. Balanced parentheses checker   6. Print queue simulation   0. Exit")
        choice = ask("Choose: ")
        if choice == "1":
            run_structure("ArrayStack", ArrayStack(ask_int("Capacity: ")), True)
        elif choice == "2":
            run_structure("LinkedStack", LinkedStack(), True)
        elif choice == "3":
            run_structure("ArrayQueue", ArrayQueue(ask_int("Capacity: ")), False)
        elif choice == "4":
            run_structure("LinkedQueue", LinkedQueue(), False)
        elif choice == "5":
            text = ask("Enter a string of brackets: ")
            print("Balanced" if is_balanced(text) else "NOT balanced")
        elif choice == "6":
            jobs = []
            for i in range(ask_int("Number of jobs: ")):
                job_id = ask(f"Job {i + 1} ID: ")
                jobs.append((job_id, ask_int("Pages: ")))
            run_print_queue(jobs)
        elif choice == "0":
            print("Goodbye!")
            return
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
