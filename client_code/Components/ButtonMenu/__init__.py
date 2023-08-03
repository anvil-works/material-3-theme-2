from ._anvil_designer import ButtonMenuTemplate
from anvil import *

class ButtonMenu(ButtonMenuTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # TODO: needs an event handler to close when not focused

  @property
  def text(self):
    return self._text
  @text.setter
  def text(self, value):
    self._text = value
    self.menu_button.text = value
  
  def toggle_menu_visibility(self, **event_args):
    self.set_visibility()

  def set_visibility(self, value = None):
    classes = self.dom_nodes['anvil-m3-buttonMenu-items-container'].classList
    if value:
      classes.toggle('anvil-m3-buttonMenu-items-hidden', value)
    else:
      classes.toggle('anvil-m3-buttonMenu-items-hidden')

  def _anvil_get_design_info_(self, as_layout=False):
    di = super()._anvil_get_design_info_(as_layout)
    di['interactions'] = [{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-radiobutton-label'])
      }
    }]
    return di 