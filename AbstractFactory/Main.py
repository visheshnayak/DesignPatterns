from WoodenDoor import WoodenDoor
from IronDoor import IronDoor
from Carpenter import Carpenter
from Welder import Welder

#declaring doors
wdoor = WoodenDoor(False)
idoor = IronDoor(False)

#declaring fixers
carp = Carpenter()
weld = Welder()

#check the decription
wdoor.get_description()
idoor.get_description()

#fix the doors
carp.fix_door(wdoor)
weld.fix_door(idoor)

#check the description after the action
wdoor.get_description()
idoor.get_description()