from ._anvil_designer import CardTemplate
from anvil import *
import anvil.designer
from anvil import HtmlTemplate
from anvil.js import get_dom_node
from anvil.js import window
from ...utils.properties import get_unset_spacing, anvil_prop, tooltip_property, role_property, style_property, spacing_property, margin_property, padding_property, color_property, border_property

class Card(CardTemplate):
  def __init__(self, **properties):
    self.tooltip_node = None
    self.tag = ComponentTag()
    self._props = properties
    self._tooltip_node = None
    self.init_components(**properties)
    
  def _anvil_get_unset_property_values_(self):
    el = self.dom_nodes["anvil-m3-card"]
    rv = get_unset_spacing(el, el, self.spacing)
    return {"spacing": rv}

  def add_component(self, component, slot="card-content-slot", **layout_props):
    super().add_component(component, slot=slot, **layout_props)
    
  def _set_class_of_nodes(self, appearance, val):
    self.dom_nodes['anvil-m3-card'].classList.toggle(f'anvil-m3-{appearance}', val)
    self.dom_nodes['content'].classList.toggle(f'anvil-m3-{appearance}', val)

  @anvil_prop
  def appearance(self, value):
    for appearance in ['outlined', 'filled', 'elevated']:
      self._set_class_of_nodes(appearance, False)
    self._set_class_of_nodes(value, True)

  @anvil_prop
  def orientation(self, value):
    for c in ['anvil-m3-card-direction-column', 'anvil-m3-card-direction-row']:
      self.dom_nodes['anvil-m3-card'].classList.remove(c)
    self.dom_nodes['anvil-m3-card'].classList.add(f'anvil-m3-card-direction-{value}')

  spacing = spacing_property('anvil-m3-card')
  tooltip = tooltip_property('anvil-m3-card')
  border = style_property('anvil-m3-card', 'border', 'border')
  role = role_property('anvil-m3-card')
  align = style_property('anvil-m3-card', 'justifyContent', 'align')
  visible = HtmlTemplate.visible
  background_color = color_property('anvil-m3-card', 'backgroundColor', 'background_color')

  #!componentProp(material_3.Card)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!componentProp(material_3.Card)!1: {name:"border",type:"string",description:"The border of this component. Can take any valid CSS border value."}
  #!componentProp(material_3.Card)!1: {name:"background_color",type:"color",description:"The color of the background of this component."}
  #!componentProp(material_3.Card)!1: {name:"align",type:"enum",description:"The position of this component in the available space."} 
  #!componentProp(material_3.Card)!1: {name:"spacing",type:"spacing",description:"The margin and padding (pixels) of the component."}
  #!componentProp(material_3.Card)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  #!componentProp(material_3.Card)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles"} 
  #!componentProp(material_3.Card)!1: {name:"tag",type:"object",description:"Use this property to store any extra data for the component."}
  #!componentProp(material_3.Card)!1: {name:"appearance",type:"enum",options:["elevated", "filled", "outlined"],description:"A predefined style for this component."}
  #!componentProp(material_3.Card)!1: {name:"orientation",type:"enum",options:["column", "row"],description:"The orientation of the content in this Card"}


#!defClass(material_3,Card, anvil.Component)!:
