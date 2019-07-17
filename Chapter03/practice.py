print(list('cat')) #１文字ごとの文字列に変換

tuple = ('ready', 'fire', 'aim')
print(list(tuple)) # タプルをリストに変換

print(set('letterws')) # 集合へ変換

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'vodka', 'kahlua', 'cream'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
    }

print('-------')
for name, contents in drinks.items():
    if 'vodka' in contents: # Vodka のみを抽出
        print(name)

print('-------')
for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

print('-------')
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

print('-------')
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'orange juice'}:
        print(name)
