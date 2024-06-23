#!/usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.calc import do_calculate, RULE


def main():
    engine(do_calculate, RULE)


if __name__ == '__main__':
    main()
