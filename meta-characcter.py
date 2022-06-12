import re
pattern = r"gr..y"
if re.match(pattern, "gray"):
    print('match found')
else:
    print('no match found')

# ------------------------------

pattern = r"^gr.y$"
if re.match(pattern, "grey"):
    print('match1')
else:
    print('no match found')
