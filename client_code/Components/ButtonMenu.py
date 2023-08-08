from anvil import Container
from anvil.js import document

class ButtonMenu(Container):
  def __init__(self, **properties):
    self.dom_element = document.createElement("div")

  @property
  def _anvil_dom_element_(self):
    return self.dom_element

  

  