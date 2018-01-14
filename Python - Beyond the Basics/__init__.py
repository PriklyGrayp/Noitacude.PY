__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

from reader.compressed.bzipped import opener as bz2_opener
from reader.compressed.gzipped import opener as gz_opener

__all__ = ['bz2_opener', 'gz_opener']