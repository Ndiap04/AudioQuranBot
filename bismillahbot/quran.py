import re
import xml.etree.ElementTree as ET
from random import randint
from typing import Tuple


def make_index():
    """An index of the Surahs in the Quran, formatted to send over Telegram."""
    chapters = Quran.surah_names[:]
    # padding...
    for i in range(9):
        chapters[i] = " " + chapters[i] + " " * (14 - len(chapters[i]))
    for i in range(9, 58):
        chapters[i] += " " * (14 - len(chapters[i]))

    index = []
    left = range(1, 58)
    right = range(58, 115)
    for i, j in zip(left, right):
        index.append("/{} <code>{}</code>/{} {}"
                     .format(i, chapters[i - 1], j, chapters[j - 1]))
    return "\n".join(index)
