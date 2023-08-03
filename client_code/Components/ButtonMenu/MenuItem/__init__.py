from ._anvil_designer import MenuItemTemplate
from anvil import *

class MenuItem(MenuItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.dom_nodes['button'].addEventListener("click", self.handle_click)

  def handle_click(self, event):
    event.preventDefault()
    self.raise_event("click")

  
