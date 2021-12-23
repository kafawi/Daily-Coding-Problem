# justify(word_seq :[String], k :int) &rarr; [String]

- The result is a blocked text with the width `k`.
- Words ar seperated with at least one space or the newline.
- The line schould start and en with an word, and the spaces are "streched" evenly within, by adding new spaces.
- If there are less spaces left than the number of gaps, add the leftover spaces to the left most gaps one each.
- if a single word is in the line, pad the line with spaces on the right side.
- precondition is guarantied: words length `<=k`

## thoughts

We pass through the sequence by summing up the length of the words the number of gabs that are the same as the number of words in this line minus 1. If this is length is bigger than k , we will construct the line. by getting the min width by simply integer division and the number of all wider gaps by modulo:

 1. `delta = k - sum of words length in the line`
 2. `number of gap = number of words in line - 1`
 3. `min gap width = delta / number of gap`
 4. `number of bigger gap = delta %  number of gap`

after that we can construct the line and continuing fillen up a new line with words.

## algorithm

```text
justify(word_seq :[String], k :int) -> [String]
  lines = new [String]
  line_length_sum = 0
  line = [String]
  for each word in word_seq:
    if line_length_sum + line.length + word.length > k:
      #building time
      lines.append(_line2string(line, delta))
      line.empty()
      line_length_sum = 0
    line.append(word)
    line_length_sum += word.length
  lines.append(_line2string(line, delta))
  return lines

_line2string(line : [String], delta) -> String:
  s = line[0]
  if line.length == 1:
    s += SPACE delta times
  else:
    min_gap_width = delta / line.length - 1
    n_bigger_gap = delta % line.length - 1 
    for i=1; i < line.length; i++ :
      s += SPACE min_gap_width times
      if i < n_bigger_gap: s += SPACE
      s += line[i]
  return s
```

[code](solution.py)
[test](test.py)
