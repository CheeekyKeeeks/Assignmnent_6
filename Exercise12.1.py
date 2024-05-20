>>> from collections import Counter
>>> import string
>>>
>>> def most_frequent(text):
...     filtered_text = ''.join(filter(str.isalpha, text)).lower()
...     letter_counts = Counter(filtered_text)
...     sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
...     for letter, frequency in sorted_letters:
...             print(f"{letter}: {frequency}")
...
>>> sample_text = "This is a sample text to demonstrate the most_frequent function."
>>> most_frequent(sample_text)
t: 10
e: 7
s: 5
o: 4
n: 4
i: 3
a: 3
m: 3
h: 2
r: 2
f: 2
u: 2
p: 1
l: 1
x: 1
d: 1
q: 1
c: 1
>>> english_text = "To be, or not to be, that is the question: Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune..."
>>> spanish_text = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero..."
>>> french_text = "Il était une fois, dans une contrée lointaine, un petit village entouré de montagnes et de forêts enchantées..."
>>> german_text = "Alle Menschen sind frei und gleich an Würde und Rechten geboren. Sie sind mit Vernunft und Gewissen begabt und sollen einander im Geist der Brüderlichkeit begegnen..."
>>> russian_text = "В некотором царстве, в некотором государстве жил-был могучий богатырь, который всем был известен своими подвигами..."
>>> print("English text letter frequencies:")
English text letter frequencies:
>>> most_frequent(english_text)
t: 14
o: 12
e: 12
r: 8
n: 8
s: 8
h: 6
i: 6
u: 5
a: 4
f: 4
b: 3
w: 2
l: 2
d: 2
g: 2
q: 1
m: 1
>>> print("\nSpanish text letter frequencies:")

Spanish text letter frequencies:
>>> most_frequent(spanish_text)
e: 12
a: 12
o: 11
n: 9
u: 7
l: 7
r: 6
d: 6
m: 5
i: 5
c: 4
h: 4
g: 2
q: 2
t: 2
v: 2
s: 2
y: 1
b: 1
p: 1
í: 1
z: 1
>>> print("\nFrench text letter frequencies:")

French text letter frequencies:
>>> most_frequent(french_text)
e: 13
n: 12
t: 11
i: 7
a: 6
o: 6
s: 5
l: 4
é: 4
u: 4
d: 3
r: 3
f: 2
c: 2
g: 2
p: 1
v: 1
m: 1
ê: 1
h: 1
>>> print("\nGerman text letter frequencies:")

German text letter frequencies:
>>> most_frequent(german_text)
e: 25
n: 19
i: 12
d: 10
r: 9
s: 8
g: 7
l: 6
t: 6
u: 5
b: 5
a: 4
c: 4
h: 4
m: 3
f: 2
w: 2
ü: 2
o: 2
v: 1
k: 1
>>> print("\nRussian text letter frequencies:")

Russian text letter frequencies:
>>> most_frequent(russian_text)
о: 13
в: 8
е: 7
т: 7
и: 7
р: 6
м: 6
с: 6
а: 4
г: 4
ы: 4
н: 3
к: 3
л: 3
б: 3
у: 2
д: 2
й: 2
ц: 1
ж: 1
ч: 1
ь: 1
з: 1
п: 1
>>>