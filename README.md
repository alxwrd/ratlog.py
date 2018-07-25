<p align="center"><img src="https://raw.githubusercontent.com/ratlog/ratlog-spec/master/rat.png" width="15%"></p>

# :rat: Ratlog.py

_Application Logging for Rats, Humans and Machines_

[![Build Status](https://travis-ci.org/alxwrd/ratlog.py.svg?branch=master)](https://travis-ci.org/alxwrd/ratlog.py)

```python
>>> import ratlog

>>> log = ratlog.Log()

>>> log("hello world")
hello world

# Add fields
>>> log("counting", {"count": 1})
counting | count: 1

# Add fields and tag
>>> log("counting", {"count": -1}, "negative")
[negative] counting | count: -1

# Create another logger bound to a tag
>>> warn = ratlog.Log("warning")
>>> warn("disk space low")
[warning] disk space low

# Adding more tags
>>> crit = ratlog.Log("warning", "critical")
>>> crit("shutting down all servers")
[warning|critical] shutting down all servers
```
