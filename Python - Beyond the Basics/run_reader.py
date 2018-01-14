__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

'''Befor adding reader to the __init__'''
# import reader.reader as rr
# rr.__file__

# r = rr.Reader('reader/reader.py')
# print(r.read())
# r.close()

'''After adding reader to the __init__'''
# import reader
# r = reader.Reader('reader/__init__.py')
# print(r.read())
# r.close()

'''After adding compressed module'''
# import reader
# import reader.compressed
# import reader.compressed.gzipped
# import reader.compressed.bzipped

'''After adding the zipped files'''
# import reader
# r = reader.Reader('reader/compressed/test.bz2')
# print(r.read())
# r.close()
#
# r = reader.Reader('reader/compressed/test.gz')
# print(r.read())
# r.close()
#
# r = reader.Reader('reader/__init__.py')
# print(r.read())
# r.close()

'''After creating an executable directory'''
# reader reader/__main__.py  # Run in IDLE