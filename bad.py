from random import sample
import string


def generate_random_alphabet():
    alphabet = string.ascii_lowercase
    mixed_alphabet = sample(alphabet, len(alphabet))

    return mixed_alphabet


def output_alphabet_as_a_string(alphabet):
    print(''.join(alphabet))


result = generate_random_alphabet()
output_alphabet_as_a_string(result)
