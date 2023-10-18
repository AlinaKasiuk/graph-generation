# -*- coding: utf-8 -*-
"""
Generating custum graphs to join the segments on parallel lines

Created on Wed Sep 20 12:40:41 2023

@author: Alina Kasiuk
"""

import igraph as ig
import matplotlib.pyplot as plt

from scipy.spatial import Delaunay

import numpy as np
import random
import pandas as pd
import math


def LineGenerate(lenght, m):
    """
    Creating a line with m random segments
    """
    line = np.zeros(lenght,)
    ab = np.array(sorted(random.sample(range(0, lenght-1), m*2))) # random start and end of the segments
    ab = ab.reshape((m,2)) # start and end of the segments coordinates
    return ab



def MultipleLines(line_lenght, min_seg, max_seg, line_num, max_hight):
    """
    Creating n parallel lines with m random segments each
    """
    
    seg_hights = sorted(random.sample(range(0, max_hight), line_num))
    lines = pd.DataFrame(columns = ['Start','End', 'Height', 'Line'])
    for i in range(line_num):
        line =  pd.DataFrame(LineGenerate(line_lenght, random.randrange(min_seg, max_seg)), columns = ['Start','End'])
        line["Height"] = seg_hights[i]
        line["Line"] = i
        lines = pd.concat([lines,line], ignore_index=True)
    return lines


def PlotTheGraph(g):
    """
    Plotting a graph
    """
    
    edge_width = [2 + 10 * int(is_segment) for is_segment in g.es["is_segment"]]
    fig, ax = plt.subplots(figsize=(50,50))
    ig.plot(
        g,
        target=ax,
        layout='auto',
        vertex_size=0.5,
        vertex_frame_width=4.0,
        edge_width = edge_width,
    )
    plt.show()


def AddSegments(g, segments):
    """
    Adding segment edges on a graph
    """
    
    for i in range(segments.shape[0]):
        g.es[g.get_eid(int(segments[i,0]), int(segments[i,1]))]["is_segment"] = True    
    g.es["is_segment"] = [False if is_segment is None else is_segment for is_segment in g.es["is_segment"]]


def WeighEdges(g):
    """
    Defining edges weights as a geometrical distance
    """   
    
    for i in range(len(g.get_edgelist())):
        edge_nodes = g.get_edgelist()[i]
        x_dist = g.vs[edge_nodes[1]]['x'] - g.vs[edge_nodes[0]]['x']
        y_dist = g.vs[edge_nodes[1]]['y'] - g.vs[edge_nodes[0]]['y']
        
        distance = math.sqrt(x_dist**2+y_dist**2)        
        g.es[i]["weight"] = distance


def BuildDelaunay(g, segments):
    """
    Delaunay triangulation
    """  
    g_delaunay = g.copy()
    layout = g_delaunay.layout_auto()   
    delaunay = Delaunay(layout.coords)
    for tri in delaunay.simplices:
        g_delaunay.add_edges([
            (tri[0], tri[1]),
            (tri[1], tri[2]),
            (tri[0], tri[2]),
        ])
    g_delaunay.simplify()
    
    WeighEdges(g_delaunay)
    AddSegments(g_delaunay, segments)
    PlotTheGraph(g_delaunay)
    return g_delaunay


def BuildFull(n_vertices, segments):
    
    """
    Full connected graph
    """  
    
    g_comp = g.complementer(loops=False)
    g_full = g|g_comp
    layout = g_full.layout_auto()   
    g_full.simplify()
    
    WeighEdges(g_full)
    AddSegments(g_full, segments)
    PlotTheGraph(g_full)
    return g_full


def DeleteLongEdges(g, max_lenght):
    for i in reversed(range(len(g.get_edgelist()))):
        if (g.es[i]["weight"]>max_lenght) and (g.es[i]["is_segment"]==False):
            g.delete_edges(i)


def BuildMaxLenghtGraph(g, max_lenght):
    
    g_max_lenght = g.copy()
    
    DeleteLongEdges(g_max_lenght, max_lenght)
    
    PlotTheGraph(g_max_lenght)
    return g_max_lenght


# In[27]:


max_lenght = 20
g_max_lenght = BuildMaxLenghtGraph(g_full, max_lenght)


# In[106]:


def DeleteNotClosest(g, n):
    for i in reversed(range(g.vcount())):
        v = g.vs[i]
        if v.degree()>n: 
            edge = v.incident()
            w = np.empty(0)
            for j in range(len(edge)):
                w = np.append(w, edge[j]["weight"]) 
            sorted_weights = np.sort(w)
        
            max_lenght = sorted_weights[n-1]
        
            for k in reversed([ed.index for ed in edge]):
                if 
                if (g.es[k]["weight"] > max_lenght) and (g.es[k]["is_segment"]==False):
                    g.delete_edges(k)


# In[107]:


def BuildNClosest(g, n):
    g_n_closest = g.copy()
    
    DeleteNotClosest(g_n_closest, n)
    
    PlotTheGraph(g_n_closest)
    return g_n_closest


# In[117]:


g_n_closest = BuildNClosest(g_full, 10)


# In[ ]:




