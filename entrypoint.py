#!/usr/bin/env python3
import sys
from cb_client import runners


def main():
    runner = runners.Geekbench4Runner()
    while 1:
        runner.run()


if __name__ == '__main__':
    main()
