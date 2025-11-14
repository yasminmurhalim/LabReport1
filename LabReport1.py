# LabReport1

import streamlit as st
from collections import deque
graph = {
    'A': ['B', 'D'],   
    'B': ['C', 'E'],      
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['F', 'G']
}
start_node = 'A'

#Search Algorithm Functions
def bfs(graph, start_node):
    """Performs BFS following alphabetical tie-breaking."""
    visited = set()
    queue = deque([start_node])
    path = []
    visited.add(start_node)
    while queue:
        s = queue.popleft() 
        path.append(s)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return path

def dfs(graph, start_node):
    """Performs DFS using recursion following alphabetical tie-breaking."""
    visited = set()
    path = []
    def dfs_recursive(node):
        if node not in visited:
            visited.add(node)
            path.append(node)
            for neighbour in graph[node]:
                dfs_recursive(neighbour)
    dfs_recursive(start_node)
    return path

#Streamlit Application 
def main():
    st.set_page_config(layout="wide")
    st.title("Question 2: Graph Search Algorithms (BFS & DFS)")
    st.subheader("Implementation with Alphabetical Tie-Breaking Rule")

   
    st.header("1. Directed Graph Visualization")
    try:
        
        st.image('LabReport_BSD2513_#1.jpg', caption="Graph for BFS and DFS Traversal")
    except FileNotFoundError:
        st.error("'LabReport_BSD2513_#1.jpg' not found. Please ensure it is in the same folder as the script.")
    
    st.subheader("Graph Structure (Adjacency List)")
    st.code(str(graph), language='python')
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)

    # 2. Display BFS Results
    with col1:
        st.header("2. Breadth-First Search (BFS)")
        bfs_path = bfs(graph, start_node)
        st.success(f"**Process Path:** {' → '.join(bfs_path)}")
        st.markdown(
            f"""
            **Level Progression:**
            * Level 0: [{start_node}]
            * Level 1: [B, D]
            * Level 2: [C, E]
            * Level 3: [H]
            * Level 4: [F, G]
            """
        )

    # 3. Display DFS Results
    with col2:
        st.header("3. Depth-First Search (DFS)")
        dfs_path = dfs(graph, start_node)
        st.success(f"**Process Path:** {' → '.join(dfs_path)}")
        st.markdown(
            """
            **Traversal Logic:**
            * Follows the **alphabetical** neighbor first, then goes as deep as possible before backtracking.
            """
        )


if __name__ == '__main__':
    main()

