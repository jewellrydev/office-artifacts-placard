#!/usr/bin/env python3
"""Stapler of the Binding Court — entry for Office Artifacts: The One-Line Placard Contest on make.fun.

Prints exactly one line: a museum placard for an ordinary office object,
written as if it were an ancient artifact from a lost civilisation.
"""

LINE = "Stapler of the Binding Court (brass age): priests used it to fasten offerings of paper before the Great Shredding began."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()
