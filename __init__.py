# -*- coding: utf-8 -*-
"""
/***************************************************************************
 spa
                                 A QGIS plugin
 Spatial Data Analysis
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-07-05
        copyright            : (C) 2021 by Javier Arellano-Verdejo
        email                : javier_arellano_verdejo@hotmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load spa class from file spa.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .spa import spa
    return spa(iface)
