from ._anvil_designer import MenuItemTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
from anvil import HtmlTemplate
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Functions import property_with_callback, innerText_property, spacing_property, enabled_property, underline_property, italic_property, bold_property, font_size_property, color_property, theme_color_to_css, font_family_property, tooltip_property

import anvil.designer

class MenuItem(MenuItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.tag = ComponentTag()
    self._props = properties
    self._tooltip_node = None
    self.init_components(**properties)
    self.dom_nodes['anvil-m3-menuItem-container'].addEventListener("click", self.handle_click)

  @property
  def leading_icon(self):
    return self._props.get('leading_icon')
    
  @leading_icon.setter
  def leading_icon(self, value):
    self._props['leading_icon'] = value
    self.dom_nodes["anvil-m3-menuItem-leadingIcon"].innerHTML = value[3:] or " "
    if value:
      self.dom_nodes["anvil-m3-menuItem-leadingIcon"].classList.add("anvil-m3-menuItem-showLeadingIcon")
    elif not value and not self.add_icon_space:
      self.dom_nodes["anvil-m3-menuItem-leadingIcon"].classList.remove("anvil-m3-menuItem-showLeadingIcon")
    
  # text = innerText_property('anvil-m3-menuItem-labelText')
  italic = italic_property('anvil-m3-menuItem-labelText')
  bold = bold_property('anvil-m3-menuItem-labelText')
  underline = underline_property('anvil-m3-menuItem-labelText')
  font_size = font_size_property('anvil-m3-menuItem-labelText')
  leading_icon_size = font_size_property('anvil-m3-menuItem-leadingIcon', 'leading_icon_size')
  trailing_icon_size = font_size_property('anvil-m3-menuItem-trailingIcon', 'trailing_icon_size')
  font_family = font_family_property('anvil-m3-menuItem-labelText', 'font_family')
  text_color = color_property('anvil-m3-menuItem-labelText', 'color', 'text_color')
  trailing_icon_color = color_property('anvil-m3-menuItem-trailingIcon', 'color', 'trailing_icon_color')
  leading_icon_color = color_property('anvil-m3-menuItem-leadingIcon', 'color', 'leading_icon_color')
  background_color = color_property('anvil-m3-menuItem-container', 'backgroundColor', 'background')
  visible = HtmlTemplate.visible
  spacing = spacing_property('anvil-m3-menuItem-container')
  tooltip = tooltip_property('anvil-m3-menuItem-container')

  # def innerText_property(dom_node_name, prop_name="text"):
  # def set_innerText(self, value):
  #   self.dom_nodes[dom_node_name].innerText = value
  # return property_with_callback(prop_name, set_innerText)

  
  def _set_text(self, value):
    if isinstance(value, tuple):
      self.dom_nodes['anvil-m3-menuItem-labelText'].innerText = value[0]
    else:
      self.dom_nodes['anvil-m3-menuItem-labelText'].innerText = value
  text = property_with_callback("text", _set_text)

  @property
  def trailing_icon(self):
    return self._trailing_icon
    
  @trailing_icon.setter
  def trailing_icon(self, value):
    self._trailing_icon = value
    self.dom_nodes["anvil-m3-menuItem-trailingIcon"].innerText = value[3:] 
    
  @property
  def trailing_text(self):
    return self._trailing_text
    
  @trailing_text.setter
  def trailing_text(self, value):
    self._trailing_text = value
    self.dom_nodes["anvil-m3-menuItem-trailingText"].innerText = value 

  @property 
  def add_icon_space(self):
    return self._props.get('add_icon_space')
    
  @add_icon_space.setter
  def add_icon_space(self, value):
    self._props['add_icon_space'] = value
    if value:
      self.dom_nodes["anvil-m3-menuItem-leadingIcon"].classList.add("anvil-m3-menuItem-showLeadingIcon")
    elif not self.leading_icon and not value:
      self.dom_nodes["anvil-m3-menuItem-leadingIcon"].classList.remove("anvil-m3-menuItem-showLeadingIcon")
      

  @property
  def enabled(self):
    return self._enabled
    
  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    self.dom_nodes["anvil-m3-menuItem-container"].classList.toggle("anvil-m3-menuItem-disabled", not value)

  """ Functions """
  def handle_click(self, event):
    event.preventDefault() #TODO: make sure this doesn't prevent the menu from closing
    self.raise_event("click")

  def _anvil_get_interactions_(self):
    return [{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-menuItem-labelText'])
      }
    }]

  #!componentProp(material_3.MenuItem)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!componentProp(material_3.MenuItem)!1: {name:"enabled",type:"boolean",description:"If True, this component allows user interaction."}
  #!componentProp(material_3.MenuItem)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles"} 
  #!componentProp(material_3.MenuItem)!1: {name:"text_color",type:"color",description:"The colour of the text on this component."} 
  #!componentProp(material_3.MenuItem)!1: {name:"font_family",type:"string",description:"The font family to use for this component."}
  #!componentProp(material_3.MenuItem)!1: {name:"leading_icon",type:"enum",description:"The icon to display on this component."} 
  #!componentProp(material_3.MenuItem)!1: {name:"trailing_icon",type:"enum",description:"The icon to display on this component."} 
  #!componentProp(material_3.MenuItem)!1: {name:"text",type:"string",description:"The text displayed on this component."}
  #!componentProp(material_3.MenuItem)!1: {name:"trailing_text",type:"string",description:"The text to be displayed on the right side of the component. Will be to the left of the trailing icon if both exist."}
  #!componentProp(material_3.MenuItem)!1: {name:"font_size",type:"number",description:"The font size of the text displayed on this component."}
  #!componentProp(material_3.MenuItem)!1: {name:"underline",type:"boolean",description:"If True, the text will be underlined."}
  #!componentProp(material_3.MenuItem)!1: {name:"italic",type:"boolean",description:"If True, the text will be italic."}
  #!componentProp(material_3.MenuItem)!1: {name:"bold",type:"boolean",description:"If True, the text will be bold."}
  #!componentProp(material_3.MenuItem)!1: {name:"leading_icon_color",type:"color",description:"The colour of the leading icon displayed on this component."}
  #!componentProp(material_3.MenuItem)!1: {name:"trailing_icon_color",type:"color",description:"The colour of the tailing icon displayed on this component."}
  #!componentProp(material_3.MenuItem)!1: {name:"background_color",type:"color",description:"The background colour of this component."}
  #!componentProp(material_3.MenuItem)!1: {name:"leading_icon_size",type:"number",description:"The size (pixels) of the leading icon displayed on this component."}
  #!componentProp(material_3.MenuItem)!1: {name:"trailing_icon_size",type:"number",description:"The size (pixels) of the trailing icon displayed on this component."}
  #!componentProp(material_3.MenuItem)!1: {name:"spacing",type:"spacing",description:"The margin and padding (pixels) of the component."}
  #!componentProp(material_3.MenuItem)!1: {name:"add_icon_space",type:"boolean",description:"If True, add a space where the leading_icon would be so that this MenuItem is aligned with MenuItems with leading_icons."}
  #!componentProp(material_3.MenuItem)!1: {name:"tag",type:"object",description:"Use this property to store any extra data for the component."}
  #!componentProp(material_3.MenuItem)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}


  #!componentEvent(material_3.MenuItem)!1: {name: "click", description: "When the component is clicked.", parameters:[]}

#!defClass(material_3, MenuItem, anvil.Component)!:
