from ._anvil_designer import CircularProgressIndicatorTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from ...Functions import innerText_property, enabled_property, color_property, style_property, property_with_callback
from math import pi, cos, sin

class CircularProgressIndicator(CircularProgressIndicatorTemplate):
  def __init__(self, **properties):
    self._props = properties
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  visible = HtmlTemplate.visible

  def update_determinance(self, value):
    v = True if value is "determinate" else False
    self.dom_nodes['anvil-m3-progressindicator-indeterminate'].classList.toggle('anvil-m3-progressindicator-hidden', v)
    self.dom_nodes['anvil-m3-progressindicator-determinate'].classList.toggle('anvil-m3-progressindicator-hidden', not v)

  type = property_with_callback("type", update_determinance)

  def update_progress(self, value):
    v = max(min(value or 0, 100), 0)
    self.draw_path(v)
    # self.dom_nodes['anvil-m3-progressindicator-indicator'].setAttribute("x2", f"{v}%")

  progress = property_with_callback("progress", update_progress)

  def draw_path(self, percent):
    cx, cy = 24, 24 #center of circle
    rx, ry = 18, 18 #major/minor radius
    t1 = 3 * pi / 2 #start angle in radians
    phi = 0 # Rotation on the whole in radians
    
    radian = pi * percent /  50
    delta = radian # Angle to sweep in radians (positive)

    if percent < 100:
      radian = pi * percent /  50
      delta = radian # Angle to sweep in radians (positive)
      d = self.f_svg_ellipse_arc(cx, cy, rx, ry, t1, delta)
      
      self.dom_nodes['anvil-m3-progressindicator-arc'].setAttribute("d", d)
    else:
      radian = pi * 99 /  50
      delta = radian # Angle to sweep in radians (positive)
      d = self.f_svg_ellipse_arc(cx, cy, rx, ry, t1, delta)
      self.dom_nodes['anvil-m3-progressindicator-arc'].setAttribute("d", d + " Z")

  def f_matrix_times(self, matrix, vector):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    x, y = vector[0], vector[1]
    return [a * x + b * y, c * x + d * y]

  def f_rotate_matrix(self, x):
    return [[cos(x), -sin(x)],
            [sin(x), cos(x)]]

  def f_vec_add(self, vector1, vector2):
    return [vector1[0] + vector2[0], vector1[1] + vector2[1]]

  def f_svg_ellipse_arc(self, cx, cy, rx, ry, t1, delta, phi = 0):
    delta = delta % (2 * pi)
    rotMatrix = self.f_rotate_matrix(phi)
    sX, sY = self.f_vec_add(self.f_matrix_times(rotMatrix, [rx * cos(t1), ry * sin(t1)]), [cx, cy])
    eX, eY = self.f_vec_add(self.f_matrix_times(rotMatrix, [rx * cos(t1 + delta), ry * sin(t1 + delta)]), [cx, cy])
    fA = 1 if delta > pi else 0
    fS = 1 if delta > 0 else 0
    return f"M {sX} {sY} A {rx} {ry} {(phi / (2 * pi)) * 360} {fA} {fS} {eX} {eY}"