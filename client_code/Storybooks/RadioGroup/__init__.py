from ._anvil_designer import RadioGroupTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RadioGroup(RadioGroupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    self.text_3.text = self.radio_group_1.selected_item

  def radio_button_1_click(self, **event_args):
    """This method is called when the component is selected."""
    print("changed")
