from ._anvil_designer import menu_testpageTemplate
from anvil import *
import plotly.graph_objects as go

class menu_testpage(menu_testpageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(self.checkbox_1.selected)

