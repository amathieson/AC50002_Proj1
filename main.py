# Upper Case 3 Letter
# Apostrophes are dropped, any other non-letter == space
# Must start with the same letter
# Must be unique
# Lower score is better
#   First letter of any word 0
#   Last Letter of any word 5 or 20 if E
#   1 + value for second letter of any word
#   2 + value for third letter of any word
#   3 + value for any other letter of any word
# Load all data
# Generate priority queues for each word's possible acronyms
# Dedupe using the score

import pathlib
import sys

import pandas as pd

from processor import algo
from tests import test


def main():
    file = input("Please enter a file name or ? for test mode: \x1b[1;2;4m")
    print("\x1b[0mLoading \x1b[1;33mData\x1b[0m...")
    try:
        letter_scores = pd.read_csv('values.txt', header=None, names=['letter', 'score'],
                                    sep="\s+", index_col=0)['score']
    except FileNotFoundError as e:
        print(f"\x1b[1;31mFailed to open {e.filename}!\x1b[0m")
        return -1
    processor = algo(letter_scores)
    if file == "?":
        test(processor)
        return 0
    else:
        try:
            filePath = pathlib.Path(file)
            output = filePath.parent.joinpath(f"MATHIESON_{filePath.stem}_abbrevs.txt")
            records = pd.read_csv(file, header=None, names=['record'])
        except FileNotFoundError as e:
            print(f"\x1b[1;31mFailed to open {e.filename}!\x1b[0m")
            return -1
        print(f"Loaded \x1b[1;33m{len(records)}\x1b[0m records")
        output_dict = processor.generate_set(records['record'])
        with open(output, 'w') as f:
            for key, value in output_dict.items():
                if value is not None:
                    f.write(f"{key}\n{' '.join(value)}\n")
                else:
                    f.write(f"{key}\n\n")
        print(f"Saved to \x1b[1;33m{output}\x1b[0m")
        return 0


if __name__ == '__main__':
    sys.exit(main())
