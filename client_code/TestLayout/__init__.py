from ._anvil_designer import TestLayoutTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class TestLayout(TestLayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def navigation_link_1_click(self, **event_args):
    """This method is called when the component is clicked"""
    alert(title="Alert", content="You're on the home page!", buttons=["Continue", "Cancel"], role="")

