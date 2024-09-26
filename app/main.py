import sys

# import pyparsing
# import lark - available if you need it!

def check_next(input_line, pattern, offset_next):
    if (len(pattern) > offset_next + 1) and pattern[offset_next] == "+":
        return match_local(input_line, pattern[offset_next + 1 :]) or match_local(
            input_line, pattern
        )
    return match_local(input_line, pattern[offset_next:])

def check(predicate: bool, input_line: str, pattern: str, offset: int):
    is_optional = len(pattern) > offset + 1 and pattern[offset] == "?"
    if predicate:
        return check_next(
            input_line[1:], pattern, offset + 1 if is_optional else offset
        )
    else:
        return check_next(input_line, pattern, offset + 1) if is_optional else False


def match_local(input_line: str, pattern: str):
    if len(pattern) == 0:
        return True
    if len(input_line) == 0:
        return pattern == "$"
    if pattern.startswith("."):
        return check(True, input_line, pattern, 1)
    if pattern.startswith("\d"):
        return check(input_line[0].isdigit(), input_line, pattern, 2)
    elif pattern.startswith("\w"):
        return check(input_line[0].isalnum(), input_line, pattern, 2)
    elif pattern.startswith("[^") and "]" in pattern:
        chars = pattern[1 : pattern.index("]")]
        return check(
            input_line[0] not in chars, input_line, pattern, pattern.index("]") + 1
        )
    elif pattern.startswith("[") and "]" in pattern:
        chars = pattern[1 : pattern.index("]")]
        return check(
            input_line[0] in chars, input_line, pattern, pattern.index("]") + 1
        )
    elif pattern.startswith("(") and ")" in pattern:
        first, second = pattern[1 : pattern.index(")")].split("|")
        pattern_truncated = pattern[pattern.index(")") + 1 :]
        return match_local(input_line, first + pattern_truncated) or match_local(
            input_line, second + pattern_truncated
        )
    else:
        return check(pattern[0] == input_line[0], input_line, pattern, 1)
def match_pattern(input_line: str, pattern: str):
    if pattern[0] == "^":
        return match_local(input_line, pattern[1:])
    if match_local(input_line, pattern):
        return True
    else:
        truncated = input_line[1:]
        if len(truncated) == 0:
            return pattern == "$"
        return match_pattern(truncated, pattern)


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read().splitlines()[0]
    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()