import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

class Pattern:
    DIGIT = r"\\d"
    ALNUM = r"\\w"

def match_pattern(input_line, pattern):
    if len(input_line) == 0 and len(pattern) == 0:
        return True
    if not pattern:
        return True
    if not input_line:
        return False
    
    # Check if the current pattern is a digit (\d)
    if pattern.startswith(Pattern.DIGIT):
        if input_line[0].isdigit():
            return match_pattern(input_line[1:], pattern[2:])
        else:
            return False
    
    # Check if the current pattern is an alphanumeric (\w)
    elif pattern.startswith(Pattern.ALNUM):
        if input_line[0].isalnum():
            return match_pattern(input_line[1:], pattern[2:])
        else:
            return False
    
    # Check for negative character groups like [^xyz]
    elif pattern.startswith("[^") and pattern.endswith("]"):
        excluded_chars = set(pattern[2:-1])
        if input_line[0] not in excluded_chars:
            return match_pattern(input_line[1:], pattern[3:])
        else:
            return False
    
    # Check for positive character groups like [abc]
    elif pattern.startswith("[") and pattern.endswith("]"):
        included_chars = set(pattern[1:-1])
        if input_line[0] in included_chars:
            return match_pattern(input_line[1:], pattern[3:])
        else:
            return False
    
    # Handle exact matches for other characters
    elif pattern[0] == input_line[0]:
        return match_pattern(input_line[1:], pattern[1:])
    
    else:
        # Move forward in input_line if no specific pattern matches
        return match_pattern(input_line[1:], pattern)

def main():
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