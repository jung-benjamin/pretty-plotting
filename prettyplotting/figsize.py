#! /usr/bin/env python3

"""Adjust the figsize to LaTeX"""

def set_size(width, fraction=1, subplots=(1, 1), higher=False):
    """Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width: float or string referring to a documentclass
            Document textwidth or columnwidth in pts
            Use \the\columnwidth or \the\textwidth in the 
            LaTeX document to find the correct width
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy
    subplots: tuple of two integers, optional 
            Configuration of subplots in the figure
    higher: bool, optional
            rescale the figure to be longer in the y-axis

    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    
    if width == 'mythesis':
        width_pt = 426.79
    elif width == 'a4paper-default':
        width_pt = 360.0
    elif width == 'twocolumn':
        width_pt = 252.
    elif width == 'beamer':
        width_pt = 577.17543
    else:
        width_pt = width
        
    # Width of figure (in pts)
    fig_width_pt = width_pt * fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    # https://disq.us/p/2940ij3
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    
    if higher:
        fig_height_in = fig_width_in * golden_ratio * (subplots[0] * 1.3 / subplots[1])
    else:
        fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])
    fig_dim = (fig_width_in, fig_height_in)

    return fig_dim
