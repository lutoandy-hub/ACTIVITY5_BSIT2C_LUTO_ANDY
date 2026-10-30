Stacks and Queues
Name: [Lastname, Firstname M.] Course, Year, and Section: [Course - Year and Section]

About
This program shows how stacks and queues work using arrays and linked lists. It also has a parentheses checker and a small print queue program.

Files
array_stack.py — stack made with a fixed-size list.
linked_stack.py — stack made with linked nodes.
array_queue.py — circular queue made with a fixed-size list.
linked_queue.py — queue with front and rear nodes.
main.py — menu for testing the four data structures.
balanced_parentheses.py — checks matching parentheses, brackets, and braces.
print_queue.py — adds and prints jobs in first-in, first-out order.
analysis.md — answer to the analysis question.
sample_runs.md — sample runs showing overflow, underflow, and wrap-around.
Requirements
Python 3 is required. No extra packages are needed.

Run the programs
Open a terminal in this folder and run:

python main.py
To run the parentheses checker:

python balanced_parentheses.py
To run the print queue:

python print_queue.py

Things to test
Push more items than the capacity into the Array Stack to see overflow (try capacity 3).
Pop from an empty stack to see underflow.
Enqueue more items than the capacity into the Circular Array Queue to see overflow.
Dequeue from an empty queue to see underflow.
For queue wrap-around, use capacity 3: enqueue A, B, C; dequeue A and B; then enqueue D and E. The array will show D and E in the freed slots at the front.
In the parentheses checker, try {[()]} (balanced) and ([)] (not balanced).
