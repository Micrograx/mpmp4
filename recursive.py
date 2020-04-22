

def cards_rec(number):
    res = []
    if (number == 1):
        res.append(0)
    else:
        prev = cards_rec(number - 1)
        res = prev + [(number-1)] + prev
    return res


if __name__ == "__main__":

    final = cards_rec(100)
    print(final)
