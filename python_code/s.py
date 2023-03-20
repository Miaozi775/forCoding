import sys

def read_graph(filename):
    """
    Reads the interference graph from a file and returns it as a dictionary.
    """
    graph = {}
    with open(filename) as f:
        for line in f:
            nodes = line.split()
            node = int(nodes[0])
            neighbours = set(map(int, nodes[1:]))
            graph[node] = neighbours
    return graph

def get_colour(node, graph, colours):
    """
    Returns the lowest available colour for a node.
    """
    neighbour_colours = set(colours[neighbour] for neighbour in graph[node] if neighbour in colours)
    for colour in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if colour not in neighbour_colours:
            return colour
    return None

def colour_graph(graph):
    """
    Assigns colours to the nodes of the interference graph and returns a dictionary of coloured nodes.
    """
    colours = {}
    for node in sorted(graph):
        colour = get_colour(node, graph, colours)
        if colour is None:
            print("Error: Cannot colour the graph with 26 colours or less.")
            return None
        colours[node] = colour
    return colours

def write_colours(filename, colours):
    """
    Writes the coloured nodes to a file.
    """
    with open(filename, 'w') as f:
        for node in sorted(colours):
            f.write(f"{node}{colours[node]}\n")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python program.py input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        graph = read_graph(input_file)
        colours = colour_graph(graph)
        if colours is not None:
            write_colours(output_file, colours)
