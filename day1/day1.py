import re
with open("input.txt", "r") as f:
    lines = f.readlines()

print("Part 1:")
print(sum(list(map(lambda x: int(f"{x[0]}{x[-1]}"),
                   [re.findall("[0-9]", y) if len(re.findall("[0-9]", y)) > 0 else [0]
                    for y in lines if len(y.strip()) > 0]))))

word_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
rgx = "|".join(word_dict.keys()) + "|" + "[0-9]"
back_rgx = "(?s:.*)" + "(" + rgx +")"
translate_func = lambda x: x if not x in word_dict else word_dict[x]

print("Part 2:")
print(sum(list(map(lambda x: int(f"{translate_func(x[0])}{translate_func(x[-1])}"),
                   [(re.search(rgx, y).group(0) if re.search(rgx, y) is not None else 0,
                     re.search(back_rgx, y).group(1) if re.search(rgx, y) is not None else 0)
                    for y in lines if len(y.strip()) > 0]))))
