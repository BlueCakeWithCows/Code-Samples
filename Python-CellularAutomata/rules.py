def getDefaultConwayRules():
    def rule1(graph, tile_id, val, neighbors):
        if val and sum(neighbors) < 2: 
            graph.set_tile(tile_id, 0)
    def rule2(graph, tile_id, val, neighbors):
        if val and (sum(neighbors) == 2 or sum(neighbors) == 3): 
            graph.set_tile(tile_id, 1)
    def rule3(graph, tile_id, val, neighbors):
        if val and sum(neighbors) > 3: 
            graph.set_tile(tile_id, 0)
    def rule4(graph, tile_id, val, neighbors):
        if not val and sum(neighbors) == 3: 
            graph.set_tile(tile_id, 1)        
    rules = [rule1, rule2, rule3, rule4]
    return rules

def getCaveGenerationRules():
    def rule1(graph, tile_id, val, neighbors):
        if not val and sum(neighbors) > 4:
            graph.set_tile(tile_id, 1)
    def rule2(graph, tile_id, val, neighbors):
        if val and sum(neighbors) > 3:
            graph.set_tile(tile_id, 0)
    rules = [rule1, rule2]
    return rules
    
rules = {}
rules["DEFAULT_CONWAY_RULES"] = getDefaultConwayRules()
rules["CAVE_GENERATION_RULES"] = getCaveGenerationRules()

def getRuleByName(rule):
    if rule in rules:
        return rules[rule]
    else: return None
    