from ._anvil_designer import DropdownMenuTemplate
from anvil import HtmlTemplate
from anvil import *
# from ...Functions import underline_property, italic_property, style_property, color_property, innerText_property, bold_property, font_size_property

class DropdownMenu(DropdownMenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    # self.menuNode = self.dom_nodes['anvil-m3-menu-items-container']
    textFieldNode = self.text_field.dom_nodes['anvil-m3-text-field'];
    
    self.handle_box_click = self.handle_box_click
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    textFieldNode.addEventListener('click', self.handle_box_click)
  # click event listener on box to toggle open or closed menu
  
    # document.addEventListener('keydown', self.handle_keyboard_events)
    # self.shield.addEventListener('click', self.remove_shield_handler)
    # self.menuNode.addEventListener('click', self.child_clicked)
  def on_cleanup(self, **event_args):
    textFieldNode.removeEventListener('click', self.handle_box_click)
    # document.removeEventListener('keydown', self.handle_keyboard_events)
    # self.shield.removeEventListener('click', self.remove_shield_handler)
    # self.menuNode.removeEventListener('click', self.child_clicked)
  
  
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

  def handle_box_click(self):
    self.set_menu_visibility()

  def set_menu_visibility(self, value = None):
    if (value is None):
      value = not self.menu.visible
    self.menu.visible = value