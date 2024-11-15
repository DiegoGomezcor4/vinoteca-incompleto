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

    def buscarBodega(id):
        pass  # completar

    def buscarCepa(id):
        pass  # completar

    def buscarVino(id):
        pass  # completar

    def __parsearArchivoDeDatos():
        pass  # completar

    def __convertirJsonAListas(lista):
        pass  # completar
