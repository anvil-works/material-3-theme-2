from ._anvil_designer import LinearProgressIndicatorTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from ...Functions import innerText_property, enabled_property, color_property, style_property, property_with_callback

class LinearProgressIndicator(LinearProgressIndicatorTemplate):
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
    self.dom_nodes['anvil-m3-progressindicator-indicator'].setAttribute("x2", f"{v}%")
    
  progress = property_with_callback("progress", update_progress)