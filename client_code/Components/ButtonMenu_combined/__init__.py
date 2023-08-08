from ._anvil_designer import ButtonMenu_combinedTemplate
from anvil import *
from anvil.js.window import document
import random, string

class ButtonMenu_combined(ButtonMenu_combinedTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # TODO: needs an event handler to close when not focused
    # self.id = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

  @property
  def text(self):
    return self._text
  @text.setter
  def text(self, value):
    self._text = value
    self.menu_button.text = value

  @property
  def appearance(self):
    return self._appearance
  @appearance.setter
  def appearance(self, value):
    self.menu_button.appearance = value

  # @property
  # def menuOpen(self):
  #   return self._menuOpen
  # @menuOpen.setter
  # def menuOpen(self, value):
  #   self._menuOpen = value or False
  #   self.dom_nodes['anvil-m3-buttonMenu-container']
  #   if value:
  #     # check if the eventlistener is there. do nothing if so.
  #     # else add it.
  #     pass
  #   else:
  #     # remove event listener
  #     pass
  #     # self.dom_nodes['anvil-m3-buttonMenu-container'].removeEventListener('focus', self.checkFocus)

  @property
  def enabled(self):
    return self._enabled
  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    self.menu_button.enabled = value

  @property
  def position(self):
    return self._position;
  @position.setter
  def position(self, value = {"topLeft": 0, "topRight": 0, "bottomLeft": 0, "y2": 0}):
    self._position = value

  def toggle_menu_visibility(self, **event_args):
    self.set_visibility()
    self.menuOpen = not self.dom_nodes['anvil-m3-buttonMenu-items-container'].classList.contains('anvil-m3-buttonMenu-items-hidden')

  def set_visibility(self, value = None):
    classes = self.dom_nodes['anvil-m3-buttonMenu-items-container'].classList
    if value is not None:
      classes.toggle('anvil-m3-buttonMenu-items-hidden', not value)
    else:
      classes.toggle('anvil-m3-buttonMenu-items-hidden')

  def checkFocus(self, event):
    # document.activeElement
    # var descendants = theElement.querySelectorAll("*");
    print(event.target)
    pass

  def _anvil_get_design_info_(self, as_layout=False):
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["interactions"] = [
      {
        "type": "on_selection",
        "callbacks": {
          "onSelectDescendent": self._on_select_descendant,
          "onSelectOther": self._on_select_other
        }
      },
    ]
    return design_info

  def _on_select_descendant(self):
    print("Selected! Open")
    self.set_visibility(True)

  def _on_select_other(self):
    print("Something else selected! Close the menu!")
    self.set_visibility(False)

  def get_button_position(self, **event_args):
    """This method is called when the form is shown on the page"""
    pass

