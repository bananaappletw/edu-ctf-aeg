#!/usr/bin/env python
import angr
import logging

logging.getLogger('simuvex.vex.irsb').setLevel(logging.ERROR)

proj = angr.Project('./angrman.out', load_options={'auto_load_libs':False})
exitangr = 0x400627
end = 0x400d2b

ex = proj.surveyors.Explorer(find=(end,),
                                 avoid=(exitangr,),
                                 enable_veritesting=True)

ex.run()

if ex.found:
	print ex.found[0].state.posix.dumps(0)
