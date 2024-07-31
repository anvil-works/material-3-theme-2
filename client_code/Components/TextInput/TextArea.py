import anvil.server
from . import TextInput
import anvil.designer
import anvil.js
from anvil.js.window import ResizeObserver, requestAnimationFrame
from ...Functions import property_with_callback, italic_property, bold_property, underline_property, font_family_property, font_size_property, color_property

input_text_property = {"name": "input_text",
                 "type": "string",
                 "default_value": "None",
                 "description": "The input text displayed on this component",
                 "supportsWriteback": True,
                 # "binding_writeback_events": ["lost_focus"],
                 "important": True}

class TextArea(TextInput):
  _anvil_properties_ = [input_text_property, *TextInput._anvil_properties_]
  
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    hiddenInput = self.dom_nodes['anvil-m3-textfield']
    self.dom_nodes['anvil-m3-input-container'].removeChild(hiddenInput)

    # self.update_height = self.update_height
    self._on_change = self._on_change
    self._on_focus = self._on_focus
    self._on_lost_focus = self._on_lost_focus

    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)

  def _on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-textarea'].addEventListener("input", self._update_height)
    self.dom_nodes['anvil-m3-textarea'].addEventListener("input", self._on_input)
    self.dom_nodes['anvil-m3-textarea'].addEventListener("change", self._on_change)
    self.dom_nodes['anvil-m3-textarea'].addEventListener("focus", self._on_focus)
    self.dom_nodes['anvil-m3-textarea'].addEventListener("blur", self._on_lost_focus)
    self.resize_observer = ResizeObserver(self._on_resize)
    self.resize_observer.observe(self.dom_nodes['anvil-m3-textarea'])
    
  def _on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-textarea'].removeEventListener("input", self._update_height)
    self.dom_nodes['anvil-m3-textarea'].removeEventListener("input", self._on_input)
    self.dom_nodes['anvil-m3-textarea'].removeEventListener("change", self._on_change)
    self.dom_nodes['anvil-m3-textarea'].removeEventListener("focus", self._on_focus)
    self.dom_nodes['anvil-m3-textarea'].removeEventListener("blur", self._on_lost_focus)
    self.resize_observer.unobserve(self.dom_nodes['anvil-m3-textarea'])
  
  italic_display = italic_property('anvil-m3-textarea', 'italic_label')
  bold_display = bold_property('anvil-m3-textarea', 'bold_display')
  underline_display = underline_property('anvil-m3-textarea', 'underline_display')
  display_font_size = font_size_property('anvil-m3-textarea', 'display_font_size')
  display_font = font_family_property('anvil-m3-textarea', 'display_font')
  input_text_color = color_property('anvil-m3-textarea', 'color', 'input_text_color')
  background = color_property('anvil-m3-textarea', 'backgroundColor', 'background')

  def focus(self):
    self.dom_nodes['anvil-m3-textarea'].focus()

  def select(self):
    self.dom_nodes['anvil-m3-textarea'].select()

  def _set_placeholder(self, value):
    input = self.dom_nodes['anvil-m3-textarea']
    if value:
      input.placeholder = value
      input.classList.add('anvil-m3-has-placeholder')
    else:
      input.placeholder = " "
      input.classList.remove('anvil-m3-has-placeholder')
  placeholder = property_with_callback('placeholder', _set_placeholder)

  @property
  def input_text(self):
    return self.dom_nodes['anvil-m3-textarea'].value

  @input_text.setter
  def input_text(self, value):
    self.dom_nodes['anvil-m3-textarea'].value = value

  def _set_label(self, value):
    self.dom_nodes['anvil-m3-label-text'].innerText = value or ""
    if value:
      self.dom_nodes['anvil-m3-textarea'].classList.toggle('has_label_text', True)
    else:
      self.dom_nodes['anvil-m3-textarea'].classList.toggle('has_label_text', anvil.designer.in_designer);
  label_text = property_with_callback("label_text", _set_label)
  
  def _set_enabled(self, value):
    supporting_text = self.dom_nodes['anvil-m3-subcontent']
    if value:
      self.dom_nodes['anvil-m3-textarea'].removeAttribute("disabled")
      supporting_text.classList.remove("anvil-m3-textinput-disabled")
    else:
      self.dom_nodes['anvil-m3-textarea'].setAttribute("disabled", " ")
      supporting_text.classList.add("anvil-m3-textinput-disabled")
  enabled = property_with_callback("enabled", _set_enabled)

  def _set_id(self, value):
    super()._set_id(value)
    self.dom_nodes["anvil-m3-textarea"].id = value

  def _update_height(self, event):
    self.dom_nodes['anvil-m3-textarea'].style.height = '56px' #min-height based off specs
    h = event.target.scrollHeight;
    self._set_height(h)

  def _on_resize(self, entries, observer):
    for entry in entries:
      h = entry.target.scrollHeight
    requestAnimationFrame(lambda _: self._set_height(h))

  def _set_height(self, h):
    self.dom_nodes['anvil-m3-textarea'].style.height = f'{h}px'
    self.dom_nodes['anvil-m3-border-container'].style.height = f'{h}px'

  def _set_character_limit(self, value):
    if value is None or value < 1:
      text_field_input = self.dom_nodes['anvil-m3-textarea'].removeAttribute("maxlength")
      self.dom_nodes['anvil-m3-character-counter'].style = "display: none"
    else:
      text_field_input = self.dom_nodes['anvil-m3-textarea'].setAttribute("maxlength", value)
      self.dom_nodes['anvil-m3-character-counter'].style = "display: inline";
      self.dom_nodes['anvil-m3-character-limit'].innerText = int(value);
  character_limit = property_with_callback("character_limit", _set_character_limit)

  #!componentProp(material_3.TextArea)!1: {name:"align",type:"enum",options:["left", "right", "center"],description:"The position of this component in the available space."} 
  #!componentProp(material_3.TextArea)!1: {name:"appearance",type:"enum",options:["filled", "outlined"],description:"A predefined style for this component."}  
  #!componentProp(material_3.TextArea)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!componentProp(material_3.TextArea)!1: {name:"enabled",type:"boolean",description:"If True, this component allows user interaction."}
  #!componentProp(material_3.TextArea)!1: {name:"error",type:"boolean",description:"If True, this component is in an error state."}
  #!componentProp(material_3.TextArea)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles"}

  #!componentProp(material_3.TextArea)!1: {name:"label_text_color",type:"color",description:"The colour of the label text on the component."} 
  #!componentProp(material_3.TextArea)!1: {name:"label_text",type:"string",description:"The label text of the component."} 
  #!componentProp(material_3.TextArea)!1: {name:"label_font_family",type:"string",description:"The font family to use for the label on this component."}
  #!componentProp(material_3.TextArea)!1: {name:"label_font_size",type:"number",description:"The font size of the label text on this component."}
  #!componentProp(material_3.TextArea)!1: {name:"underline_label",type:"boolean",description:"If True, the label text will be underlined."}
  #!componentProp(material_3.TextArea)!1: {name:"italic_label",type:"boolean",description:"If True, the label text will be italic."}
  #!componentProp(material_3.TextArea)!1: {name:"bold_label",type:"boolean",description:"If True, the label text will be bold."}

  #!componentProp(material_3.TextArea)!1: {name:"input_text_color",type:"color",description:"The colour of the input text displayed on this component."}
  #!componentProp(material_3.TextArea)!1: {name:"display_font_family",type:"string",description:"The font family to use for the input and placeholder text."}
  #!componentProp(material_3.TextArea)!1: {name:"display_font_size",type:"number",description:"The font size of the input and placeholder text."}
  #!componentProp(material_3.TextArea)!1: {name:"underline_display",type:"boolean",description:"The font family to use for the label on this component."}
  #!componentProp(material_3.TextArea)!1: {name:"italic_display",type:"boolean",description:"If True, the input and placeholder text will be italic."}
  #!componentProp(material_3.TextArea)!1: {name:"bold_display",type:"boolean",description:"If True, the input and placeholder text will be bold."}

  #!componentProp(material_3.TextArea)!1: {name:"supporting_text",type:"string",description:"The supporting text displayed underneath this component"}
  #!componentProp(material_3.TextArea)!1: {name:"supporting_text_color",type:"color",description:"The colour of the supporting text underneath this component."}
  #!componentProp(material_3.TextArea)!1: {name:"supporting_text_font_family",type:"color",description:"The font family to use for the supporting text underneath this component."}
  #!componentProp(material_3.TextArea)!1: {name:"supporting_text_font_size",type:"color",description:"The font size of the supporting text displayed underneath this component."}

  #!componentProp(material_3.TextArea)!1: {name:"character_limit",type:"number",description:"The max number of characters a user can enter into this component. The limit is displayed below the component."}
  #!componentProp(material_3.TextArea)!1: {name:"character_limit_color",type:"color",description:"The colour of the character limit text displayed underneath this component."}
  #!componentProp(material_3.TextArea)!1: {name:"character_limit_font_family",type:"number",description:"The font family of the character limit text displayed underneath this component."}
  #!componentProp(material_3.TextArea)!1: {name:"character_limit_font_size",type:"number",description:"The font size of the character limit text displayed underneath this component."}

  #!componentProp(material_3.TextArea)!1: {name:"background_color",type:"color",description:"The colour of the background of this component."}
  #!componentProp(material_3.TextArea)!1: {name:"border_color",type:"color",description:"The colour of the border of this component."}
  #!componentProp(material_3.TextArea)!1: {name:"placeholder",type:"string",description:"The text to be displayed when the component is empty"}

  #!componentProp(material_3.TextArea)!1: {name:"spacing",type:"spacing",description:"The margin and padding of this component. Default value is in pixels."}
  #!componentProp(material_3.TextArea)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  #!componentProp(material_3.TextArea)!1: {name:"input_text",type:"string",description:"The input text to display on this component"}

  #!componentEvent(material_3.TextArea)!1: {name: "change", description: "When the text in this component is edited.", parameters:[]}
  #!componentEvent(material_3.TextArea)!1: {name: "focus", description: "When the component gets focus.", parameters:[]}
  #!componentEvent(material_3.TextArea)!1: {name: "lost_focus", description: "When the component loses focus.", parameters:[]}

  #!componentEvent(material_3.TextArea)!1: {name: "change", description: "When the text in this component is edited.", parameters:[]}
  #!componentEvent(material_3.TextArea)!1: {name: "focus", description: "When the component gets focus.", parameters:[]}
  #!componentEvent(material_3.TextArea)!1: {name: "lost_focus", description: "When the component loses focus.", parameters:[]}

  #!defMethod(_)!2: "Set the keyboard focus to this TextArea." ["focus"]
  #!defMethod(_)!2: "Set the input text on this TextArea." ["select"]

#!defClass(material_3,TextArea, anvil.Component)!:
