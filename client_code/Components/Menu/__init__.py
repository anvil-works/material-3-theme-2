from ._anvil_designer import MenuTemplate
from anvil import *

class Menu(MenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  @property
  def visible(self):
    return self._visible

  @visible.setter
  def visible(self, value)
    return self.