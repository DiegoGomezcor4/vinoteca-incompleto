from entidadvineria import EntidadVineria
#from vinoteca import Vinoteca

class Bodega(EntidadVineria):
    
    def __init__(self, id: str, nombre: str, vinos=None):
        super().__init__(id, nombre)  # Llama al constructor de la clase base correctamente.
        self.__vinos = vinos if vinos is not None else []  # Inicializa la lista de vinos.

    
    """devuelven listas de vinos y cepas asociadas a la bodega."""
    def obtenerVinos(self):
        return [vino for vino in Vinoteca.obtenerVinos() if vino.bodega == self.id]
    
    def obtenerCepas(self):
        cepas = set()
        for vino in self.obtenerVinos():
            cepas.update(vino.cepas)
        return list(cepas)

