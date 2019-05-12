import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import Module.ModuleTest.test

print Module.ModuleTest.test.pp()