from anvil.js import import_from
from anvil.js.window import document, window

# https://floating-ui.com/
# can't import from cdn, load js file in assets and import from there
fui = import_from("https://cdn.jsdelivr.net/npm/@floating-ui/dom@1.5.3/+esm")

_static_arrow_position = {
  'top': 'bottom',
  'right': 'left',
  'bottom': 'top',
  'left': 'right',
}

def auto_update(
  reference_el,
  floating_el,
  *,
  placement="bottom",
  strategy="absolute",
  offset=6,
  shift={"padding": 5},
  hide={"padding": 15},
  arrow=None
):
  """starts auto updating position of floating element to a reference element
  returns a cleanup function
  if using arrow, arrow should be an HTMLElement
  call this function in x-anvil-page-added
  call the cleanup in x-anvil-page-removed"""

  def update(*args):
    floating_el.style.removeProperty('height')
    floating_el.style.removeProperty('bottom')
    floating_el.style.removeProperty('top')
    
    middleware = [fui.offset(offset), fui.flip(), fui.shift(shift), fui.hide(hide)]
    if arrow:
      middleware.append(fui.arrow({"element": arrow}))
    
    rv = fui.computePosition(reference_el, floating_el, {
      'placement': placement,
      'strategy': strategy,
      'middleware': middleware,
    })

    floating_el.style.left = f"{rv.x}px"

    if "bottom" in rv.placement:
      floating_el.style.top = f"{rv.y}px"
    else:
      

    # custom stuff. This is not from fui. It's just so we can get the menus to resize and scroll if there iesn't enough vertical space
    # el_height = int(window.getComputedStyle(floating_el).height[:-2])
    # el_height = floating_el.offsetHeight
    # print(el_height)
    
    # if "bottom" in rv.placement:
    #   available_space = window.innerHeight - reference_el.getBoundingClientRect().bottom
    #   # print(available_space)
    #   if (available_space < el_height):
    #     # pass
    #     floating_el.style.height = f"{available_space}px"
    # else:
    #   available_space = reference_el.getBoundingClientRect().top
    #   # print(available_space)
    #   if (available_space < el_height):
    #     # pass
    #     floating_el.style.height = f"{available_space}px"
    
    middlewareData = rv.middlewareData
    if "hide" in middlewareData:
      hidden = middlewareData.hide.referenceHidden
      floating_el.style.visibility = "hidden" if hidden else "visible"

    if arrow and "arrow" in middlewareData:
      x = middlewareData.arrow.get("x")
      y = middlewareData.arrow.get("y")
      static_side = _static_arrow_position.get(placement.split("-")[0])
      arrow.style.left = "" if x is None else f"{x}px"
      arrow.style.top = "" if y is None else f"{y}px"
      arrow.style.right = ""
      arrow.style.bottom = ""
      if static_side:
        # assumes the arrow element is 8px 8px
        arrow.style[static_side] = "-4px"


  return fui.autoUpdate(reference_el, floating_el, update)
