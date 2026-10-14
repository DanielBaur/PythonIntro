import numpy as np
import plotly.graph_objects as go


def styled_figure(data: list, title: str = "Plot", title_x: str = "", title_y: str = "") -> go.Figure:
    """
    This function provides a uniform style framework for the plots.
    :param data: list of plotly.graph_objects
    :type data: list
    :param title: Title of the figure
    :type title: str
    :param title_x: X-axis title
    :type title_x: str
    :param title_y: Y-axis title
    :type title_y: str
    :return: plotly.graph_objects.Figure
    """

    # Define layout
    layout = go.Layout(
        title=dict(
            text=title,
            x=0.5,
            xanchor="center"
        ),
        
        showlegend=True,
        legend=dict(
            yanchor="top", y=0.9, 
            xanchor="left", x=1.05
        ),
        
        xaxis=dict(
            title=title_x,
            linecolor="#BCCCDC",
            showspikes=False,  # Show spike line for X-axis
            # Format spike
            spikethickness=2,
            spikedash="dot",
            spikecolor="#999999",
            spikemode="marker",
            spikesnap="data",
            showline=True,
            linewidth=1,
            automargin=True,
        ),
        
        yaxis=dict(
            title=title_y,
            linecolor="#BCCCDC",
            showline=True,
            linewidth=1,
            automargin=True,
        ),
        
        width=700,
        height=550,
        margin=dict(
            l=50, 
            r=50, 
            b=100, 
            t=100, 
            pad=2),
        
        plot_bgcolor="white",
        
        hovermode="closest",
        hoverdistance=100,  # Distance to show hover label of data point
        spikedistance=1000,  # Distance to show spike
    )

    # Create figure
    fig = go.Figure(data=data, layout=layout)
    return fig


def dot_scatter(
    visible: bool = True,
    x: np.array = np.array([]),
    y: np.array = np.array([]),
    name: str = "Observed points",
    mode="markers+text",
    showlegend: bool = True,
    text=None,
) -> go.Scatter:
    """
    This function creates a scatter plot with dots and text.
    :param visible:
    :type visible: bool
    :param x: x values
    :type x: np.ndarray
    :param y: y values
    :type y: np.ndarray
    :param name: Name of the scatter trace
    :type name: str
    :param mode: Mode of the scatter trace, default: "markers+text"
    :type mode: str
    :param showlegend: Show legend
    :type showlegend: bool
    :param text: Text to be displayed on each point
    :type text: list
    :return: plotly.graph_objects.Scatter
    """
    return go.Scatter(
        x=x,
        y=y,
        visible=visible,
        text=text,
        textposition="top center",
        mode=mode,
        name=name,
        marker=dict(size=8),
        showlegend=showlegend,
    )
