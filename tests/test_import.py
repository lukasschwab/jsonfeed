"""
Check package structure to avoid breaking changes.
"""
import unittest


class TestImport(unittest.TestCase):
    def test_jsonfeed(self):
        import jsonfeed as jf  # noqa: F401
        self.assertIsNotNone(jf.Feed)
        from jsonfeed import Feed, Author, Hub, Item, Attachment  # noqa: F401
        # TODO: test interfaces.

    def test_converters_from_jsonfeed(self):
        from jsonfeed import converters as jfc1 # noqa: F401
        import jsonfeed.converters as jfc2 # noqa: F401
        for jfc in [jfc1, jfc2]:
            self.assertIsNotNone(jfc.get_content)
        # TODO: test interfaces.
