"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):
    return f" :: {vocab_words[0]}".join(vocab_words)


def remove_suffix_ness(word):
    rootword = word[0:-4]
    if rootword[-1] == "i":
        return rootword[0:-1] + "y"
    else:
        return rootword


def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index]
    if index == -1:
        return adjective[:-1]+ "en"
    else:
        return adjective + "en"
