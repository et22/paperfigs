import numpy as np
import seaborn as sns
from scipy.stats import pearsonr, spearmanr, ranksums

from paperfigs.utils import asterix_generator

def plot_line(x, y, ax, hue=None, palette=None, errorbar='se', label=""):
  num_lines = len(np.unique(hue)) if hue is not None else 1

  if palette is None:
    palette = sns.color_palette("icefire", desat = 1, n_colors=num_lines)

  if hue is not None:
    sns.lineplot(x=x, y=y, errorbar=errorbar, hue=hue, ax=ax, palette=palette)
    ax.legend(frameon=False) 
  else:
    sns.lineplot(x=x, y=y, errorbar=errorbar, ax=ax, hue = [label for _ in range(len(x))], palette=palette)

    if label != "":
      ax.legend(frameon=False) 

def plot_scatter(x, y, ax, color=None, include_text=True, corr_type='pearson'):
  if color is None:
    color = 'k'

  if corr_type == 'pearson':
    result = pearsonr(x, y)
    sub = 'p'
  elif corr_type == 'spearman':
    result = spearmanr(x, y)
    sub = 's'
  else:
    raise ValueError("corr_type must be 'pearson' or 'spearman'")

  ax.scatter(x, y, s=5, c=color)

  if include_text:
    r = result.statistic
    p = result.pvalue
    n = len(x)
    ax.text(0.2, 0.6, f'$r_{sub}={np.around(r, 2)}$\n$p_{sub}={"{:.2e}".format(p)}$ \n$n ={int(n)}$', transform=ax.transAxes)

def plot_bar(x, y, ax, hue=None, palette=None, label="", include_text=True, stat_type="mean", errorbar='se'):
    num_bars = len(np.unique(hue)) if hue is not None else 1

    if palette is None:
      palette = sns.color_palette("icefire", desat = 1, n_colors=num_bars)
    if hue is not None:
      sns.barplot(x=x, y=y, ax=ax, hue=hue, palette=palette, errorbar=errorbar,capsize=0.3, err_kws={'linewidth': 1})
      ax.legend(frameon=False) 
    else:
      sns.barplot(x=x,y=y,errorbar=errorbar, ax=ax, hue = [label for _ in range(len(np.unique(x)))], palette=palette)

    if label != "":
      ax.legend(frameon=False) 

    if include_text:
      hue_values = np.unique(hue)
      x_values = np.sort(np.unique(x))

      assert len(hue_values) == 2

      for i, x_value in enumerate(x_values):
        idx1 = hue_values[0] == hue
        idx2 = hue_values[1] == hue
        y1 = y[idx1 & (x == x_value)]
        y2 = y[idx2 & (x == x_value)]
        result = ranksums(y1, y2)

        # get range of y axis
        y_min, y_max = ax.get_ylim()
        x_min, x_max = ax.get_xlim()
        x_range = x_max - x_min
        y_range = y_max - y_min

        # select y locations for text and asterix
        y_val = max(np.mean(y1), np.mean(y2))
        ast_y = y_val + 0.22 * y_range
        text_y = y_val + 0.2 * y_range

        # display text on the axis and vertically center it
        if result.pvalue < 0.05:
          ax.text(i, ast_y, asterix_generator(result.pvalue), ha='center')
          ax.plot([i-.05*x_range, i + .05 * x_range], [text_y, text_y], 'k-')
