import sys

class Pattern:
    DIGIT = r"\d"  # Use raw strings to avoid warnings
    ALNUM = r"\w"

def match_pattern(input_line, pattern):
    ptr1 = 0  # Pointer for input_line
    ptr2 = 0  # Pointer for pattern

    print(f"Starting match_pattern with input_line: '{input_line}' and pattern: '{pattern}'")

    while ptr1 < len(input_line) and ptr2 < len(pattern):
        print(f"Current input character: '{input_line[ptr1]}' at position {ptr1}, current pattern character: '{pattern[ptr2]}' at position {ptr2}")

        # Handle digit matching
        if pattern[ptr2:ptr2 + 2] == Pattern.DIGIT:
            print("Matching digit pattern")
            if input_line[ptr1].isdigit():
                ptr1 += 1
                ptr2 += 2
            else:
                print("Digit match failed")
                return False
        # Handle alphanumeric matching
        elif pattern[ptr2:ptr2 + 2] == Pattern.ALNUM:
            print("Matching alphanumeric pattern")
            if input_line[ptr1].isalnum():
                ptr1 += 1
                ptr2 += 2
            else:
                print("Alphanumeric match failed")
                return False
        # Handle character class
        elif pattern[ptr2] == "[":
            closing_bracket = pattern.find("]", ptr2)
            if closing_bracket == -1:  # No closing bracket found
                print("No closing bracket found for character class")
                return False
            char_class = pattern[ptr2 + 1:closing_bracket]
            if char_class.startswith("^"):
                print(f"Matching negative character class: {char_class}")
                if input_line[ptr1] in char_class[1:]:  # Check if character is in the class
                    print(f"Character '{input_line[ptr1]}' is in negative class, match failed")
                    return False
            else:
                print(f"Matching regular character class: {char_class}")
                if input_line[ptr1] not in char_class:  # Regular character class
                    print(f"Character '{input_line[ptr1]}' not found in class, match failed")
                    return False
            ptr1 += 1
            ptr2 = closing_bracket + 1  # Move past the closing bracket
        # Handle regular character matching
        elif pattern[ptr2] == input_line[ptr1]:
            print(f"Matching regular character: '{input_line[ptr1]}'")
            ptr1 += 1
            ptr2 += 1
        else:
            print(f"Characters do not match: '{input_line[ptr1]}' and '{pattern[ptr2]}', moving to next input character")
            return False

    # Ensure any remaining characters in the pattern are valid
    while ptr2 < len(pattern):
        if pattern[ptr2:ptr2 + 2] == Pattern.DIGIT:
            print("Extra digits expected, match failed")
            return False
        elif pattern[ptr2:ptr2 + 2] == Pattern.ALNUM:
            print("Extra alphanumeric expected, match failed")
            return False
        ptr2 += 1

    print("Match succeeded!" if ptr1 == len(input_line) else "Match failed!")
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

    print(f"Input line: '{input_line}', Pattern: '{pattern}'")
    
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)

if __name__ == "__main__":
    main()