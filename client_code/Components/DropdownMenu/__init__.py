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
    self.placeholder = ""
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
    self.shield.classList.toggle("anvil-m3-menu-clickShield", True)
    
    self.container = self.dom_nodes['anvil-m3-dropdownMenu-container']
    self.menuNode = self.dom_nodes['anvil-m3-dropdownMenu-items-container']
    self.selectionField = self.dom_nodes['anvil-m3-dropdownMenu-textfield']

    if anvil.designer.in_designer: #hides so doesn't do the ghosty visible thing when in designer cuz i want it to just straight up not show cuz its nto like you can add stuffin anyways. 
      self.menuNode.classList.toggle("anvil-m3-menu-hidden", True)

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
  def items(self):
    return self._items
  @items.setter
  def items(self, value):
    self._items = value
 
  @property
  def label_text(self):
    return self._label_text
  @label_text.setter
  def label_text(self, value):
    self._label_text = value
    self.selection_field.label_text = value or ""
    
  @property
  def placeholder(self):
    return self._placeholder
  @placeholder.setter
  def placeholder(self, value):
    self._placeholder = value

  @property
  def selected_value(self):
     return self._selected_value
  @selected_value.setter
  def selected_value(self, value):
    self._selected_value = value
    if type(value) is list:
      self.selection_field.dom_nodes['text-field-input'].value = value[0]
    else:
      self.selection_field.dom_nodes['text-field-input'].value = value
    self.raise_event("change")
  
  @property
  def include_placeholder(self):
    return self._include_placeholder
  @include_placeholder.setter
  def include_placeholder(self, value):
    self._include_placeholder = value or ""
    
  def on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-dropdownMenu-container'].addEventListener('click', self.handle_component_click)
    self.shield.addEventListener('click', self.remove_shield_handler)
    self.menuNode.addEventListener('click', self.child_clicked)
    
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-dropdownMenu-container'].removeEventListener('click', self.handle_component_click)
    self.shield.removeEventListener('click', self.remove_shield_handler)
    self.menuNode.removeEventListener('click', self.child_clicked)

  def handle_component_click(self, event):
    self.set_menu_visibility()

  def set_menu_visibility(self, value = None):
    if (value is None):
      value = not self.menu.visible
    self.menu.visible = value
    if value:
      if not anvil.designer.in_designer:
        self.place_shield()
      self.get_textfield_measurements()
      self.update_menu_placement()
    
  def update_menu_placement(self):
    # menuNode = self.dom_nodes['anvil-m3-dropdownMenu-items-container']
    menuNode = self.menu.dom_nodes['anvil-m3-menu-items-container']
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
    
  def get_textfield_measurements(self):
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
    event.stopPropagation()
    self.remove_shield()
    self.set_menu_visibility(False)
    
  def form_show(self, **event_args):
    self.create_menu_items()
    if anvil.designer.in_designer:
      if not self.label_text:
        self.label_text = anvil.designer.get_design_name(self)

  def create_menu_items(self):
    if self.include_placeholder:
      p = MenuItem()
      p.text = self.placeholder
      p.hide_leading_icon = True
      def handle_select_placeholder(**e):
        self.selected_value = None
        
      p.add_event_handler('click', handle_select_placeholder)
      self.menu.add_component(p, slot="anvil-m3-menu-slot")
      
    for item in self.items:
      selection = MenuItem()
      selection.hide_leading_icon = True
      if type(item) is list:
        selection.text = item[0]
      else:
        selection.text = item
        
      def handle_selection_click(value = item, **e): 
        self.selected_value = value
          
      selection.add_event_handler('click', handle_selection_click)
      self.menu.add_component(selection, slot="anvil-m3-menu-slot")
