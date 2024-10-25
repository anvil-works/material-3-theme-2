import anvil.server
from .Card import Card
import anvil.designer
from ..Functions import property_with_callback

#todo figure out how to get default value to work
# another_proerty = {"name": "asdf", "type": "boolean", "important": True, "designerHint": "enabled", "group": "Interaction", "description": "If True, this component allows user interaction.", "showInDesignerWhen": "another_property"}
enabled_property = {"name": "enabled", "type": "boolean", "important": True, "designerHint": "enabled", "group": "Interaction", "description": "If True, this component allows user interaction."}
click_event = {"name": "click", "defaultEvent": True, "description": "When the component is clicked"}

class InteractiveCard(Card):
  _anvil_properties_ = [enabled_property, *Card._anvil_properties_]
  _anvil_events_ = [click_event, *Card._anvil_events_]
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    #module component props don't get their default values initialized by default. this makes sure the enabled setter has run
    self.enabled = self.enabled
    self.dom_nodes['anvil-m3-card'].classList.toggle('anvil-m3-interactive', True)
    self.dom_nodes['anvil-m3-card'].addEventListener("click", self._handle_click)

  def _set_enabled(self, value): #why not being set in the beginning??
    self.dom_nodes['anvil-m3-card'].classList.toggle('anvil-m3-disabled', not value)
    
  enabled = property_with_callback("enabled", _set_enabled, default_value=True)

  def _handle_click(self, event):
    event.preventDefault()
    self.raise_event("click")

  #!componentProp(material_3.InteractiveCard)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!componentProp(material_3.InteractiveCard)!1: {name:"border",type:"string",description:"The border of this component. Can take any valid CSS border value."}
  #!componentProp(material_3.InteractiveCard)!1: {name:"background_color",type:"color",description:"The color of the background of this component."}
  #!componentProp(material_3.InteractiveCard)!1: {name:"align",type:"enum",description:"The position of this component in the available space."} 
  #!componentProp(material_3.InteractiveCard)!1: {name:"spacing",type:"spacing",description:"The margin and padding (pixels) of the component."}
  #!componentProp(material_3.InteractiveCard)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  #!componentProp(material_3.InteractiveCard)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles"} 
  #!componentProp(material_3.InteractiveCard)!1: {name:"tag",type:"object",description:"Use this property to store any extra data for the component."}
  #!componentProp(material_3.InteractiveCard)!1: {name:"appearance",type:"enum",options:["elevated", "filled", "outlined"],description:"A predefined style for this component."}
  #!componentProp(material_3.InteractiveCard)!1: {name:"orientation",type:"enum",options:["column", "row"],description:"The orientation of the content in this Card"}  
  #!componentProp(material_3.InteractiveCard)!1: {name:"enabled",type:"boolean",description:"If True, this component allows user interaction."}

  #!componentEvent(material_3.InteractiveCard)!1: {name: "click", description: "When the component is clicked.", parameters:[]}

#!defClass(material_3,InteractiveCard, anvil.Component)!:
