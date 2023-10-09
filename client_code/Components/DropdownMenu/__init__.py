from ._anvil_designer import DropdownMenuTemplate
from anvil import HtmlTemplate
from anvil import *
# from ...Functions import underline_property, italic_property, style_property, color_property, innerText_property, bold_property, font_size_property

class DropdownMenu(DropdownMenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  visible = HtmlTemplate.visible
  
  @property
  def enabled(self):
    return self._enabled
  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    self.text_field.enabled = value
  
  @property
  def font(self):
    return self._font
  @font.setter
  def font(self, value):
    self._font = value
    self.text_field.font = value
    # this should maybe change the font of the menuItems too