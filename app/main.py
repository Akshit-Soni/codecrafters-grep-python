import sys

# Use raw strings for pattern definitions
class Pattern:
    DIGIT = r"\d"
    ALNUM = r"\w"

def match_pattern(input_line, pattern):
    ptr1 = 0  # Pointer for input_line
    ptr2 = 0  # Pointer for pattern

    while ptr1 < len(input_line) and ptr2 < len(pattern):
        if pattern[ptr2:ptr2 + 2] == Pattern.DIGIT:
            if input_line[ptr1].isdigit():
                ptr1 += 1
                ptr2 += 2
            else:
                return False
        elif pattern[ptr2:ptr2 + 2] == Pattern.ALNUM:
            if input_line[ptr1].isalnum():
                ptr1 += 1
                ptr2 += 2
            else:
                return False
        elif pattern[ptr2] == input_line[ptr1]:
            ptr1 += 1
            ptr2 += 1
        else:
            return False

    # After processing all characters in the pattern,
    # ensure that all remaining characters in the pattern are checked
    while ptr2 < len(pattern):
        if pattern[ptr2:ptr2 + 2] == Pattern.DIGIT:
            return False  # Extra digits expected
        elif pattern[ptr2:ptr2 + 2] == Pattern.ALNUM:
            return False  # Extra alphanumeric expected
        ptr2 += 1

    return ptr1 == len(input_line)  # Ensure all input_line is consumed

def main():
    if len(sys.argv) != 3:
        print("Usage: ./your_program.sh -E <pattern>")
        exit(1)

    pattern = sys.argv[2]
    input_line = sys.stdin.read().strip()
    
    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)

if __name__ == "__main__":
    main()