class FordFulkerson():
    def __init__(self, graph):
        self.graph = graph
        self.fluxo = {}
        self.init_residual()
        self.max_fluxo = 0
        
    def init_residual(self):
        for origem in self.graph.keys():
            for vertex, weight in self.graph.get(origem).iteritems():
                self.fluxo[(origem,vertex)] = 0
 
    def get_path(self, origem, destino, caminho):
        if origem == destino:
            return caminho
        for vertex, weight in self.graph.get(origem).iteritems():
            residual = int(weight) - self.fluxo[(origem, vertex)]
            if residual > 0 and not ((origem,vertex), residual) in caminho:
                proximo_vertice = self.get_path( vertex, destino, caminho + [((origem,vertex),residual)] )
                if proximo_vertice != None:
                    return proximo_vertice
 
    def get_fluxo_max(self, origem, destino):
        caminho = self.get_path(origem, destino, [])
        while caminho != None:
            fluxo = min(residuo for vertex, residuo in caminho)
            self.max_fluxo += fluxo
            print "caminho %s" %caminho
            for vertex , residuo in caminho:
                self.fluxo[(vertex[0], vertex[1])] += fluxo
                self.fluxo[(vertex[1], vertex[0])] -= fluxo
            caminho = self.get_path(origem, destino, [])
        return self.max_fluxo

if __name__ == '__main__':
    graph = { 
            '1': { '2': 6 , '5': 5 },
            '2': { '1': 0 , '5': 2, '3': 3, '4': 2 },
            '3': { '2': 0 , '4': 4 },
            '4': { '3': 0 , '2': 0, '5': 0 },
            '5': { '2': 0 , '1': 0, '4': 3 },
            }
    g=FordFulkerson(graph)
    print g.get_fluxo_max('1','4')