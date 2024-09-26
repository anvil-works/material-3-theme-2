import anvil.server
from . import TextInput
import anvil.designer
from ...Functions import property_with_callback, italic_property, bold_property, underline_property, font_family_property, font_size_property, color_property
from anvil.property_utils import anvil_property
from ...utils import _m3_icons

input_text_property = {"name": "input_text",
                 "type": "string",
                 "default_value": "None",
                 "description": "The text displayed on this component.",
                 "supportsWriteback": True,
                 "important": True}
leading_icon_property = {"name": "leading_icon",
                         "type": "icon",
                         "iconsets": ["material-icons"],
                         "group": "Icon",
                         "important": True,
                         "default_value": "",
                         "includeNoneOption": True, # This might change to snake case at some point
                         "description": "The leading icon to display on this component."}
trailing_icon_property = {"name": "trailing_icon",
                          "type": "icon",
                          "iconsets": ["material-icons"],
                          "group": "Icon",
                          "important": True,
                          "default_value": "",
                          "includeNoneOption": True,
                          "description": "The trailing icon to display on this component."}
type_property = {"name": "type", 
                 "type": "enum", 
                 "options": ["text", "number", "email", "tel", "url"], 
                 "group": "Other", 
                 "important": False, 
                 "default_value": "text",
                 "description": "The type of data that the user can enter into this box."}
hide_text_property = {"name": "hide_text", 
                      "type": "boolean", 
                      "group": "Other", 
                      "important": False, 
                      "default_value": False,
                      "description": "If True, display stars instead of text when the user types input into this component."}
leading_icon_color_property = {"name": "leading_icon_color", 
                               "type": "color", 
                               "group": "Look and Feel", 
                               "important": False, 
                               "default_value": "",
                               "description": "The colour of the leading icon."}
trailing_icon_color_property = {"name": "trailing_icon_color", 
                               "type": "color", 
                               "group": "Look and Feel", 
                               "important": False, 
                               "default_value": "",
                               "description": "The colour of the trailing icon."}


click_event = {"name": "trailing_icon_click", "defaultEvent": False, "description": "When the trailing icon is clicked."}
pressed_enter_event = {"name": "pressed_enter", "defaultEvent": True, "description": "When the user presses enter in this component."}

