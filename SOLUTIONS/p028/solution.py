from typing import List

def justify(word_seq :List[str], k :int) -> List[str]:
  lines = []
  line_length_sum = 0
  line = []
  for word in word_seq:
    if line_length_sum + len(line) - 1 + len(word) > k:
      #building time
      lines.append(_line2string(line, k - line_length_sum))
      line.clear()
      line_length_sum = 0
    line.append(word)
    line_length_sum += len(word)
  lines.append(_line2string(line,  k - line_length_sum))
  return lines

def _line2string(words : List[str], delta :int) -> str:
  s = words[0]
  if len(words) == 1:
    s += " "*delta
  else:
    min_gap_width, n_bigger_gap = divmod(delta, len(words)-1)
    for i, word in enumerate(words[1:]):
      s += " " * min_gap_width
      if i < n_bigger_gap: s += " "
      s += word
  return s
