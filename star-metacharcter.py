import re
pattern = r"eggs(bacon)*"

if re.match(pattern, "eggs"):
    print('match found')
