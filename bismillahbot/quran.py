# BismillahBot -- Explore the Holy Qur'an on Telegram
# Copyright (C) 1436-1438 AH  Rahiel Kasim
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
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


def save_json(quran):
    """Save Quran to a json file."""
    import json

    with open("quran.json", "w") as f:
        json.dump(quran, f, ensure_ascii=False)
