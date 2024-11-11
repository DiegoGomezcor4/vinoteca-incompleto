from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    def __init__(self, nombre):
        self._id = id               # atributo protegido
        self._nombre = nombre       # atributo protegido
        
    def establecerNombre(self, nombre):
        self._nombre = nombre
        
    @abstractmethod
    def obtenerId(self):
        """Metodo abstracto para obtener el ID"""
        return self._id
    
    def obtenerNombre(self):
        return self._nombre
    
    def __eq__(self, other):
        return isinstance(other, EntidadVineria) and self._id == other._id