import os
import networkx as nx
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Facebook Ego Network Analysis",
    page_icon="🕸️",
    layout="wide",
)

# Determine base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def resolve_path(*parts):
    return os.path.join(BASE_DIR, *parts)


def find_visuals_dir():
    preferred = resolve_path("visualizations")
    fallback = resolve_path("data")
    if os.path.isdir(preferred):
        return preferred
    return fallback


def list_ego_nodes(data_dir):
    nodes = []
    for name in os.listdir(data_dir):
        if name.endswith(".edges"):
            nodes.append(name.replace(".edges", ""))
    return sorted(nodes, key=lambda x: int(x) if x.isdigit() else x)


@st.cache_data(show_spinner=False)
def load_graph(data_dir, ego_node):
    edges_path = resolve_path("data", f"{ego_node}.edges")
    if not os.path.exists(edges_path):
        return None
    graph = nx.read_edgelist(edges_path, nodetype=int)
    return graph


@st.cache_data(show_spinner=False)
def compute_stats(graph):
    n_nodes = graph.number_of_nodes()
    n_edges = graph.number_of_edges()
    degrees = [d for _, d in graph.degree()]
    avg_degree = sum(degrees) / max(n_nodes, 1)
    clustering = nx.average_clustering(graph) if n_nodes > 0 else 0.0
    if n_nodes > 0 and nx.is_connected(graph):
        avg_path_length = nx.average_shortest_path_length(graph)
    else:
        lcc = max(nx.connected_components(graph), key=len)
        subgraph = graph.subgraph(lcc)
        avg_path_length = nx.average_shortest_path_length(subgraph)
    return {
        "nodes": n_nodes,
        "edges": n_edges,
        "avg_degree": avg_degree,
        "clustering": clustering,
        "avg_path_length": avg_path_length,
    }


st.title("Facebook Ego Network Analysis")
st.caption(
    "Network science approach to optimizing outreach via community detection and influence modeling."
)

left, right = st.columns([2, 1])

with left:
    st.subheader("Project Overview")
    st.write(
        "This demo shows basic statistics for a selected ego network from the "
        "Stanford SNAP Facebook dataset, along with key analysis visuals."
    )

with right:
    st.subheader("Select Ego Network")
    data_dir = resolve_path("data")
    if not os.path.isdir(data_dir):
        st.error(f"Data directory not found at: {data_dir}")
        st.info("Expected location: data/ folder in the project root")
        st.stop()
    ego_nodes = list_ego_nodes(data_dir)
    if not ego_nodes:
        st.error("No ego network files (*.edges) found in data directory.")
        st.stop()
    default_node = "0" if "0" in ego_nodes else ego_nodes[0]
    ego_node = st.selectbox("Ego node", ego_nodes, index=ego_nodes.index(default_node))

graph = load_graph(data_dir, ego_node)
if graph is None:
    st.error("Unable to load the ego network data.")
    st.stop()

stats = compute_stats(graph)

st.subheader("Network Statistics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Nodes", f"{stats['nodes']}")
col2.metric("Edges", f"{stats['edges']}")
col3.metric("Avg Degree", f"{stats['avg_degree']:.2f}")
col4.metric("Clustering", f"{stats['clustering']:.3f}")

st.write(
    f"Average path length (largest connected component): "
    f"{stats['avg_path_length']:.2f}"
)

st.subheader("Key Visualizations")
visuals_dir = find_visuals_dir()
visuals = [
    "day1_results.png",
    "day2_results.png",
    "day3_results.png",
    "part1_results.png",
    "part2_results.png",
]

found_visuals = []
for image_name in visuals:
    image_path = os.path.join(visuals_dir, image_name)
    if os.path.exists(image_path):
        found_visuals.append((image_name, image_path))

if found_visuals:
    cols = st.columns(2)
    col_index = 0
    for image_name, image_path in found_visuals:
        cols[col_index].image(image_path, caption=image_name, use_container_width=True)
        col_index = 1 - col_index
else:
    st.info("Visualizations will appear here. Run the full analysis notebook to generate them.")

st.subheader("Methods Summary")
st.markdown(
    "- Louvain community detection\n"
    "- Centrality analysis (degree, betweenness, eigenvector)\n"
    "- Threshold-based influence simulation\n"
    "- Comparison of targeted vs. random seeding"
)

st.subheader("Links")
st.markdown(
    "- Repository: https://github.com/aymanmomin/Facebook-Ego-Network-Analysis-for-Political-Outreach-Optimization\n"
    "- Dataset: https://snap.stanford.edu/data/ego-Facebook.html"
)
