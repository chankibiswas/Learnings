'''
Regex
-----

Identifiers -
\d Any number
\D Anything except a number
\w Any character
\W Anything except a charater
\s Any space
\S Anything except a spcae
. (Also called a period) Any character excpet a newline
\b White space around word
\. a period

Modifiers -
{1,3} Anything in between 1 to 3 size
+ Match one or more
? Match zero or 1
* Match 0 or more
$ Match end of string
^ Match beginning of string
| Either or
[] Range or variance
{x} We're expecting 'x' amount

White space characters -
\n New line
\t Tab
\s space
\e escape
\f form feed
\r return carriage
'''

import re

str = '''
Ram is 20 years old. Harish is 25.
Ramesh is 32 years old and Suresh is 29.
'''

ages = re.findall(r'\d{1,3}', str)
names = re.findall(r'[A-Z][a-z]*', str)
print(ages)
print(names)

personDictionary = {}

x = 0
for name in names:
    personDictionary[name] = ages[x]
    x+=1

print(personDictionary)













