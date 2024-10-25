from ._anvil_designer import SlidersTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server

class Sliders(SlidersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def slider_4_change(self, **event_args):
    """This method is called when the value of the component is changed"""
    print(self.slider_4.value)
