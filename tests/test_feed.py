import unittest

import jsonfeed as jf


class TestFeed(unittest.TestCase):
    def test_items_reuse(self):
        """Regression test for a bug found in the Feed class."""
        feed = jf.Feed("test")
        feed.items.append(jf.Item(id=1))

        feed2 = jf.Feed("test2")
        self.assertEqual(feed2.items, [])

    def test_hubs_reuse(self):
        """Regression test for a bug found in the Feed class."""
        feed = jf.Feed("test")
        feed.hubs.append(jf.Hub("test", "https://example.com"))

        feed2 = jf.Feed("test2")
        self.assertEqual(feed2.items, [])
