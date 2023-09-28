path_to_book = "books/frankenstein.txt"
with open(path_to_book) as f:
    file_contents = f.read()


# print(len(words))

def report(book,path):
    print(f"--- Begin report of {path} ---")

    dic = count_letters(book)
    lst = list(dic.items())
    lst.sort(key=lambda a: a[1], reverse=True)
    words = book.split()
    print(f"{len(words)} words found in the document")
    print(" ")
    for l in lst:
        print(f"the '{l[0]}' character was found {l[1]} times")


def count_letters(book_str):
    dic = {
        "a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,
        "i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,
        "q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,
        "y":0,"z":0
    }

    for word in book_str:
        low_word = word.lower()
        for letter in low_word:
            if letter == "a":
                dic["a"] += 1
            elif letter == "b":
                dic["b"] += 1
            elif letter == "c":
                dic["c"] += 1
            elif letter == "d":
                dic["d"] += 1
            elif letter == "e":
                dic["e"] += 1
            elif letter == "f":
                dic["f"] += 1
            elif letter == "g":
                dic["g"] += 1
            elif letter == "h":
                dic["h"] += 1
            elif letter == "i":
                dic["i"] += 1
            elif letter == "j":
                dic["j"] += 1
            elif letter == "k":
                dic["k"] += 1
            elif letter == "l":
                dic["l"] += 1
            elif letter == "m":
                dic["m"] += 1
            elif letter == "n":
                dic["n"] += 1
            elif letter == "o":
                dic["o"] += 1
            elif letter == "p":
                dic["p"] += 1
            elif letter == "q":
                dic["q"] += 1
            elif letter == "r":
                dic["r"] += 1
            elif letter == "s":
                dic["s"] += 1
            elif letter == "t":
                dic["t"] += 1
            elif letter == "u":
                dic["u"] += 1
            elif letter == "v":
                dic["v"] += 1
            elif letter == "w":
                dic["w"] += 1
            elif letter == "x":
                dic["x"] += 1
            elif letter == "y":
                dic["y"] += 1
            elif letter == "z":
                dic["z"] += 1
    return dic

report(file_contents,path_to_book)