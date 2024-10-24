from ._anvil_designer import DividerTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Functions import color_property, role_property, margin_property
from ...utils.properties import get_unset_margin

class Divider(DividerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.tag = ComponentTag()
    self._props = properties
    self.init_components(**properties)

  def _anvil_get_unset_property_values_(self):
    el = self.dom_nodes["anvil-m3-divider"]
    m = get_unset_margin(el, self.margin)
    return {"margin": m}

  #!componentEvent(material_3.Divider)!1: {name: "show", description: "When the Divider is shown on the screen."}
  #!componentEvent(material_3.Divider)!1: {name: "hide", description: "When the Divider is removed from the screen."}

  #!componentProp(material_3.Divider)!1: {name:"type",type:"enum",options:["full_width", "inset"],description:"Display the Divider across the full width of the container or inset."}
  #!componentProp(material_3.Divider)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!componentProp(material_3.Divider)!1: {name:"color",type:"color",description:"The colour of this component."}
  #!componentProp(material_3.Divider)!1: {name:"margin",type:"margin",description:"The margin (pixels) of the component."}
  #!componentProp(material_3.Divider)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles."} 

  visible = HtmlTemplate.visible
  color = color_property('anvil-m3-divider', 'border-color', 'color')
  role = role_property('anvil-m3-divider')
  margin = margin_property('anvil-m3-divider')
  
  @property
  def type(self):
    return self._props.get('type')

  @type.setter
  def type(self, value):
    divider = self.dom_nodes['anvil-m3-divider']
    self._props['type'] = value
    value = value.lower().replace(' ', '-')
    divider.className = "anvil-m3-divider"
    self.dom_nodes['anvil-m3-divider'].classList.add(value)

#!defClass(material_3, Divider, anvil.Component)!:
