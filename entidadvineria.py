"""entidadvineria.py, bodega.py, cepa.py, vino.py: Cada archivo contiene la clase que representa una
entidad específica. EntidadVineria es la clase base abstracta que define atributos comunes a bodegas, 
cepas y vinos"""

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