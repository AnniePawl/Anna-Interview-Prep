# Given an "out" string w/ length 4 ("<<>>"), and a word, return new string where word is in middle of out string.


def make_out_word(out, word):
    return(out[:2] + word + out[-2:])


print(make_out_word('<<>>', 'Yay'))  # <<Yay>>
print(make_out_word('(())', 'WooHoo'))  # ((WooHoo))
print(make_out_word('[[]]', 'Hooray'))  # ((WooHoo))
