# src/analysis/plots/plot_styles.py


def apply_plot_styles(fig, style):
    fig.update_layout(**style)
    return fig


PLOT_COLORS = ["#7eb0d5", "#fd7f6f", "#b2e061", "#ffb55a"]
PLOT_COLORS_LIGHT = ["#c7d6eb", "#f9d4d0", "#d9f4be", "#ffe6c7"]
PLOT_COLORS_DARK = ["#3d6cb9", "#c13a2d", "#6fae3f", "#c6851a"]

BAR_CHART_PLOT_STYLE = {
    "template": "seaborn",
    "plot_bgcolor": "rgba(255,255,0,0)",
    "legend": {
        "title": None,
        "orientation": "h",
        "yanchor": "top",
        "y": -0.2,
        "xanchor": "center",
        "x": 0.5,
        "font": {"size": 12},
    },
    "xaxis": {
        "showgrid": False,
        "zeroline": False,
    },
    "yaxis": {
        "showgrid": False,
        "zeroline": False,
        "showticklabels": False,
    },
}
