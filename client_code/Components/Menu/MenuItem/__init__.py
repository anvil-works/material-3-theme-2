from ._anvil_designer import MenuItemTemplate
from anvil import *

import anvil.designer

class MenuItem(MenuItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.dom_nodes['anvil-m3-menuItem-container'].addEventListener("click", self.handle_click)

  """ Properties """
  @property
  def leading_icon(self):
    return self._leading_icon
  @leading_icon.setter
  def leading_icon(self, value):
    self._leading_icon = value
    self.dom_nodes["anvil-m3-menuItem-leadingIcon"].innerHTML = value or " "

  @property
  def text(self):
    return self._text
  @text.setter
  def text(self, value):
    self._text = value
    self.dom_nodes["anvil-m3-menuItem-labelText"].innerText = value

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
  
  @property 
  def hide_leading_icon(self):
    return self._hide_leading_icon
  @hide_leading_icon.setter
  def hide_leading_icon(self, value):
    self._hide_leading_icon = value
    self.dom_nodes["anvil-m3-menuItem-leadingIcon"].classList.toggle("anvil-m3-menuItem-hideLeadingIcon", value)
  # anvil-m3-menuItem-hideLeadingIcon

  @property
  def enabled(self):
    return self._enabled
  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    self.dom_nodes["anvil-m3-menuItem-container"].classList.toggle("anvil-m3-menuItem-disabled", not value)

  """ Functions """
  def handle_click(self, event):
    event.preventDefault() #TODO: make sure this doesn't prevent the menu from closing
    self.raise_event("click")

  def _anvil_get_design_info_(self, as_layout=False):
    di = super()._anvil_get_design_info_(as_layout)
    di['interactions'] = [{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-menuItem-labelText'])
      }
    }]
    return di