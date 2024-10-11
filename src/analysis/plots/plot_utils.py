import plotly.express as px
from src.constants.paths import PLOT_EXAMPLES_PATH

# Define default plot colors
PLOT_COLORS = ["#7eb0d5", "#fd7f6f", "#b2e061", "#ffb55a"]


# Apply custom layout to figures
def apply_custom_layout(
    fig,
    title_x=0.5,
    title_y=0.97,
    margins=dict(l=20, r=20, t=40, b=20),
    legend_title="",
    xaxis_title="",
    yaxis_title="",
    width=800,
    height=500,
    bargap=0.05,
):
    """
    Apply custom layout values to a Plotly figure.

    Parameters:
    - fig: Plotly figure.
    - title_x: Horizontal alignment of the title.
    - title_y: Vertical alignment of the title.
    - margins: Margins for the plot.
    - legend_title: Title of the legend.
    - xaxis_title: X-axis title.
    - yaxis_title: Y-axis title.
    - width: Width of the figure.
    - height: Height of the figure.
    - bargap: Gap between bars for bar charts.
    """
    fig.update_layout(
        title_x=title_x,
        title_y=title_y,
        margin=margins,
        width=width,
        height=height,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5,
        ),
        bargap=bargap,
        legend_title=legend_title,
        yaxis_title=yaxis_title,
        xaxis_title=xaxis_title,
    )
    return fig

# HISTOGRAM
def create_histogram(
    df,
    x_axis: str,
    title: str = None,
    nbins=16,
    color: str = "#3D6CB9",
    save_plot_as_png: str = None,
    show_plot: bool = False,
    file_name: str = None,
    **layout_kwargs,
):
    """
    Create a histogram using Plotly Express and apply custom layout settings.

    Parameters:
    - df: DataFrame containing the data.
    - x_axis: The column to plot on the x-axis.
    - title: Title of the histogram.
    - nbins: Number of bins (default: 16).
    - color: Color of the bars (default: "#3D6CB9").
    - save_plot_as_png: Path to save the plot as PNG.
    - show_plot: Boolean to control whether to display the plot.
    - file_name: Custom file name to save the plot.
    """
    fig = px.histogram(df, x=x_axis, nbins=nbins, title=title)
    fig.update_traces(marker_color=color)
    fig = apply_custom_layout(fig, **layout_kwargs)

    if save_plot_as_png:
        file_path = f"{PLOT_EXAMPLES_PATH}/{file_name}"
        fig.write_image(file_path)

    if show_plot:
        fig.show()

# LINE PLOT
def create_line_plot(
    df,
    x_axis: str,
    y_axis: str,
    title: str = None,
    color: str = "#3D6CB9",
    line_width: int = 3,
    save_plot_as_png: str = None,
    show_plot: bool = False,
    file_name: str = None,
    rolling_average: bool = False,
    rolling_window_days: int = 7,
    y_label: str = None,
    x_label: str = None,
    **layout_kwargs,
):
    """
    Create a line plot using Plotly Express and apply custom layout settings.

    Parameters:
    - df: DataFrame containing the data.
    - x_axis: The column to plot on the x-axis.
    - y_axis: The column to plot on the y-axis.
    - title: Title of the line plot.
    - color: Color of the line (default: "#3D6CB9").
    - line_width: Width of the line (default: 3).
    - save_plot_as_png: Path to save the plot as PNG.
    - show_plot: Boolean to control whether to display the plot.
    - file_name: Custom file name to save the plot.
    - rolling_average: Bool to indicate whether to plot a rolling average.
    - rolling_window_days: Window size for the rolling average calculation.
    - x_label: Custom x-axis label.
    - y_label: Custom y-axis label.
    """
    if rolling_average:
        df[f"{y_axis} Rolling"] = df[y_axis].rolling(window=rolling_window_days).mean()
        y_axis = f"{y_axis} Rolling"
        title = title or f"Rolling {y_label} ({rolling_window_days}-Day Average)"
    else:
        title = title or y_label

    fig = px.line(df, x=x_axis, y=y_axis, title=title, labels={y_axis: y_label, x_axis: x_label})
    fig.update_traces(line=dict(color=color, width=line_width))
    fig = apply_custom_layout(fig, **layout_kwargs)

    if save_plot_as_png:
        file_path = f"{PLOT_EXAMPLES_PATH}/{file_name}"
        fig.write_image(file_path)

    if show_plot:
        fig.show()

# BOX PLOT
def create_box_plot(
    df,
    x_axis: str,
    y_axis: str,
    title: str = None,
    color: str = "#3D6CB9",
    save_plot_as_png: str = None,
    show_plot: bool = False,
    file_name: str = None,
    y_label: str = None,
    x_label: str = None,
    **layout_kwargs,
):
    """
    Create a box plot using Plotly Express and apply custom layout settings.

    Parameters:
    - df: DataFrame containing the data.
    - x_axis: The column to plot on the x-axis.
    - y_axis: The column to plot on the y-axis.
    - title: Title of the box plot.
    - color: Color of the boxes (default: "#3D6CB9").
    - save_plot_as_png: Path to save the plot as PNG.
    - show_plot: Boolean to control whether to display the plot.
    - file_name: Custom file name to save the plot.
    - x_label: Custom x-axis label.
    - y_label: Custom y-axis label.
    """
    fig = px.box(df, x=x_axis, y=y_axis, title=title, labels={y_axis: y_label, x_axis: x_label})
    fig.update_traces(marker_color=color)
    fig = apply_custom_layout(fig, **layout_kwargs)

    if save_plot_as_png:
        file_path = f"{PLOT_EXAMPLES_PATH}/{file_name}"
        fig.write_image(file_path)

    if show_plot:
        fig.show()
