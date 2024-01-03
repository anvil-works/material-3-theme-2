from ._anvil_designer import TextInputTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Functions import property_without_callback

class TextInput(TextInputTemplate):
  def __init__(self, **properties):
    self._props = properties
    self.init_components(**properties)

  label_text = property_without_callback("label_text")
  supporting_text = property_without_callback("supporting_text")
  placeholder = property_without_callback("label_text")

    # Any code you write here will run before the form opens.
