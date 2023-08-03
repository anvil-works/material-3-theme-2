from ._anvil_designer import ButtonMenuTemplate
from anvil import *

class ButtonMenu(ButtonMenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def toggle_menu_visibility(self, **event_args):
    classes = self.dom_nodes['anvil-m3-buttonMenu-items-container']
    
    self._disabled = value
    card = self.dom_nodes['anvil-m3-card']
    classes = card.classList
    classes.toggle('anvil-m3-disabled', value)