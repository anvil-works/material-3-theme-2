import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from .IconButton import IconButton
import anvil.designer
from ..Functions import property_with_callback, theme_color_to_css

selected_property = {"name": "selected", "type": "boolean", "group": "Interaction", "important": True, "default_value": False, "description": "If True, the component is in the selected state"}
selected_border_property = {"name": "selected_border", "type": "string", "group": "Toggled Style" , "description": "The border style when the component is in the selected state. Accepts any valid CSS border value."}
selected_background_property = {"name": "selected_background", "type": "color", "group": "Toggled Style" , "description": "The background color when the component is in the selected state."}
selected_icon_color_property = {"name": "selected_icon_color", "type": "color", "group": "Toggled Style" , "description": "The icon color when the component is in the selected state."}
tag_property = {"name": "tag", "type": "object", "important": False, "group": "Other", "description": "Use this property to store any extra data for the component."}
   
class ToggleIconButton(IconButton):
  _anvil_properties_ = [tag_property, selected_property, selected_border_property, selected_background_property, selected_icon_color_property, *IconButton._anvil_properties_]
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
  
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("anvil-m3-toggle", True)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("anvil-m3-toggle", True)   

    # I think there is a smarter way to do this. I don't know the setter isn't getting called in the beginning.
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("anvil-m3-selected", self.selected)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("anvil-m3-selected", self.selected)

  def _anvil_get_interactions_(self):
    return [
      {
        "type": "region",
        "bounds": self.dom_nodes['anvil-m3-iconbutton-component-container'],
        "sensitivity": 0,
        "callbacks": {
          "execute": self._toggle_selected
        }
      }
    ]
    
  def _apply_styles(self, value):
    if value:
      self.dom_nodes['anvil-m3-iconbutton-container'].style.backgroundColor = theme_color_to_css(self.selected_background) if self.selected_background else None
      self.dom_nodes['anvil-m3-iconbutton-container'].style.border = self.selected_border
      self.dom_nodes['anvil-m3-iconbutton-icon'].style.color = theme_color_to_css(self.selected_icon_color) if self.selected_icon_color else None
    else:
      self.dom_nodes['anvil-m3-iconbutton-container'].style.backgroundColor = theme_color_to_css(self.background) if self.background else None
      self.dom_nodes['anvil-m3-iconbutton-container'].style.border = self.border
      self.dom_nodes['anvil-m3-iconbutton-icon'].style.color = theme_color_to_css(self.icon_color) if self.icon_color else None 

  def _selected_setter(self, value):
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("anvil-m3-selected", value)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("anvil-m3-selected", value)
    self._apply_styles(value)

  def _handle_click(self, event):
    event.preventDefault()
    self.selected = not self.selected
    self.raise_event("click")

  def _toggle_selected(self):
    self.selected = not self.selected
    anvil.designer.update_component_properties(self, {'selected': self.selected})

  #!componentProp(material_3.ToggleIconButton)!1: {name:"align",type:"enum",options:["left", "right", "center"],description:"The position of this component in the available space."} 
  #!componentProp(material_3.ToggleIconButton)!1: {name:"appearance",type:"enum",options:["standard", "filled", "tonal", "outlined"],description:"A predefined style for this component."}  
  #!componentProp(material_3.ToggleIconButton)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!componentProp(material_3.ToggleIconButton)!1: {name:"enabled",type:"boolean",description:"If True, this component allows user interaction."}
  #!componentProp(material_3.ToggleIconButton)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles"} 
  #!componentProp(material_3.ToggleIconButton)!1: {name:"icon",type:"enum",description:"The icon to display on this component."} 
  #!componentProp(material_3.ToggleIconButton)!1: {name:"icon_color",type:"color",description:"The colour of the icon displayed on this component."}
  #!componentProp(material_3.ToggleIconButton)!1: {name:"background",type:"color",description:"The colour of the background of this component."}
  #!componentProp(material_3.ToggleIconButton)!1: {name:"margin",type:"margin",description:"The margin (pixels) of the component."}
  #!componentProp(material_3.ToggleIconButton)!1: {name:"border",type:"string",description:"The border of this component. Can take any valid CSS border value."}
  #!componentProp(material_3.ToggleIconButton)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  #!componentProp(material_3.ToggleIconButton)!1: {name:"selected",type:"boolean",description:"If True, the component is in the selected state."}
  #!componentProp(material_3.ToggleIconButton)!1: {name:"selected_border",type:"string",description:"The border style when the component is in the selected state. Accepts any valid CSS border value."}
  #!componentProp(material_3.ToggleIconButton)!1: {name:"selected_background",type:"color",description:"The background colour when the component is in the selected state."}
  #!componentProp(material_3.ToggleIconButton)!1: {name:"selected_icon_color",type:"color",description:"The icon colour when the component is in the selected state."}
  #!componentProp(material_3.ToggleIconButton)!1: {name:"tag",type:"object",description:"Use this property to store any extra data for the component."}

  #!componentEvent(material_3.ToggleIconButton)!1: {name: "click", description: "When the component is clicked.", parameters:[]}
  
  border = property_with_callback("border", _apply_styles)
  icon_color = property_with_callback("icon_color", _apply_styles)
  background = property_with_callback("background", _apply_styles)
  selected_border = property_with_callback("selected_border", _apply_styles)
  selected_background = property_with_callback("selected_background", _apply_styles)
  selected_icon_color = property_with_callback("selected_icon_color", _apply_styles)
  selected = property_with_callback("selected", _selected_setter)

#!defClass(material_3,ToggleIconButton, anvil.component)!:
    