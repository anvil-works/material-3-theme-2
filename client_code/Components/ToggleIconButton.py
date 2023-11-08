import anvil.server
from .IconButton import IconButton
import anvil.designer
from ..Functions import property_with_callback, theme_color_to_css

# icon_button_properties = getattr(IconButton, "_anvil_properties_", [])

selected_property = {"name": "selected", "type": "boolean", "group": "Attributes", "important": True, "default_value": False}
selected_border_property = {"name": "selected_border", "type": "string", "group": "Toggled Style" , "description": "Border style when component is in the selected state. Accepts any valid CSS border value."}
selected_background_property = {"name": "selected_background", "type": "color", "group": "Toggled Style" , "description": "Background color when component is in the selected state."}
selected_icon_color_property = {"name": "selected_icon_color", "type": "color", "group": "Toggled Style" , "description": "Icon color when component is in the selected state."}

class ToggleIconButton(IconButton):
  _anvil_properties_ = [selected_property, selected_border_property, selected_background_property, selected_icon_color_property, *IconButton._anvil_properties_]
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
  
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("toggle", True)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("toggle", True)   

    # I think there is a smarter way to do this. I don't know the setter isn't getting called in the beginning.
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("selected", self.selected)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("selected", self.selected)
    
  # Properties 
  def apply_styles(self, value):
    if value:
      self.dom_nodes['anvil-m3-iconbutton-container'].style.backgroundColor = theme_color_to_css(self.selected_background) if self.selected_background else None
      self.dom_nodes['anvil-m3-iconbutton-container'].style.border = self.selected_border
      self.dom_nodes['anvil-m3-iconbutton-icon'].style.color = theme_color_to_css(self.selected_icon_color) if self.selected_icon_color else None
    else:
      self.dom_nodes['anvil-m3-iconbutton-container'].style.backgroundColor = theme_color_to_css(self.background) if self.background else None
      self.dom_nodes['anvil-m3-iconbutton-container'].style.border = self.border
      self.dom_nodes['anvil-m3-iconbutton-icon'].style.color = theme_color_to_css(self.icon_color) if self.icon_color else None 

  def selected_setter(self, value):
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("selected", value)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("selected", value)
    self.apply_styles(value)
    
  border = property_with_callback("border", apply_styles)
  icon_color = property_with_callback("icon_color", apply_styles)
  background = property_with_callback("background", apply_styles)
  selected_border = property_with_callback("selected_border", apply_styles)
  selected_background = property_with_callback("selected_background", apply_styles)
  selected_icon_color = property_with_callback("selected_icon_color", apply_styles)
  selected = property_with_callback("selected", selected_setter)
    
  def handle_click(self, event):
    event.preventDefault()
    self.selected = not self.selected
    self.raise_event("click")

