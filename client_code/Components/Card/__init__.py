from ._anvil_designer import CardTemplate
from anvil import *

class Card(CardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  @property
  def appearance(self):
    return self._appearance

  @appearance.setter
  def appearance(self, value):
    card = self.dom_nodes['card']
    if value:
      card.classList.add(value)

  