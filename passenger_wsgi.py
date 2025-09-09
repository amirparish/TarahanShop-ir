import os
import sys 
sys.path.insert(0, os.path.dirname(__file__))
import tarahanshop.wsgi as wsgi


application = wsgi.application