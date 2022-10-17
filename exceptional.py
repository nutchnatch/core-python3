import sys
from math import log

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'nine': '9',
    'ten': '10',
}

def convert(s):
    """Convert a String to an Integer."""
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
    except (KeyError, TypeError) as e:
        #pass
        print(f"Conversion error: {e!r}",
            file=sys.stderr)
        raise
        return -1
    return x

def string_log(s):
    v = convert(s)
    return log(v)