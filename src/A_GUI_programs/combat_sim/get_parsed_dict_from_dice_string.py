import re


def get_parsed_dict_from_dice_string(dice_string):
    """
    Turns a dice-notation string like:
        "1d20 + 1d12 + 1d10 + 1d8 + 1d6 + 1d4 + 4"
    into a dict like:
        {
            20: 1,
            12: 1,
            10: 1,
            8: 1,
            6: 1,
            4: 1,
            "constant": 4
        }

    - keys are the die's side-count (e.g. 20 for a d20), values are how many
      of that die appear.
    - if the same die size shows up more than once (e.g. "2d6 + 1d6"), their
      counts are added together rather than one overwriting the other.
    - a bare number with no "d" in it (e.g. the trailing "+ 4") is treated as
      the flat "constant" modifier. Multiple bare numbers get summed into
      "constant" too.
    - handles "+" and "-" between terms (e.g. "1d8 - 2" subtracts 2 from
      the constant; "1d8 - 1d4" subtracts a count, in the rare case that's
      meaningful for your use case).

    claude made this.
    i'd sooner eat glue than mess around with regex blud.
    """
    result = {}

    # split on + or -, keeping the sign attached to each term
    # e.g. "1d20 + 1d12 - 4" -> ["1d20", "+1d12", "-4"]
    terms = re.findall(r"[+-]?\s*\d*d\d+|[+-]?\s*\d+", dice_string.replace(" ", ""))

    for term in terms:
        term = term.replace(" ", "")
        sign = -1 if term.startswith("-") else 1
        term = term.lstrip("+-")

        if "d" in term:
            count_str, sides_str = term.split("d")
            count = int(count_str) if count_str != "" else 1
            sides = int(sides_str)
            result[sides] = result.get(sides, 0) + (sign * count)
        else:
            constant = int(term)
            result["constant"] = result.get("constant", 0) + (sign * constant)

    return result


if __name__ == "__main__":
    example = "1d20 + 1d12 + 1d10 + 1d8 + 1d6 + 1d4 + 4"
    print(get_parsed_dict_from_dice_string(example))
    # {20: 1, 12: 1, 10: 1, 8: 1, 6: 1, 4: 1, 'constant': 4}

    example2 = "2d6 + 1d6 + 3"
    print(get_parsed_dict_from_dice_string(example2))
    # {6: 3, 'constant': 3}   <- counts for the same die size get combined