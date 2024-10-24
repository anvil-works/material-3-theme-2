from ._anvil_designer import ButtonMenuFUITemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from anvil.js import get_dom_node

class ButtonMenuFUI(ButtonMenuFUITemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    lp = get_dom_node(self.linear_panel_1)
    lp.style.height = "70vh"
    lp.style.overflow = "scroll"

    # Any code you write here will run before the form opens.
