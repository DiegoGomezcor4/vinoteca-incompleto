from entidadvineria import EntidadVineria
from vinoteca import Vinoteca

class Bodega(EntidadVineria):
    
    """devuelven listas de vinos y cepas asociadas a la bodega."""
    def obtenerVinos(self):
        return [vino for vino in Vinoteca.obtenerVinos() if vino.bodega == self.id]
    
    def obtenerCepas(self):
        cepas = set()
        for vino in self.obtenerVinos():
            cepas.update(vino.cepas)
        return list(cepas)

