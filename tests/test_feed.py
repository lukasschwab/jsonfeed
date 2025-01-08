import unittest

from jsonfeed import Feed, Item, Hub


class TestFeed(unittest.TestCase):
    def test_items_memory_leak(self):
        """Regression test for a bug found in the Feed class."""
        feed = Feed("test")
        feed.items.append(Item(id=1))

        feed2 = Feed("test2")
        self.assertEqual(feed2.items, [])

    def test_hubs_memory_leak(self):
        """Regression test for a bug found in the Feed class."""
        feed = Feed("test")
        feed.hubs.append(Hub("test", "https://example.com"))

        feed2 = Feed("test2")
        self.assertEqual(feed2.items, [])