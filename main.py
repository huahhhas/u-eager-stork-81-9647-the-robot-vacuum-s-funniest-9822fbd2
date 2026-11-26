"""The Robot Vacuum's Funniest Excuse — a make.fun one-line entry.

A robot vacuum explains why it missed a spot.

The program writes the line to /output/entry.txt (the artifact the
grader reads) and prints it to stdout.
"""

import os

LINE = "I didn't miss that spot — the dust bunny unionised, and I respect a picket line."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
