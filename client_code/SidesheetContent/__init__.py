from ._anvil_designer import SidesheetContentTemplate
from anvil import *
import anvil.server

#TODO: add to _Components
#TODO: in toolbox item yaml, add heading and icon button to appropriate slots as a composite component

class SidesheetContent(SidesheetContentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
