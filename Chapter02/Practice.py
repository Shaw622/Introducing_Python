letters = 'abcdefghijklmnopqrstuvwxyz'

print(letters[0])
print(letters[2])
print(letters[-1])
print(letters[-2])
print(letters[:])
print(letters[20:])
print(letters[12:15])
print(letters[-3:])
print(letters[18:-3])
print(letters[::7])
print(letters[::-1])

print(len(letters))
print(letters.split('g'))


name = 'Henny'
print(name.replace('H', 'P'))
print(name)
print('P' + name[1:])
print(name.count('e'))
print(name.count('n'))
print(name.find('n'))
print(name.rfind('n'))
print(name.isalnum())


list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
string = ', '.join(list)
print('Found and siging book deals:', string)
print('Found and siging book deals:' + string)


setup = 'a duck goes into a bar...'
print(setup.strip('.'))
print(setup.capitalize())
print(setup.title())
print(setup.upper())
print(setup.swapcase()) #大文字小文字の入れ替え
print(setup.center(30))
print(setup.ljust(30))
print(setup.rjust(30))
print(setup.replace('duck', 'marmoset'))
print(setup.replace('a ', 'a famous ', 100))