class TextField(TextInput):
  _anvil_properties_ = [input_text_property, leading_icon_property, trailing_icon_property, type_property, hide_text_property, leading_icon_color_property, trailing_icon_color_property, *TextInput._anvil_properties_]
  _anvil_events_ = [click_event, pressed_enter_event, *TextInput._anvil_events_]
  
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    hiddenInput = self.dom_nodes['anvil-m3-textarea']
    self.dom_nodes['anvil-m3-input-container'].removeChild(hiddenInput)
    
    self._on_key_down = self._on_key_down
    self._on_change = self._on_change
    self._handle_click = self._handle_click
    self._on_focus = self._on_focus
    self._on_lost_focus = self._on_lost_focus

    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)

  def _on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-textfield'].addEventListener("input", self._on_input)
    self.dom_nodes['anvil-m3-textfield'].addEventListener("keydown", self._on_key_down)
    self.dom_nodes['anvil-m3-textfield'].addEventListener("change", self._on_change)
    self.dom_nodes['anvil-m3-textfield'].addEventListener("focus", self._on_focus)
    self.dom_nodes['anvil-m3-textfield'].addEventListener("blur", self._on_lost_focus)
    self.dom_nodes['anvil-m3-trailing-icon'].addEventListener("click", self._handle_click)
    
  def _on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-textfield'].removeEventListener("input", self._on_input)
    self.dom_nodes['anvil-m3-textfield'].removeEventListener("keydown", self._on_key_down)
    self.dom_nodes['anvil-m3-textfield'].removeEventListener("change", self._on_change)
    self.dom_nodes['anvil-m3-trailing-icon'].removeEventListener("click", self._handle_click)
    self.dom_nodes['anvil-m3-textfield'].removeEventListener("focus", self._on_focus)
    self.dom_nodes['anvil-m3-textfield'].removeEventListener("blur", self._on_lost_focus)

  def _on_key_down(self, e):
    if e.key == "Enter":
      self.raise_event("x-anvil-write-back-input_text")
      self.raise_event("pressed_enter")

  def _set_placeholder(self, value):
    input = self.dom_nodes['anvil-m3-textfield']
    if value:
      input.placeholder = value
      input.classList.add('anvil-m3-has-placeholder')
    else:
      input.placeholder = " "
      input.classList.remove('anvil-m3-has-placeholder')
  placeholder = property_with_callback('placeholder', _set_placeholder)

  def focus(self):
    self.dom_nodes['anvil-m3-textfield'].focus()

  def select(self):
    self.dom_nodes['anvil-m3-textfield'].select()
  
  @property
  def input_text(self):
    if self._props.get('type') == "number" and self.dom_nodes['anvil-m3-textfield'].value:
      return float(self.dom_nodes['anvil-m3-textfield'].value)
    else:
      return self.dom_nodes['anvil-m3-textfield'].value

  @input_text.setter
  def input_text(self, value):
    self.dom_nodes['anvil-m3-textfield'].value = value
      
  def _set_label(self, value):
    self.dom_nodes['anvil-m3-label-text'].innerText = value or ""
    if value:
      self.dom_nodes['anvil-m3-textfield'].classList.toggle('has_label_text', True)
    else:
      self.dom_nodes['anvil-m3-textfield'].classList.toggle('has_label_text', anvil.designer.in_designer);
  label_text = property_with_callback("anvil-m3-label-text", _set_label)

  def _set_enabled(self, value):
    supporting_text = self.dom_nodes['anvil-m3-subcontent']
    trailing_icon = self.dom_nodes['anvil-m3-trailing-icon']
    if value:
      self.dom_nodes['anvil-m3-textfield'].removeAttribute("disabled")
      supporting_text.classList.remove("anvil-m3-textinput-disabled")
      trailing_icon.classList.remove("anvil-m3-disable-icon")
    else:
      self.dom_nodes['anvil-m3-textfield'].setAttribute("disabled", " ")
      supporting_text.classList.add("anvil-m3-textinput-disabled")
      trailing_icon.classList.add("anvil-m3-disable-icon")
  enabled = property_with_callback("enabled", _set_enabled)
  
  def _set_id(self, value):
    super()._set_id(value)
    self.dom_nodes["anvil-m3-textfield"].id = value

  def _set_error(self, value):
    super()._set_error(value)
    if value:
      icon = "error"
      self._set_trailing_icon(icon)
      self.dom_nodes["anvil-m3-trailing-icon"].classList.add("anvil-m3-error-icon")
    else:
      icon = self.trailing_icon
      self._set_trailing_icon(icon)
      self.dom_nodes["anvil-m3-trailing-icon"].classList.remove("anvil-m3-error-icon")
    # icon = "error" if value else self.trailing_icon
  error = property_with_callback("error", _set_error)
    
  def _set_leading_icon(self, value):
    icon_container = self.dom_nodes['anvil-m3-icon-container']
    leading_icon = self.dom_nodes['anvil-m3-leading-icon']
    text_field_input = self.dom_nodes['anvil-m3-textfield']
    border_container = self.dom_nodes['anvil-m3-border-container']

    if value and value.startswith("mi:"):
      leading_icon.style.display = "block"
      leading_icon.innerText = value[3:]
      icon_container.style.paddingLeft = "12px"
      text_field_input.style.paddingLeft = "48px"
      border_container.classList.add("with-icon")
    else:
      leading_icon.style.display = "none"
      leading_icon.innerText = ""
      icon_container.style.paddingLeft = "16px"
      text_field_input.style.paddingLeft = "16px"
      border_container.classList.remove("with-icon")
  leading_icon = property_with_callback("leading_icon", _set_leading_icon)  
  
  def _set_trailing_icon(self, value):
    icon_container = self.dom_nodes['anvil-m3-icon-container']
    trailing_icon = self.dom_nodes['anvil-m3-trailing-icon']
    text_field_input = self.dom_nodes['anvil-m3-textfield']

    if value:
      trailing_icon.style.display = "block"
      trailing_icon.innerText = value
      text_field_input.style.paddingRight = "48px"
    else:
      trailing_icon.style.display = "none"
      trailing_icon.innerText = ""
      text_field_input.style.paddingRight = "16px"
  trailing_icon = property_with_callback("trailing_icon", _set_trailing_icon)

  display_italic = italic_property('anvil-m3-textfield', 'display_italic')
  display_bold = bold_property('anvil-m3-textfield', 'display_bold')
  display_underline = underline_property('anvil-m3-textfield', 'display_underline')
  display_font_size = font_size_property('anvil-m3-textfield', 'display_font_size')
  display_font_family = font_family_property('anvil-m3-textfield', 'display_font')
  input_text_color = color_property('anvil-m3-textfield', 'color', 'input_text_color')
  background = color_property('anvil-m3-textfield', 'backgroundColor', 'background' )
  leading_icon_color = color_property('anvil-m3-leading-icon', 'color', 'leading_icon_color')
  trailing_icon_color = color_property('anvil-m3-trailing-icon', 'color', 'trailing_icon_color')

  def _set_character_limit(self, value):
    if value is None or value < 1:
      text_field_input = self.dom_nodes['anvil-m3-textfield'].removeAttribute("maxlength")
      self.dom_nodes['anvil-m3-character-counter'].style = "display: none"
    else:
      text_field_input = self.dom_nodes['anvil-m3-textfield'].setAttribute("maxlength", value)
      self.dom_nodes['anvil-m3-character-counter'].style = "display: inline"
      self.dom_nodes['anvil-m3-character-limit'].innerText = int(value)
  character_limit = property_with_callback("character_limit", _set_character_limit)

  def _set_type(self, value):
    self.dom_nodes['anvil-m3-textfield'].setAttribute("type", value)
  type = property_with_callback("type", _set_type)

  def _set_hide_text(self, value):
    self.dom_nodes['anvil-m3-textfield'].setAttribute("type", "password" if value else self.type)
  hide_text = property_with_callback("hide_text", _set_hide_text)

  def _handle_click(self, event):
    event.preventDefault()
    self.raise_event("trailing_icon_click")

  #!componentProp(material_3.TextField)!1: {name:"align",type:"enum",options:["left", "right", "center"],description:"The position of this component in the available space."} 
  #!componentProp(material_3.TextField)!1: {name:"appearance",type:"enum",options:["filled", "outlined"],description:"A predefined style for this component."}  
  #!componentProp(material_3.TextField)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!componentProp(material_3.TextField)!1: {name:"enabled",type:"boolean",description:"If True, this component allows user interaction."}
  #!componentProp(material_3.TextField)!1: {name:"error",type:"boolean",description:"If True, this component is in an error state."}
  #!componentProp(material_3.TextField)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles"}

  #!componentProp(material_3.TextField)!1: {name:"label_text_color",type:"color",description:"The colour of the label text on the component."} 
  #!componentProp(material_3.TextField)!1: {name:"label_text",type:"string",description:"The label text of the component."} 
  #!componentProp(material_3.TextField)!1: {name:"label_font_family",type:"string",description:"The font family to use for the label this component."}
  #!componentProp(material_3.TextField)!1: {name:"label_font_size",type:"number",description:"The font size of the label text on this component."}
  #!componentProp(material_3.TextField)!1: {name:"label_underline",type:"boolean",description:"If True, the label text will be underlined."}
  #!componentProp(material_3.TextField)!1: {name:"label_italic",type:"boolean",description:"If True, the label text will be italic."}
  #!componentProp(material_3.TextField)!1: {name:"label_bold",type:"boolean",description:"If True, the label text will be bold."}

  #!componentProp(material_3.TextField)!1: {name:"input_text_color",type:"color",description:"The colour of the input text displayed on this component."}
  #!componentProp(material_3.TextField)!1: {name:"display_font_family",type:"string",description:"The font family to use for the input and placeholder text."}
  #!componentProp(material_3.TextField)!1: {name:"display_font_size",type:"number",description:"The font size of the input and placeholder text."}
  #!componentProp(material_3.TextField)!1: {name:"display_underline",type:"boolean",description:"If True, the input and placeholder text will be underlined."}
  #!componentProp(material_3.TextField)!1: {name:"display_italic",type:"boolean",description:"If True, the input and placeholder text will be italic."}
  #!componentProp(material_3.TextField)!1: {name:"display_bold",type:"boolean",description:"If True, the input and placeholder text will be bold."}

  #!componentProp(material_3.TextField)!1: {name:"leading_icon",type:"enum",description:"The leading icon to display on this component."} 
  #!componentProp(material_3.TextField)!1: {name:"trailing_icon",type:"enum",description:"The trailing icon to display on this component."}
  #!componentProp(material_3.TextField)!1: {name:"leading_icon_color",type:"color",description:"The colour of the leading icon displayed on this component."}
  #!componentProp(material_3.TextField)!1: {name:"trailing_icon_color",type:"color",description:"The colour of the trailing icon displayed on this component."}

  #!componentProp(material_3.TextField)!1: {name:"supporting_text",type:"string",description:"The supporting text displayed below this component"}
  #!componentProp(material_3.TextField)!1: {name:"supporting_text_color",type:"color",description:"The colour of the supporting text below this component."}
  #!componentProp(material_3.TextField)!1: {name:"supporting_text_font_family",type:"color",description:"The font family to use for the supporting text below this component."}
  #!componentProp(material_3.TextField)!1: {name:"supporting_text_font_size",type:"color",description:"The font size of the supporting text displayed below this component."}

  #!componentProp(material_3.TextField)!1: {name:"character_limit",type:"number",description:"The max number of characters a user can enter into this component. The limit is displayed below the component."}
  #!componentProp(material_3.TextField)!1: {name:"character_limit_color",type:"color",description:"The colour of the character limit text displayed below this component."}
  #!componentProp(material_3.TextField)!1: {name:"character_limit_font_family",type:"number",description:"The font family of the character limit text displayed below this component."}
  #!componentProp(material_3.TextField)!1: {name:"character_limit_font_size",type:"number",description:"The font size of the character limit text displayed below this component."}

  #!componentProp(material_3.TextField)!1: {name:"background_color",type:"color",description:"The colour of the background of this component."}
  #!componentProp(material_3.TextField)!1: {name:"border_color",type:"color",description:"The colour of the border of this component."}
  #!componentProp(material_3.TextField)!1: {name:"placeholder",type:"string",description:"The text to be displayed when the component is empty"}

  #!componentProp(material_3.TextField)!1: {name:"spacing",type:"spacing",description:"The margin and padding (pixels) of the component."}
  #!componentProp(material_3.TextField)!1: {name:"type",type:"enum",options:["text", "number", "email", "tel", "url"],description:"The type of data that the user can enter into this box."}
  #!componentProp(material_3.TextField)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  #!componentProp(material_3.TextField)!1: {name:"input_text",type:"string",description:"The input text to display on this component"}
  #!componentProp(material_3.TextField)!1: {name:"hide_text",type:"boolean",description:"If True, display stars instead of text when the user types input into this component."}
  #!componentProp(material_3.TextField)!1: {name:"tag",type:"object",description:"Use this property to store any extra data for the component."}

  #!componentEvent(material_3.TextField)!1: {name: "change", description: "When the text in this component is edited.", parameters:[]}
  #!componentEvent(material_3.TextField)!1: {name: "focus", description: "When the component gets focus.", parameters:[]}
  #!componentEvent(material_3.TextField)!1: {name: "lost_focus", description: "When the component loses focus.", parameters:[]}
  #!componentEvent(material_3.TextField)!1: {name: "trailing_icon_click", description: "When the trailing icon is clicked.", parameters:[]}
  #!componentEvent(material_3.TextField)!1: {name: "pressed_enter", description: "When the user presses enter in this component.", parameters:[]}

  #!defMethod(_)!2: "Set the keyboard focus to this TextField." ["focus"]
  #!defMethod(_)!2: "Set the input text on this TextField." ["select"]

#!defClass(material_3,TextField, anvil.Component)!:
