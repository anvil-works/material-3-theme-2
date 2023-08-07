from ._anvil_designer import CheckboxTemplate
from anvil import *
from ...Functions import checked_property, innerText_property, enabled_property
import anvil.designer

#TODO: 
# * add focus method
# * add change event

class Checkbox(CheckboxTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.dom_nodes['anvil-m3-checkbox-hover'].addEventListener("click", self.handle_click)

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    if anvil.designer.in_designer and not self.text:
      self.updateText(anvil.designer.get_design_name(self), True)

  def _anvil_get_design_info_(self, as_layout=False):
    di = super()._anvil_get_design_info_(as_layout)
    di['interactions'] = [{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-checkbox-label'])
      }
    }]
    return di
  
  def updateText(self, value, in_designer_placeholder):
    self.dom_nodes['anvil-m3-checkbox-label'].innerText = value or ""
    if not in_designer_placeholder:
      self.dom_nodes['anvil-m3-checkbox-label'].removeAttribute("style")
  
  enabled = enabled_property('anvil-m3-checkbox')
  label = innerText_property('anvil-m3-checkbox-label')

  @property
  def checked(self):
    return self._checked

  @checked.setter
  def checked(self, value):
    

  @property
  def text(self):
    return self._text

  @text.setter
  def text(self, value):
    self._text = value
    if value:
      self.updateText(value, False)

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

  def handle_click(self, event):
    if self.enabled:
      self.dom_nodes['anvil-m3-checkbox'].focus()
      self.selected = not self.selected
      self.raise_event("click")
