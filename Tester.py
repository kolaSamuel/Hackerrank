"""
    Opens the hackerrank Amazon database to compare solutions so as to
    determine test case that is faulty.
"""

import urllib
opener = urllib.URLopener()


def tester(my_url):
    # my_file is  a haackerrank aws solution link
    myfile = opener.open(my_url)
    outfile = open('Test.txt', 'r')
