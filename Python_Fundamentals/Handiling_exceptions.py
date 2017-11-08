'''Exeptions and controll flow'''
import sys
from math import log

def convert(s):
    x = -1
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print('Conversion error: {}'\
              .format(str(e)),
              file=sys.stderr)
        raise


def string_log(s):
    v = convert(s)
    return log(v)

