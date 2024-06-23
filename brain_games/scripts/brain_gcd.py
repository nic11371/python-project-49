#!/usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.gcd import found_divide, RULE


def main():
    engine(found_divide, RULE)


if __name__ == '__main__':
    main()
