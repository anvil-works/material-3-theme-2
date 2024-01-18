from ._anvil_designer import CardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.designer
from anvil import HtmlTemplate
from ...Functions import property_with_callback, style_property, spacing_property, margin_property, padding_property

class Card(CardTemplate):
  def __init__(self, **properties):
    self._props = properties
    self.card_image_temp_url = None
    self._on_page = False
    self.init_components(**properties)
    if not anvil.designer.in_designer:
      self.dom_nodes['empty-image'].style.display = "none"
      self.dom_nodes['empty-content'].style.display = "none"

  # align = style_property('anvil-m3-card-component', 'justifyContent', 'align')
  visible = HtmlTemplate.visible

  def set_nodes_class_by_image(self, image_position, val):
    self.dom_nodes['anvil-m3-card'].classList.toggle(f'{image_position}-image', val)
    self.dom_nodes['content'].classList.toggle(f'{image_position}-image', val)
    self.dom_nodes['image'].classList.toggle(f'{image_position}-image', val)
    
  def set_image_position(self, value):
    for position in [None, 'top', 'bottom', 'left', 'right', 'full']:
      self.set_nodes_class_by_image(position or 'none', False)
    
    self.set_nodes_class_by_image(value or 'none', True)
  image_position = property_with_callback("image_position", set_image_position)

  def set_class_of_nodes(self, appearance, val):
    self.dom_nodes['anvil-m3-card'].classList.toggle(f'anvil-m3-{appearance}', val)
    self.dom_nodes['image'].classList.toggle(f'anvil-m3-{appearance}', val)
    self.dom_nodes['content'].classList.toggle(f'anvil-m3-{appearance}', val)
    
  def set_appearance(self, value):
    for appearance in ['outlined', 'filled', 'elevated']:
      self.set_class_of_nodes(appearance, False)

    self.set_class_of_nodes(value, True)
  appearance = property_with_callback("appearance", set_appearance)

  image_width = align = style_property('image', 'width', 'image_width')
  image_height = align = style_property('image', 'height', 'image_height')

  def _set_card_img(self, *_args):
    if self.card_image:
      #set a card position so the image appears
      self.image_position = 'top'
      if type(self.card_image) is str:
        self.dom_nodes['image'].style.backgroundImage = f"url('{self.card_image}')"
      elif type(self.card_image) is anvil.LazyMedia:
        self.dom_nodes['image'].style.backgroundImage = f"url('{self.card_image.get_url()}')"
      else:
        if self._on_page:
          self.card_image_temp_url = anvil.media.TempUrl(self.card_image)
          self.dom_nodes['image'].style.backgroundImage = f"url('{self.card_image_temp_url.url}')"
    else:
      self.dom_nodes['image'].style.removeProperty = "background-image"

  card_image = property_with_callback("card_image", _set_card_img)

  def _set_rounded_img(self, value):
     self.dom_nodes['image'].classList.toggle('anvil-m3-card-rounded', value)
  rounded_image = property_with_callback("rounded_image", _set_rounded_img)

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self._on_page = True
    self._set_card_img()

  def form_hide(self, **event_args):
    """This method is called when the form is removed from the page"""
    self._on_page = False
    if self.card_image_temp_url:
      print("revoking url...")
      self.card_image_temp_url.revoke()
      self.card_image_temp_url = None

  margin = margin_property('anvil-m3-card')
  card_content_padding = padding_property('content', 'card_content_padding')
  card_image_content_padding = padding_property('image', 'card_image_content_padding')
      
