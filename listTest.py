Python 3.8.9 (tags/v3.8.9:a743f81, Apr  2 2021, 11:10:41) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> boy = ['t,h,i']
>>> boy.append('s')
>>> print(boy)
['t,h,i', 's']
>>> boy = ['t','h','i']
>>> boy.append('s')
>>> print(boy)
['t', 'h', 'i', 's']
>>> print(boy[2])
i
>>> print(boy.remove('h'))
None
>>> boy.remove('h')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    boy.remove('h')
ValueError: list.remove(x): x not in list
>>> print(boy)
['t', 'i', 's']
>>> boy.insert(1,'b')
>>> print(boy)
['t', 'b', 'i', 's']
>>> del boy[2]
>>> print(boy)
['t', 'b', 's']
>>> gril = boy.pop(-1)
>>> print(gril)
s
>>> print(boy)
['t', 'b']
>>> boy.append('s')
>>> print(boy)
['t', 'b', 's']
>>> boy[1]='tesla'
>>> print(boy)
['t', 'tesla', 's']
>>> print(len(boy))
3
>>> users=['z','r','t','b','n','p']
>>> users.sort()
>>> print(users)
['b', 'n', 'p', 'r', 't', 'z']
>>> users.sort(reverse=True)
>>> print(users)
['z', 't', 'r', 'p', 'n', 'b']
>>> print(sorted(users))
['b', 'n', 'p', 'r', 't', 'z']
>>> print(users)
['z', 't', 'r', 'p', 'n', 'b']
>>> users=['z','r','t','b','n','p']
>>> users.reverse()
>>> print(users)
['p', 'n', 'b', 't', 'r', 'z']
>>> for u in users:
	print(u)

	
p
n
b
t
r
z
>>> for u in sorted(users)
SyntaxError: invalid syntax
>>> for u in sorted(users):
	print(u)

	
b
n
p
r
t
z
>>> for u in sorted(users):
	print(u)

	
b
n
p
r
t
z
>>> users.reverse()
>>> for u in users:
	print(u)

	
z
r
t
b
n
p
>>> 