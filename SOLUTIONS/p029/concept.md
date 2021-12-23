# run-length encoding and decoding

## Why not pseudocode

```text
encode(text :String) -> String:
  if text is empty: return ""
  s = ""
  char = text[0]
  count = 1
  for each c in text:
    if char != c:
      s += String(count) + char
      char = c
      count = 1
    else:
      count += 1
  s += String(count) + char
  return s
   

decode(text :String) -> String:
  s = ""
  for (i = 0; i < text.length; i+=2):
    do int(text[i]) times:
      s += text[i+1]
  return s 
```

[code](solution.py)
