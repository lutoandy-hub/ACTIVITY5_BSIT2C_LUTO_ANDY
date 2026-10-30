# Sample Runs

Output of `python main.py` with the inputs shown (answers are echoed after each prompt).

## ArrayStack: overflow and underflow

```text

===== Stacks and Queues =====
1. ArrayStack   2. LinkedStack   3. ArrayQueue   4. LinkedQueue
5. Balanced parentheses checker   6. Print queue simulation   0. Exit
Choose: 1
Capacity: 2

--- ArrayStack ---
1. push   2. pop   3. peek   4. is_empty   5. is_full   0. Back
Choose: 1
Value: A
push OK
State: [A] <- top

--- ArrayStack ---
1. push   2. pop   3. peek   4. is_empty   5. is_full   0. Back
Choose: 1
Value: B
push OK
State: [A, B] <- top

--- ArrayStack ---
1. push   2. pop   3. peek   4. is_empty   5. is_full   0. Back
Choose: 1
Value: C
Error: Stack overflow: cannot push, the stack is full
State: [A, B] <- top

--- ArrayStack ---
1. push   2. pop   3. peek   4. is_empty   5. is_full   0. Back
Choose: 2
pop returned: B
State: [A] <- top

--- ArrayStack ---
1. push   2. pop   3. peek   4. is_empty   5. is_full   0. Back
Choose: 2
pop returned: A
State: [] (empty)

--- ArrayStack ---
1. push   2. pop   3. peek   4. is_empty   5. is_full   0. Back
Choose: 2
Error: Stack underflow: cannot pop from an empty stack
State: [] (empty)

--- ArrayStack ---
1. push   2. pop   3. peek   4. is_empty   5. is_full   0. Back
Choose: 0

===== Stacks and Queues =====
1. ArrayStack   2. LinkedStack   3. ArrayQueue   4. LinkedQueue
5. Balanced parentheses checker   6. Print queue simulation   0. Exit
Choose: 0
Goodbye!
```

## LinkedStack: push, peek, underflow

```text

===== Stacks and Queues =====
1. ArrayStack   2. LinkedStack   3. ArrayQueue   4. LinkedQueue
5. Balanced parentheses checker   6. Print queue simulation   0. Exit
Choose: 2

--- LinkedStack ---
1. push   2. pop   3. peek   4. is_empty   5. is_full   0. Back
Choose: 1
Value: X
push OK
State: top -> X

--- LinkedStack ---
1. push   2. pop   3. peek   4. is_empty   5. is_full   0. Back
Choose: 1
Value: Y
push OK
State: top -> Y -> X

--- LinkedStack ---
1. push   2. pop   3. peek   4. is_empty   5. is_full   0. Back
Choose: 3
peek returned: Y
State: top -> Y -> X

--- LinkedStack ---
1. push   2. pop   3. peek   4. is_empty   5. is_full   0. Back
Choose: 2
pop returned: Y
State: top -> X

--- LinkedStack ---
1. push   2. pop   3. peek   4. is_empty   5. is_full   0. Back
Choose: 2
pop returned: X
State: [] (empty)

--- LinkedStack ---
1. push   2. pop   3. peek   4. is_empty   5. is_full   0. Back
Choose: 2
Error: Stack underflow: cannot pop from an empty stack
State: [] (empty)

--- LinkedStack ---
1. push   2. pop   3. peek   4. is_empty   5. is_full   0. Back
Choose: 0

===== Stacks and Queues =====
1. ArrayStack   2. LinkedStack   3. ArrayQueue   4. LinkedQueue
5. Balanced parentheses checker   6. Print queue simulation   0. Exit
Choose: 0
Goodbye!
```

## ArrayQueue: wrap-around, overflow and underflow

