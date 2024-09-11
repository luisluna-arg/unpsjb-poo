from enum import Enum

class TipoCartaEnum(Enum):
    BronceEspecial = 0
    Oro = 1
    Especial = 2
    
    @classmethod
    def values(cls):
        return [cls.BronceEspecial, cls.Oro, cls.Especial]