#!/usr/bin/env python3
import random


ACHIEVEMENTS: list[str] = [
    "Master Explorer", "Boss Slayer", "World Savior",
    "Collector Supreme", "Crafting Genius", "Untouchable",
    "Strategist", "Speed Runner", "Unstoppable", "Survivor",
    "Treasure Hunter", "First Steps", "Sharp Mind",
    "Hidden Path Finder"
]


def gen_player_achievements() -> set[str]:
    """Randomly assign achievements from the fixed list"""
    count: int = random.randint(4, len(ACHIEVEMENTS) - 2)
    return set(random.sample(ACHIEVEMENTS, count))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()

    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }
    all_achievements: set[str] = set(ACHIEVEMENTS)

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    sets: list[set[str]] = list(players.values())
    all_distinct: set[str] = sets[0].union(*sets[1:])
    common: set[str] = sets[0].intersection(*sets[1:])

    print()
    print(f"All distinct achievements: {all_distinct}")
    print()
    print(f"Common achievements: {common}")
    print()

    for name, achievements in players.items():
        others: set[str] = set().union(
            *[v for k, v in players.items() if k != name]
        )
        only: set[str] = achievements.difference(others)
        print(f"Only {name} has: {only}")

    print()
    for name, achievements in players.items():
        missing: set[str] = all_achievements.difference(achievements)
        print(f"{name} is missing: {missing}")
