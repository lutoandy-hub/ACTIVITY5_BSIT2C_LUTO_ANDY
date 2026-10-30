# Analysis

The linked-list stack pushes and pops at the head because the head is the only end we can reach and update in O(1). Removing from the tail of a singly linked list would force us to walk the whole list to find the second-to-last node, making `pop` O(n). Working at the head keeps `push`, `pop`, and `peek` all O(1) and needs only one reference (`top`).

The array queue must be circular because a plain array wastes the slots freed at the front after each dequeue, or else we must shift every element left (O(n) dequeue). Using the modulo operator lets `front` and the rear position wrap to index 0, so freed slots are reused and both `enqueue` and `dequeue` stay O(1). A separate `size` counter distinguishes a full queue from an empty one.
