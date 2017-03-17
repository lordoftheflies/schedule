"""
Publish a new version:

$ git tag X.Y.Z -m "Release X.Y.Z"
$ git push --tags

$ pip install --upgrade twine wheel
$ python setup.py sdist bdist_wheel
$ twine upload dist/*
"""
import codecs
import os
import sys
from setuptools import setup


SCHEDULE_VERSION = '0.5.2'
SCHEDULE_DOWNLOAD_URL = (
    'https://github.com/lordoftheflies/cronlikescheduler/tarball/' + SCHEDULE_VERSION
)

def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, 'r', 'utf8') as f:
        return f.read()

setup(
    name='cronlikescheduler',
    packages=['schedule'],
    version=SCHEDULE_VERSION,
    description='Job scheduling for humans.',
    long_description=read_file('README.rst'),
    license='MIT',
    author='Daniel Bader',
    author_email='mail@dbader.org',
    url='https://github.com/lordoftheflies/cronlikescheduler',
    download_url=SCHEDULE_DOWNLOAD_URL,
    keywords=[
        'schedule', 'periodic', 'jobs', 'scheduling', 'clockwork', 'cron'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
    ],
)
