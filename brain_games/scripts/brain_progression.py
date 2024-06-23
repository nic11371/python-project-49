#!/usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.progression import make_progression, RULE


def main():
    engine(make_progression, RULE)


if __name__ == '__main__':
    main()
