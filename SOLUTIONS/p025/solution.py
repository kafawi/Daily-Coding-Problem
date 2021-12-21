# iteration 2 and 3
def matches(text :str, pattern :str) -> bool: 
    return _matches(text, 0, pattern, 0) 

def _matches(text :str, idx_text_start :int, pattern :str , idx_pattern: int) -> bool:
    # sourcery skip: merge-else-if-into-elif, reintroduce-else
    for i in range(idx_text_start, len(text)):
        # guard if text is > pattern
        if not _is_idx_in_bounds(pattern, idx_pattern): return False
        if _is_optional(pattern, idx_pattern):
            # skip this state and try the next with recurrsion (this is greedy)
            if _matches(text, i, pattern, idx_pattern + 2): return True
            # else check if char matches
            if not _matches_char(pattern[idx_pattern], text[i]): return False
        else:
            if not _matches_char(pattern[idx_pattern], text[i]): return False
            idx_pattern += 1
    # end of pattern? and text
    return _is_pattern_finished(pattern, idx_pattern)

def _is_pattern_finished(pattern :str, idx_pattern :int) -> bool:
    length = len(pattern[idx_pattern:])
    is_empty = length == 0
    is_right_slice_optional = length % 2 == 0 and \
        all((c in "*" for c in  pattern[(idx_pattern+1)::2])) 
    return is_empty or is_right_slice_optional

def _is_optional(pattern :str, idx :int) -> bool:
    return idx + 1 < len(pattern) and pattern[idx+1] in "*"

def _is_idx_in_bounds(array :str, idx :int) ->bool:
    return 0 <= idx < len(array)

def _matches_char(pattern_char, text_char :str) -> bool:
    return "." in pattern_char or text_char in pattern_char
    
"""
# iteration 0
def matches(text :str, pattern :str) -> bool:
    if len(text) != len(pattern): return False
    for char_text, char_pattern in zip(text, pattern):
        if char_text != char_pattern: return False
    return True

# iteration 1
def matches(text :str, pattern :str) -> bool:
    if len(text) != len(pattern): return False
    for char_text, char_pattern in zip(text, pattern):
        if char_pattern == ".": continue
        if char_text != char_pattern: return False
    return True 

"""
