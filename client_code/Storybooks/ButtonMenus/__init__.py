from ._anvil_designer import ButtonMenusTemplate
from anvil import *
import anvil.server

class ButtonMenus(ButtonMenusTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def menu_item_5_click(self, **event_args):
    """This method is called when the component is clicked"""
    pass

