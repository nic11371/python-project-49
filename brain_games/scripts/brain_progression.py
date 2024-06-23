#!/usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.progression import logic_function, RULE


def main():
    engine(logic_function, RULE)


if __name__ == '__main__':
    main()
