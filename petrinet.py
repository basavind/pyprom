import graphviz as gv
from algo.fitting import check_fitting


def build(yl, ti, to, output_file):
    pn = gv.Digraph(format='png')
    pn.attr(rankdir='LR')  # left to righ layout - default is top down
    pn.node('start')
    pn.node('end')

    underfitted, fitted, overfitted = check_fitting(yl)

    for elem in yl:
        for i in elem[0]:
            pn.edge(i, str(elem))
            pn.node(i, shape='box')
            color = 'green'
            if elem in underfitted:
                color = 'blue'
            elif elem in overfitted:
                color = 'red'
            pn.node(str(elem), shape='circle', color=color)
        for i in elem[1]:
            pn.edge(str(elem), i)
            pn.node(i, shape='box')
    for i in ti:
        pn.edge('start', i)
    for o in to:
        pn.edge(o, 'end')
    pn.render(output_file)
