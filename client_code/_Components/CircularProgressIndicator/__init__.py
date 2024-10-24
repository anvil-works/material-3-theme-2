from ._anvil_designer import CircularProgressIndicatorTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from ...Functions import tooltip_property, role_property, theme_color_to_css, innerText_property, color_property, style_property, property_with_callback, margin_property
from math import pi, cos, sin
from ...utils.properties import get_unset_margin

class CircularProgressIndicator(CircularProgressIndicatorTemplate):
  def __init__(self, **properties):
    self.tag = ComponentTag()
    self._tooltip_node = None
    self._props = properties
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def _anvil_get_unset_property_values_(self):
    el = self.dom_nodes["anvil-m3-progressindicator-component"]
    m = get_unset_margin(el, self.margin)
    return {"margin": m}

  visible = HtmlTemplate.visible
  align = style_property('anvil-m3-progressindicator-component', 'justifyContent', 'align')
  margin = margin_property('anvil-m3-progressindicator-component')
  tooltip = tooltip_property('anvil-m3-progressindicator')
  role = role_property('anvil-m3-progressindicator')

  @property
  def color(self):
    return self._props.get('color')

  @color.setter
  def color(self, value):
    if value: value = theme_color_to_css(value)
    self.dom_nodes['anvil-m3-progressindicator-arc'].style['stroke'] = value
    self.dom_nodes['anvil-m3-progressindicator-arc-indeterminate'].style['stroke'] = value
    self._props['color'] = value

  def _update_determinance(self, value):
    v = value is "determinate"
    self.dom_nodes['anvil-m3-progressindicator-indeterminate'].classList.toggle('anvil-m3-progressindicator-hidden', v)
    self.dom_nodes['anvil-m3-progressindicator-determinate'].classList.toggle('anvil-m3-progressindicator-hidden', not v)
  type = property_with_callback("type", _update_determinance)

  def _update_progress(self, value):
    v = max(min(value or 0, 100), 0)
    self._draw_path(v)
  progress = property_with_callback("progress", _update_progress)

  def _draw_path(self, percent):
    cx, cy = 24, 24 #center of circle
    rx, ry = 18, 18 #major/minor radius
    t1 = 3 * pi / 2 #start angle in radians
    phi = 0 # Rotation on the whole in radians
    
    radian = pi * percent /  50
    delta = radian # Angle to sweep in radians (positive)

    if percent < 100:
      radian = pi * percent /  50
      delta = radian # Angle to sweep in radians (positive)
      d = self._f_svg_ellipse_arc(cx, cy, rx, ry, t1, delta)
      
      self.dom_nodes['anvil-m3-progressindicator-arc'].setAttribute("d", d)
    else:
      radian = pi * 99 /  50
      delta = radian # Angle to sweep in radians (positive)
      d = self._f_svg_ellipse_arc(cx, cy, rx, ry, t1, delta)
      self.dom_nodes['anvil-m3-progressindicator-arc'].setAttribute("d", d + " Z")

  def _f_matrix_times(self, matrix, vector):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    x, y = vector[0], vector[1]
    return [a * x + b * y, c * x + d * y]

  def _f_rotate_matrix(self, x):
    return [[cos(x), -sin(x)],
            [sin(x), cos(x)]]

  def _f_vec_add(self, vector1, vector2):
    return [vector1[0] + vector2[0], vector1[1] + vector2[1]]

  def _f_svg_ellipse_arc(self, cx, cy, rx, ry, t1, delta, phi = 0):
    delta = delta % (2 * pi)
    rotMatrix = self._f_rotate_matrix(phi)
    sX, sY = self._f_vec_add(self._f_matrix_times(rotMatrix, [rx * cos(t1), ry * sin(t1)]), [cx, cy])
    eX, eY = self._f_vec_add(self._f_matrix_times(rotMatrix, [rx * cos(t1 + delta), ry * sin(t1 + delta)]), [cx, cy])
    fA = 1 if delta > pi else 0
    fS = 1 if delta > 0 else 0
    return f"M {sX} {sY} A {rx} {ry} {(phi / (2 * pi)) * 360} {fA} {fS} {eX} {eY}"

  #!componentProp(material_3.CircularProgressIndicator)!1: {name:"color",type:"color",description:"The colour of the progress bar"}  
  #!componentProp(material_3.CircularProgressIndicator)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!componentProp(material_3.CircularProgressIndicator)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles"} 
  #!componentProp(material_3.CircularProgressIndicator)!1: {name:"progress",type:"number",description:"The progress of the CircularProgressIndicator."}
  #!componentProp(material_3.CircularProgressIndicator)!1: {name:"margin",type:"margin",description:"The margin (pixels) of the component."}
  #!componentProp(material_3.CircularProgressIndicator)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  #!componentProp(material_3.CircularProgressIndicator)!1: {name:"tag",type:"object",description:"Use this property to store any extra data for the component."}
  #!componentProp(material_3.CircularProgressIndicator)!1: {name:"type",type:"enum",options:["determinate", "indeterminate"],description:"Display a determinate or indeterminate progress indicator. Use determinate to set the progress with the progress property. Use indeterminate to express an unspecified amount of wait time."}

#!defClass(material_3,CircularProgressIndicator,anvil.Component)!:
