from ._anvil_designer import ButtonMenuTemplate
from anvil import *
from anvil.js.window import document
import random, string

class ButtonMenu(ButtonMenuTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # TODO: needs an event handler to close when not focused

  """ Properties """
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

  # @property
  # def menuOpen(self):
  #   return self._menuOpen
  # @menuOpen.setter
  # def menuOpen(self, value):
  #   self._menuOpen = value or False
    # self.dom_nodes['anvil-m3-buttonMenu-container']
    # if value:
    #   self.dom_nodes['anvil-m3-buttonMenu-container'].addEventListener('focus', self.checkFocus)
  
  @property
  def enabled(self):
    return self._enabled
  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    self.menu_button.enabled = value
    
  """ Functions """
  def set_visibility(self, value = None):
    self.menu.set_or_toggle_visibility(value)

  # def closeOnLoseFocus(self, event):
  #   if not self.dom_nodes['anvil-m3-buttonMenu-items-container'].contains(event.target):
  #     self.set_visibility(False)

  # def checkFocus(self, event):
  #   # document.activeElement
  #   # var descendants = theElement.querySelectorAll("*");
  #   print(event.target)
  #   pass


  def _anvil_get_design_info_(self, as_layout=False):
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["interactions"] = [
      {
        "type": "on_selection",
        "callbacks": {
          "onSelectDescendent": self._on_select_descendant, 
          "onSelectOther": self._on_select_other
        }
      },
    ]
    return design_info
   
  def _on_select_descendant(self):
    self.set_visibility(True)

  def _on_select_other(self):
    self.set_visibility(False)

  def set_menu_visibility(self, **event_args):
    self.set_visibility()

