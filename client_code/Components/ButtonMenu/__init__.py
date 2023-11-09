from ._anvil_designer import ButtonMenuTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from anvil.js import window
from anvil.js.window import document
import random, string, math
import anvil.designer
from ..Menu.MenuItem import MenuItem
from ...Functions import property_with_callback

class ButtonMenu(ButtonMenuTemplate):
  def __init__(self, **properties):
    self._props = properties
    self.init_components(**properties)
    self.open = False
    self._window_size = {}
    self._menu_size = {}
    self._button_positioning = {}

    self.hoverIndex = None
    self.itemIndices = set()
    self.children = None
    
    self.shield = document.createElement("div")
    self.shield.classList.toggle("anvil-m3-menu-clickShield", True)
    self.menuNode = self.dom_nodes['anvil-m3-buttonMenu-items-container']

    # This is here for because the cleanup uses object identity to figure out which event handler to actually remove. 
    # calling self.foo creates a new function each time so the addEventListener and removeEventListener are looking for two different functions
    # To not have to do this, Stu is considering creating a add_event_listener() and remove_event_listener() to anvil.js
    self.handle_keyboard_events = self.handle_keyboard_events
    self.remove_shield_handler = self.remove_shield_handler
    self.child_clicked = self.child_clicked

    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    document.addEventListener('keydown', self.handle_keyboard_events)
    self.shield.addEventListener('click', self.remove_shield_handler)
    self.menuNode.addEventListener('click', self.child_clicked)
  def on_cleanup(self, **event_args):
    document.removeEventListener('keydown', self.handle_keyboard_events)
    self.shield.removeEventListener('click', self.remove_shield_handler)
    self.menuNode.removeEventListener('click', self.child_clicked)
  
  visible = HtmlTemplate.visible
  def set_text(self, value):
    self.menu_button.text = value
  text = property_with_callback("text", set_text)

  def set_appearance(self, value):
    self.menu_button.appearance = value
  appearance = property_with_callback("appearance", set_appearance)

  def set_enabled(self, value):
    self.menu_button.enabled = value
  enabled = property_with_callback("enabled", set_enabled)

  def toggle_menu_visibility(self, **event_args):
    self.set_visibility()

  def set_visibility(self, value = None):
    classes = self.menuNode.classList
    if value is not None:
      classes.toggle('anvil-m3-buttonMenu-items-hidden', not value)
    else:
      classes.toggle('anvil-m3-buttonMenu-items-hidden')
      
    self.open = not classes.contains('anvil-m3-buttonMenu-items-hidden')
    if self.open:
      if not anvil.designer.in_designer:
        self.place_shield()
      self.get_button_measurements()
      self.update_menu_placement()

      self.get_hover_index_information()
        
    else:
      self.menuNode.removeAttribute("style")
      self.hoverIndex = None
      self.clear_hover_styles()

  def update_menu_placement(self):
    menuNode = self.dom_nodes['anvil-m3-buttonMenu-items-container']
    menuNode.removeAttribute("style")
    menuNode.style.maxWidth = "unset"
    self._window_size = {"width": window.innerWidth, "height": window.innerHeight}
    self._menu_size = {"width": menuNode.offsetWidth, "height": menuNode.offsetHeight}
    
    # horizontal placement
    menuLeft = self._button_positioning['left']
    menuRight = menuLeft + self._menu_size['width']
    if self._window_size['width'] < menuRight:
      menuNode.style.right = '5px'
    else:
      menuNode.style.left = f"{math.floor(menuLeft) + 5}px"
    
    # vertical placement
    menuTop = self._button_positioning['bottom']
    menuBottom = menuTop + self._menu_size['height']
    spaceAtTop = self._button_positioning['top']
    spaceAtBottom = self._window_size['height'] - self._button_positioning['bottom']
    
    # menu won't fit in the standrd spot under the text field
    if spaceAtBottom < self._menu_size["height"]:
      # place the menu at the bottom
      if spaceAtBottom > spaceAtTop:
        menuNode.style.top = f"{math.floor(menuTop + 1)}px"
        menuNode.style.height = f"{math.floor(spaceAtBottom - 10)}px"
      # place the menu at the top
      else:
        menuNode.style.bottom = f"{math.floor(7 + self._window_size['height'] - self._button_positioning['top'])}px"
        if spaceAtTop < self._menu_size["height"]:
          menuNode.style.height = f"{math.floor(spaceAtTop - 10)}px"
    else:
      menuNode.style.top = f"{math.floor(menuTop + 1)}px"
  
    
  def get_button_measurements(self):
    rect = self.menu_button.dom_nodes['anvil-m3-button'].getBoundingClientRect()
    self._button_positioning = {
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
    
    if event.key in ["ArrowUp", "ArrowDown"]:
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
  def _anvil_get_interactions_(self):
    return [
      {
        "type": "designer_events",
        "callbacks": {"onSelectDescendent": self._on_select_descendent, "onSelectOther": self._on_select_other},
      },
      {
        "type": "whole_component",
        "title": "Edit text",
        "icon": "edit",
        "default": True,
        "callbacks": {
          "execute": lambda: anvil.designer.start_inline_editing(
            self, "text", self.menu_button.dom_nodes["anvil-m3-button-text"]
          )
        },
      },
    ]

  def _on_select_descendent(self):
    self.set_visibility(True)

  def _on_select_other(self):
    self.set_visibility(False)
