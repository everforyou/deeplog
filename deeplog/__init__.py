"""
deeplog - Tagged terminal logging with timestamps and elapsed time.
"""

import io
import sys
import time
from datetime import datetime

from colorama import Fore, Style, init

# Set the standard output encoding to UTF-8 (only if we have a buffer)
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

init()

_tags: dict[str, int] = {}
_timestamps: dict[str, float] = {}


def terminal_print(text: str, tag: str = "DEFAULT") -> None:
    """
    Print text to the terminal with optional tag, timestamp, and elapsed time.

    Args:
        text: Message to print.
        tag: Tag name for grouping/counting. Use 'DEFAULT' for no tag styling.
    """
    global _tags, _timestamps

    # Time cost since last call with this tag
    if tag in _timestamps and _timestamps[tag]:
        time_cost = time.time() - _timestamps[tag]
        time_cost_str = f" | {time_cost:.6f} secs"
    else:
        time_cost_str = ""

    _timestamps[tag] = time.time()

    if tag != "DEFAULT":
        _tags[tag] = _tags.get(tag, 0) + 1
        tag_index = list(_tags.keys()).index(tag)
        tree_tag = (
            f'{Fore.LIGHTBLACK_EX}{"_" if tag_index == 0 else "|"}'
            f'{"_" * tag_index}{tag}({_tags[tag]})_{Style.RESET_ALL}'
        )
        text = f"{tree_tag}{text} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{time_cost_str}"

    if isinstance(text, str):
        text = text.encode("utf-8", errors="replace").decode("utf-8")
    print(text, flush=True)


def reset() -> None:
    """Reset tag counts and timestamps (useful between runs or sections)."""
    global _tags, _timestamps
    _tags.clear()
    _timestamps.clear()


__all__ = ["terminal_print", "reset"]
