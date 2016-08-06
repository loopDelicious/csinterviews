""" given a directed graph, design an algorithm to find out whether there is a route between 2 nodes """

def are_connected(self, name1, name2):
    """ determine if there's a route between 2 nodes """

    def _are_connected(node, name2, seen):

        if node.name == name2:
            return True

        seen.add(node)

        for n in node1.adjacent:

            if n in seen:
                continue

            if are_connected(n, node2, seen):
                return True

        return False

    return _are_connected(self.nodes[name1], name2, set())