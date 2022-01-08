from typing import Optional


class Node(object):
    def __init__(self, value=None, next_node=None, prev_node=None):
        self.value = value
        if next_node:
            assert isinstance(next_node, Node)
        self.next = next_node  # type: Optional[Node]
        if prev_node:
            assert isinstance(prev_node, Node)
        self.prev = prev_node  # type: Optional[Node]

    def __repr__(self):
        if self.next and self.prev:
            return f"<Node value={self.value} next={self.next.value} prev={self.prev.value}>"
        elif self.next:
            return f"<Node value={self.value} next={self.next.value}>"
        elif self.prev:
            return f"<Node value={self.value} prev={self.prev.value}>"
