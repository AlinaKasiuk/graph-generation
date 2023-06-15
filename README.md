# Generating different set-up with graphs for parallel line covering task

## Starting python-igraph:

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

### TODO:
* Generate bases:
  * Connect to all nodes
  * Cennect with nodes on a distance less than L
* Garantee every node can be accesed at least from one base
* Devide the segments: Add more nodes in between
* Avoid edge overlapping
 
