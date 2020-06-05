def no_dups(s):
    strings = s.split()

    count = set()

    res = []

    for word in strings:
        if word not in count:
            count.add(word)
            res.append(word)

    return " ".join(res)

# in place?



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))