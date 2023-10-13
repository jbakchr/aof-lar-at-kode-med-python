"""
ADDITIONAL EXERCISE

In this exercise you are to create a function that slices some text
provided to a function that'll return the sliced text.

To complete this exercise do the following:
- 1)  Create a function that'll return some sliced string given with these 3 parameters:
      - 1.1) a parameter called "txt" that should be the string to be sliced
      - 1.2) an integer parameter called "start" that'll define from where to start the slice of the string
      - 1.3) an integer parameter called "stop" that'll define from where to stop the slice of the string

"""

def text_shortener(txt, start, stop):
  return txt[start:stop]

print(text_shortener("Jonas", 0, 4))