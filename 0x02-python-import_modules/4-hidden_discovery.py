#!/usr/bin/python3
if __name__ == "__main__":
    """Print the value of variable a from variable_load_5."""
import hidden_4

names = dir(hidden_4)
for name in names:
    if name[:2] != "__":
        print(name)
