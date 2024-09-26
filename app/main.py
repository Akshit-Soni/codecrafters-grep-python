import sys

# Define the class to hold patterns, using raw strings
class Pattern:
    DIGIT = r"\d"  # Use raw strings to avoid warnings
    ALNUM = r"\w"

def match_pattern(input_line, pattern):
    ptr1 = 0  # Pointer for input_line
    ptr2 = 0  # Pointer for pattern

    while ptr1 < len(input_line) and ptr2 < len(pattern):
        # Handle digit matching
        if pattern[ptr2:ptr2 + 2] == Pattern.DIGIT:
            if input_line[ptr1].isdigit():
                ptr1 += 1
                ptr2 += 2
            else:
                return False
        # Handle alphanumeric matching
        elif pattern[ptr2:ptr2 + 2] == Pattern.ALNUM:
            if input_line[ptr1].isalnum():
                ptr1 += 1
                ptr2 += 2
            else:
                return False
        # Handle character class
        elif pattern[ptr2] == "[":
            closing_bracket = pattern.find("]", ptr2)
            if closing_bracket == -1:  # No closing bracket found
                return False
            char_class = pattern[ptr2 + 1:closing_bracket]
            if char_class.startswith("^"):
                # Negative character class
                if input_line[ptr1] in char_class[1:]:  # Check if character is in the class
                    return False
            else:
                if input_line[ptr1] not in char_class:  # Regular character class
                    return False
            ptr1 += 1
            ptr2 = closing_bracket + 1  # Move past the closing bracket
        # Handle regular character matching
        elif pattern[ptr2] == input_line[ptr1]:
            ptr1 += 1
            ptr2 += 1
        else:
            return False

    # Ensure any remaining characters in the pattern are valid
    while ptr2 < len(pattern):
        if pattern[ptr2:ptr2 + 2] == Pattern.DIGIT:
            return False  # Extra digits expected
        elif pattern[ptr2:ptr2 + 2] == Pattern.ALNUM:
            return False  # Extra alphanumeric expected
        ptr2 += 1

    return ptr1 == len(input_line)  # Check if the entire input_line has been consumed

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