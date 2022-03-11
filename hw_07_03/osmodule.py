# למצוא 2 פקודות שונות של מודול os
import os


# returns cpu count
def cpu_count():
    return os.cpu_count()


# returns the name of your opreating system
def op_name():
    if os.name == 'nt':
        return 'Windows'
    return os.name
