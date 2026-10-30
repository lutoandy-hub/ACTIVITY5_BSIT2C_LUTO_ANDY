"""Application (a): check balanced ()[]{} using a stack."""

from linked_stack import LinkedStack

PAIRS = {")": "(", "]": "[", "}": "{"}


def is_balanced(text):
    stack = LinkedStack()
    for ch in text:
        if ch in "([{":
            stack.push(ch)                       # opening: remember it
        elif ch in PAIRS:
            if stack.is_empty() or stack.pop() != PAIRS[ch]:
                return False                     # closing with no/wrong opener
    return stack.is_empty()                      # leftovers mean unbalanced


if __name__ == "__main__":
    for s in ["()", "([]{})", "(]", "(()", "{[()]}", ")("]:
        print(f"{s!r:10} -> {'balanced' if is_balanced(s) else 'NOT balanced'}")
