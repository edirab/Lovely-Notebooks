import re

s = """Any large snake that "constricts" its prey (see Constriction)."""
s = s.lower()
print(re.split('[^a-z]', s))

