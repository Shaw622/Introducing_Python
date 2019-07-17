years_list = [1991, 1992, 1993, 1994, 1995, 1996]
print(years_list[3])
print(years_list[-1])

things = ["mozzarella", "cinderella", "salmonella"]
print(things)

print(things[1].capitalize())
print(things)

things[1] = things[1].capitalize()
print(things)

things[0] = things[0].upper()
print(things)

del things[-1]
print(things)

surprise = ["Groucho", "Chico", "Harpo"]
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1].capitalize()
print(surprise[-1])


e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print(e2f["walrus"])


life = {
    "animals": {
        "cats": [
            'Henri', 'Grumpy', 'Lucy'
            ],
        "octopi": {},
        "emus": {}
        },
    "plants": {},
    "other": {}
    }
print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])
