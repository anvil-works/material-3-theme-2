from ._anvil_designer import CheckboxTemplate
from anvil import *
import anvil.server

class Checkbox(CheckboxTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.checkbox_3.checked = None
    self.checkbox_5.checked = None
    self.checkbox_9.checked = None

    # Any code you write here will run before the form opens.
