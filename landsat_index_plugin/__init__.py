# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LandsatIndexPlugin
                                 A QGIS plugin
 Calculating indices
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-06-03
        copyright            : (C) 2025 by Pratibimb
        email                : iampratibimb07rc@gmail.com
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
    """Load LandsatIndexPlugin class from file LandsatIndexPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .landsat_index_plugin import LandsatIndexPlugin
    return LandsatIndexPlugin(iface)
