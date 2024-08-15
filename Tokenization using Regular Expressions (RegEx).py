b. Tokenization using Regular Expressions (RegEx) 
Tokenization using Regular Expressions (RegEx) is a powerful and flexible method for splitting text into tokens based on complex patterns. Regular expressions allow you to define patterns for identifying the tokens you want to extract from a string. This method is particularly useful for handling a variety of delimiters, removing unwanted characters, and performing more complex text processing tasks.

Code:
import re
text = """Founded in 2002, SpaceX’s mission is to enable humans to become a spacefaring civilization and a multiplanet
species by building a self-sustaining city on Mars. In 2008, SpaceX’s Falcon 1 became the first privately developed
liquid-fuel launch vehicle to orbit the Earth."""
tokens = re.findall("[\w']+", text)
print(tokens)
