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
    
  @property
  def appearance(self):
    return self._appearance
  @appearance.setter
  def appearance(self, value):
    self.menu_button.appearance = value

  # get all the child components in the menu container
  
  
  def toggle_menu_visibility(self, **event_args):
    self.set_visibility()

  def set_visibility(self, value = None):
    classes = self.dom_nodes['anvil-m3-buttonMenu-items-container'].classList
    if value:
      classes.toggle('anvil-m3-buttonMenu-items-hidden', value)
    else:
      classes.toggle('anvil-m3-buttonMenu-items-hidden')

  def _anvil_get_design_info_(self, as_layout=False):
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["interactions"] = [
      {
        "type": "whole_component",
        
      }
        # {"type": "on_selection", {"onSelect": self._on_select, "onDeselect": self._on_deselect, "onSelectDescendent": self._on_select_descendant, "onDeselectDescendant": self._on_deselect_descendant, "onSelectOther": self._on_select_other}}
    ]
    return design_info

    # plus a whole bunch of methods called _on_select() etc

  
