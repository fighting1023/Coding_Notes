adict = {"a": 1, 'b': [4, 5, 6]}
print(type(adict.get('a')), adict.get('a'))
# <class 'int'> 1
print(type(adict.get('c', 'nothing')), adict.get('c', 'nothing'))
# <class 'str'> nothing