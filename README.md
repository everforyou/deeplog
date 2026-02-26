# deeplog

Tagged terminal logging with timestamps and elapsed time. Use tags to group and count log lines and see time between calls.

## Install

From this directory (editable install for development):

```bash
pip install -e .
```

From a built wheel or from Git later:

```bash
pip install deeplog
```

## Use

```python
from deeplog import terminal_print, reset

# Simple print (no tag)
terminal_print("Hello")

# With a tag: shows tag tree, count, timestamp, and time since last call with same tag
terminal_print("Step one", tag="MAIN")
terminal_print("Step two", tag="MAIN")
terminal_print("Sub step", tag="SUB")

# Reset counts and timestamps when starting a new section
reset()
terminal_print("New section", tag="MAIN")
```

## API

- **`terminal_print(text, tag='DEFAULT')`** — Print `text` to stdout. If `tag` is not `'DEFAULT'`, prepends a tree-style tag with count, timestamp, and elapsed time since the last call with that tag.
- **`reset()`** — Clear all tag counts and timestamps.

## Requirements

- Python 3.9+
- colorama (installed automatically)
