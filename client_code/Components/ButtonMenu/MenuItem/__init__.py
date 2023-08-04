# <div anvil-name="anvil-m3-menuItem-container" class="anvil-m3-menuItem-container" tabindex=0>
#   <i anvil-name="anvil-m3-menuItem-leadingIcon" class="material-symbols-outlined anvil-m3-menuItem-leadingIcon"></i>
#   <div anvil-name="anvil-m3-menuItem-content" class="anvil-m3-menuItem-content">
#     <div anvil-name="anvil-m3-menuItem-text" class="anvil-m3-menuItem-text"></div>
#     <div anvil-name="anvil-m3-menuItem-trailingText" class="anvil-m3-menuItem-trailingText"></div>
#     <i anvil-name="anvil-m3-menuItem-trailingIcon" class="material-symbols-outlined anvil-m3-menuItem-trailingIcon"></i>
#   </div>
# </div>

from ._anvil_designer import MenuItemTemplate
from anvil import *

class MenuItem(MenuItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.dom_nodes['button'].addEventListener("click", self.handle_click)

  @property
  def leading_icon(self):
    return self._leading_icon
  @leading_icon.setter
  def leading_icon(self, value):
    self._leading_icon = value
    self.dom_nodes["anvil-m3-menuItem-leadingIcon"].innerText = value or " "

  @property
  def text(self):
    return self._text
  @text.setter
  def text(self, value):
    self._text = value
    self.dom_nodes["anvil-m3-menuItem-text"].innerText = value

  @property
  def trailing_icon(self):
    return self._trailing_icon
  @trailing_icon.setter
  def trailing_icon(self, value):
    self._trailing_icon = value
    self.dom_nodes["anvil-m3-menuItem-trailingIcon"].innerText = value 
    
  @property
  def trailing_text(self):
    return self._trailing_text
  @trailing_text.setter
  def trailing_text(self, value):
    self._trailing_text = value
    self.dom_nodes["anvil-m3-menuItem-trailingText"].innerText = value 
  
  # hide_leading_icon

  def handle_click(self, event):
    event.preventDefault()
    self.raise_event("click")

  
