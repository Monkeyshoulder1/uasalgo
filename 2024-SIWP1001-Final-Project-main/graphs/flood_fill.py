class DepthFirst():
    def __init__(self):
        pass

    def run(self, graph_str, start):
        import ast
        graph = ast.literal_eval(graph_str)
        start = int(start)
        return self.search(graph, start)

    def search(self, graph, start):
        visited = []
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack.extend(graph[node])

        return visited