# <div anvil-slot="anvil-m3-menu-slot" anvil-name="anvil-m3-menu-items-container" class="anvil-m3-menu-items-container">
#   <p anvil-if-slot-empty="anvil-m3-menu-slot" style="color: #BBB;"><i>Menu items go here</i></p>
# </div>

from ._anvil_designer import MenuTemplate
from anvil import *

class Menu(MenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  """ Properties """
  @property
  def visible(self):
    return self._visible

  @visible.setter
  def visible(self, value):
    self._visible = value
    self.dom_nodes['anvil-m3-menu-items-container'].classList.toggle('anvil-m3-menu-hidden', not value)

  """ Functions """
  def set_or_toggle_visibility(self, value = None):
    if value is not None:
      self.visible = value
    else:
      currVal = self.visible
      self.visible = not currVal

  def _anvil_get_design_info_(self, as_layout=False):
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["interactions"] = [
      {
        "type": "designer_events",
        "callbacks": {
          "onSelectDescendent": self._on_select_descendant, 
          "onSelectOther": self._on_select_other
        }
      },
    ]
    return design_info

  def _on_select_descendant(self):
    pass
    # print("I did something on select")

  def _on_select_other(self):
    pass
    # print("something happened on deselect")