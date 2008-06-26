
import sys,os
if os.path.exists(os.path.join(sys.path[0], 'larvotto.py')):
	 del sys.path[0]

import larvotto
print larvotto.__file__
from larvotto.commandline import main

main()
