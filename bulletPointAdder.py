#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line on the clipboard.

import pyperclip
text = pyperclip.paste()

'Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nList of cultivars'

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
