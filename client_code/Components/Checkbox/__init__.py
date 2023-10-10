from ._anvil_designer import CheckboxTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from ...Functions import enabled_property, style_property, underline_property, italic_property, bold_property, font_size_property, color_property, theme_color_to_css, innerText_property
import anvil.designer


class Checkbox(CheckboxTemplate):
  def __init__(self, **properties):
    self._props = properties
    self._allow_indeterminate = properties['allow_indeterminate']
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-checkbox-hover'].addEventListener("click", self.handle_change)

  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-checkbox-hover'].removeEventListener('click', self.handle_change)

  def focus(self):
    self.dom_nodes['anvil-m3-checkbox'].focus()

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    if anvil.designer.in_designer and not self.text:
      self.text = anvil.designer.get_design_name(self)

  def _anvil_get_design_info_(self, as_layout=False):
    di = super()._anvil_get_design_info_(as_layout)
    di['interactions'] = [{
      "type": "whole_component",
      "title": "Toggle",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": self.toggle_checked 
      }
    },
    {
      "type": "region",
      "bounds": self.dom_nodes['anvil-m3-checkbox-label'],
      "callbacks": {
        "doubleClick": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-checkbox-label'])
      }
    }       
    ]
    return di

  def toggle_checked(self):
    self.checked = not self.checked
    anvil.designer.update_component_properties(self, {'checked': self.checked})

  def handle_change(self, event):
    if self.enabled:
      self.dom_nodes['anvil-m3-checkbox'].focus()
      self.checked = not self.checked
      self.raise_event("change")

  enabled = enabled_property('anvil-m3-checkbox')
  visible = HtmlTemplate.visible
  underline = underline_property('anvil-m3-checkbox-label')
  italic = italic_property('anvil-m3-checkbox-label')
  bold = bold_property('anvil-m3-checkbox-label')
  font_size = font_size_property('anvil-m3-checkbox-label')
  border = style_property('anvil-m3-checkbox-container', 'border')
  font = style_property('anvil-m3-checkbox-label', 'fontFamily')
  text_color = color_property('anvil-m3-checkbox-label', 'color')
  background = color_property('anvil-m3-checkbox-container', 'backgroundColor')
  text = innerText_property('anvil-m3-checkbox-label')
  align = style_property('anvil-m3-checkbox-component', 'justifyContent')

  @property
  def checkbox_color(self):
    return self._checkbox_color

  @checkbox_color.setter
  def checkbox_color(self, value):
    self._checkbox_color = value
    if value:
      value = theme_color_to_css(value)
      self.dom_nodes['anvil-m3-checkbox-unchecked'].style.color = value
      self.dom_nodes['anvil-m3-checkbox-checked'].style.color = value
      self.dom_nodes['anvil-m3-checkbox-indeterminate'].style.color = value

  @property
  def checked(self):
    return self._checked

  @checked.setter
  def checked(self, value):
    self._checked = value
    if self._checked == None and self.allow_indeterminate:
      self.dom_nodes['anvil-m3-checkbox'].indeterminate = True
      self.dom_nodes['anvil-m3-checkbox-unchecked'].style.display = 'none'
      self.dom_nodes['anvil-m3-checkbox-checked'].style.display = 'none'
      self.dom_nodes['anvil-m3-checkbox-indeterminate'].style.display = 'inline'
    else:
      self.dom_nodes['anvil-m3-checkbox'].checked = value

  @property
  def allow_indeterminate(self):
    return self._allow_indeterminate

  @allow_indeterminate.setter
  def allow_indeterminate(self, value):
    self._allow_indeterminate = value

  @property
  def error(self):
    return self._error

  @error.setter
  def error(self, value):
    self.dom_nodes['anvil-m3-checkbox-container'].classList.remove('anvil-m3-checkbox-error')
    self._error = value
    if value:
      self.dom_nodes['anvil-m3-checkbox-container'].classList.add('anvil-m3-checkbox-error')
      self._error = value

