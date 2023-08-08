from ._anvil_designer import menu_test_pageTemplate
from anvil import *

class menu_test_page(menu_test_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
