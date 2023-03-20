import sys

# run the whole steps
if __name__ == '__main__':

    # Check if command line arguments are valid
    if len(sys.argv) != 3:
        print("Invalid number of command line arguments. Usage: python <myprogram> input.txt output.txt")
        sys.exit()

    inputflie = sys.argv[1]
    outputfile = sys.argv[2]

    # Read input file
    try:
        with open(inputflie, 'r') as f:
            graph = {}
            for line in f:
                line = line.strip().split(' ')
                node, neighbours = line[0], line[1:]
                graph[node] = neighbours

    except FileNotFoundError:
        print("Input file not found.")
        sys.exit()

    # Check if there are more than 26 nodes
    if len(graph) > 26:
        print("The algorithm cannot produce a result with 26 colours or less.")
        sys.exit()

    # Define the list of colours
    colours = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Rank nodes by the number of neighbours
    node_ranking = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)

    # Assign colours to nodes
    # record the colours of each node
    node_colours = {}
    # the loop will stop when all nodes are coloured
    while len(node_colours) < len(graph):
        # loop through the nodes in the ranking
        for node in node_ranking:
            # if the node is already coloured, skip it
            if node in node_colours:
                continue
            # if the node is not coloured, check if it has any neighbours
            if len(graph[node]) == 0:
                # if it has no neighbours, assign it a colour
                node_colours[node] = colours[0]
            else:
                # if it has neighbours, check if any of its neighbours is coloured
                neighbour_colours = [node_colours[neighbour] for neighbour in graph[node] if neighbour in node_colours]
                # if it has coloured neighbours, assign it a colour that is not used by its neighbours
                if len(neighbour_colours) > 0:
                    for colour in colours:
                        if colour not in neighbour_colours:
                            node_colours[node] = colour
                            break
                # if it has no coloured neighbours, assign it a colour
                else:
                    node_colours[node] = colours[0]

    

    # Write output file
    try:
        f = open(outputfile, 'w')
        for node in sorted(node_colours.keys()):
            f.write(f"{node} {node_colours[node]}\n")
        f.close()
    except PermissionError:
        print("Output file could not be written. Permission denied.")
        sys.exit()

    # Print success message
    print(f"Colours assigned and written to {outputfile}. Please check the {outputfile} for the result.")
