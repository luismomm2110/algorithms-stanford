from anytree import Node, RenderTree
import numpy as np


def create_alphabeth(filepath):
    weights = np.array(list())
    symbols = []

    file = open(filepath, "r")

    lines = file.readlines()

    i = 0
    for line in lines[1:]:
        weight = int(line.split()[0])
        weights = np.append(weights, weight)
        symbol = Node(i)
        symbols.append(symbol)
        i += 1

    return symbols, weights


def build_tree(symbols, weights):
    while(len(symbols) >= 2):
        tree3 = Node("temp root")

        index1 = np.argmin(weights)
        tree1 = symbols[index1]
        weight1 = weights[index1]
        weights = np.delete(weights, index1)
        symbols.pop(index1)

        index2 = np.argmin(weights)
        tree2 = symbols[index2]
        weight2 = weights[index2]
        weights = np.delete(weights, index2)
        symbols.pop(index2)

        tree1.parent = tree3
        tree2.parent = tree3

        weights = np.append(weights, weight1 + weight2)
        symbols.append(tree3)

    return symbols


def minDepth(root):
    if root is None:
        return 0

    if len((root.children)) == 0:
        return 1

    # Base Case : Leaf node.This accounts for height = 1
    if root.children[0] is None and root.children[1] is None:
        return 1

    # If children[0] subtree is Null, recur for children[1] subtree
    if root.children[0] is None:
        return minDepth(root.children[1])+1

    # If children[1] subtree is Null , recur for children[0] subtree
    if root.children[1] is None:
        return minDepth(root.children[0]) + 1

    return min(minDepth(root.children[0]), minDepth(root.children[1]))+1


def main():
    alphabeth, weights = create_alphabeth("huffman1.txt")
    print(alphabeth)
    print(weights)

    final_tree = build_tree(alphabeth, weights)[0]
    print(final_tree.height)
    print(minDepth(final_tree)-1)

   # for pre, fill, node in RenderTree(final_tree):
    #   print("%s%s" % (pre, node.name))


if __name__ == "__main__":
    main()
