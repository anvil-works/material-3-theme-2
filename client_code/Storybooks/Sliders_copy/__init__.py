from ._anvil_designer import Sliders_copyTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server

class Sliders_copy(Sliders_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def slider_4_change(self, **event_args):
    """This method is called when the value of the component is changed"""
    print(self.slider_4.value)

  def button_1_click(self, **event_args):
    """This method is called when the component is clicked."""
    print(type(self.slider_7.value))

  def slider_1_change(self, **event_args):
    """This method is called when the value of the component is changed"""
    print(self.slider_1.value)
    print(self.slider_1.dom_nodes['anvil-m3-slider-input'].value)