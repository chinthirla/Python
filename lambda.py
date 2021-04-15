raise_to_power=lambda x,y: x ** y
raise_to_power(2,3)
nums = [48, 6, 9, 21, 1]
sqare_all = map(lambda num: num ** 2,nums)
print(list(sqare_all))


def echo_word(word1, echo):
    """Concatenate echo copies of word1."""
    words = word1 * echo
    print(words)
    return words
