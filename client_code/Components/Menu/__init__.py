# <div anvil-slot="anvil-m3-menu-slot" anvil-name="anvil-m3-menu-items-container" class="anvil-m3-menu-items-container">
#   <p anvil-if-slot-empty="anvil-m3-menu-slot" style="color: #BBB;"><i>Menu items go here</i></p>
# </div>

from ._anvil_designer import MenuTemplate
from anvil import *

class Menu(MenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  @property
  def visible(self):
    return self._visible

  @visible.setter
  def visible(self, value):
    self._visible = value
    # anvil-m3-menu-hidden
    self.dom_nodes['anvil-m3-menu-items-container'].classList.toggle('anvil-m3-menu-hidden', value)


  def set_or_toggle_visibility(self, value = None):
    classes = self.dom_nodes['anvil-m3-menu-items-container'].classList
    if value:
      classes.toggle('anvil-m3-menu-hidden', not value)
    else:
      classes.toggle('anvil-m3-menu-hidden')