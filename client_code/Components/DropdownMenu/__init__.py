from ._anvil_designer import DropdownMenuTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from ...Functions import style_property # underline_property, italic_property, , color_property, innerText_property, bold_property, font_size_property
from anvil.js import window
from anvil.js.window import document
import random, string, math
import anvil.designer
from ..Menu.MenuItem import MenuItem

class DropdownMenu(DropdownMenuTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.handle_component_click = self.handle_component_click
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)
    
    self.selection_field.dom_nodes['text-field-input'].style.caretColor = 'transparent'
    
    self.shield = document.createElement("div")
    self.shield.classList.toggle("anvil-m3-menu-clickShield", True)

  #properties
  visible = HtmlTemplate.visible
  align = style_property('anvil-m3-dropdownMenu-component', 'justifyContent')
  
  @property
  def enabled(self):
    return self._enabled
  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    self.selection_field.enabled = value

  @property
  def include_placeholder(self):
    return self._include_placeholder
  @include_placeholder.setter
  def include_placeholder(self, value):
    self._include_placeholder = value
    
  @property
  def placeholder(self):
    return self._placeholder
  @placeholder.setter
  def placeholder(self, value):
    self._placeholder = value
    # todo: what to do about this 
    self.selection_field.placeholder = value
    
  def on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-dropdownMenu-container'].addEventListener('click', self.handle_component_click)
    self.shield.addEventListener('click', self.remove_shield_handler)
    
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-dropdownMenu-container'].removeEventListener('click', self.handle_component_click)
    self.shield.removeEventListener('click', self.remove_shield_handler)

  def handle_component_click(self, event):
    print("clicked")
    self.set_menu_visibility()

  def set_menu_visibility(self, value = None):
    if (value is None):
      value = not self.menu.visible
    self.open = value
    self.menu.visible = value
    if value:
      if not anvil.designer.in_designer:
        self.place_shield()
  
  def place_shield(self):
    if not document.contains(self.shield):
      document.body.appendChild(self.shield)
      document.body.style.overflow = "hidden"
    
  def remove_shield_handler(self, event):
    self.remove_shield()
    self.set_menu_visibility(False)
    
  def remove_shield(self):
    if document.contains(self.shield):
      document.body.removeChild(self.shield)
      document.body.style.removeProperty("overflow")


# <div anvil-name="anvil-m3-dropdownMenu-component"  style="display:flex">
#   <div anvil-name="anvil-m3-dropdownMenu-container" class="anvil-m3-dropdownMenu-container" >
#   <!-- could put shield over this to prevent typing??? -->
#     <div anvil-slot="anvil-m3-dropdownMenu-textfield" class="anvil-m3-dropdownMenu-textfield" anvil-slot-internal> </div>
    
#     <div anvil-slot="anvil-m3-dropdownMenu-slot" anvil-name="anvil-m3-dropdownMenu-items-container" 
#         class="anvil-m3-dropdownMenu-items-container anvil-m3-dropdownMenu-items-hidden" anvil-slot-internal>
#           <p anvil-if-slot-empty="anvil-m3-dropdownMenu-slot" style="color: #BBB;"><i>No items to select</i></p>
#     </div>
#   </div>
# </div>
