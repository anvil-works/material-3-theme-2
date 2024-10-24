# <div anvil-slot="anvil-m3-menu-slot" anvil-name="anvil-m3-menu-items-container" class="anvil-m3-menu-items-container">
#   <p anvil-if-slot-empty="anvil-m3-menu-slot" style="color: #BBB;"><i>Menu items go here</i></p>
# </div>

from ._anvil_designer import MenuTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from ...Functions import color_property

class Menu(MenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.tag = ComponentTag()
    self._props = properties
    self.init_components(**properties)
    

  """ Properties """
  visible = HtmlTemplate.visible
  background_color = color_property('anvil-m3-menu-items-container', 'backgroundColor', 'background_color')
  
  # @property
  # def visible(self):
  #   return self._visible

  # @visible.setter
  # def visible(self, value):
  #   self._visible = value
  #   self.dom_nodes['anvil-m3-menu-items-container'].classList.toggle('anvil-m3-menu-hidden', not value)

  """ Functions """
  def set_or_toggle_visibility(self, value = None):
    if value is not None:
      self.visible = value
    else:
      currVal = self.visible
      self.visible = not currVal

  

  def _anvil_get_interactions_(self):
    return [
      {
        "type": "designer_events",
        "callbacks": {
          "onSelectDescendent": self._on_select_descendant, 
          "onSelectOther": self._on_select_other
        }
      },
    ]

  def _on_select_descendant(self):
    pass
    # print("I did something on select")

  def _on_select_other(self):
    pass
    # print("something happened on deselect")