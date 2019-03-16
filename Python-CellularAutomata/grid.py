import json
import ast
import rules

class Graph:
    def __init__(self, size = 0, state = None, rules_name = "", rules = [],  wraparound = False):
        self.tiles = [0] * size
        self.next_tiles = [0] * size
        if state is not None:
            self.next_tiles = state
            for i in range(0,len(self.next_tiles)):
                self.tiles[i] = self.next_tiles[i]
        self.rules = rules
        self.size = size
        self.wraparound = wraparound
        self.rules_name = rules_name
    
    
    def get_value(self, tile_id):
        return self.tiles[tile_id]
    
    def get_neighbors(self, tile_id):
        pass
        
    def get_value_and_neighbor_values(self, tile_id):
        
        return self.get_value(tile_id), [self.get_value(i) for i in self.get_neighbors(tile_id)]
    
    def update(self):
        for i in range(0, len(self.next_tiles)):
            val, neighbors = self.get_value_and_neighbor_values(i)
            for rule in self.rules:
                rule(self, i, val, neighbors)
        for i in range(0, len(self.next_tiles)):
            self.tiles[i] = self.next_tiles[i]
            
    def set_tile(self, tile_id, value):
        self.next_tiles[tile_id] = value
    
    def to_json(self):
        dict = {}
        dict["state"] = self.tiles
        dict["rules_name"] = self.rules_name
        dict["size"] = self.size 
        dict["wraparound"] = self.wraparound
        dict["type"] = type(self).__name__
        return dict
        
    
class Grid2D(Graph):
    _NEIGHBORS = [(0,1), (1,0), (1,1), (0,-1), (-1, -1), (-1, 0), (1, -1), (-1, 1)]
    def __init__(self, width = 10, height = 10, **kwargs):
        Graph.__init__(self, size = int(width)*int(height), **kwargs)
        self.width = int(width)
        self.height = int(height)
    
    def get_neighbors(self, tile_id):
        pos = self.id_to_xy(tile_id)
        neighbors_pos = [ (pos[0] + direction[0], pos[1] + direction[1]) for direction in self._NEIGHBORS]
        filtered_neighbors = []
        for npos in neighbors_pos:
            nx, ny = npos
            if self.wraparound:
                if nx < 0: nx = self.width -1
                if ny < 0: ny = self.height -1
                if nx >= self.width: nx = 0
                if ny >= self.height: ny = 0
                filtered_neighbors.append((nx, ny))
            elif nx >=0 and ny >=0 and nx < self.width and ny < self.height:
                filtered_neighbors.append((nx, ny))
        lst =  [self.xy_to_id(npos) for npos in filtered_neighbors]
        return lst
    
    def getValue(self, pos):
        return self.get_value(self. xy_to_id(pos))
        
    def getValueAndNeighborValues(self, pos):
        return self.get_value_and_neighbor_values(self.xy_to_id(pos))
              
    def id_to_xy(self, tile_id):
        return (tile_id // self.height, tile_id % self.height)
        
    def xy_to_id(self, pos):
        return pos[0] * self.height + pos[1]
    
    def __str__(self):
        message = ""
        for y in range(0, self.height):
            for x in range(0, self.width):
                message += str(self.getValue((x,y)))
            message += "\n"
        return message
    def toJson(self):
        dict = self.to_json()
        args = {}
        args["width"] = self.width
        args["height"] = self.height
        dict["args"] = args
        return dict

def load(filename):
    with open(filename) as json_data:
        data = json.load(json_data)
    
    grid_args = data["args"] 
    grid_args["rules"] = rules.getRuleByName(data["rules_name"])
    grid_args["rules_name"] = data["rules_name"]
    grid_args["wraparound"] = data["wraparound"]
    grid_args["state"] = [int(i) for i in data["state"]]
    grid = eval(data["type"])(**grid_args)
    return grid

def save(json_object, filename):
    with open(filename, 'w') as outfile:
        json.dump(json_object.toJson(), outfile)
    
if __name__ == "__main__":
    my_grid = load("demo.json")
    my_grid.update()
    save(my_grid, "demo.json")