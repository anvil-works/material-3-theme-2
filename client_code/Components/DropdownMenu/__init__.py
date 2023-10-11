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

    self.window_size = {}
    self.menu_size = {}
    self.box_positioning = {}

    # self.hoverIndex = None
    # self.itemIndices = set()
    # self.children = None
    self.child_clicked = self.child_clicked
    self.handle_component_click = self.handle_component_click
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)
    
    self.selection_field.dom_nodes['text-field-input'].style.caretColor = 'transparent'
    
    self.shield = document.createElement("div")
    self.shield.style = "opacity: .3; background-color: green"
    self.shield.classList.toggle("anvil-m3-menu-clickShield", True)
    
    self.container = self.dom_nodes['anvil-m3-dropdownMenu-container']
    self.menuNode = self.dom_nodes['anvil-m3-dropdownMenu-items-container']
    self.selectionField = self.dom_nodes['anvil-m3-dropdownMenu-textfield']

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
  def appearance(self):
    return self._appearance
  @appearance.setter
  def appearance(self, value):
    self._appearance = value
    self.selection_field.appearance = value
    

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
    self.menuNode.addEventListener('click', self.child_clicked)
    
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-dropdownMenu-container'].removeEventListener('click', self.handle_component_click)
    self.shield.removeEventListener('click', self.remove_shield_handler)
    self.menuNode.removeEventListener('click', self.child_clicked)

  def handle_component_click(self, event):
    print("clicked")
    self.set_menu_visibility()

  def set_menu_visibility(self, value = None):
    print("*** trying to set visibility to: ")
    print(value)
    if (value is None):
      value = not self.menu.visible
    print("supposed to actually set visibility to: ")
    print(value)
    self.menu.visible = value
    if value:
      if not anvil.designer.in_designer:
        self.place_shield()
      self.get_button_measurements()
      self.update_menu_placement()
    
  def update_menu_placement(self):
    menuNode = self.dom_nodes['anvil-m3-dropdownMenu-items-container']
    self.window_size = {"width": window.innerWidth, "height": window.innerHeight}
    self.menu_size = {"width": menuNode.offsetWidth, "height": menuNode.offsetHeight}
    # horizontal placement
    menuLeft = self.box_positioning['left']
    menuRight = menuLeft + self.menu_size['width']
    if self.window_size['width'] < menuRight:
      menuNode.style.right = '5px'
    else:
      menuNode.style.left = f"{math.floor(menuLeft) + 5}px"
      
    # vertical placement
    menuTop = self.box_positioning['bottom']
    menuBottom = menuTop + self.menu_size['height']

    ## menu too tall!
    if (self.window_size['height'] - self.box_positioning['height']) < self.menu_size['height']: 
      spaceAtTop = self.box_positioning['top']
      spaceAtBottom = self.window_size['height'] - (spaceAtTop + self.box_positioning['height'])

      # put at the top and set container height
      if spaceAtTop > spaceAtBottom:
        menuNode.style.bottom = f"{math.floor(self.window_size['height'] - (self.box_positioning['top'] - 5))}px"
        menuNode.style.height = f"{math.floor(spaceAtTop - 7)}px"
        
      # put at the bottom and set container height
      else:
        menuNode.style.top = f"{math.floor(menuTop + 5)}px"
        menuNode.style.height = f"{math.floor(spaceAtBottom - 7)}px"

    ## menu fits
    else: 
      # default placement is out of bounds
      if self.window_size['height'] < menuBottom:
        menuNode.style.bottom = f"{math.floor(self.window_size['height'] - (self.box_positioning['top'] - 5))}px"
      # fits in default position
      else:
        menuNode.style.top = f"{math.floor(menuTop + 5)}px"
    
  def get_button_measurements(self):
    rect = self.selection_field.dom_nodes['text-field-input'].getBoundingClientRect()
    self.box_positioning = {
      "top": rect.top,
      "right": rect.right,
      "bottom": rect.bottom,
      "left": rect.left,
      "height": rect.bottom - rect.top,
      "width": rect.right - rect.left,
    }
  
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

  def child_clicked(self, event):
    # do the click action. The child should handle this
    self.remove_shield()
    self.set_menu_visibility(False)

# <div anvil-name="anvil-m3-dropdownMenu-component"  style="display:flex">
#   <div anvil-name="anvil-m3-dropdownMenu-container" class="anvil-m3-dropdownMenu-container" >
#   <!-- could put shield over this to prevent typing??? -->
#     <div anvil-slot="anvil-m3-dropdownMenu-textfield" anvil-name="anvil-m3-dropdownMenu-textfield" class="anvil-m3-dropdownMenu-textfield" anvil-slot-internal> </div>
    
#     <div anvil-slot="anvil-m3-dropdownMenu-slot" anvil-name="anvil-m3-dropdownMenu-items-container" 
#         class="anvil-m3-menu-items-container" anvil-slot-internal>
#     </div>
#   </div>
# </div>