from entidadvineria import EntidadVineria
from vinoteca import Vinoteca

class Cepa(EntidadVineria):
    def obtenerVinos(self):
        return [vino for vino in Vinoteca.obtenerVinos() if self.id in vino.cepas]
    
    