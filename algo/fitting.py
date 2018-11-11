def check_fitting(yl):
    underfitted = []
    fitted = []
    overfitted = []
    for node in yl:
        in_node, out_node = node
        if len(in_node) == len(out_node):
            fitted.append(node)
        elif len(in_node) < len(out_node):
            underfitted.append(node)
        else:
            overfitted.append(node)

    return underfitted, fitted, overfitted
