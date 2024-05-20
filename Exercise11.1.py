>>> count = 0
>>> fname = input("C:\$\words.txt")
C:\$\words.txt
>>> if len(fname) < 1 : fname = ("C:\$\words.txt")
...
>>> make_dictionary = dict()
>>> fhand = open(fname)
>>>
>>> for line in fhand:
...	words = line.split()
...	for word in words:
...		count = count + 1
...		make_dictionary[word] = count
...
... if 'skills' in make_dictionary:
...	print('True')
... else:
... 	print('False')
...
True
>>>
>>> print(make_dictionary)
