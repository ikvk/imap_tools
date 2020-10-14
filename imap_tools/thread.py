from itertools import chain
from collections import deque, OrderedDict

from .message import MailMessage


class ThreadItem:
    """Element of thread tree"""

    def __init__(self,
                 message: MailMessage = None,
                 parent: 'ThreadItem' or None = None,
                 children: ['ThreadItem'] = None):
        self.message = message
        self.parent = parent
        self.children = children or []

    @property
    def is_empty(self) -> bool:
        """Is thread item has some content"""
        return any((self.message, self.parent, self.children))

    def add_child(self, item: 'ThreadItem'):
        """Add a child to children"""
        if item.parent:
            item.parent.remove_child(item)
        self.children.append(item)
        item.parent = self

    def remove_child(self, item: 'ThreadItem'):
        """Remove a child from children"""
        self.children.remove(item)
        item.parent = None

    def has_descendant(self, item: 'ThreadItem') -> bool:
        """
        Check if item is a descendant of this item
        True if item is a descendant of self
        """
        for_see = deque([self])
        seen = set()  # avoid infinite recursion
        while for_see:
            node = for_see.pop()
            if node is item:
                return True
            seen.add(node)
            for child in node.children:
                if child not in seen:
                    for_see.append(child)
        return False

    @property
    def child_count(self) -> int:
        """Recursively count the number of children items"""
        return sum([child.child_count for child in self.children])

    @property
    def depth(self) -> int:
        """Depth of item in the tree hierarchy"""
        if self.parent is None:
            return 0
        else:
            return 1 + self.parent.depth

    @property
    def root(self) -> 'ThreadItem':
        """Most top level thread item"""
        if self.parent is None:
            return self
        else:
            return self.parent.root

    def flatten(self) -> ['ThreadItem']:
        """Flatten version of item tree branch"""
        in_list = [[self]] + [child.flatten() for child in self.children]
        return list(chain.from_iterable(in_list))

    def draw_tree(self) -> str:
        """Pseudo graphical representation of a branch"""
        # todo
        return """
            -- 1
               |-- 2
               +-- 3
                   |-- A
                   +-- B
        """


class ThreadBuilder:
    """
    Grouping messages together in parent/child relationships based on which messages are replies to which others.
    """

    def __init__(self, message_set: [MailMessage]):
        self.message_set = message_set
        self._root_items = self._build()

    def root_items(self) -> [ThreadItem]:
        return self.root_items

    def _build(self) -> [ThreadItem]:
        """
        Build hierarchy tree
        :return: [ThreadItem]: root thread items
        """
        # todo
        # step by step
        return []

# Usage example:
# for root_thread_item in ThreadBuilder(message_list).root_items():
#     print(root_thread_item.draw_tree())
