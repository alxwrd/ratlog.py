# :rat: Ratlog.py

_Application Logging for Rats, Humans and Machines_

[![Build Status](https://travis-ci.org/alxwrd/ratlog.py.svg?branch=master)](https://travis-ci.org/alxwrd/ratlog.py)

> **Disclaimer:** _The Ratlog specification is still alpha status and might be
subject to breaking changes. Beware, because of that, this API and format
might change significantly. We will try our best to tag a stable release as
soon as possible. [Leave feedback](https://github.com/alxwrd/ratlog.py/issues)
and help us get there faster!_

```python
>>> import ratlog

>>> log = ratlog.Log()

>>> log("hello world")
hello world

# Add fields
>>> log("counting", {"count": 1})
counting | count: 1

# Add fields and tag
>>> log("counting", {"count": 1}, "negative")
[negative] counting | count: -1

# Create another logger bound to a tag
>>> warn = ratlog.Log("warning")
>>> warn("disk space low")
[warning] disk space low

# Adding more tags
>>> crit = ratlog.Log("warning", "critical")
[warning|critical] shutting down all servers
```
