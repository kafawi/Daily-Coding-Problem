def are_brackets_balanced(bracket_seq :str) -> bool:
    partners = {"(" : ")",
                "[" : "]",
                "{" : "}"}
    stack = []
    for bracket in bracket_seq:
        if bracket in "([{": 
            stack.append(bracket)
        elif bracket in ")]}":
            if stack and bracket == partners[stack[-1]]:
                stack.pop()
            else: 
                return False
    return not stack 
