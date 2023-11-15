from ._anvil_designer import CardTemplate
import anvil.designer
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from ...Functions import property_with_callback, style_property

class Card(CardTemplate):
  def __init__(self, **properties):
    self._props = properties
    self.init_components(**properties)
    if not anvil.designer.in_designer:
      self.dom_nodes['empty-content-slot'].style = "display: none";
      self.dom_nodes['empty-iamge-slot'].style = "display: none";
  align = style_property('anvil-m3-card-component', 'justifyContent', 'align')
  visible = HtmlTemplate.visible
    
  def set_nodes_class_by_image(self, image_position, val):
    self.dom_nodes['anvil-m3-card-shadow'].classList.toggle(f'{image_position}-image', val)
    self.dom_nodes['anvil-m3-card-content'].classList.toggle(f'{image_position}-image', val)
    self.dom_nodes['anvil-m3-card-image'].classList.toggle(f'{image_position}-image', val)
    
  def set_image_position(self, value):
    for position in ['none', 'top', 'bottom', 'left', 'right', 'full']:
      self.set_nodes_class_by_image(position, False)
    self.set_nodes_class_by_image(value.lower(), True)
  image_position = property_with_callback("image_position", set_image_position)

  def set_class_of_nodes(self, appearance, val):
    self.dom_nodes[f'anvil-m3-card-shadow'].classList.toggle(f'anvil-m3-{appearance}', val)
    self.dom_nodes[f'anvil-m3-card-image'].classList.toggle(f'anvil-m3-{appearance}', val)
    self.dom_nodes[f'anvil-m3-card-content'].classList.toggle(f'anvil-m3-{appearance}', val)
    
  def set_appearance(self, value):
    for appearance in ['outlined', 'filled', 'elevated']:
      self.set_class_of_nodes(appearance, False)

    self.set_class_of_nodes(value.lower(), True)
  appearance = property_with_callback("appearance", set_appearance)

  def set_image(self, value):
    if value:
      self.dom_nodes['anvil-m3-card-image'].style.backgroundImage = f"url('{value}')";
    else:
      self.dom_nodes['anvil-m3-card-image'].style.element.style.removeProperty = "background-image"
  card_image = property_with_callback("card_image", set_image)