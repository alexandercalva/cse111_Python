from sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb
import pytest

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["the", "one"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
def test_get_noun():
    get_noun(1)

def test_get_verb():
    get_verb(1, "present")

def test_get_preposition():
    get_preposition()

def test_get_prepositional_phrase():
    get_prepositional_phrase(1)

pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])
