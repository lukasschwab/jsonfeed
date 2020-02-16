# jsonfeed [![Python 3.6](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

`jsonfeed` is a Python package for parsing and constructing [JSON Feeds](https://jsonfeed.org/version/1). It explicitly supports JSON Feed Version 1.

## Usage

This package's constructor arguments and class variables exactly match the field names defined in the JSON schema spec. I hope that the code is clear enough that the spec can be its granular documentation.

### Parsing a JSON feed

```python
import jsonfeed as jf
import requests

# Requesting a valid JSON schema!
r = requests.get('https://arxiv-feeds.appspot.com/json/test')
# Parse from raw text...
feed_from_text = jf.parse(r.text)
# ...or parse JSON separately.
r_json = r.json()
feed_from_json = jf.Feed.parse(r_json)
```

### Constructing a JSON feed

```python
import jsonfeed as jf

me = jf.Author(
  name="Lukas Schwab",
  url="https://github.com/lukasschwab"
)
feed = jf.Feed("My Feed Title", author=me)
item = jf.Item("some_item_id")
feed.items.append(item)

print(feed.toJSON())
```

Note, `jsonfeed` is designed to be minimally restrictive. It does not require fields that are not required in the JSON Feed spec. This means it's possible to construct nonmeaningful JSON feeds (e.g. with this valid `Author` object: `{}`).

## Notes

+ There are known areas for improvement. Please feel empowered to open a PR!
  - [ ] Date format validation *or* construction from `datetime` objects.
  - [ ] Type annotations.
  - [ ] Unit tests.
  - [ ] Distribution on `PyPI`.

+ Dictionaries maintain insertion order as of Python 3.6. `jsonfeed` takes advantage of this to retain the order suggested in the JSON Feed spec (namely, that `version` appear at the top of the JSON object). This order may not be enforced in earlier versions of Python, but out-of-order JSON Feeds are not invalid.

+ I made a conscious decision to shoot for code that's readable––vis à vis the JSON Feed spec––rather than code that's minimal or performant. Additionally, I opted to avoid dependencies outside of the standard library. Hopefully this makes for easy maintenance.