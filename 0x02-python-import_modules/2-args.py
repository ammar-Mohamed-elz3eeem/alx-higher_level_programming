#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv = argv[1:]
    argc = len(argv)

    print("{:d} argument{:s}".format(argc, 's:' if
                                     argc > 1 else 's.' if argc == 0 else ':'))
    for i in range(argc):
        print("{:d}: {:s}".format(i + 1, argv[i]))
