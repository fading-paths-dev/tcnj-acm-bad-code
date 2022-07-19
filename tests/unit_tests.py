import string
from bad import generate_random_alphabet
from hamcrest import assert_that, equal_to
from unittest import TestCase

ALPHABET_LENGTH = 26


class TestBadCode(TestCase):
    def test_output_length(self):
        result = generate_random_alphabet()
        assert_that(len(result), equal_to(ALPHABET_LENGTH))

    def test_output_contents_do_not_repeat(self):
        result = generate_random_alphabet()
        test = 0
        for i in range(ALPHABET_LENGTH):
            for p in range(ALPHABET_LENGTH):
                if result[i] == result[p]:
                    test += 1

        assert_that(test, equal_to(ALPHABET_LENGTH))

    def test_output_contents_contain_every_letter(self):
        result = generate_random_alphabet()
        alphabet = string.ascii_lowercase
        test = [0] * ALPHABET_LENGTH
        compare = [1] * ALPHABET_LENGTH
        for i in range(ALPHABET_LENGTH):
            for p in range(ALPHABET_LENGTH):
                if result[i] == alphabet[p]:
                    test[p] += 1
        assert_that(test, equal_to(compare))
