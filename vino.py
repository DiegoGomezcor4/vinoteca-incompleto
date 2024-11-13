from entidadvineria import EntidadVineria
from vinoteca import Vinoteca

class Vino(EntidadVineria):
    def __init__(self, id, nombre, bodega, cepas, partidas):
        super().__init__(id, nombre)
        self.bodega = bodega
        self.cepas = cepas
        self.partidas = partidas
        
    """para devolver la bodega que produce el vino y las cepas con las que se elabora."""
    
    def obtener_bodega(self):
        """Devuelve la bodega a la que pertenece el vino."""
        return self.bodega

    def obtener_cepa(self):
        """Devuelve la lista de cepas asociadas al vino."""
        return self.cepas