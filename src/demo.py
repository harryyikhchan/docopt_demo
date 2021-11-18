# author: Harry Chan
# date: 2021-11-18

"""This script prints out docopt args.
Usage: demo.py <arg1> --arg2=<arg2> [--arg3=<arg3>] [--arg4=<arg4>]
Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[--arg4=<arg4>]   Takes any value (this is an optional option)
"""

from docopt import docopt
opt = docopt(__doc__)
print(opt)
print(type(opt))
print(opt["--arg4"])