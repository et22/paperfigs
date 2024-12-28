def apply_over_axes(func, ax_dict):
    for i, ax in enumerate(ax_dict.values()):
      func(ax)

def asterix_generator(p):
  if p < 0.001:
    return "***"
  elif p < 0.01:
    return "**"
  elif p < 0.05:
    return "*"
  else:
    return ""