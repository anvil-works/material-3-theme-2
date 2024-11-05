import anvil.server
from anvil import *

from ._anvil_designer import SidesheetContentTemplate


class SidesheetContent(SidesheetContentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
