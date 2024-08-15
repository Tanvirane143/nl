a. Tokenization using Python’s split() function
Tokenization is the process of splitting text into smaller units called tokens,
which can be words, phrases, or even characters. One of the simplest methods to
perform tokenization in Python is by using the split() function. This function
divides a string into a list of substrings based on a specified delimiter.
By default, split() uses whitespace as the delimiter.

Code:
text = """Founded in 2002, SpaceX’s mission is to enable humans to become a spacefaring civilization and a multi-planet species by building a self-sustaining city on Mars. In 2008, SpaceX’s Falcon 1 became the first privately developed liquid-fuel launch vehicle to orbit the Earth."""
# Splits at space
a=text.split()
print(a)
