import unittest

from jsonfeed import Item, Hub


class TestFeed(unittest.TestCase):
    def test_tags_memory_leak(self):
        """Regression test for a bug found in the Item class."""
        item = Item(id=1)
        item.tags.append("test")

        feed2 = Item("test2")
        self.assertEqual(feed2.tags, [])

    def test_attachments_memory_leak(self):
        """Regression test for a bug found in the Item class."""
        item = Item(id=1)
        item.attachments.append("test")

        feed2 = Item("test2")
        self.assertEqual(feed2.attachments, [])