from ._anvil_designer import DropdownMenuTemplate
from anvil import HtmlTemplate
from anvil import *
from ...Functions import underline_property, italic_property, style_property, color_property, innerText_property, bold_property, font_size_property

class DropdownMenu(DropdownMenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  visible = HtmlTemplate.visible
    