from typing import Any

class WoodenHouse:

    def __init__(self)->None:
        self.parts = []

    def add(self,part:Any)->None:
        self.parts.append(part)

    def listParts(self)->None:
        print("\n".join(self.parts,))
