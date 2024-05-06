import networkx as nx
import matplotlib.pyplot as plt

class DiGraph:

    def __init__(self, actions, pl, alias_map):
        self.action_list = actions
        self.player_list = pl 
        self.alias_dict = alias_map
        self.alias_list = alias_map.keys()
        self.G = nx.DiGraph()
        self.x_coordinates = {}
        self.y_coordinates = {}
        self.pos = {}

    def check_player(self,alias):
        if alias_dict[alias] == 'Noise':
            return alias 
        return alias_dict[alias]
    
    def create_graph(self):
        for from_alias, to_alias, action, priority in self.action_list: 
            from_alias = self.check_player(from_alias)
            self.x_coordinates.setdefault(from_alias, []).append(priority)
            self.x_coordinates[from_alias].sort()    

        for i, alias in enumerate(self.alias_list, start=1):
            alias = self.check_player(alias)
            self.y_coordinates[alias] = i

        y_count = len(self.y_coordinates)

        for from_alias, to_alias, action, priority in self.action_list:
            from_alias = self.check_player(from_alias)
            to_alias = self.check_player(to_alias)
            if from_alias not in self.G:
                self.G.add_node(from_alias)
            if to_alias not in self.G:
                self.G.add_node(to_alias)
            if (from_alias, to_alias) in self.G.edges:
                self.G[from_alias][to_alias]['label'] += ', ' + action
            else:
                self.G.add_edge(from_alias, to_alias, label=action)

        for alias in self.alias_list:
            alias = self.check_player(alias) 
            if alias in self.y_coordinates:
                y = self.y_coordinates[alias]
            else:
                y = y_count
                y_count += 1
            self.pos[alias] = (self.x_coordinates.get(alias, [10])[0], y)

    def display_graph(self):
        self.create_graph()
        plt.figure(figsize=(10, 6))  # Set the figure size
        nx.draw(self.G, self.pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")
        edge_labels = nx.get_edge_attributes(self.G, 'label')
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=edge_labels)

        plt.xticks(range(11), range(11))

        plt.show()


actionplayer_list = [('Spiderz', 'Alimidia', 'Ability Block', 0),
               ('Dylan', 'Alimidia', 'Shot Block', 1),
               ('Spiderz', 'Alimidia', 'Heal', 2),
               ('Alimidia', 'Zorquax', 'Shot', 8),
               ('Dylan', 'zwerd', 'Doc', 6)]

player_list = ['Alimidia', 'Dylan', 'Spiderz', 'Zorquax', 'zwerd']

action_list = [('xd', 'Big Boy', 'Ability Block', 0),
               ('Valoranter', 'Big Boy', 'Shot Block', 1),
               ('xd', 'Big Boy', 'Heal', 2),
               ('Big Boy', 'The Cosmic', 'Shot', 8),
               ('Valoranter', '200 hours on OSU', 'Doc', 6),
               ('fireflies', 'doorknob', 'Shot', 8)]

alias_dict = {
    'Big Boy': 'Alimidia',
    'Valoranter': 'Dylan',
    'xd': 'Spiderz',
    'The Cosmic': 'Zorquax',
    '200 hours on OSU': 'zwerd',
    'fireflies': 'Zorquax NPC',
    'doorknob': 'Noise'
}

n1 = DiGraph(action_list, player_list, alias_dict)
n1.display_graph()