# coding: utf-8
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='umuus_arg_parser',
    description='A simple argument parser.',
    long_description=('A simple argument parser.\n'
 '\n'
 'Example\n'
 '-------\n'
 '\n'
 '    $ python umuus_arg_parser.py -a.b.c 1 -a.b.d 2\n'
 "    {'a': {'b': {'d': '2', 'c': '1'}}}\n"
 '\n'
 '    >>> import umuus_arg_parser\n'
 '\n'
 "    >>> umuus_arg_parser.parse(('-a.b', '1', '-a.c', '1'))\n"
 "    {'a': {'c': '1', 'b': '1'}}\n"
 '\n'),
    packages=setuptools.find_packages('.') + [
        os.path.join(root, dir)
        for path in os.listdir('.')
        if os.path.isdir(path)
        and not path.startswith('.')
        and path not in ['pip-egg-info', 'build', 'dist']
        for root, dirs, files in os.walk(path)
        for dir in dirs if not dir.startswith('.')],
    package_data={
        '': ['*']
    },
    include_package_data=True,
    zip_safe=False,
    py_modules=['umuus_arg_parser'],
    version='0.1',
    url='https://github.com/junmakii/umuus_arg_parser',
    author='Jun Makii',
    author_email='junmakii@gmail.com',
    keywords=[],
    license='GPLv3',
    scripts=[],
    install_requires=['umuus_dict_util'],
    classifiers=['Intended Audience :: Developers',
 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
 'Natural Language :: English',
 'Programming Language :: Python',
 'Programming Language :: Python :: 3'],
    entry_points={'console_scripts': ['umuus_arg_parser = umuus_arg_parser:main']},
)