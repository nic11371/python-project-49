#!/usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.prime import checked_prime, RULE


def main():
    engine(checked_prime, RULE)


if __name__ == '__main__':
    main()
