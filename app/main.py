import sys

class Pattern:
    DIGIT = r"\d"  # Use raw strings to avoid warnings
    ALNUM = r"\w"

def match_pattern(input_line, pattern):
    input_index = 0  # Pointer for input_line
    pattern_index = 0  # Pointer for pattern

    while pattern_index < len(pattern):
        print(f"Matching input: '{input_line[input_index:]}' with pattern: '{pattern[pattern_index:]}'")

        if input_index < len(input_line):
            # Match digits
            if pattern[pattern_index:pattern_index + 2] == Pattern.DIGIT:
                if input_line[input_index].isdigit():
                    input_index += 1
                    pattern_index += 2
                else:
                    print(f"Expected digit at input '{input_line[input_index]}', match failed.")
                    return False
            # Match alphanumeric characters
            elif pattern[pattern_index:pattern_index + 2] == Pattern.ALNUM:
                if input_line[input_index].isalnum():
                    input_index += 1
                    pattern_index += 2
                else:
                    print(f"Expected alphanumeric at input '{input_line[input_index]}', match failed.")
                    return False
            # Match regular characters
            elif pattern[pattern_index] == input_line[input_index]:
                input_index += 1
                pattern_index += 1
            else:
                print(f"Characters do not match: input '{input_line[input_index]}', pattern '{pattern[pattern_index]}'.")
                return False
        else:
            print(f"Input exhausted but pattern remains: '{pattern[pattern_index:]}'")
            return False

    # Check if we have consumed the entire input
    if input_index == len(input_line) and pattern_index == len(pattern):
        print("Full match found.")
        return True
    else:
        print("Pattern did not fully match input.")
        return False

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