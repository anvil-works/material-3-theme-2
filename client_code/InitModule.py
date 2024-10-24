import anvil.pluggable_ui
from .._Components.Button import Button
from .._Components.TextInput.TextField import TextField

def make_footer_button(button_type, **kwargs):
  return Button(**kwargs)

anvil.pluggable_ui.provide("m3", {
  "anvil.TextBoxWithLabel": TextField,
  "anvil.TextBox": TextField,
  "anvil.Button": Button,
  "anvil.alerts.FooterButton": make_footer_button
})


print('hello world')

