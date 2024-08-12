from ._anvil_designer import DropdownsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Dropdowns(DropdownsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


    # Any code you write here will run before the form opens.

  def text_field_1_trailing_icon_click(self, **event_args):
    """This method is called when the trailing icon is clicked."""
    print("blah blah blah")
