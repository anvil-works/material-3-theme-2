from ._anvil_designer import InteractiveCardsTemplate
from anvil import *
import anvil.server

class InteractiveCards(InteractiveCardsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def full_outline_click(self, **event_args):
    alert("Clicked")
