"""
Example script using the deeplog package.
Run from project root: python main.py
"""

from deeplog import terminal_print, reset

if __name__ == "__main__":
    terminal_print("Starting...")
    terminal_print("First step", tag="MAIN")
    terminal_print("Second step", tag="MAIN")
    terminal_print("Nested", tag="SUB")
    reset()
    terminal_print("After reset", tag="MAIN")
