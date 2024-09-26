import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

def matcher(input_line, pattern):
    ptr1 = 0
    ptr2 = 0
    
    while ptr1 < len(input_line):
        if ptr2 < len(pattern) and pattern[ptr2] == '\\':
            # Check for escape sequences
            if ptr2 + 1 < len(pattern) and pattern[ptr2 + 1] in ['d', 'w']:
                if pattern[ptr2 + 1] == 'd' and input_line[ptr1].isdigit():
                    return matcher(input_line[ptr1 + 1:], pattern[ptr2 + 2:])
                elif pattern[ptr2 + 1] == 'w' and input_line[ptr1].isalnum():
                    return matcher(input_line[ptr1 + 1:], pattern[ptr2 + 2:])
                else:
                    ptr1 += 1
                    continue
        elif ptr2 < len(pattern) and pattern[ptr2] == input_line[ptr1]:
            # Normal character match
            return matcher(input_line[ptr1 + 1:], pattern[ptr2 + 1:])
        elif ptr2 < len(pattern) and pattern[ptr2] == '+':
            # Handle the '+' quantifier
            if ptr2 == 0:
                return False  # '+' cannot be at the start of a pattern
            # Check if previous character matches at least once
            if ptr1 < len(input_line) and input_line[ptr1] == pattern[ptr2 - 1]:
                return matcher(input_line[ptr1 + 1:], pattern)  # Match one or more
            else:
                return matcher(input_line[ptr1 + 1:], pattern)  # Try next character
        else:
            ptr1 += 1
            
    # If the pattern ends, check for leftover characters
    return ptr2 >= len(pattern)

def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern == "\\d":
        for i in range(10):
            if input_line.find(str(i)) != -1:
                return True
    elif pattern == "\\w":
        return input_line.isalnum()
    elif pattern[0:2] == "[^":
        pat = pattern[2:-1]
        for ch in pat:
            if input_line.find(ch) != -1:
                return False
        return True
    elif pattern[0] == "[" and pattern[-1] == "]":
        pat = pattern[1:-1]
        for ch in pat:
            if input_line.find(ch) != -1:
                return True
        return False
    elif pattern[0] == "^":
        if input_line.startswith(pattern[1:]):
            return True
        return False
    elif pattern[-1] == "$":
        l = len(pattern[:-1])
        if input_line[-l:] == pattern[:-1]:
            return True
        return False
    else:
        return matcher(input_line, pattern)

def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()
    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)
    print("Logs from your program will appear here!")
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)

if __name__ == "__main__":
    main()