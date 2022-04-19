import time

from SplayTreeIm.SplayTree import SplayTree, Node


def test_splay_tree(treesize=1000):
    print("Building trees")

    spltree = SplayTree()
    x = [i for i in range(0, treesize)]
    for n in x:
        spltree.insert(Node(n))
    print("Done building")
    searches = x

    # Search the splay tree 1000 times
    t1 = time.time()
    for i in range(0, treesize):
        for n in searches:
            node = spltree.search_tree(Node(n))
            if (node == None):
                print("ERROR: %d" % n)
    t2 = time.time()
    print(f"Нашло и добавило {treesize} элементов: %.1f sec" % (treesize, t2 - t1))


test_splay_tree()
