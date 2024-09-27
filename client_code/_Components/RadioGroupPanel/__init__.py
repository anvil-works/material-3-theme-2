from ._anvil_designer import RadioGroupPanelTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RadioGroup:
  def __init__(self):
    self._buttons = []
    self._selected_button = None

  @property
  def buttons(self):
    return self._buttons

  def _add_button(self, button):
    self._buttons.append(button)

  def _handle_change(self):
    try:
      self.raise_event("change")
    except AttributeError:
      pass
  
  @property
  def selected_button(self):
    for button in self.buttons:
      if button.selected:
        return button
    return None

  @selected_button.setter
  def selected_button(self, button):
    if button is None:
      # Deselect the currently selected button
      selected_button = self.selected_button
      if selected_button:
        selected_button.selected = False
    else:
      button.selected = True

  @staticmethod
  def enclosing(component):
    while component:
      component = component.parent
      if isinstance(component, RadioGroup):
        return component

    # No enclosing RadioGroup container, return a global one
    global global_radio_group
    return global_radio_group


global_radio_group = RadioGroup()


class RadioGroupPanel(RadioGroupPanelTemplate, RadioGroup):
  def __init__(self, **properties):
    RadioGroup.__init__(self)
    self.init_components(**properties)
