import unittest

import jsonfeed as jf


class TestItem(unittest.TestCase):
    def test_tags_reuse(self):
        """Regression test for a bug found in the Item class."""
        item = jf.Item(id=1)
        item.tags.append("test")

        feed2 = jf.Item("test2")
        self.assertEqual(feed2.tags, [])

    def test_attachments_reuse(self):
        """Regression test for a bug found in the Item class."""
        item = jf.Item(id=1)
        item.attachments.append("test")

        feed2 = jf.Item("test2")
        self.assertEqual(feed2.attachments, [])
