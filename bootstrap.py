#!/usr/bin/env python

import sys
sys.path.insert(0, "src/main/python")

from isphere.command import VSphereREPL

VSphereREPL().cmdloop()
