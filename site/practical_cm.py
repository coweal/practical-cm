import sys
import os
import time

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib'))
sys.path.append(os.path.abspath(os.getcwd()))    
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))


from meta import *
from views import *
from filters import *

if __name__ == "__main__":
    app.run()