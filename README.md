# python_challenge
Practice on http://www.pythonchallenge.com/

all code in solutions.py

official solution: https://the-python-challenge-solutions.hackingnote.com/

## notes

### challenge 5 - about pickle
* Python has a more primitive serialization module called marshal, but in general pickle should always be the preferred way to serialize Python objects. 
* marshal exists primarily to support Python’s .pyc files.
* classes are pickled by named reference, so the same restrictions in the unpickling environment apply. Note that none of the class’s code or data is pickled. **These restrictions are why picklable functions and classes must be defined in the top level of a module.**
