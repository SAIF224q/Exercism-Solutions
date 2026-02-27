def is_paired(input_string):
    closing_to_opening = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    opening_brackets = set(closing_to_opening.values())
    
    stack = []
    
    for char in input_string:
        if char in opening_brackets:

            stack.append(char)
        elif char in closing_to_opening:

            if not stack:  
                return False
            
            if stack[-1] != closing_to_opening[char]:
                return False

            stack.pop()
    
    return len(stack) == 0
