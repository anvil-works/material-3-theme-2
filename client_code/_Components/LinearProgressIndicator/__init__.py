from ._anvil_designer import LinearProgressIndicatorTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from ...Functions import tooltip_property, property_with_callback, margin_property, theme_color_to_css, role_property, color_property
from ...utils.properties import get_unset_margin

class LinearProgressIndicator(LinearProgressIndicatorTemplate):
  def __init__(self, **properties):
    self._tooltip_node = None
    self.tag = ComponentTag()
    self._props = properties
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def _anvil_get_unset_property_values_(self):
    el = self.dom_nodes["anvil-m3-progressindicator-linear"]
    m = get_unset_margin(el, self.margin)
    return {"margin": m}

  visible = HtmlTemplate.visible
  tooltip = tooltip_property('anvil-m3-progressindicator-linear')
  role = role_property('anvil-m3-progressindicator-linear')
  
  @property
  def progress_color(self):
    return self._props.get('progress_color')

  @progress_color.setter
  def progress_color(self, value):
    if value: value = theme_color_to_css(value)
    self.dom_nodes['anvil-m3-progressindicator-indicator'].style['stroke'] = value
    self.dom_nodes['anvil-m3-progressindicator-indicator-indeterminate'].style['stroke'] = value
    self.dom_nodes['anvil-m3-progressindicator-indicator-indeterminate-2'].style['stroke'] = value
    self._props['progress_color'] = value

  @property
  def track_color(self):
    return self._props.get('track_color')

  @track_color.setter
  def track_color(self, value):
    if value: value = theme_color_to_css(value)
    self.dom_nodes['anvil-m3-progressindicator-indeterminate'].style.backgroundColor = value
    self.dom_nodes['anvil-m3-progressindicator-determinate'].style.backgroundColor = value
    self._props['track_color'] = value

  def _update_determinance(self, value):
    v = value == "determinate"
    self.dom_nodes['anvil-m3-progressindicator-indeterminate'].classList.toggle('anvil-m3-progressindicator-hidden', v)
    self.dom_nodes['anvil-m3-progressindicator-determinate'].classList.toggle('anvil-m3-progressindicator-hidden', not v)

  type = property_with_callback("type", _update_determinance)

  def _update_progress(self, value):
    v = max(min(value or 0, 100), 0)
    self.dom_nodes['anvil-m3-progressindicator-indicator'].setAttribute("x2", f"{v}%")
    
  progress = property_with_callback("progress", _update_progress)
  margin= margin_property('anvil-m3-progressindicator-linear')

  #!componentProp(material_3.LinearProgressIndicator)!1: {name:"progress_color",type:"color",description:"The colour of the progress bar"}  
  #!componentProp(material_3.LinearProgressIndicator)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!componentProp(material_3.LinearProgressIndicator)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles"} 
  #!componentProp(material_3.LinearProgressIndicator)!1: {name:"progress",type:"number",description:"The progress of the LinearProgressIndicator."}
  #!componentProp(material_3.LinearProgressIndicator)!1: {name:"margin",type:"margin",description:"The margin (pixels) of the component."}
  #!componentProp(material_3.LinearProgressIndicator)!1: {name:"track_color",type:"color",description:"The colour of the LinearProgressIndicator track."}
  #!componentProp(material_3.LinearProgressIndicator)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  #!componentProp(material_3.LinearProgressIndicator)!1: {name:"tag",type:"object",description:"Use this property to store any extra data for the component."}
  #!componentProp(material_3.LinearProgressIndicator)!1: {name:"type",type:"enum",options:["determinate", "indeterminate"],description:"Display a determinate or indeterminate progress indicator. Use determinate to set the progress with the progress property. Use indeterminate to express an unspecified amount of wait time."}

#!defClass(material_3,LinearProgressIndicator,anvil.Component)!:
