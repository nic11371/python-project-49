#!/usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.even import checked_even, RULE


def main():
    engine(checked_even, RULE)


if __name__ == '__main__':
    main()
