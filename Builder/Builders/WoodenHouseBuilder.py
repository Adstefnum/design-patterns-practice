from ..BuilderFactoryInterface import BuilderFactory

class woodenHouseBuilder(BuilderFactory):

  def buildFoundation()->str:
    return "Wooden Foundation built"


  def buildWalls()->str:
    return "Wooden Walls built"


  def buildRooms()->str:
    return "Wooden Rooms furnished"


  def buildDoors()->str:
    return "Wooden Victorian Doors built"


  def buildWindows()->str:
    "Haha of course we used glass windows"


  def buildRoof()->str:
    return "Wooden roof put up"


  def buildSwimmingPool()->str:
    "No swimming pool for this wooden house"
