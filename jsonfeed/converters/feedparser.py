from jsonfeed import *

# This file provides some bodge utils for converting feedparser-parsed ATOM or
# RSS feeds into JSON feeds. It makes few guarantees about feed quality (for
# example, it makes no effort to convert datetime formats) so it should probably
# not be used in any serious application.
#
# Example usage:
#
#   import jsonfeed.converters as jfc
#   import feedparser
#   obj = feedparser.parse('https://www.schneier.com/blog/atom.xml')
#   feed = jfc.from_feedparser_obj(obj)
#
# Filter example:
#
#    obj = feedparser.parse('https://www.schneier.com/blog/atom.xml')
#    feed = from_feedparser_obj(obj)
#    feed.items = [e for e in feed.items if not e.tags or "squid" not in e.tags]
#    feed.toJSON()

def from_feedparser_obj(feedparser_obj):
    author = Author(
        name=feedparser_obj.feed.author,
    ) if "author" in feedparser_obj.feed else None
    items = [from_feedparser_entry(e) for e in feedparser_obj.entries]
    return Feed(
        title=feedparser_obj.feed.title if "title" in feedparser_obj.feed else None,
        description=feedparser_obj.feed.info if "info" in feedparser_obj.feed else None,
        icon=feedparser_obj.feed.image.link if "image" in feedparser_obj.feed else None,
        favicon=feedparser_obj.feed.icon if "icon" in feedparser_obj.feed else None,
        language=feedparser_obj.feed.language if "language" in feedparser_obj.feed else None,
        author=author,
        authors=[author] if author else None,
        items=items
    )

def from_feedparser_entry(entry):
    author = Author(name=entry.author) if "author" in entry else None
    return Item(
        id=entry.id if "id" in entry else None,
        url=entry.link if "link" in entry else None,
        external_url=entry.source.link if "source" in entry else None,
        title=entry.title if "title" in entry else None,
        content_html=get_content(entry, "text/html"),
        content_text=get_content(entry, "text/plain"),
        summary=entry.summary if "summary" in entry else None,
        date_published=entry.published if "published" in entry else None,
        date_modified=entry.updated if "updated" in entry else None,
        author=author,
        authors=[author] if author else None,
        tags=[t.term for t in entry.tags] if "tags" in entry else None,
        attachments=[from_feedparser_link(l) for l in entry.links] if "links" in entry else None,
    )

def from_feedparser_link(link):
    # TODO: extract the standard fieldnames.
    return Attachment(
        link.href,
        link.type,
        None,
        link.length if "length" in link else None,
        None
    )

# A helper for pulling a content body with a specific format out of a feedparser
# entry's array of contents.
#
# For our purposes, content_type is "text/html" or "text/plain".
def get_content(entry, content_type):
    if "content" not in entry:
        return None
    for content in entry.content:
        if content.type == content_type:
            return content.value
    return None
