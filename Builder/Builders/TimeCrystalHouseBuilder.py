from ..BuilderFactoryInterface import BuilderFactory

class TimeCrystalHouseBuilder(BuilderFactory):

  def buildFoundation()->str:
    return "TimeCrystal Foundation built"


  def buildWalls()->str:
    return "TimeCrystal Walls built"


  def buildRooms()->str:
    return "TimeCrystal Rooms furnished"


  def buildDoors()->str:
    return "TimeCrystal Victorian Doors built"


  def buildWindows()->str:
    "Haha of course we used glass windows"


  def buildRoof()->str:
    return "TimeCrystal roof put up"


  def buildSwimmingPool()->str:
    "No swimming pool for this TimeCrystal house"
