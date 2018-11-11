import graphviz as gv

def build(places, initial_activities, terminal_activities, output_file):
    pn = gv.Digraph(format='png')
    pn.attr(rankdir='LR')  # left to righ layout - default is top down
    pn.node('start')
    pn.node('end')

    for in_places, out_places, params in places:
        place_label = str((in_places, out_places, params['type']))
        for activity in in_places:
            pn.edge(activity, place_label)
            pn.node(activity, shape='box')
            color = 'black'
            if 'color' in params:
                color = params['color']
            pn.node(place_label, shape='circle', color=color)
        for activity in out_places:
            pn.edge(place_label, activity)
            pn.node(activity, shape='box')
    for activity in initial_activities:
        pn.edge('start', activity)
    for activity in terminal_activities:
        pn.edge(activity, 'end')
    pn.render(output_file)
