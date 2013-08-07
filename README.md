christieSplus16 v0.1
====================

python module to communicate with christie roadster S+16 projectors. 
Version 0.1 can get lamp and temperature data.


### usage:

import christieSplus16 as projector


*// create projector instance with projector(HOST, PORT)*

**pr1 = projector("192.168.0.8", 3002)**

*// get all Lamp data as Dictionary*

**print pr1.getLampInfo()**

*// get lamp hours data as integer*

**print pr1.getLampInfo()["LampHours"]**



*// get all temperature data as Dictionary*

**print pr1.getTemperatures()**

*// get red DMD temperature as integer*

**print pr1.getTemperatures()["red"]**



