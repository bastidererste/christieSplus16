christieSplus16 v0.1
====================

python module to communicate with christie roadster S+16 projectors.


### usage:

import christieSplus16 as projector

*// create projector instance with projector(HOST, PORT)*
pr1 = projector("192.168.0.8", 3002)

*// get all Lamp data as Dictionary*
print pr1.getLampInfo()

*// get lamp hours data as integer*
print pr1.getLampInfo()["LampHours"]



