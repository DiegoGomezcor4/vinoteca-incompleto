from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    """constructor"""
    def __init__(self,id: str, nombre: str):
        self._id : str = id               # atributo protegido
        self._nombre : str = nombre       # atributo protegido
    
    """comandos"""    
    def establecerNombre(self, nombre: str) -> None:
        self._nombre = nombre
     
    """consultas"""   
    @abstractmethod
    def obtenerId(self) -> str:
        """Metodo abstracto para obtener el ID"""
        return self._id
    
    def obtenerNombre(self) -> str:
        return self._nombre
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, EntidadVineria) and self._id == other._id