import os
import sys

sys.path.append('/home/')
sys.path.append('/home/practical-cm')
sys.path.append('/home/practical-cm/site')

def application(environ, start_response):
    from practical_cm.site.practical_cm import app as _application
    return _application(environ, start_response)