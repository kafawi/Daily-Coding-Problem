"""Test
>>> find_original_sentence(["a", "b"], "")
[]

>>> find_original_sentence(['bbb', 'aabb'], "aabbb") is None
True

>>> find_original_sentence(['bb', 'aab'], "aabbb")
['aab', 'bb']

>>> a = find_original_sentence(['bed', 'bath', 'bedbath', 'and', 'beyond'], "bedbathandbeyond")
>>> a in [['bed', 'bath', 'and', 'beyond'], ['bedbath', 'and', 'beyond']]
True

>>> find_original_sentence(['quick', 'brown', 'the', 'fox'], "thequickbrownfox")
['the', 'quick', 'brown', 'fox']

>>> find_original_sentence(['quick', 'brown', 'the', 'fox', ''], "thequickbrownfox")
['the', 'quick', 'brown', 'fox']
"""
from typing import Optional, List, Set


def find_original_sentence(dictionary: Set[str], nospace_sentence: str) -> Optional[List[str]]:
    assert nospace_sentence is not None
    assert dictionary
    
    if len(nospace_sentence) == 0: return [] 
    if "" in dictionary: dictionary.remove("")
    original_sentence :List[str] = None
    for word in dictionary:
        original_sentence = None
        if word == nospace_sentence[:len(word)]:
            original_sentence = find_original_sentence(dictionary, nospace_sentence[len(word):])
            if original_sentence is not None:
                original_sentence = [word] + original_sentence
                break
    return original_sentence


if __name__ == "__main__":
    import doctest
    doctest.testmod()
