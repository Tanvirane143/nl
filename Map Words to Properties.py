e. Map Words to Properties Using Python Dictionaries

Mapping words to their properties using Python dictionaries is a common and powerful technique. You can create dictionaries where words are keys and their properties are values. These properties can include part-of-speech tags, frequencies, definitions, or any other relevant information.

Code : 
#creating and printing a dictionary by mapping word with its properties
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print('length:', len(thisdict))
