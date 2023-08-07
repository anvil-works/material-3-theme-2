from ._anvil_designer import ButtonMenuTemplate
from anvil import *
from anvil.js.window import document
import random, string

class ButtonMenu(ButtonMenuTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # TODO: needs an event handler to close when not focused
    self.id = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    
  @property
  def id(self):
    return self._id
  @id.setter
  def id(self, value):
    self._id = value
    self.dom_nodes['anvil-m3-buttonMenu-container'].id = value
  
  @property
  def text(self):
    return self._text
  @text.setter
  def text(self, value):
    self._text = value
    self.menu_button.text = value
    
  @property
  def appearance(self):
    return self._appearance
  @appearance.setter
  def appearance(self, value):
    self.menu_button.appearance = value

  @property
  def menuOpen(self):
    return self._menuOpen
  @menuOpen.setter
  def menuOpen(self, value):
    self._menuOpen = value or False
  
  def toggle_menu_visibility(self, **event_args):
    self.set_visibility()
    # return classes.contains(className)
    self.menuOpen = not self.dom_nodes['anvil-m3-buttonMenu-items-container'].classList.contains('anvil-m3-buttonMenu-items-hidden')

  def set_visibility(self, value = None):
    classes = self.dom_nodes['anvil-m3-buttonMenu-items-container'].classList
    if value:
      classes.toggle('anvil-m3-buttonMenu-items-hidden', not value)
    else:
      classes.toggle('anvil-m3-buttonMenu-items-hidden')

  def closeOnLoseFocus(self, event):
    if not self.dom_nodes['anvil-m3-buttonMenu-items-container'].contains(event.target):
      self.set_visibility(False)


# 
    # print("menu is")
    # print(value)
    # if self._menuOpen:
    #   document.addEventListener("click", self.closeOnLoseFocus)
    # else:
    #   document.removeEventListener("click", self.closeOnLoseFocus) 
  
  def _anvil_get_design_info_(self, as_layout=False):
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["interactions"] = [
      {
        "type": "on_selection",
        "callbacks": {
          # "onSelect": self._on_select,  
          # "onDeselect": self._on_deselect, 
          "onSelectDescendent": self._on_select_descendant, 
          # "onDeselectDescendant": self._on_deselect_descendant, 
          "onSelectOther": self._on_select_other
        }
      },
      # { # TODO: get this to work so you can edit the text in the button
      # "type": "whole_component",
      # "title": "Edit button text",
      # "icon": "edit",
      # "callbacks": 
      #   {
      #     "execute": lambda: anvil.designer.start_inline_editing(self.menu_button, "text", self.menu_button.dom_nodes['anvil-m3-button-text'])
      #   }
      # }
    ]
    return design_info

  # def _anvil_enable_drop_mode_(self, dropping_object):
  #   return []

    # plus a whole bunch of methods called _on_select() etc
  # def _on_select(self):
  #   print("on_select called")

  def _on_deselect(self):
    self.set_visibility(False)

  def _on_select_descendant(self):
    self.set_visibility(True)

  def _on_deselect_descendant(self):
    self.set_visibility(False)

  def _on_select_other(self):
    print("_on_select_other called")
