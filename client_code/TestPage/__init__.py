from ._anvil_designer import TestPageTemplate
from anvil import *
import plotly.graph_objects as go

class TestPage(TestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.indeterminate_checkbox_1.checked = None

    # Any code you write here will run before the form opens.
  



    