```text

===== Stacks and Queues =====
1. ArrayStack   2. LinkedStack   3. ArrayQueue   4. LinkedQueue
5. Balanced parentheses checker   6. Print queue simulation   0. Exit
Choose: 3
Capacity: 3

--- ArrayQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 1
Value: A
enqueue OK
State: front -> [A] <- rear
  array: [A, _, _]  front index=0, size=1

--- ArrayQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 1
Value: B
enqueue OK
State: front -> [A, B] <- rear
  array: [A, B, _]  front index=0, size=2

--- ArrayQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 1
Value: C
enqueue OK
State: front -> [A, B, C] <- rear
  array: [A, B, C]  front index=0, size=3

--- ArrayQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 1
Value: D
Error: Queue overflow: cannot enqueue, the queue is full
State: front -> [A, B, C] <- rear
  array: [A, B, C]  front index=0, size=3

--- ArrayQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 2
dequeue returned: A
State: front -> [B, C] <- rear
  array: [_, B, C]  front index=1, size=2

--- ArrayQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 2
dequeue returned: B
State: front -> [C] <- rear
  array: [_, _, C]  front index=2, size=1

--- ArrayQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 1
Value: D
enqueue OK
State: front -> [C, D] <- rear
  array: [D, _, C]  front index=2, size=2

--- ArrayQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 1
Value: E
enqueue OK
State: front -> [C, D, E] <- rear
  array: [D, E, C]  front index=2, size=3

--- ArrayQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 2
dequeue returned: C
State: front -> [D, E] <- rear
  array: [D, E, _]  front index=0, size=2

--- ArrayQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 2
dequeue returned: D
State: front -> [E] <- rear
  array: [_, E, _]  front index=1, size=1

--- ArrayQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 2
dequeue returned: E
State: front -> [] <- rear
  array: [_, _, _]  front index=2, size=0

--- ArrayQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 2
Error: Queue underflow: cannot dequeue from an empty queue
State: front -> [] <- rear
  array: [_, _, _]  front index=2, size=0

--- ArrayQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 0

===== Stacks and Queues =====
1. ArrayStack   2. LinkedStack   3. ArrayQueue   4. LinkedQueue
5. Balanced parentheses checker   6. Print queue simulation   0. Exit
Choose: 0
Goodbye!
```

## LinkedQueue: enqueue, dequeue, underflow

```text

===== Stacks and Queues =====
1. ArrayStack   2. LinkedStack   3. ArrayQueue   4. LinkedQueue
5. Balanced parentheses checker   6. Print queue simulation   0. Exit
Choose: 4

--- LinkedQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 1
Value: A
enqueue OK
State: front -> A <- rear

--- LinkedQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 1
Value: B
enqueue OK
State: front -> A -> B <- rear

--- LinkedQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 2
dequeue returned: A
State: front -> B <- rear

--- LinkedQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 2
dequeue returned: B
State: [] (empty)

--- LinkedQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 2
Error: Queue underflow: cannot dequeue from an empty queue
State: [] (empty)

--- LinkedQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 1
Value: C
enqueue OK
State: front -> C <- rear

--- LinkedQueue ---
1. enqueue   2. dequeue   3. peek_front   4. is_empty   5. is_full   0. Back
Choose: 0

===== Stacks and Queues =====
1. ArrayStack   2. LinkedStack   3. ArrayQueue   4. LinkedQueue
5. Balanced parentheses checker   6. Print queue simulation   0. Exit
Choose: 0
Goodbye!
```

## Balanced parentheses

```text

===== Stacks and Queues =====
1. ArrayStack   2. LinkedStack   3. ArrayQueue   4. LinkedQueue
5. Balanced parentheses checker   6. Print queue simulation   0. Exit
Choose: 5
Enter a string of brackets: {[()]}
Balanced

===== Stacks and Queues =====
1. ArrayStack   2. LinkedStack   3. ArrayQueue   4. LinkedQueue
5. Balanced parentheses checker   6. Print queue simulation   0. Exit
Choose: 5
Enter a string of brackets: ([)]
NOT balanced

===== Stacks and Queues =====
1. ArrayStack   2. LinkedStack   3. ArrayQueue   4. LinkedQueue
5. Balanced parentheses checker   6. Print queue simulation   0. Exit
Choose: 5
Enter a string of brackets: ((
NOT balanced

===== Stacks and Queues =====
1. ArrayStack   2. LinkedStack   3. ArrayQueue   4. LinkedQueue
5. Balanced parentheses checker   6. Print queue simulation   0. Exit
Choose: 0
Goodbye!
```

## Print queue simulation

```text

===== Stacks and Queues =====
1. ArrayStack   2. LinkedStack   3. ArrayQueue   4. LinkedQueue
5. Balanced parentheses checker   6. Print queue simulation   0. Exit
Choose: 6
Number of jobs: 3
Job 1 ID: DOC-1
Pages: 5
Job 2 ID: DOC-2
Pages: 12
Job 3 ID: DOC-3
Pages: 2
Enqueued job DOC-1 (5 pages)
Enqueued job DOC-2 (12 pages)
Enqueued job DOC-3 (2 pages)

Printing in FIFO order:
  #1: Job DOC-1 - 5 pages (waited behind 0 job(s), 0 page(s))
  #2: Job DOC-2 - 12 pages (waited behind 1 job(s), 5 page(s))
  #3: Job DOC-3 - 2 pages (waited behind 2 job(s), 17 page(s))

All jobs printed. Total pages: 19

===== Stacks and Queues =====
1. ArrayStack   2. LinkedStack   3. ArrayQueue   4. LinkedQueue
5. Balanced parentheses checker   6. Print queue simulation   0. Exit
Choose: 0
Goodbye!
```
