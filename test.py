def func():
    for i in range(5):
        yield i

a = []


def _neighbors(node, seen=[], deadends=[]):
    val, depth = [n for n in node[0]], node[1]
    for i in range(4):
        for j in (1, -1):
            new_val = val[:]
            new_val[i] = str((int(new_val[i]) + j + 10) % 10)
            new_node = ''.join(new_val)
            if new_node not in seen and new_node not in deadends:
                yield (new_node, depth+1)

res = neighbors(('0000', 1))
