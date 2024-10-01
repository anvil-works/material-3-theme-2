from ._anvil_designer import IconButtonTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.designer
from ...Functions import innerText_property, tooltip_property, role_property, enabled_property, color_property, style_property, property_with_callback, border_property, margin_property
from anvil import HtmlTemplate

#TODO: all classes should have anvil-m3 prefix

class IconButton(IconButtonTemplate):
  def __init__(self, **properties):
    self._props = properties
    self._tooltip_node = None
    self._appearance = ""
    self.init_components(**properties)
    
    self._handle_click = self._handle_click

    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)

  def _on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-iconbutton-container'].addEventListener('click', self._handle_click)
  def _on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-iconbutton-container'].removeEventListener('click', self._handle_click)
    

  def _handle_click(self, event):
    event.preventDefault()
    self.raise_event("click")

  def _appearance_setter(self, value):
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("anvil-m3-filled", False)
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("anvil-m3-tonal", False)
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("anvil-m3-outlined", False)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("anvil-m3-filled", False)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("anvil-m3-tonal", False)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("anvil-m3-outlined", False)
    
    if value and value != 'standard':
      self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle(f'anvil-m3-{value}', True)
      self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle(f'anvil-m3-{value}', True)

  #!componentProp(material_3.IconButton)!1: {name:"align",type:"enum",description:"The position of this component in the available space."} 
  #!componentProp(material_3.IconButton)!1: {name:"appearance",type:"enum",options:["standard", "filled", "tonal", "outlined"],description:"A predefined style for this component."}  
  #!componentProp(material_3.IconButton)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!componentProp(material_3.IconButton)!1: {name:"enabled",type:"boolean",description:"If True, this component allows user interaction."}
  #!componentProp(material_3.IconButton)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles"} 
  #!componentProp(material_3.IconButton)!1: {name:"icon",type:"enum",description:"The icon to display on this component."} 
  #!componentProp(material_3.IconButton)!1: {name:"icon_color",type:"color",description:"The colour of the icon displayed on this component."}
  #!componentProp(material_3.IconButton)!1: {name:"background",type:"color",description:"The colour of the background of this component."}
  #!componentProp(material_3.IconButton)!1: {name:"margin",type:"margin",description:"The margin (pixels) of the component."}
  #!componentProp(material_3.IconButton)!1: {name:"border",type:"string",description:"The border of this component. Can take any valid CSS border value."}
  #!componentProp(material_3.IconButton)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  #!componentProp(material_3.IconButton)!1: {name:"tag",type:"object",description:"Use this property to store any extra data for the component."}

  #!componentEvent(material_3.IconButton)!1: {name: "click", description: "When the component is clicked.", parameters:[]}
  
  appearance = property_with_callback("appearance", _appearance_setter)
  visible = HtmlTemplate.visible
  # icon = innerText_property('anvil-m3-iconbutton-icon', 'icon')
  enabled = enabled_property('anvil-m3-iconbutton-container')
  align = style_property('anvil-m3-iconbutton-component', 'justifyContent', 'align')
  border = border_property('anvil-m3-iconbutton-container')
  icon_color = color_property('anvil-m3-iconbutton-icon', 'color', 'icon_color')
  background_color = color_property('anvil-m3-iconbutton-container', 'backgroundColor', 'background_color')
  margin = margin_property('anvil-m3-iconbutton-component')
  role = role_property('anvil-m3-iconbutton-container')
  tooltip = tooltip_property('anvil-m3-iconbutton-component')

  @property
  def icon(self):
    return self._props.get('icon')

  @icon.setter
  def icon(self, value):
    self._props['icon'] = value
    self.dom_nodes['anvil-m3-iconbutton-icon'].innerText = value[3:]

#!defClass(material_3,IconButton,anvil.Component)!: