from ._anvil_designer import TestPage_copyTemplate
from anvil import *
import plotly.graph_objects as go

class TestPage_copy(TestPage_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(self.checkbox_1.selected)

    # Any code you write here will run before the form opens.

  def button_3_click(self, **event_args):
    """This method is called when the component is clicked"""
    alert("clicked button in elevated card")

  def group_a1_click(self, **event_args):
    self.label_5.text = self.radio_button_1.get_group_value()

  def group_t2_click(self, **event_args):
    self.label_6.text = self.radio_button_5.get_group_value()

  def group_qwer_click(self, **event_args):
    self.label_7.text = self.radio_button_8.get_group_value()
