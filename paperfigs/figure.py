import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

# figure styling - assuming even number of rows
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

from paperfigs.styles import style_pdf_text, style_axes

def init_figure(nrows=None, ncols=None, col_widths=None, row_widths=None, white_space=0.1, is_subplot=False, fig=None, gs=None, figsize=None, return_gs=False, return_fig=False, uppercase=True):
  sz = 100
  
  if not is_subplot:
    fig = plt.figure(constrained_layout=False, figsize=figsize)  # Disable constrained_layout
    gs = GridSpec(sz, sz, figure=fig)


  if nrows is None:
    nrows = len(col_widths)
  if ncols is None:
    ncols = len(row_widths)

  if row_widths is None:
    row_widths = [1] * nrows
  if col_widths is None:
    col_widths = [[1] * ncols for _ in range(nrows)]
  
  if is_subplot:
    pad = int(13 * white_space/0.1)
  else:
    pad = 0

  row_sz = sz // nrows
  row_pos = 0

  ax_dict = dict()
  gs_dict = dict()
  i = 0

  if uppercase:
    labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']  # List of labels
  else:
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']  # List of labels

  for row_idx, (widths, row_width) in enumerate(zip(col_widths, row_widths)):
    row_sz = int(row_width/np.sum(row_widths) * sz)
    col_pos = 0

    if is_subplot:
      col_pos = pad

    for col_idx, width in enumerate(widths):
      col_sz = int(width/np.sum(widths) * sz)
      gs_sub = GridSpecFromSubplotSpec(100 + pad, 100 + pad, subplot_spec=gs[row_pos:row_pos+row_sz, col_pos:col_pos+col_sz])
      ax = fig.add_subplot(gs_sub[:, :])

      ax_dict[labels[i]] = ax
      gs_dict[labels[i]] = gs_sub

      col_pos += col_sz
      i += 1

    row_pos += row_sz
  
  ws_ratio = fig.get_size_inches()[1]/fig.get_size_inches()[0]
  for i, ax in enumerate(ax_dict.values()):
      pos = ax.get_position()  # Get the current position
      ax.set_position([pos.x0 + ws_ratio*white_space, pos.y0 + white_space, pos.width - ws_ratio*white_space, pos.height - white_space])  # Add some whitespace
      ax.text(ax.get_position().x0 - 0.8 * ws_ratio*white_space, ax.get_position().y1 + 0.3 * white_space, labels[i], va="center", ha="center", weight="bold", transform=fig.transFigure, fontsize=14)
  
  style_pdf_text()
  style_axes(ax_dict)
  if return_fig and return_gs:
    return ax_dict, gs_dict, fig
  elif return_fig:
    return ax_dict, fig
  elif return_gs:
    return ax_dict, gs_dict
  return ax_dict



## WORKING - PLOTTING SUBPLOTS WITHIN SUBPLOT ##
"""
if rec and row_idx ==0 and col_idx == 0:
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.spines['bottom'].set_visible(False)
  ax.spines['left'].set_visible(False)
  ax.tick_params(top=False, bottom=False, left=False, right=False, labelleft=False, labelbottom=False, labeltop=False, labelright=False)

  plot_grids(gs_sub, rec=False, ws=0.05)
else:
  ax = fig.add_subplot(gs_sub[:, :]) #gs[row_pos:row_pos+row_sz, col_pos:col_pos+col_sz])
"""



  