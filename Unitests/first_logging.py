import logging
import sys
import os

logger = logging.getLogger('MYFIRSTLOGS')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'apply.log')
file_handler = logging.FileHandler(filename, encoding='utf-8')
logger.addHandler(file_handler)
