#!/usr/bin/env python3
import sys


def main() -> None:
    """Process scores from command-line and calculate analytics"""
    scores: list[int] = []
    print("=== Player Score Analytics ===")
    for i in range(1, len(sys.argv)):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
    if len(scores) == 0:
        print(
            f"No scores provided. Usage: python3 "
            f"{sys.argv[0]} <score1> <score2> ..."
        )
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
