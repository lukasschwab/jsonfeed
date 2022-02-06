"""
Check package structure to avoid breaking changes.
"""
import unittest


class TestImport(unittest.TestCase):
    def test_jsonfeed(self):
        import jsonfeed as _  # noqa: F401
        from jsonfeed import Feed, Author, Hub, Item, Attachment  # noqa: F401
        # TODO: test interfaces.

    def test_converters_from_jsonfeed(self):
        from jsonfeed import converters  # noqa: F401
        import jsonfeed.converters  # noqa: F401
        # TODO: test interfaces.
