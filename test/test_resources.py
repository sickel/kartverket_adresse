# coding=utf-8
"""Resources test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'morten@sickel.net'
__date__ = '2022-10-28'
__copyright__ = 'Copyright 2022, Morten Sickel'

import unittest

from qgis.PyQt.QtGui import QIcon



class KartverketAdresseDialogTest(unittest.TestCase):
    """Test rerources work."""

    def setUp(self):
        """Runs before each test."""
        pass

    def tearDown(self):
        """Runs after each test."""
        pass

    def test_icon_png(self):
        """Test we can click OK."""
        path = ':/plugins/KartverketAdresse/icon.png'
        icon = QIcon(path)
        self.assertFalse(icon.isNull())

if __name__ == "__main__":
    suite = unittest.makeSuite(KartverketAdresseResourcesTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)



