from anvil import pluggable_ui
from ._Components.Button import Button
from ._Components.TextInput.TextField import TextField
from ._Components.Checkbox import Checkbox

def make_footer_button(button_type, **kwargs):
  return Button(**kwargs)

pluggable_ui.provide("m3", {
  "anvil.TextBoxWithLabel": TextField,
  "anvil.TextBox": TextField,
  "anvil.Button": Button,
  "anvil.CheckBox": Checkbox,
  "anvil.alerts.FooterButton": make_footer_button
})

