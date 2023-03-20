# for <myprogram> input.txt output.txt
import sys

# run the whole steps
if __name__ == '__main__':

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # define the interference graph
    # key: node
    # value: list of nodes that interfere with the key node
    graph = {} 

    # define color list
    # 26 colors from A to Z
    # colour_list = [chr(ord('A')+i) for i in range(26)]

    # open input file and read it line by line
    for line in open(input_file).readlines():
        line = line.strip().split(' ')
        # the first element is the node
        # the rest are the neighbours
        node = line[0]
        neighbours = line[1:]
        graph[node] = neighbours
    
    # rank the nodes according to the number of neighbours in descending order
    # than with the lowest id

    # assign colors to the nodes
            

    # write output file
    f = open(output_file,"w")
 


