# Graph Generation for Parallel Line Covering Tasks

This repository contains Python code for generating various graph structures, specifically tailored for tasks involving parallel line coverage. The project focuses on creating custom graphs with defined nodes and edges, incorporating attributes like weight (distance) and segment identification. It leverages the `igraph` library for graph manipulation and `matplotlib` for visualization.

## Features

- **Custom Graph Generation:** Functions to generate different graph structures, including:
    - **Delaunay Triangulation:** Creates a triangulation of a set of points.
    - **Fully Connected Graph:** Connects every node to every other node.
    - **Max Length Connection:** Connects nodes only if the distance between them is below a specified threshold `L`.
    - **N-Closest Connection:** Connects each node to its `N` closest neighbors.
- **Node and Edge Attributes:** Nodes have X and Y coordinates, and edges have 'weight' (distance) and 'is segment' (boolean) attributes.
- **Parallel Line Segment Generation:** Includes functionality to generate segments on parallel lines, which is crucial for the intended application.

## Implementation Details

The core logic resides in `graph-generation.py` and `Starting python-igraph.ipynb`.

- **`LineGenerate(length, m)`:** This function generates a line with `m` random segments, defining their start and end coordinates.
- **`create_graph(points, graph_type, L=None, N=None)`:** This function takes a set of points and a `graph_type` (e.g., 'delaunay', 'full', 'max_length', 'n_closest') to construct the graph. Optional parameters `L` and `N` are used for specific graph types.
- **Visualization:** The `matplotlib.pyplot` library is used to visualize the generated graphs, allowing for a clear understanding of the graph structure.

## Usage

To use this project, you need to have Python, `igraph`, `matplotlib`, `numpy`, `pandas`, and `scipy` installed. You can run the `graph-generation.py` script or execute the Jupyter Notebook `Starting python-igraph.ipynb`.

```bash
python graph-generation.py
```

## Potential Applications

- **Drone Coverage Optimization:** Generating optimal flight paths for drones to cover a given area with parallel lines.
- **Robotics:** Path planning and navigation for autonomous robots.
- **Network Design:** Designing efficient communication or transportation networks.
  
### TODO:
* Generate bases:
  * Connect to all nodes
  * Cennect with nodes on a distance less than L
* Garantee every node can be accesed at least from one base
* Devide the segments: Add more nodes in between
* Avoid edge overlapping
 
### Python-igraph tutorial:
https://python.igraph.org/en/stable/tutorial.html

### Starting python-igraph:

<b> Segments on parallel lines </b>

<b> Nodes:</b> Start and end points 
<b> Node attributes:</b> X and Y coordinates
<b> Edge attributes:</b> 
* "Weight" is equal to the distance between points conected by the edge
* "Is segment": bool

<b> Generated graph structure:</b> 
* Delaunay triangulation
* Full Connected Graph
* Max lenght: Connect only nodes with a distance less than L
* N-closest

