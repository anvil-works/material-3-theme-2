from ._anvil_designer import TestPageTemplate
from anvil import *
import plotly.graph_objects as go

class TestPage(TestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def menu_item_1_click(self, **event_args):
    alert("YOU CLICKED THE ITEM! IT'S A PERSON!")

  def menu_item_2_click(self, **event_args):
    alert("YOU CLICKED THE ITEM! IT'S PEOPLE!")

  def button_1_click(self, **event_args):
    """This method is called when the component is clicked"""
    self.button_menu_combined_1.place_shield()


  

  