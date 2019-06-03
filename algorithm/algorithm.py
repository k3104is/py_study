def fizzbazz():
    for i in range(1, 100):
        i_mod3 = i % 3 == 0
        i_mod5 = i % 5 == 0
        if i_mod3 and i_mod5:
            str = "FizzBuzz"
        elif i_mod3:
            str = "Fizz"
        elif i_mod5:
            str = "Buzz"
        else:
            str = i
        print(str)


def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found


def linear_test():
    numbers = range(0, 100)
    s1 = ss(numbers, 2)
    s2 = ss(numbers, 202)
    print(s1)
    print(s2)


def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)


def anagram_test():
    print(anagram("iceman", "cinema"))
    print(anagram("leaf", "tree"))


def occur_test():
    count_characters(""
def main():
    anagram_test()


if __name__ == "__main__":
    main()
