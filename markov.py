import random
# from sys import argv

# script, filename, text_length = argv

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    source_file = open(corpus)
    word_bank = {}
    joined = source_file.read()
    split_source = joined.split()
    for i in range(len(split_source)-2):
        key = (split_source[i], split_source[i+1])
        idv_value = split_source[i+2]
        # if key is not already there, make it (it has no value rn)
        if key not in word_bank.keys():
            word_bank[key] = []
        # stick the value in there
        word_bank[key].append(idv_value)
    return word_bank

def make_text(filename):
    """Takes dictionary of markov chains; returns random text."""
    # Get a Markov chain
    chain_dict = make_chains(filename)
    chosen_key = random.choice(chain_dict.keys())
    our_string = " ".join(chosen_key)
    character_count = 0
    while character_count < 140:
        for value in chain_dict[chosen_key]:
            value = random.choice(chain_dict[chosen_key])
            our_string = our_string + " " + (value)
            split_string = our_string.split(" ")
            chosen_key = (split_string[-2], split_string[-1])
            character_count = len(our_string)
    print our_string

make_text(raw_input("Enter the filename of the selected text: "))