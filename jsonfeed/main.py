import json

class ParseError(Exception):
    pass

class MissingRequiredValueError(ParseError):
    def __init__(self, structure, key):
        self.structure = structure
        self.key = key

def parse(maybeFeedString):
    maybeFeed = json.loads(maybeFeedString)
    return Feed.parse(maybeFeed)

class Feed:
    version = "https://jsonfeed.org/version/1.1"
    def __init__(
        self,
        title,
        home_page_url=None,
        feed_url=None,
        description=None,
        user_comment=None,
        next_url=None,
        icon=None,
        favicon=None,
        author=None, # 1.1 deprecated; use authors.
        authors=None,
        expired=False,
        language=None,
        hubs=[],
        items=[]
    ):
        assert title
        self.title = title
        self.home_page_url = home_page_url
        self.feed_url = feed_url
        self.description = description
        self.user_comment = user_comment
        self.next_url = next_url
        self.icon = icon
        self.favicon = favicon
        self.author = author
        self.authors = authors
        self.expired = expired
        self.language = language
        self.hubs = hubs
        self.items = items

    @staticmethod
    def parse(maybeFeed):
        if 'title' not in maybeFeed or not maybeFeed['title']:
            raise MissingRequiredValueError("Feed", "title")
        # The only required field exists.
        parsed = Feed(maybeFeed['title'])
        # Basic string fields.
        parsed.home_page_url = maybeFeed.get('home_page_url')
        parsed.feed_url = maybeFeed.get('feed_url')
        parsed.description = maybeFeed.get('description')
        parsed.user_comment = maybeFeed.get('user_comment')
        parsed.next_url = maybeFeed.get('next_url')
        parsed.icon = maybeFeed.get('icon')
        parsed.favicon = maybeFeed.get('favicon')
        parsed.expired = maybeFeed.get('expired', False)
        parsed.language = maybeFeed.get('language')
        # Structures requiring additional parsing.
        if 'author' in maybeFeed:
            parsed.author = Author.parse(maybeFeed['author'])
        if 'authors' in maybeFeed:
            parsed.authors = [Author.parse(a) for a in maybeFeed['authors']]
        if 'hubs' in maybeFeed:
            parsed.hubs = [Hub.parse(h) for h in maybeFeed['hubs']]
        if 'items' in maybeFeed:
            parsed.items = [Item.parse(i) for i in maybeFeed['items']]
        return parsed

    def toJSON(self, **kwargs):
        return json.dumps(self._toOrderedDict(), **kwargs)

    def _toOrderedDict(self):
        ordered = {
            'version': self.version,
            'title': self.title,
            'expired': self.expired
        }
        if self.home_page_url: ordered['home_page_url'] = self.home_page_url
        if self.feed_url: ordered['feed_url'] = self.feed_url
        if self.description: ordered['description'] = self.description
        if self.user_comment: ordered['user_comment'] = self.user_comment
        if self.next_url: ordered['next_url'] = self.next_url
        if self.icon: ordered['icon'] = self.icon
        if self.favicon: ordered['favicon'] = self.favicon
        if self.author: ordered['author'] = self.author._toOrderedDict()
        if self.authors:
            ordered['authors'] = [a._toOrderedDict() for a in self.authors]
        if self.hubs:
            ordered['hubs'] = [h._toOrderedDict() for h in self.hubs]
        if self.items:
            ordered['items'] = [i._toOrderedDict() for i in self.items]
        return ordered

class Author:
    def __init__(self, name=None, url=None, avatar=None):
        self.name = name
        self.url = url
        self.avatar = avatar

    @staticmethod
    def parse(maybeAuthor):
        return Author(
            name=maybeAuthor.get('name'),
            url=maybeAuthor.get('url'),
            avatar=maybeAuthor.get('avatar')
        )

    def _toOrderedDict(self):
        ordered = {}
        if self.name: ordered['name'] = self.name
        if self.url: ordered['url'] = self.url
        if self.avatar: ordered['avatar'] = self.avatar
        return ordered

class Hub:
    def __init__(self, type, url):
        self.type = type
        self.url = url

    @staticmethod
    def parse(maybeHub):
        if 'type' not in maybeHub or not maybeHub['type']:
            raise MissingRequiredValueError("Hub", "type")
        if 'url' not in maybeHub or not maybeHub['url']:
            raise MissingRequiredValueError("Hub", "url")
        return Hub(maybeHub['type'], maybeHub['url'])

    def _toOrderedDict(self):
        return { 'type': self.type, 'url': self.url }

