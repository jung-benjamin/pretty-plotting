#! /usr/bin/env python3

"""Adjust the figsize to LaTeX"""

def set_size(width, fraction=1, subplots=(1, 1), ratio='golden'):
    """Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width
        float or string referring to a documentclass
        Document textwidth or columnwidth in pts
        Use \the\columnwidth or \the\textwidth in the 
        LaTeX document to find the correct width
    
    fraction
        float, optional
        Fraction of the width which you wish the figure to occupy
    
    subplots 
        tuple of two integers, optional 
        Configuration of subplots in the figure
    
    ratio 
        float or string, optional
        ratio of the x and y directions of the plots

    Returns
    -------
    fig_dim
        tuple
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

    if ratio == 'golden':
        ratio_num = golden_ratio
    else:
        ratio_num = ratio

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    
    fig_height_in = fig_width_in * ratio_num * (subplots[0] / subplots[1])
    fig_dim = (fig_width_in, fig_height_in)

    return fig_dim
