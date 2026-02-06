import networkx as nx
import pandas as pd


def build_transaction_graph(df):
    G = nx.Graph()

    for _, row in df.iterrows():
        user = f"user:{row['user_id']}"
        device = f"device:{row['device_id']}"
        merchant = f"merchant:{row['merchant_id']}"

        G.add_edge(user, device)
        G.add_edge(device, merchant)

    return G


def compute_graph_features(df, G):

    device_degree = dict(G.degree())
    df["device_graph_degree"] = df["device_id"].apply(
        lambda x: device_degree.get(f"device:{x}", 0)
    )

    merchant_degree = dict(G.degree())
    df["merchant_graph_degree"] = df["merchant_id"].apply(
        lambda x: merchant_degree.get(f"merchant:{x}", 0)
    )

    return df
