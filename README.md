
umuus_arg_parser
================

A simple argument parser.

Example
-------

    $ python umuus_arg_parser.py -a.b.c 1 -a.b.d 2
    {'a': {'b': {'d': '2', 'c': '1'}}}

    >>> import umuus_arg_parser

    >>> umuus_arg_parser.parse(('-a.b', '1', '-a.c', '1'))
    {'a': {'c': '1', 'b': '1'}}



Author
------

Jun Makii <junmakii@gmail.com>

License
-------

GPLv3
