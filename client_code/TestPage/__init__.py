from ._anvil_designer import TestPageTemplate
from anvil import *
import plotly.graph_objects as go

class TestPage(TestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def radio_button_1_click(self, **event_args):
    self.label_1.text = self
    
  def radio_button_2_click(self, **event_args):
    pass
    
  def radio_button_3_click(self, **event_args):
    pass


  

  




