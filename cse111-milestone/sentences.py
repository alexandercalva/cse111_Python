import random

def get_determiner(grammatical_number):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If grammatical_number == 1, this function will return
    either "the" or "one". Otherwise this function will
    return either "some" or "many".

    Parameter
        grammatical_number: an integer.
            If grammatical_number == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if grammatical_number == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(grammatical_number):
    """Return a randomly chosen noun.
    If grammatical_number == 1, this function will
    return one of these ten single nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these
    ten plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        grammatical_number: an integer that determines
            if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if grammatical_number == 1:
        noun = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    else:    
        noun = [ "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]    
     # Randomly choose and return a determiner.
    word = random.choice(noun)
    return word
    

def get_verb(grammatical_number, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and grammatical_number is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and grammatical_number is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        grammatical_number: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if grammatical_number == 1 and tense == "present":
        verb = ["drinks", "eats", "grows", "laughs", "thinks",
         "runs", "sleeps", "talks", "walks", "writes"]
    else:    
        if tense == "past":
            verb = ["drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"]
        elif tense == "present":
            verb = ["drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"]           
        elif tense == "future":
            verb = [ "will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"]
        else:
            verb = ["Enter a tense correctly"]
    # Randomly choose and return a determiner.
    word = random.choice(verb)
    return word
def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    preposition = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    word = random.choice(preposition)
    return word
    
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
    if quantity == 1:   # single
        phrase = get_preposition() + " " + get_determiner(quantity) + " " + get_noun(quantity) 
    else:
        phrase = get_preposition() + " " + get_determiner(quantity) + " " + get_noun(quantity)
    
    return phrase
def tense_verb():
    print("Please, choose the option for the tense: ")
    print("a: past")
    print("b: present")
    print("c: future")
    option =  input("Enter the tense: a , b or c: ")
    option = option.lower()
    while option != "a" and option != "b" and option != "c":
        print("a: past")
        print("b: present")
        print("c: future")
        option =  input("Please enter the tense: a , b or c ")
    
    if option == "a":
        return "past"
        
    elif option == "b":
        return "present"
        u
    else:
        return "future"

def single_plural():
     
    print("1: Single")
    print("2: Plural")
    option = int(input("Choose an option 1 if is single or 2 if is plural: "))
    while option != 1 and option != 2:
        print("1: Single")
        print("2: Plural")
        option = int(input("Choose an option 1 if is single or 2 if is plural: "))

    if option == 1:
        return 1
    else:
        return 2

def main():
   n = single_plural()
   tense = tense_verb()
   print(f" {get_determiner(n)} {get_noun(n)} {get_verb(n, tense)} {get_prepositional_phrase(n)} ")

main()