"""vinoteca.py: Contiene la clase Vinoteca, que centraliza la lógica de consultas sobre el archivo JSON 
y provee métodos para buscar y filtrar bodegas, cepas y vinos"""

# librerias
import os
import json

# modelos
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino


class Vinoteca:

    __archivoDeDatos = "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []

    @staticmethod
    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)

    @staticmethod
    def obtenerBodegas(orden=None, reverso=False):
        bodegas = Vinoteca.__bodegas
        if isinstance(orden, str):
            if orden == "nombre":
                bodegas = sorted(bodegas, key=lambda b: b.obtenerNombre(), reverse=reverso)
            elif orden == "vinos":
                bodegas = sorted(bodegas, key=lambda b: len(b.obtenerVinos()), reverse=reverso )
        return bodegas

    @staticmethod
    def obtenerCepas(orden=None, reverso=False):
        cepas = Vinoteca.__cepas
        if isinstance(orden, str):
            if orden == "nombre":
                cepas = sorted(cepas, key=lambda c: c.obtener(), reverse=reverso)
        return cepas

    def obtenerVinos(anio=None, orden=None, reverso=False):
        vinos = Vinoteca.__vinos
        
        if isinstance(anio, int):
            vinos = [v for v in vinos if v.obtenerAnio() == anio]
        if isinstance(orden, str):
            if orden == "nombre":
                vinos = sorted(vinos, key=lambda v: v.obtenerNombre(), reverse=reverso)
            elif orden == "bodega":
                vinos = sorted(vinos, key=lambda v: v.obtenerBodega().obtenerNombre(), reverse=reverso)
            elif orden == "cepas":
                vinos = sorted(vinos, key=lambda v: len(v.obtenerCepas()), reverse=reverso)
        return vinos
    
    @staticmethod
    def buscarBodega(id):
        for bodega in Vinoteca.__bodegas:
            if bodega.obtenerId() == id:
                return bodega
        return None

    @staticmethod
    def buscarCepa(id):
        for cepa in Vinoteca.__cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None

    @staticmethod
    def buscarVino(id):
        for vino in Vinoteca.__vinos:
            if vino.obtenerId() == id:
                return vino
        return None

    @staticmethod
    def __parsearArchivoDeDatos():
        if not os.path.exists(Vinoteca.__archivoDeDatos):
            raise FileNotFoundError(f"No se encontró el archivo {Vinoteca.__archivoDeDatos}")

        with open(Vinoteca.__archivoDeDatos, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    @staticmethod
    def __convertirJsonAListas(lista):
        if "bodegas" in lista:
            Vinoteca.__bodegas = [Bodega(**b) for b in lista["bodegas"]]
        if "cepas" in lista:
            Vinoteca.__cepas = [Cepa(**c) for c in lista["cepas"]]
        if "vinos" in lista:
            Vinoteca.__vinos = [Vino(**v) for v in lista["vinos"]]