# TODO: validate that dates are in RFC 3339 format OR a datetime that can be
# represented in RFC 3339.

class Item:
    def __init__(
        self,
        id,
        url=None,
        external_url=None,
        title=None,
        content_html=None,
        content_text=None,
        summary=None,
        image=None,
        banner_image=None,
        date_published=None,
        date_modified=None,
        author=None,
        authors=None,
        tags=[],
        attachments=[]
    ):
        self.id = id
        self.url = url
        self.external_url = external_url
        self.title = title
        self.content_html = content_html
        self.content_text = content_text
        self.summary = summary
        self.image = image
        self.banner_image = banner_image
        self.date_published = date_published
        self.date_modified = date_modified
        self.author = author
        self.authors = authors
        self.tags = tags
        self.attachments = attachments

    @staticmethod
    def parse(maybeItem):
        if 'id' not in maybeItem or not maybeItem['id']:
            raise MissingRequiredValueError("Item", "id")
        parsed = Item(maybeItem['id'])
        parsed.url = maybeItem.get('url')
        parsed.external_url = maybeItem.get('external_url')
        parsed.title = maybeItem.get('title')
        parsed.content_html = maybeItem.get('content_html')
        parsed.content_text = maybeItem.get('content_text')
        parsed.summary = maybeItem.get('summary')
        parsed.image = maybeItem.get('image')
        parsed.banner_image = maybeItem.get('banner_image')
        parsed.date_published = maybeItem.get('date_published')
        parsed.date_modified = maybeItem.get('date_modified')
        parsed.tags = maybeItem.get('tags', [])
        if 'authors' in maybeFeed:
            parsed.authors = [Author.parse(a) for a in maybeFeed['authors']]
        if 'author' in maybeItem and maybeItem['author']:
            parsed.author = Author.parse(maybeItem['author'])
        if 'attachments' in maybeItem and maybeItem['attachments']:
            parsed.attachments = [Attachment.parse(a) for a in maybeItem['attachments']]
        return parsed

    def _toOrderedDict(self):
        ordered = { 'id': self.id }
        if self.url: ordered['url'] = self.url
        if self.external_url: ordered['external_url'] = self.url
        if self.title: ordered['title'] = self.title
        if self.content_html: ordered['content_html'] = self.content_html
        if self.content_text: ordered['content_text'] = self.content_text
        if self.summary: ordered['summary'] = self.summary
        if self.image: ordered['image'] = self.image
        if self.banner_image: ordered['banner_image'] = self.banner_image
        if self.date_published: ordered['date_published'] = self.date_published
        if self.date_modified: ordered['date_modified'] = self.date_modified
        if self.tags: ordered['tags'] = self.tags
        if self.author: ordered['author'] = self.author._toOrderedDict()
        if self.authors:
            ordered['authors'] = [a._toOrderedDict() for a in self.authors]
        if self.attachments:
            ordered['attachments'] = [a._toOrderedDict() for a in self.attachments]
        return ordered

class Attachment:
    def __init__(
        self,
        url,
        mime_type,
        title=None,
        size_in_bytes=None,
        duration_in_seconds=None
    ):
        self.url = url
        self.mime_type = mime_type
        self.title = title
        self.size_in_bytes = size_in_bytes
        self.duration_in_seconds = duration_in_seconds

    @staticmethod
    def parse(maybeAttachment):
        if 'url' not in maybeAttachment or not maybeAttachment['url']:
            raise MissingRequiredValueError("Attachment", "url")
        if 'mime_type' not in maybeAttachment or not maybeAttachment['mime_type']:
            raise MissingRequiredValueError("Attachment", "mime_type")
        parsed = Attachment(maybeAttachment['url'], maybeAttachment['mime_type'])
        parsed.title = maybeAttachment.get('title')
        parsed.size_in_bytes = maybeAttachment.get('size_in_bytes'),
        parsed.duration_in_seconds = maybeAttachment.get('duration_in_seconds')
        return parsed

    def _toOrderedDict(self):
        ordered = { 'url': self.url, 'mime_type': self.mime_type }
        if self.title: ordered['title'] = self.title
        if self.size_in_bytes: ordered['size_in_bytes'] = self.size_in_bytes
        if self.duration_in_seconds:
            ordered['duration_in_seconds'] = self.duration_in_seconds
        return ordered
