import plotly.express as px


def plot_lap_times(df):
    """
    Create a lap time vs lap number chart
    """

    fig = px.line(
        df,
        x="LapNumber",
        y="LapTimeSeconds",
        color="Driver",
        title="Lap Time Comparison",
        markers=True
    )

    fig.update_layout(
        xaxis_title="Lap Number",
        yaxis_title="Lap Time (seconds)",
        template="plotly_dark"
    )

    fig.show()