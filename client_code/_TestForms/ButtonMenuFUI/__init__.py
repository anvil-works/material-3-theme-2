from anvil import *
from anvil.js import get_dom_node

from ._anvil_designer import ButtonMenuFUITemplate


class ButtonMenuFUI(ButtonMenuFUITemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    lp = get_dom_node(self.linear_panel_1)
    lp.style.height = "70vh"
    lp.style.overflow = "scroll"

    # Any code you write here will run before the form opens.
