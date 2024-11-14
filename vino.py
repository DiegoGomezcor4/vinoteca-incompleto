from entidadvineria import EntidadVineria
from vinoteca import Vinoteca

class Vino(EntidadVineria):
    # Atributos de clase
    vinoteca = Vinoteca() # Instancia de Vinoteca para buscar bodegas y cepas
    
    # Constructor
    def __init__(self, id, nombre, bodega, cepas, partidas):
        super().__init__(id, nombre)
        self._bodega = bodega        # Nombre de la bodega
        self._cepas = cepas          # Lista de nombres de cepas
        self._partidas = partidas    # Lista de partidas (int)
        
    """para devolver la bodega que produce el vino y las cepas con las que se elabora."""
    
    # Comandos
    def establecerBodega(self, bodega):
        """Establece el nombre de la bodega del vino"""
        self._bodega = bodega
    
    def establecerPartidas(self, partidas):
        """Establece la lista de partidas asociadas al vino"""
        self._partidas = partidas
        
        
        
    # consultas
    
    def obtenerId(self):
        """Devuelve el ID del vino"""
        return self._id
    
    def obtenerBodega(self):
        """Devuelve el objeto de tipo Bodega asociado al vino"""
        return self.vinoteca.buscarBodega(self._bodega)
    
    def obtenerCepas(self):
        """Devuelve una lista de objetos de tipo Cepa asociados al vino."""
        return [self.vinoteca.buscarCepa(cepa) for cepa in self._cepas]
    
    def obtenerPartidas(self):
        """Devuelve la lista de partidas asociadas al vino"""
        return self._partidas
    
    def convertirAJSON(self):
        """Convierte los atributos básicos del vino a un diccionario Json"""
        return {
            "id": self._id,
            "nombre": self._bodega,
            "bodega": self._cepas,
            "partidas": self._partidas
        }
        
    def convertirAJSONFull(self):
        """Convierte todos los detalles del vino a un diccionario Json, incluyendo bodega y cepas completas"""
        return {
            "id": self._id,
            "nombre": self._nombre,
            "bodega": self.obtenerBodega(), #Objeto completo de Bodega
            "cepas": [cepa for cepa in self.obtenerCepas()], #Lista de objetos de Cepa
            "partidas": self._partidas
        }      