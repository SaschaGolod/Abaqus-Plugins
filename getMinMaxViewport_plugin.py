import os

import osutils
from abaqusConstants import ALL
from abaqusGui import *

###########################################################################
# Class definition
###########################################################################


class GetMinMaxViewport_plugin(AFXForm):

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):

        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(
            mode=self,
            method="getMinMaxViewport",
            objectName="pluginFuncions",
            registerQuery=False,
        )
        pickedDefault = ""

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import getMinMaxViewportDB

        return getMinMaxViewportDB.GetMinMaxViewportDB(self)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        #
        for kw1, kw2, d in self.radioButtonGroups.values():
            try:
                value = d[kw1.getValue()]
                kw2.setValue(value)
            except:
                pass
        return True

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Register the plug-in
#
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText="Get MinMax @ frames in Viewport",
    object=GetMinMaxViewport_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    kernelInitString="import pluginFuncions",
    # applicableModules=ALL,
    applicableModules=["Visualization"],
    version="1.0",
    author="Johannes Huber",
    description="N/A",
    helpUrl="N/A",
)
