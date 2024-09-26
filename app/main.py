import sys

class Pattern:
    DIGIT = r"\d"  # Use raw strings to avoid warnings
    ALNUM = r"\w"

def match_pattern(input_line, pattern):
    input_index = 0  # Pointer for input_line
    pattern_index = 0  # Pointer for pattern

    while pattern_index < len(pattern):
        print(f"Matching input: '{input_line[input_index:]}' with pattern: '{pattern[pattern_index:]}'")

        # If we reached the end of the input but still have a pattern left to match
        if input_index >= len(input_line):
            print(f"Input exhausted but pattern remains: '{pattern[pattern_index:]}'")
            return False

        # Match digits
        if pattern[pattern_index:pattern_index + 2] == Pattern.DIGIT:
            # Look for a digit anywhere in the remaining input
            found_digit = False
            while input_index < len(input_line):
                if input_line[input_index].isdigit():
                    found_digit = True
                    input_index += 1  # Move past the digit
                    pattern_index += 2  # Move past the \d in pattern
                    break
                input_index += 1  # Move to next character in input

            if not found_digit:
                print("No matching digit found.")
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

    # Check if we have consumed the entire input
    if pattern_index == len(pattern) and input_index <= len(input_line):
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