# Analysis Question

The linked-list stack pushes at the head because inserting at the head takes O(1) time. Popping from the head also takes O(1) time because the top reference can move to the next node directly. If we push or pop at the tail of a singly linked list, removing the last node could take O(n) time because we need to find the node before the tail. The array queue must be circular so that the empty spaces at the beginning of the array can be reused. It allows the front and rear positions to wrap around to the beginning of the array without shifting all the elements.
