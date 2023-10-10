from ._anvil_designer import DropdownMenu_integratedTemplate
from anvil import *
from anvil import HtmlTemplate
from ...Functions import style_property # underline_property, italic_property, , color_property, innerText_property, bold_property, font_size_property
from anvil.js import window
from anvil.js.window import document
import random, string, math
import anvil.designer
from ..Menu.MenuItem import MenuItem

class DropdownMenu_integrated(DropdownMenu_integratedTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.open = False
    self.window_size = {}
    self.menu_size = {}
    self.dropdown_field_positioning = {}

    self.hoverIndex = None
    self.itemIndices = set()
    self.children = None
    
    self.shield = document.createElement("div")
    self.shield.classList.toggle("anvil-m3-menu-clickShield", True)
    self.dropdown_field = self.dom_nodes['anvil-m3-dropdownMenu-container']
    self.menuNode = self.dom_nodes['anvil-m3-dropdownMenu-items-container']
    print(self.menuNode)

    self.toggle_menu_visibility = self.toggle_menu_visibility
    self.handle_keyboard_events = self.handle_keyboard_events
    self.remove_shield_handler = self.remove_shield_handler
    self.child_clicked = self.child_clicked

    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    self.dropdown_field.addEventListener('click', self.toggle_menu_visibility)
    document.addEventListener('keydown', self.handle_keyboard_events)
    self.shield.addEventListener('click', self.remove_shield_handler)
    self.menuNode.addEventListener('click', self.child_clicked)
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-dropdownMenu-textfield'].removeEventListener('click', self.toggle_menu_visibility)
    document.removeEventListener('keydown', self.handle_keyboard_events)
    self.shield.removeEventListener('click', self.remove_shield_handler)
    self.menuNode.removeEventListener('click', self.child_clicked)
  
  visible = HtmlTemplate.visible
  align = style_property('anvil-m3-dropdownMenu-component', 'justifyContent')
  
  # @property
  # def text(self):
  #   return self._text
  # @text.setter
  # def text(self, value):
  #   self._text = value
  #   self.menu_button.text = value

  @property
  def appearance(self):
    return self._appearance
  @appearance.setter
  def appearance(self, value):
    self.text_field.appearance = value
  #   self.menu_button.appearance = value
    self._appearance = value

  @property
  def enabled(self):
    return self._enabled
  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    self.text_field.enabled = value
    
  def toggle_menu_visibility(self, event):
    self.set_visibility()

  def set_visibility(self, value = None):
    classes = self.menuNode.classList
    if value is not None:
      classes.toggle('anvil-m3-dropdownMenu-items-hidden', not value)
    else:
      classes.toggle('anvil-m3-dropdownMenu-items-hidden')
      
    self.open = not classes.contains('anvil-m3-dropdownMenu-items-hidden')
    if self.open:
      if not anvil.designer.in_designer:
        self.place_shield()
      self.get_dropdown_measurements()
      self.update_menu_placement()

      self.get_hover_index_information()
        
    else:
      self.menuNode.removeAttribute("style")
      self.hoverIndex = None
      self.clear_hover_styles()
    
  def update_menu_placement(self):
    menuNode = self.dom_nodes['anvil-m3-dropdownMenu-items-container']
    self.window_size = {"width": window.innerWidth, "height": window.innerHeight}
    self.menu_size = {"width": menuNode.offsetWidth, "height": menuNode.offsetHeight}
    # horizontal placement
    menuLeft = self.dropdown_field_positioning['left']
    menuRight = menuLeft + self.menu_size['width']
    if self.window_size['width'] < menuRight:
      menuNode.style.right = '5px'
    else:
      menuNode.style.left = f"{math.floor(menuLeft) + 5}px"
      
    # vertical placement
    menuTop = self.dropdown_field_positioning['bottom']
    menuBottom = menuTop + self.menu_size['height']

    ## menu too tall!
    if (self.window_size['height'] - self.dropdown_field_positioning['height']) < self.menu_size['height']: 
      spaceAtTop = self.dropdown_field_positioning['top']
      spaceAtBottom = self.window_size['height'] - (spaceAtTop + self.dropdown_field_positioning['height'])

      # put at the top and set container height
      if spaceAtTop > spaceAtBottom:
        menuNode.style.bottom = f"{math.floor(self.window_size['height'] - (self.dropdown_field_positioning['top'] - 5))}px"
        menuNode.style.height = f"{math.floor(spaceAtTop - 7)}px"
        
      # put at the bottom and set container height
      else:
        menuNode.style.top = f"{math.floor(menuTop + 5)}px"
        menuNode.style.height = f"{math.floor(spaceAtBottom - 7)}px"

    ## menu fits
    else: 
      # default placement is out of bounds
      if self.window_size['height'] < menuBottom:
        menuNode.style.bottom = f"{math.floor(self.window_size['height'] - (self.dropdown_field_positioning['top'] - 5))}px"
      # fits in default position
      else:
        menuNode.style.top = f"{math.floor(menuTop + 5)}px"
    
  def get_dropdown_measurements(self):
    rect = self.text_field.dom_nodes['text-field'].getBoundingClientRect()
    self.dropdown_field_positioning = {
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
    self.set_visibility(False)
    
  def remove_shield(self):
    if document.contains(self.shield):
      document.body.removeChild(self.shield)
      document.body.style.removeProperty("overflow")
    
  def child_clicked(self, event):
    # do the click action. The child should handle this
    self.remove_shield()
    self.set_visibility(False)
  
  def get_hover_index_information(self):
    self.children = self.get_components()[1:]
    for i in range(0, len(self.children)):
      if isinstance(self.children[i], MenuItem):
        self.itemIndices.add(i)
   
  def handle_keyboard_events(self, event):
    if not self.open:
      return

    action_keys = set(["ArrowUp", "ArrowDown", "Tab", "Escape", " ", "Enter"])
    if event.key not in action_keys:
      #TODO: eventually want to use this to jump somewhere in the list
      return
    
    if event.key is "ArrowUp" or event.key is "ArrowDown":
      self.iterate_hover(event.key is "ArrowDown")
      return
      
    # if event.key is "Tab":
    #   pass
    hover = self.hoverIndex #holding value for situation like alerts where it awaits 
    self.remove_shield()
    self.set_visibility(False)
    
    def attemptSelect():
      event.preventDefault();
      if not hover is None:
        self.children[hover].raise_event("click")
    
    if (event.key is " "): #space key as " " is stupid
      attemptSelect()
    if (event.key is "Enter"):
      attemptSelect()
      
  def iterate_hover(self, inc = True):
    if inc:
      if self.hoverIndex is None or self.hoverIndex is (len(self.children) - 1):
        self.hoverIndex = -1
      while True:
        self.hoverIndex += 1
        if self.hoverIndex in self.itemIndices:
          break;
    else:
      if self.hoverIndex is None or self.hoverIndex is 0:
        self.hoverIndex = len(self.children)
      while True:
        self.hoverIndex -= 1
        if self.hoverIndex in self.itemIndices:
          break; 
    self.update_hover_styles();

  def clear_hover_styles(self):
    if self.children is not None:
      for child in self.children:
        if isinstance(child, MenuItem):
          child.dom_nodes['anvil-m3-menuItem-container'].classList.toggle('anvil-m3-menuItem-container-keyboardHover', False)

  def update_hover_styles(self):
    self.clear_hover_styles()
    self.children[self.hoverIndex].dom_nodes['anvil-m3-menuItem-container'].classList.toggle('anvil-m3-menuItem-container-keyboardHover', True)
    
# DESIGNER INTERACTIONS
  def _anvil_get_design_info_(self, as_layout=False):
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["interactions"] = [
      {
        "type": "designer_events",
        "callbacks": {
          "onSelectDescendent": self._on_select_descendent,
          "onSelectOther": self._on_select_other
        }
      },
      {
      "type": "whole_component",
      "title": "Visible",
      "icon": "add", #TODO: eye icon
      "callbacks": {
        "execute": self.toggle_visible
      }
    }, {
      "type": "whole_component",
      "title": "Enable",
      "icon": "add", #TODO: power icon
      "callbacks": {
        "execute": self.toggle_enabled
      }
    # },{
    #   "type": "whole_component",
    #   "title": "Edit text",
    #   "icon": "edit",
    #   "default": True,
    #   "callbacks": {
    #     "execute": lambda: anvil.designer.start_inline_editing(self.menu_button, "text", self.menu_button.dom_nodes['anvil-m3-button-text'])
    #   }
    }]
    return design_info

  def _on_select_descendent(self):
    self.set_visibility(True)

  def _on_select_other(self):
    self.set_visibility(False)

  def toggle_visible(self):
    self.visible = not self.visible
    anvil.designer.update_component_properties(self, {'visible': self.visible})

  def toggle_enabled(self):
    self.enabled = not self.enabled
    anvil.designer.update_component_properties(self, {'enabled': self.enabled})