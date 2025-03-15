import random

def get_determiner(quantity):
    """Return a randomly chosen determiner.
    If quantity is 1, returns one of: "a", "one", "the".
    Otherwise returns one of: "some", "many", "the".
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, returns one of:
      "bird", "boy", "car", "cat", "child",
      "dog", "girl", "man", "rabbit", "woman"
    Otherwise returns one of:
      "birds", "boys", "cars", "cats", "children",
      "dogs", "girls", "men", "rabbits", "women"
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(nouns)

def get_verb(quantity, tense):
    """Return a randomly chosen verb based on quantity and tense.
    For tense "past", returns one of:
      "drank", "ate", "grew", "laughed", "thought",
      "ran", "slept", "talked", "walked", "wrote"
    For tense "present" and quantity 1, returns one of:
      "drinks", "eats", "grows", "laughs", "thinks",
      "runs", "sleeps", "talks", "walks", "writes"
    For tense "present" and quantity NOT 1, returns one of:
      "drink", "eat", "grow", "laugh", "think",
      "run", "sleep", "talk", "walk", "write"
    For tense "future", returns one of:
      "will drink", "will eat", "will grow", "will laugh",
      "will think", "will run", "will sleep", "will talk",
      "will walk", "will write"
    """
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                     "runs", "sleeps", "talks", "walks", "writes"]
        else:
            verbs = ["drink", "eat", "grow", "laugh", "think",
                     "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]
    else:
        raise ValueError("Invalid tense provided.")
    return random.choice(verbs)

def get_preposition():
    """Return a randomly chosen preposition from a list."""
    prepositions = [
        "about", "above", "across", "after", "along", "around", "at",
        "before", "behind", "below", "beneath", "beside", "between", "by",
        "during", "for", "from", "in", "into", "near", "of", "off", "on",
        "over", "to", "under", "with", "without"
    ]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase.
    It is formed by a preposition, a determiner (using the given quantity),
    and a noun (using the given quantity).
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"

def get_adjective():
    """Return a randomly chosen adjective for additional functionality."""
    adjectives = ["quick", "lazy", "sleepy", "noisy", "happy", 
                  "sad", "bright", "dark", "colorful", "dull"]
    return random.choice(adjectives)

def make_sentence(quantity, tense):
    """Build and return a sentence with:
       - A determiner, an adjective, a noun, and a verb.
       - Two prepositional phrases.
       The grammatical quantity and tense are used appropriately.
    """
    determiner = get_determiner(quantity)
    adjective = get_adjective()  # additional functionality
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prep_phrase1 = get_prepositional_phrase(quantity)
    prep_phrase2 = get_prepositional_phrase(quantity)
    
    # Construct the sentence by combining the parts.
    sentence_parts = [determiner, adjective, noun, verb, prep_phrase1, prep_phrase2]
    sentence = " ".join(sentence_parts)
    # Capitalize the first letter and add a period.
    return sentence.capitalize() + "."

def main():
    while True:
        # Print six sentences with the following grammar combinations:
        # Single past, single present, single future,
        # plural past, plural present, and plural future.
        print(make_sentence(1, "past"))
        print(make_sentence(1, "present"))
        print(make_sentence(1, "future"))
        print(make_sentence(2, "past"))
        print(make_sentence(2, "present"))
        print(make_sentence(2, "future"))
        
        # Prompt the user to run the program again.
        while True:
            cont = input("Do you want to run the program again? 1 - Yes 0 - No: ")
            if cont in ("0", "1"):
                break
            print("Invalid input. Please enter 1 or 0.")
        if cont == "0":
            break

if __name__ == "__main__":
    main()