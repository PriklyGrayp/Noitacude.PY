__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

import os
from reader.compressed import bzipped, gzipped


extention_map = {
    '.bz2' : bzipped.opener,
    '.gz' : gzipped.opener
}

class Reader:
    '''Reads files with file types'''
    def __init__(self, filename):
        ''''
        Args:
            filename = raw path to file
        '''
        extension = os.path.splitext(filename)[1]
        opener = extention_map.get(extension, open)
        self.f = opener(filename, 'rt')


    def close(self):
        self.f.close()


    def read(self):
        return self.f.read()