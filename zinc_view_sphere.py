#!/usr/bin/python
"""
OpenCMISS-Zinc View Graphics tutorial example

A minimal graphical application that loads a model and views
graphics representing it.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
import sys
from PySide import QtGui
from zinc_view_graphics_ui import Ui_ZincViewGraphics

from opencmiss.zinc.context import Context as ZincContext
from opencmiss.zinc.field import Field
from opencmiss.zinc.glyph import Glyph
from opencmiss.zinc.material import Material
from opencmiss.zinc.status import OK as ZINC_OK

class ZincViewGraphics(QtGui.QMainWindow):
    '''
    Create a subclass of QWidget for our application.  We could also have derived this 
    application from QMainWindow to give us a menu bar among other things, but a
    QWidget is sufficient for our purposes.
    '''

    # ZincViewGraphics__init__ start
    def __init__(self, parent=None):
        '''
        Initialise the ZincViewGraphics first calling the QMainWindow __init__ function.
        '''
        QtGui.QMainWindow.__init__(self, parent)

        # create instance of Zinc Context from which all other objects are obtained
        self._context = ZincContext("ZincViewGraphics");

        # set up standard materials for colouring graphics
        self._context.getMaterialmodule().defineStandardMaterials()
        # set up standard glyphs, graphics to show at points e.g. spheres, arrows
        self._context.getGlyphmodule().defineStandardGlyphs()

        # Load the user interface controls
        self._ui = Ui_ZincViewGraphics()
        self._ui.setupUi(self)
        self._makeConnections()
        # Must pass the Context to the Zinc SceneviewerWidget
        self._ui.sceneviewerWidget.setContext(self._context)
        # must set other sceneviewer defaults once graphics are initialised
        self._ui.sceneviewerWidget.graphicsInitialized.connect(self._graphicsInitialized)

        # read the model and create some graphics to see it:
        self.setupModel()
        # ZincViewGraphics__init__ end

    def _graphicsInitialized(self):
        '''
        Callback for when SceneviewerWidget is initialised
        Needed since Sceneviewer is not fully constructed in __init__
        '''
        # use a white background instead of the default black
        sceneviewer = self._ui.sceneviewerWidget.getSceneviewer()
        sceneviewer.setBackgroundColourRGB([1.0, 1.0, 1.0])

    # _makeConnections start
    def _makeConnections(self):
        self._ui.customButton.clicked.connect(self.customButtonClicked)
        self._ui.viewAllButton.clicked.connect(self.viewAllButtonClicked)
        # _makeConnections end
        
    # setupModel start
    def setupModel(self):
        region = self._context.getDefaultRegion()

        # read the model file
        region.readFile('out_sphere.ex2')

        # define fields calculated from the existing fields to use for visualisation
        # starting with a scalar field giving the magnitude
        fieldmodule = region.getFieldmodule()
        coordinates = fieldmodule.findFieldByName('coordinates')

        scene = region.getScene()
        scene.beginChange()
        materialmodule = self._context.getMaterialmodule()

        # view the 1-D line elements on the edges of the cube
        lines = scene.createGraphicsLines()
        lines.setCoordinateField(coordinates)
        # default material is white, so choose black to view on white background
        black = materialmodule.findMaterialByName('black')
        lines.setMaterial(black)

        # view coordinate axes at the origin
        axes = scene.createGraphicsPoints()
        axes.setFieldDomainType(Field.DOMAIN_TYPE_POINT)
        pointAttr = axes.getGraphicspointattributes()
        pointAttr.setGlyphShapeType(Glyph.SHAPE_TYPE_AXES_XYZ)
        pointAttr.setBaseSize([1.2])
        blue = materialmodule.findMaterialByName('blue')
        axes.setMaterial(blue)

        # view the nodes at the corners of the cube as green spheres
        nodepoints = scene.createGraphicsPoints()
        nodepoints.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
        nodepoints.setCoordinateField(coordinates)
        pointAttr = nodepoints.getGraphicspointattributes()
        pointAttr.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)
        pointAttr.setBaseSize([0.05])
        green = materialmodule.findMaterialByName('green')
        nodepoints.setMaterial(green)

        scene.endChange()
        # setupModel end

    # customButtonClicked start
    def customButtonClicked(self):
        tessellationmodule = self._context.getTessellationmodule()
        fineTessellation = tessellationmodule.findTessellationByName('fine')
        result, divisions = fineTessellation.getMinimumDivisions(1)
        if result == ZINC_OK:
            divisions = divisions*2
            if divisions > 100:
                divisions = 1
            fineTessellation.setMinimumDivisions(divisions)
        # customButtonClicked end

    def viewAllButtonClicked(self):
        self._ui.sceneviewerWidget.getSceneviewer().viewAll()

# main start
def main():
    '''
    The entry point for the application, handle application arguments and initialise the 
    GUI.
    '''
    
    app = QtGui.QApplication(sys.argv)

    w = ZincViewGraphics()
    w.show()

    sys.exit(app.exec_())
# main end

if __name__ == '__main__':
    main()
