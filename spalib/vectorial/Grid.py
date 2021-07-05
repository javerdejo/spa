"""
    author: Javier Arellano-Verdejo
    mail: javier_arellano_verdejo@hotmail.com
    date: july/2021

    use:
    import spa.vectorial.Grid as grd
"""

from qgis import processing
from qgis.core import QgsProcessing

class Grid:

    def makeGrid(input_layer, pixel_length):
        # Parametros
        params = {
            'CRS': 'ProjectCrs',
            'EXTENT': input_layer,
            'HOVERLAY': 0,
            'HSPACING': int(pixel_length),
            'TYPE': 2,
            'VOVERLAY': 0,
            'VSPACING': int(pixel_length),
            'OUTPUT' : QgsProcessing.TEMPORARY_OUTPUT
        }

        # ejecuta el algoritmo
        result = processing.run("native:creategrid", params)

        # parametros para recortar la cuadricula
        # Extraer por ubicacion 
        params = {
            'INPUT': result['OUTPUT'],
            'INTERSECT': input_layer,
            'PREDICATE': [0],
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }

        # ejecuta el algoritmo
        result = processing.run("native:extractbylocation", params)

        # muestra la capa resultante
        return result['OUTPUT']
