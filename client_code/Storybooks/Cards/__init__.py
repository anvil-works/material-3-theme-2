from ._anvil_designer import CardsTemplate
from anvil import *
import anvil.server
from ...components import Switch

class Cards(CardsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


    # Any code you write here will run before the form opens.
