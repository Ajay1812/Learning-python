import sys
from sayings import hello,goodbye

if len(sys.argv) != 2:
    sys.exit()
else:
    goodbye(sys.argv[1])
