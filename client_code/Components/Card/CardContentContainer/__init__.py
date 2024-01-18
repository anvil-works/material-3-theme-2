from ._anvil_designer import CardContentContainerTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.designer

class CardContentContainer(CardContentContainerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    if not anvil.designer.in_designer:
      self.dom_nodes['empty-slot'].style.display = "none"

    # Any code you write here will run before the form opens.
