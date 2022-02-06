"""
Check package structure to avoid breaking changes.
"""
import unittest


class TestImport(unittest.TestCase):
    def test_jsonfeed(self):
        import jsonfeed as jf
        self.assertIsNotNone(jf.Feed)  # Smoke test.
        from jsonfeed import Feed, Author, Hub, Item, Attachment  # noqa: F401
        # TODO: test interfaces.

    def test_converters_from_jsonfeed(self):
        from jsonfeed.converters import feedparser
        self.assertIsNotNone(feedparser.get_content)
