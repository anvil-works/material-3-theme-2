from ._anvil_designer import ToggleIconButtonsTemplate
from anvil import *
import anvil.server

class ToggleIconButtons(ToggleIconButtonsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
