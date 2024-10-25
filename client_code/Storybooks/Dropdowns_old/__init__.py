from ._anvil_designer import Dropdowns_oldTemplate
from anvil import *
import anvil.server

class Dropdowns_old(Dropdowns_oldTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
