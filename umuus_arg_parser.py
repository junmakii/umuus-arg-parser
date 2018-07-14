"""A simple argument parser.

Example
-------

    $ python umuus_arg_parser.py -a.b.c 1 -a.b.d 2
    {'a': {'b': {'d': '2', 'c': '1'}}}

    >>> import umuus_arg_parser

    >>> umuus_arg_parser.parse(('-a.b', '1', '-a.c', '1'))
    {'a': {'c': 1, 'b': 1}}

"""
import sys
import re
import json
import umuus_dict_util
__version__ = '0.1'
__url__ = 'https://github.com/junmakii/{0}'.format(__name__)
__author__ = 'Jun Makii'
__author_email__ = 'junmakii@gmail.com'
__keywords__ = []
__license__ = 'GPLv3'
__scripts__ = []
__install_requires__ = [
    'umuus_dict_util',
]
__classifiers__ = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
]
__entry_points__ = {'console_scripts': ['{0} = {0}:main'.format(__name__)]}



def parse(a):
    args_dict = dict(zip(map(lambda _: re.sub('^-+', '', _), a[0:None:2]), a[1:None:2]))
    return umuus_dict_util.from_paths(args_dict)

def main(argv=[]):
    a = (argv or sys.argv)[1:]
    option = parse(a)
    print(json.dumps(option))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
