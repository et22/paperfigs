import matplotlib

from paperfigs.utils import apply_over_axes

def style_pdf_text():
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42

def style_axes(ax_dict):
    apply_over_axes(style_axis, ax_dict)

def style_axis(ax, fontsize=10):
  ax.tick_params(axis='both', labelsize=fontsize)  # Set the font size for tick labels
  ax.set_xlabel('', fontsize=fontsize)  # Set font size for the X-axis label
  ax.set_ylabel('', fontsize=fontsize)  # Set font size for the Y-axis label
  ax.set_title('', fontsize=fontsize)  # Set font size for the title

  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)