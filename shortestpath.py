from collections import deque, namedtuple


# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        distance_between_nodes = 0
        for index in range(1, len(path)):
            for thing in self.edges:
                if thing.start == path[index - 1] and thing.end == path[index]:
                    distance_between_nodes += thing.cost

        return path,distance_between_nodes


graph = Graph([("မဟာမြတ်မုနိ", "နန်းတွင်း", 1200),("မဟာမြတ်မုနိ", "မန္တလေးတောင်", 1680),("မဟာမြတ်မုနိ","ကျောက်တော်ကြီး",1140),("နန်းတွင်း","မန္တလေးတောင်", 3840),("နန်းတွင်း","ကျောက်တော်ကြီး", 2220),("နန်းတွင်း","ကုသိုလ်တော်",540),("မန္တလေးတောင်", "ကျောက်တော်ကြီး", 2640),("မန္တလေးတောင်","ကုသိုလ်တော်",600),("ကျောက်တော်ကြီး", "ကုသိုလ်တော်", 2100),("ကုသိုလ်တော်", "ကျောက်စိမ်းဘုရား",2580 ),("ကျောက်စိမ်းဘုရား", "ကုသိုလ်တော်",2580 ),("ကုသိုလ်တော်","နန်းတွင်း",540),("နန်းတွင်း", "မဟာမြတ်မုနိ", 1200)])
def search(data1,data2):
    test=graph.dijkstra(data1, data2)
    testlen = len(test[0])-1
    print(test)
    medium=""
    shortest1 = ""
    shortest2 = ""
    if len(test[0])>2:
    
        for i in range(1,len(test[0])-1):
                if i == len(test[0])-2:
                    medium = medium+test[0][i]
                else:
                    medium=medium+test[0][i]+"၊"

        shortest1 = test[0][0]+" မှ "+test[0][testlen]+" သို့ သွားရာတွင် "+medium+" ကို ဖြတ်သန်းသွားရပါမည်။"
    if test[1]>=3600:
        hour=test[1]//3600
        minute=test[1]%3600
        minutes=minute/60
        shortest2 = test[0][0]+" မှ "+test[0][testlen]+" သို့ သွားရန် "+str(hour)+" နာရီ "+str(minutes)+" မိနစ် ခန့် ကြာပါမည်။"
    else:
        minute=test[1]//60
        shortest2 = test[0][0]+" မှ "+test[0][testlen]+" သို့ သွားရန် "+str(minute)+" မိနစ် ခန့် ကြာပါမည်။"
    return shortest1,shortest2
