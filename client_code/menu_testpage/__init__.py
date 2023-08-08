from ._anvil_designer import menu_testpageTemplate
from anvil import *
import plotly.graph_objects as go

class menu_testpage(menu_testpageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def menu_item_1_click(self, **event_args):
    print(self.menu_item_1.text)
    print("halp")

