import random

def get_determiner(quantity):
    if quantity == 1:
        words = ["the", "one", "a"]
    else:
        words = ["some", "many"]
    return random.choice(words)

def get_noun(quantity):
    if quantity == 1:
        words = ["girl", "bird", "child", "car", "rabbit", "cat"]
    else:
        words = ["girls", "birds", "children", "cars", "rabbits", "cats"]
    return random.choice(words)

def get_verb(quantity, tense):
    if tense == "past":
        words = ["talked", "drank", "laughed", "ran", "jumped"]
    elif tense == "present":
        words = ["talks", "drinks", "laughs", "runs", "jumps"] if quantity == 1 else ["talk", "drink", "laugh", "run", "jump"]
    elif tense == "future":
        words = ["will talk", "will drink", "will laugh", "will run", "will jump"]
    return random.choice(words)

def get_preposition():
    words = [
        "about", "above", "across", "after", "along", "around", "at",
        "before", "behind", "below", "beyond", "by", "despite", "except",
        "for", "from", "in", "into", "near", "of", "off", "on", "onto",
        "out", "over", "past", "to", "under", "with", "without"
    ]
    return random.choice(words)

def get_adjective():
    """Return a randomly chosen adjective."""
    words = ["happy", "sad", "quick", "slow", "red", "blue", "smart", "tall", "short"]
    return random.choice(words)

def get_adverb():
    """Return a randomly chosen adverb."""
    words = ["quickly", "slowly", "calmly", "brightly", "sweetly", "angrily"]
    return random.choice(words)

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adjective = get_adjective()
    return f"{preposition} {determiner} {adjective} {noun}"

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adjective = get_adjective()
    adverb = get_adverb()
    verb = get_verb(quantity, tense)
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)
    sentence = f"{determiner.capitalize()} {adjective} {noun} {adverb} {verb} {prepositional_phrase1} {prepositional_phrase2}."
    return sentence

def main():
    print(make_sentence(1, "past"))       # Singular, past tense
    print(make_sentence(1, "present"))    # Singular, present tense
    print(make_sentence(1, "future"))     # Singular, future tense
    print(make_sentence(2, "past"))       # Plural, past tense
    print(make_sentence(2, "present"))    # Plural, present tense
    print(make_sentence(2, "future"))     # Plural, future tense

if __name__ == "__main__":
    main()


