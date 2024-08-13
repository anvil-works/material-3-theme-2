from ._anvil_designer import ButtonMenuTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from anvil.js import window, get_dom_node
from anvil.js.window import document
import random, string, math
import anvil.designer
from ..MenuItem import MenuItem
from ...Functions import property_with_callback, color_property, border_property, role_property
from ...utils import fui, noop

class ButtonMenu(ButtonMenuTemplate):
  def __init__(self, **properties):
    self._props = properties
    self._design_name = ""
    self.init_components(**properties)
    self._open = False
    self._cleanup = noop

    self._hoverIndex = None
    self._itemIndices = set()
    self._children = None

    self._menuNode = self.dom_nodes['anvil-m3-buttonMenu-items-container']
    self._btnNode = get_dom_node(self.menu_button).querySelector("button")

    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)

  def _on_mount(self, **event_args):
    document.addEventListener('keydown', self._handle_keyboard_events)
    self._menuNode.addEventListener('click', self._child_clicked)
    self._btnNode.addEventListener('click', self._handle_click)
    document.addEventListener('click', self._body_click)
    # this is a bit of a hack, we still have a reference to the dom node but we've moved it to the body
    # this gets around the whole, anvil containers love to set their overflow to hidden
    document.body.append(self._menuNode)

    self._cleanup = fui.auto_update(self._btnNode, self._menuNode, placement="bottom-start")
  
  def _on_cleanup(self, **event_args):
    document.removeEventListener('keydown', self._handle_keyboard_events)
    self._menuNode.removeEventListener('click', self._child_clicked)
    document.removeEventListener('click', self._body_click)
    self._cleanup()
    # remove the menu node we put on the body
    self._menuNode.remove()


  def _handle_click(self, event):
    if self.enabled:
      self.raise_event('click')
    
  menu_background_color = color_property('anvil-m3-buttonMenu-items-container', 'background', 'menu_background_color')
  menu_border = border_property('anvil-m3-buttonMenu-items-container', 'menu_border')
  visible = HtmlTemplate.visible
  
  def _set_text(self, value):
    v = value
    self.menu_button.dom_nodes['anvil-m3-button-text'].classList.toggle('anvil-m3-textlessComponentText', False)
    if anvil.designer.in_designer and not value:
      v = self._design_name
      self.menu_button.dom_nodes['anvil-m3-button-text'].classList.toggle('anvil-m3-textlessComponentText', True)
    self.menu_button.text = v
  text = property_with_callback("text", _set_text)


  def _set_appearance(self, value):
    self.menu_button.appearance = value
  appearance = property_with_callback("appearance", _set_appearance)

  def _set_tooltip(self, value):
    self.menu_button.tooltip = value
  tooltip = property_with_callback("tooltip", _set_tooltip)

  def _set_enabled(self, value):
    self.menu_button.enabled = value
  enabled = property_with_callback("enabled", _set_enabled)

  def _set_bold(self, value):
    self.menu_button.bold = value
  bold = property_with_callback("bold", _set_bold)

  def _set_italic(self, value):
    self.menu_button.italic = value
  italic = property_with_callback("italic", _set_italic)
 
  def _set_underline(self, value):
    self.menu_button.underline = value
  underline = property_with_callback("underline", _set_underline)

  def _set_button_border(self, value):
    self.menu_button.border = value
  button_border = property_with_callback("button_border", _set_button_border)

  def _set_button_background_color(self, value):
    self.menu_button.background_color = value
  button_background_color = property_with_callback("button_background_color", _set_button_background_color)

  def _set_button_text_color(self, value):
    self.menu_button.text_color = value
  button_text_color = property_with_callback("button_text_color", _set_button_text_color)

  def _set_button_font_size(self, value):
    self.menu_button.font_size = value
  button_font_size = property_with_callback("button_font_size", _set_button_font_size)

  def _set_icon(self, value):
    self.menu_button.icon = value
  icon = property_with_callback("icon", _set_icon)

  def _set_icon_color(self, value):
    self.menu_button.icon_color = value
  icon_color = property_with_callback("icon_color", _set_icon_color)

  def _set_icon_size(self, value):
    self.menu_button.icon_size = value
  icon_size = property_with_callback("icon_size", _set_icon_size)

  def _set_icon_position(self, value):
    self.menu_button.icon_position = value
  icon_position = property_with_callback("icon_position", _set_icon_position)

  def _set_margin(self, value):
    self.menu_button.margin = value
  margin = property_with_callback("margin", _set_margin)

  def _set_align(self, value):
    self.dom_nodes['anvil-m3-buttonMenu-container'].style.justifyContent = value
  align = property_with_callback("align", _set_align)

  def _set_button_font_family(self, value):
    self.menu_button.font_family = value
  button_font_family = property_with_callback("button_font_family", _set_button_font_family)

  def _set_role(self, value):
    self.menu_button.role = value
  role = property_with_callback("role", _set_role)

  def _toggle_menu_visibility(self, **event_args):
    self._set_visibility()

  def _set_visibility(self, value = None):
    classes = self._menuNode.classList
    if value is not None:
      classes.toggle('anvil-m3-buttonMenu-items-hidden', not value)
    else:
      classes.toggle('anvil-m3-buttonMenu-items-hidden')
      
    self._open = not classes.contains('anvil-m3-buttonMenu-items-hidden')
    if self._open:
      self._get_hover_index_information()
    else:
      self._hoverIndex = None
      self._clear_hover_styles()

  def _set_menu_items(self, value=[]):
    for i in value:
      self.add_component(i, slot='anvil-m3-buttonMenu-slot')
  menu_items = property_with_callback('menu_items', _set_menu_items)


  def _child_clicked(self, event):
    # do the click action. The child should handle this
    self._set_visibility(False)
    if self.enabled:
      self.raise_event("click")

  def _body_click(self, event):
    if self._btnNode.contains(event.target) or self._menuNode.contains(event.target):
      return
    self._set_visibility(False)
  
  def _get_hover_index_information(self):
    self._children = self.get_components()[1:]
    for i in range(0, len(self._children)):
      if isinstance(self._children[i], MenuItem):
        self._itemIndices.add(i)
   
  def _handle_keyboard_events(self, event):
    if not self._open:
      return

    action_keys = set(["ArrowUp", "ArrowDown", "Tab", "Escape", " ", "Enter"])
    if event.key not in action_keys:
      #TODO: eventually want to use this to jump somewhere in the list
      return
    
    if event.key in ["ArrowUp", "ArrowDown"]:
      self._iterate_hover(event.key == "ArrowDown")
      return
      
    # if event.key is "Tab":
    #   pass
    hover = self._hoverIndex #holding value for situation like alerts where it awaits 
    self._set_visibility(False)
    
    def attemptSelect():
      event.preventDefault();
      if hover is not None:
        self._children[hover].raise_event("click")
    
    if event.key == " ": #space key as " " is stupid
      attemptSelect()
    if event.key == "Enter":
      attemptSelect()
      
  def _iterate_hover(self, inc = True):
    if inc:
      if self._hoverIndex is None or self._hoverIndex is (len(self._children) - 1):
        self._hoverIndex = -1
      while True:
        self._hoverIndex += 1
        if self._hoverIndex in self._itemIndices:
          break;
    else:
      if self._hoverIndex is None or self._hoverIndex == 0:
        self._hoverIndex = len(self._children)
      while True:
        self._hoverIndex -= 1
        if self._hoverIndex in self._itemIndices:
          break; 
    self._update_hover_styles();

  def _clear_hover_styles(self):
    if self._children is not None:
      for child in self._children:
        if isinstance(child, MenuItem):
          child.dom_nodes['anvil-m3-menuItem-container'].classList.toggle('anvil-m3-menuItem-container-keyboardHover', False)

  def _update_hover_styles(self):
    self._clear_hover_styles()
    self._children[self._hoverIndex].dom_nodes['anvil-m3-menuItem-container'].classList.toggle('anvil-m3-menuItem-container-keyboardHover', True)
    
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
    self._set_visibility(True)

  def _on_select_other(self):
    self._set_visibility(False)

  def form_show(self, **event_args):
    if anvil.designer.in_designer:
      self._design_name = anvil.designer.get_design_name(self)
      if not self.text:
        self.menu_button.text = self._design_name

  #!componentProp(material_3.ButtonMenu)!1: {name:"align",type:"enum",options:["left", "right", "center"],description:"The position of this component in the available space."} 
  #!componentProp(material_3.ButtonMenu)!1: {name:"appearance",type:"enum",options:["filled", "elevated", "tonal", "outlined", "text"],description:"A predefined style for the Button."}  
  #!componentProp(material_3.ButtonMenu)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!componentProp(material_3.ButtonMenu)!1: {name:"enabled",type:"boolean",description:"If True, this component allows user interaction."}
  #!componentProp(material_3.ButtonMenu)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles"} 
  #!componentProp(material_3.ButtonMenu)!1: {name:"button_text_color",type:"color",description:"The colour of the text on the Button."} 
  #!componentProp(material_3.ButtonMenu)!1: {name:"button_font_family",type:"string",description:"The font family to use for the Button"}
  #!componentProp(material_3.ButtonMenu)!1: {name:"icon",type:"enum",description:"The icon to display on the Button."} 
  #!componentProp(material_3.ButtonMenu)!1: {name:"text",type:"string",description:"The text displayed on the Button"}
  #!componentProp(material_3.ButtonMenu)!1: {name:"button_font_size",type:"number",description:"The font size of the text displayed on the Button."}
  #!componentProp(material_3.ButtonMenu)!1: {name:"underline",type:"boolean",description:"If True, the Button’s text will be underlined."}
  #!componentProp(material_3.ButtonMenu)!1: {name:"italic",type:"boolean",description:"If True, the Button’s text will be italic."}
  #!componentProp(material_3.ButtonMenu)!1: {name:"bold",type:"boolean",description:"If True, the Button’s text will be bold."}
  #!componentProp(material_3.ButtonMenu)!1: {name:"icon_color",type:"color",description:"The colour of the icon displayed on the Button."}
  #!componentProp(material_3.ButtonMenu)!1: {name:"menu_background_color",type:"color",description:"The colour of the menu."}
  #!componentProp(material_3.ButtonMenu)!1: {name:"menu_border",type:"color",description:"The border of the menu. Can take any valid CSS border value."}
  #!componentProp(material_3.ButtonMenu)!1: {name:"icon_size",type:"number",description:"The size (pixels) of the icon displayed on this component."}
  #!componentProp(material_3.ButtonMenu)!1: {name:"button_background_color",type:"color",description:"The colour of the background of the Button."}
  #!componentProp(material_3.ButtonMenu)!1: {name:"margin",type:"margin",description:"The margin (pixels) of the component."}
  #!componentProp(material_3.ButtonMenu)!1: {name:"button_border",type:"string",description:"The border of the Button. Can take any valid CSS border value."}
  #!componentProp(material_3.ButtonMenu)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  #!componentProp(material_3.ButtonMenu)!1: {name:"icon_position",type:"enum",options:["left", "right"],description:"The alignment of the icon on this component."}
  #!componentProp(material_3.ButtonMenu)!1: {name:"menu_items",type:"object",description:"A list of components to be added to the menu."}

  #!componentEvent(material_3.ButtonMenu)!1: {name: "click", description: "When the Button is clicked.", parameters:[]}

#!defClass(material_3, ButtonMenu, anvil.Component)!:
