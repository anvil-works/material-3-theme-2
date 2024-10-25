from ._anvil_designer import NavigationLinkTemplate
from anvil import *
import anvil.server

class NavigationLink(NavigationLinkTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
