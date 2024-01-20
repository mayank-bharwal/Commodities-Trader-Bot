import plotly.graph_objects as go

def create_graph_data(trading_history):
    """
    Creates data for the graph based on the trading history.

    :param trading_history: List of tuples containing timestamps and corresponding returns.
    :return: A dictionary formatted for Plotly.
    """
    timestamps = [item[0] for item in trading_history]
    returns = [item[1] for item in trading_history]

    trace = go.Scatter(x=timestamps, y=returns, mode='lines+markers', name='Returns')
    return trace

def update_graph_data(graph_trace, new_data):
    """
    Updates the existing graph trace with new data.

    :param graph_trace: The existing graph trace.
    :param new_data: New data to add (timestamp, return).
    """
    graph_trace['x'].append(new_data[0])  # timestamp
    graph_trace['y'].append(new_data[1])  # return
