capitals = {"USA":"Washington DC",
            "Poland":"Warsaw",
            "Russia":"Moscow"
            }

# capitals.update({"Germany":"Berlin"})
# capitals.pop("USA")
# capitals.clear()

# print(capitals['Poland'])
# print(capitals.get('Russia'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items)

for key, value in capitals.items():
    print(key, value)