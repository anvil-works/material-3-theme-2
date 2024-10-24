from ._anvil_designer import TextInputsTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class TextInputs(TextInputsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_field_1_copy_2_click(self, **event_args):
    alert("clicked outlined style")

  def text_field_1_click(self, **event_args):
    alert("clicked filled style")

  def text_field_1_copy_2_copy_3_icon_click(self, **event_args):
    """This method is called when the trailing icon is clicked."""
    alert("hello")
