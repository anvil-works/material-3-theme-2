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

  @property
  def selected_button(self):
    return self._selected_button

  @selected_button.setter
  def selected_button(self, button):
    self.select(button, True)

  def select(self, button, new_state=True):
    old_button = self._selected_button
    if new_state:
      if button == old_button:
        return
      # Deselect the previously selected button
      if old_button:
        self._update_dom(old_button, False)
      # Select the new button
      self._selected_button = button
      self._update_dom(button, True)
      self._raise_change_event()

    elif old_button == button:
      self._selected_button = None
      self._update_dom(button, False)
      self._raise_change_event()

  # @TODO: Yuck
  def _raise_change_event(self):
    try:
      self.raise_event("change")
    except AttributeError:
      pass

  @staticmethod
  def _update_dom(button, new_state):
    try:
      button._update_dom(new_state)
    except AttributeError:
      pass

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
