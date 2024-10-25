from ._anvil_designer import IconButtonTemplate
from anvil import *
import anvil.server
import anvil.designer
from ...Functions import tooltip_property, role_property, enabled_property, color_property, style_property, property_with_callback, border_property, margin_property
from anvil import HtmlTemplate
from ...utils.properties import get_unset_margin, anvil_prop

class IconButton(IconButtonTemplate):
  def __init__(self, **properties):
    self.tag = ComponentTag()
    self._props = properties
    self._tooltip_node = None
    self._appearance = ""
    self.init_components(**properties)
    self.dom_nodes['anvil-m3-iconbutton-container'].addEventListener('click', self._handle_click)

  def _anvil_get_unset_property_values_(self):
    el = self.dom_nodes["anvil-m3-iconbutton-container"]
    m = get_unset_margin(el, self.margin)
    return {"margin": m}
    
  def _handle_click(self, event):
    event.preventDefault()
    self.raise_event("click")

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

  visible = HtmlTemplate.visible
  enabled = enabled_property('anvil-m3-iconbutton-container')
  align = style_property('anvil-m3-iconbutton-component', 'justifyContent', 'align')
  border = border_property('anvil-m3-iconbutton-container')
  icon_color = color_property('anvil-m3-iconbutton-icon', 'color', 'icon_color')
  background_color = color_property('anvil-m3-iconbutton-container', 'backgroundColor', 'background_color')
  margin = margin_property('anvil-m3-iconbutton-container')
  role = role_property('anvil-m3-iconbutton-container')
  tooltip = tooltip_property('anvil-m3-iconbutton-component')

  @anvil_prop
  def icon(self, value):
    self.dom_nodes['anvil-m3-iconbutton-icon'].innerText = value[3:]

  @anvil_prop
  def appearance(self, value):
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("anvil-m3-filled", False)
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("anvil-m3-tonal", False)
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("anvil-m3-outlined", False)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("anvil-m3-filled", False)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("anvil-m3-tonal", False)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("anvil-m3-outlined", False)
    if value and value != 'standard':
      self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle(f'anvil-m3-{value}', True)
      self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle(f'anvil-m3-{value}', True)
  
#!defClass(material_3,IconButton,anvil.Component)!:
