"""Test

>>> find_longest_substring_with_at_most_k_distict_chars("abcba", 2)
'bcb'

"""

from collections import deque, namedtuple



def find_longest_substring_with_at_most_k_distict_chars(s: str, k: int) -> str:
    class Cstats:
        def __init__(self):
              self.number = 0
              self.positions = list()
    # collecting
    charmap = dict()  
    for i,c in enumerate(s):
        if c not in charmap:
            charmap[c] = Cstats()
        charmap[c].number += 1
        charmap[c].positions.append(i)
    
    # get valid candidates
    Substring = namedtuple('Substring', ['start','end'])
    candidates = [Substring(0, len(s)-1)]  # default return if nothin is found
    for stats in charmap.values():
        if stats.number >= k:
            for start,end in zip(stats.positions[:-(k-1)], stats.positions[k-1:]):
                candidates.append(Substring(start, end))

    # second filtering
    candidates = sorted(candidates, key=lambda x: x.end - x.start)
    for smaller in candidates:
        for bigger in reversed(candidates):
            if smaller.start > bigger.start and smaller.end < bigger.end:
                candidates.remove(bigger)
    
    # get the longest
    longest = candidates[-1]
    return s[longest.start : longest.end+1]
    

if __name__=="__main__":
    import doctest
    doctest.testmod()