from ._anvil_designer import DropdownMenuTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from ...Functions import style_property, property_with_callback # underline_property, italic_property, , color_property, innerText_property, bold_property, font_size_property
from anvil.js import window
from anvil.js.window import document
import random, string, math
import anvil.designer
from ..Menu.MenuItem import MenuItem

class DropdownMenu(DropdownMenuTemplate):
  def __init__(self, **properties):
    self._props = properties
    self.placeholder = ""
    self.init_components(**properties)

    self._window_size = {}
    self._menu_size = {}
    self._box_positioning = {}

    self._hoverIndex = None
    self._children = None
    self._selected_menuItem = None
    
    self.selected_value = None
    
    self._has_focus = False
    self.handle_keyboard_events = self.handle_keyboard_events
    self.handle_selection_field_focus = self.handle_selection_field_focus
    self.child_clicked = self.child_clicked
    self.handle_component_click = self.handle_component_click
    
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)
    
    self.selection_field.dom_nodes['text-field-input'].style.caretColor = 'transparent'
    self.selection_field.dom_nodes['text-field-input'].style.cursor = "pointer"
    self.selection_field.dom_nodes['text-field-input'].setAttribute("readonly", True)
          
    self.shield = document.createElement("div")
    self.shield.classList.toggle("anvil-m3-menu-clickShield", True)
    
    if not self.label_text and self.placeholder:
      self.selection_field.dom_nodes['label-text'].innerText = self.placeholder

    self.menuNode = self.dom_nodes['anvil-m3-dropdownMenu-items-container']
    if anvil.designer.in_designer: #hides so doesn't do the ghosty visible thing when in designer cuz i want it to just straight up not show cuz its nto like you can add stuffin anyways. 
      self.menuNode.classList.toggle("anvil-m3-menu-hidden", True)
    

  #properties
  visible = HtmlTemplate.visible

  @property
  def background(self):
    return self._background
  @background.setter
  def background(self, value):
    self._background = value
    self.selection_field.background = value
  
  @property
  def bold_label(self):
    return self._bold_label
  @bold_label.setter
  def bold_label(self, value):
    self._bold_label = value
    self.selection_field.bold_label = value
    
  @property
  def label_font(self):
    return self._label_font
  @label_font.setter
  def label_font(self, value):
    self._label_font = value
    self.selection_field.label_font = value
    
  @property
  def label_font_size(self):
    return self._label_font_size
  @label_font_size.setter
  def label_font_size(self, value):
    self._label_font_size = value
    self.selection_field.label_font_size = value
  
  @property
  def label_text_color(self):
    return self._label_text_color
  @label_text_color.setter
  def label_text_color(self, value):
    self._label_text_color = value
    self.selection_field.label_text_color = value
  
  @property
  def italic_label(self):
    return self._italic_label
  @italic_label.setter
  def italic_label(self, value):
    self._italic_label = value
    self.selection_field.italic_label = value
  
  @property
  def underline_label(self):
    return self._underline_label
  @underline_label.setter
  def underline_label(self, value):
    self._underline_label = value
    self.selection_field.underline_label = value
  
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
  def selected_italic_display(self):
    return self._selected_italic_display
  @selected_italic_display.setter
  def selected_italic_display(self, value):
    self._selected_italic_display = value
    self.selection_field.selected_italic_display = value
    
  @property
  def selected_bold_display(self):
    return self._selected_bold_display
  @selected_bold_display.setter
  def selected_bold_display(self, value):
    self._selected_bold_display = value
    self.selection_field.selected_bold_display = value
    
  @property
  def selected_underline_display(self):
    return self._selected_underline_display
  @selected_underline_display.setter
  def selected_underline_display(self, value):
    self._selected_underline_display = value
    self.selection_field.selected_underline_display = value
    
  @property
  def selected_font(self):
    return self._selected_font
  @selected_font.setter
  def selected_font(self, value):
    self._selected_font = value
    self.selection_field.selected_font = value
    
  @property
  def selected_font_size(self):
    return self._selected_font_size
  @selected_font_size.setter
  def selected_font_size(self, value):
    self._selected_font_size = value
    self.selection_field.selected_font_size = value
    
  @property
  def selected_text_color(self):
    return self._selected_text_color
  @selected_text_color.setter
  def selected_text_color(self, value):
    self._selected_text_color = value
    self.selection_field.selected_text_color = value

  @property
  def items(self):
    return self._items
  @items.setter
  def items(self, value):
    self._items = value

  # @property
  # def label_text(self):
  #   return self._label_text
  # @label_text.setter
  # def label_text(self, value):
  #   self._label_text = value
    
  def update_label_text(self, value):
    self.selection_field.label_text = value or ""

  label_text = property_with_callback("label_text", update_label_text)
    
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
  def allow_none(self):
    return self._allow_none
  @allow_none.setter
  def allow_none(self, value):
    self._allow_none = value

  @property
  def bold_items(self):
    return self._bold_items
  @bold_items.setter
  def bold_items(self, value):
    self._bold_items = value

  @property
  def italic_items(self):
    return self._italic_items
  @italic_items.setter
  def italic_items(self, value):
    self._italic_items = value

  @property
  def underline_items(self):
    return self._underline_items
  @underline_items.setter
  def underline_items(self, value):
    self._underline_items = value

  @property
  def items_text_color(self):
    return self._items_text_color
  @items_text_color.setter
  def items_text_color(self, value):
    self._items_text_color = value

  @property
  def items_background(self):
    return self._items_background
  @items_background.setter
  def items_background(self, value):
    self._items_background = value

  @property
  def items_font(self):
    return self._items_font
  @items_font.setter
  def items_font(self, value):
    self._items_font = value

  @property
  def items_font_size(self):
    return self._items_font_size
  @items_font_size.setter
  def items_font_size(self, value):
    self._items_font_size = value
    
  def on_mount(self, **event_args):
    document.addEventListener('keydown', self.handle_keyboard_events)
    self.dom_nodes['anvil-m3-dropdownMenu-container'].addEventListener('click', self.handle_component_click)
    self.selection_field.dom_nodes['text-field-input'].addEventListener('focus', self.handle_selection_field_focus)
    self.selection_field.dom_nodes['text-field-input'].addEventListener('blur', self.handle_selection_field_blur)
    self.shield.addEventListener('click', self.remove_shield_handler)
    self.menuNode.addEventListener('click', self.child_clicked)
    
  def on_cleanup(self, **event_args):
    document.removeEventListener('keydown', self.handle_keyboard_events)
    self.dom_nodes['anvil-m3-dropdownMenu-container'].removeEventListener('click', self.handle_component_click)
    self.selection_field.dom_nodes['text-field-input'].removeEventListener('focus', self.handle_selection_field_focus)
    self.selection_field.dom_nodes['text-field-input'].removeEventListener('blur', self.handle_selection_field_blur)
    self.shield.removeEventListener('click', self.remove_shield_handler)
    self.menuNode.removeEventListener('click', self.child_clicked)

  def handle_selection_field_focus(self, event):
    self._has_focus = True
    
  def handle_selection_field_blur(self, event):
    self._has_focus = False
    
  def handle_keyboard_events(self, event):
    if not self._has_focus:
      return
    else:
      action_keys = set(["ArrowUp", "ArrowDown", "Tab", "Escape", " ", "Enter"])
      open_keys = set(["ArrowUp", "ArrowDown", " ", "Enter"])
      if not self.menu.visible:
        if event.key in open_keys:
          self.set_menu_visibility(True)          
        return
        
      if event.key not in action_keys: #   #TODO: eventually want to use this to jump somewhere in the list
        return
      
      if event.key is "ArrowUp" or event.key is "ArrowDown":
        self.iterate_hover(event.key is "ArrowDown")
        return

      if event.key in ["Tab", "Escape"]:
        self.close_menu()

      if (event.key is " "): #space key as " " is stupid
        event.preventDefault()
        self.attempt_select()
      if (event.key is "Enter"):
        self.attempt_select()
        
  def close_menu(self):
    self.remove_shield()
    self.set_menu_visibility(False)
    
  def iterate_hover(self, inc = True):
    if inc:
      if self._hoverIndex is None or self._hoverIndex is (len(self._children) - 1):
        self._hoverIndex = -1
      self._hoverIndex += 1
    else:
      if self._hoverIndex is None or self._hoverIndex is 0:
        self._hoverIndex = len(self._children)
      self._hoverIndex -= 1
    self.update_hover_styles()
    
  def attempt_select(self):
    if not self._hoverIndex is None:
      self._children[self._hoverIndex].raise_event("click")
    self.close_menu()
    
  def clear_hover_styles(self):
    if self._children is not None:
      for child in self._children:
        if isinstance(child, MenuItem):
          child.dom_nodes['anvil-m3-menuItem-container'].classList.toggle('anvil-m3-menuItem-container-keyboardHover', False)

  def update_hover_styles(self):
    self.clear_hover_styles()
    if self._hoverIndex is None:
      return
    self._children[self._hoverIndex].dom_nodes['anvil-m3-menuItem-container'].classList.toggle('anvil-m3-menuItem-container-keyboardHover', True)
    
  def handle_component_click(self, event):
    self.set_menu_visibility()

  def set_menu_visibility(self, value = None):
    if (value is None):
      value = not self.menu.visible
    self.menu.visible = value
    if value:
      if not self.label_text and self.placeholder:
        self.selection_field.dom_nodes['label-text'].innerText = ""
      if not anvil.designer.in_designer:
        self.place_shield()
        self.selection_field.trailing_icon = "arrow_drop_up"
      self.get_textfield_measurements()
      self.update_menu_placement()
    else:
      if not self.label_text and self.placeholder and self.selected_value is None:
        self.selection_field.dom_nodes['label-text'].innerText = self.placeholder
      self.selection_field.trailing_icon = "arrow_drop_down"
      self.menuNode.removeAttribute("style")
      if self.selected_value is None:
        self._hoverIndex = None

  def update_menu_placement(self):
    menuNode = self.menu.dom_nodes['anvil-m3-menu-items-container']
    menuNode.removeAttribute("style")
    menuNode.style.maxWidth = "unset"
    self._window_size = {"width": window.innerWidth, "height": window.innerHeight}
    self._menu_size = {"width": menuNode.offsetWidth, "height": menuNode.offsetHeight}
    # horizontal placement
    menuNode.style.left = f"{math.floor(self._box_positioning['left'])}px"
    menuNode.style.width = f"{math.floor(self._box_positioning['width'])}px"
    
    # vertical placement
    menuTop = self._box_positioning['bottom']
    menuBottom = menuTop + self._menu_size['height']
    spaceAtTop = self._box_positioning['top']
    spaceAtBottom = self._window_size['height'] - self._box_positioning['bottom']
    
    # menu won't fit in the standrd spot under the text field
    if spaceAtBottom < self._menu_size["height"]:
      # place the menu at the bottom
      if spaceAtBottom > spaceAtTop:
        menuNode.style.top = f"{math.floor(menuTop + 1)}px"
        menuNode.style.height = f"{math.floor(spaceAtBottom - 10)}px"
      # place the menu at the top
      else:
        menuNode.style.bottom = f"{math.floor(7 + self._window_size['height'] - self._box_positioning['top'])}px"
        if spaceAtTop < self._menu_size["height"]:
          menuNode.style.height = f"{math.floor(spaceAtTop - 10)}px"
    else:
       menuNode.style.top = f"{math.floor(menuTop + 1)}px"
      
  def get_textfield_measurements(self):
    rect = self.selection_field.dom_nodes['text-field-input'].getBoundingClientRect()
    self._box_positioning = {
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
    self.close_menu()
    
  def remove_shield(self):
    if document.contains(self.shield):
      document.body.removeChild(self.shield)
      document.body.style.removeProperty("overflow")

  def child_clicked(self, event):
    event.stopPropagation()
    self.close_menu()
    if self.selected_value is None:
      self._hoverIndex = None
    else:
      self._hoverIndex = self._children.index(self._selected_menuItem)
    self.update_hover_styles()
      
  def form_show(self, **event_args):
    self.create_menu_items()
    self._children = self.menu.get_components()
    if anvil.designer.in_designer:
      if not self.label_text:
        self.label_text = anvil.designer.get_design_name(self)
  def create_menu_items(self):
    p = MenuItem()
    p.text = self.placeholder if self.placeholder else "Clear Selection"
    p.italic = self.italic_items
    p.underline = self.underline_items
    p.text_color = self.items_text_color
    p.background = self.items_background
    p.font = self.items_font
    p.font_size = self.items_font_size
    p.hide_leading_icon = True
    
    def handle_select_placeholder(**e):
      if self.allow_none: self.selected_value = None

    if not self.allow_none:
      p.enabled = False
    
    if self.allow_none or self.placeholder:
      p.add_event_handler('click', handle_select_placeholder)
      self.menu.add_component(p, slot="anvil-m3-menu-slot")
    
    for item in self.items:
      selection = MenuItem()
      selection.hide_leading_icon = True
      
      selection.bold = self.bold_items
      selection.italic = self.italic_items
      selection.underline = self.underline_items
      selection.text_color = self.items_text_color
      selection.background = self.items_background
      selection.font = self.items_font
      selection.font_size = self.items_font_size
      
      if type(item) is list:
        selection.text = item[0]
      else:
        selection.text = item
        
      def handle_selection_click(value = item, menuItem = selection, **e): 
        self.selected_value = value
        self._selected_menuItem = menuItem
          
      selection.add_event_handler('click', handle_selection_click)
      self.menu.add_component(selection, slot="anvil-m3-menu-slot")
 
# DESIGNER INTERACTIONS
  def _anvil_get_interactions_(self):
    return [
      {
      "type": "whole_component",
      "title": "Edit Label",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "label_text", self.selection_field.dom_nodes['label-text'])
      }
    }]