from typing import Optional


class BinaryTree:

    def __init__(self,
                 value: int = 0,
                 left: Optional[object] = None,
                 right: Optional[object] = None):
        assert isinstance(value, int), f'{type(value)} is not int'
        self.value = value
        self.left = left
        self.right = right

    def _construct_layer_from_list(self,
                                  layer: int,
                                  parents: list[object],
                                  node_values: list[int]):
        '''
        construct one layer of the binary tree from node value list.
        return nodes of this layer, with None represents empty nodes.
        '''
        nodes = []
        assert node_values is not None and len(node_values) > 0, f'{node_values} is None or empty'
        if layer == 0:
            self.value = node_values[0]
            # assume only root node will call _construct_layer_from_list().
            return [self]
        #   0     layer 0
        #  /  \
        # 1    2        layer 1
        # /\   /\
        # 3 4  5  6     layer 2
        assert len(parents) == 2 ** (layer - 1), f'len(parents): {len(parents)} != 2 ** (layer: {layer} - 1)'
        for i in range(len(node_values)):
             # use (i - 1) % len(parents) to get the right parent index
             if node_values[i] is not None:
                node = BinaryTree(node_values[i])
                p_i = i // 2
                assert parents[p_i] is not None
                if i % 2 == 0:
                    parents[p_i].left = node
                else:
                    parents[p_i].right = node
                    print(f'parents[p_i]:{str(parents[p_i])}')
                nodes.append(node)
             else:
                nodes.append(None)
        return nodes


    def construct_from_list(self,
                            l: list):
        '''
        given list of values of each layer of the tree,
        None represents empty tree node.
        construct the tree.
        '''
        if l is None or len(l) == 0:
            return False
        # l[i] is a fixed position in binary tree.
        # create this tree node and put it to the right position.
        #   0
        #  /  \
        # 1    2
        # /\   /\
        # 3 4  5  6
        parents = []
        layer = 0
        start_index = 0
        while start_index < len(l):
            end_index = start_index + 2 ** layer
            print(f'start_index:{start_index}, end_index: {end_index}')
            print(f'l[start_index:end_index]:{l[start_index:end_index]}')
            print(f'parents:{str(parents)}')
            nodes = self._construct_layer_from_list(layer,
                                                    parents,
                                                    l[start_index:end_index])
            print(f'binary_tree: {self.__str__()}')
            parents = nodes
            layer += 1
            start_index = 2 ** layer - 1
        return True

    def preorder_str(self) -> str:
        s = ''
        if self.left is not None:
            s = self.left.preorder_str()
        s += str(self.value)
        if self.right is not None:
            s += self.right.preorder_str()
        return s

    def inorder_str(self) -> str:
        s = str(self.value)
        if self.left is not None:
            s += self.left.inorder_str()
        if self.right is not None:
            s += self.right.inorder_str()
        return s

    def postorder_str(self) -> str:
        s = ''
        if self.left is not None:
            s += self.left.postorder_str()
        if self.right is not None:
            s += self.right.postorder_str()
        s += str(self.value)
        return s

    __str__ = inorder_str


def test_binary_tree():
    #   0
    #  /  \
    # 1    2
    # /\   /\
    # 3 4  5  6
    bt = BinaryTree(0)
    bt.left = BinaryTree(1)
    bt.right = BinaryTree(2)
    bt.left.left = BinaryTree(3)
    bt.left.right = BinaryTree(4)
    bt.right.left = BinaryTree(5)
    bt.right.right = BinaryTree(6)
    print(f'preorder: {bt.preorder_str()}')
    assert bt.preorder_str() == '3140526', f"{bt.preorder_str()} != '3140526'"
    print(f'inorder: {bt.inorder_str()}')
    print(f'postorder: {bt.postorder_str()}')


def test_construct_binary_tree():
    #   0
    #  /  \
    # 1    2
    # /\   /\
    # 3 4  5  6
    l = [0, 1, 2, 3, 4, 5, 6]
    bt = BinaryTree()
    bt.construct_from_list(l)
    print(f'preorder: {bt.preorder_str()}')
    print(f'inorder: {bt.inorder_str()}')
    print(f'postorder: {bt.postorder_str()}')
    assert bt.inorder_str() == '0134256', f'bt.inorder_str():{bt.inorder_str()}'

    #   0
    #  /  \
    # 1    N
    # /\   /\
    # 3 4  N  N
    l = [0, 1, None, 3, 4]
    bt = BinaryTree()
    bt.construct_from_list(l)
    assert bt.inorder_str() == '0134', f'bt.inorder_str():{bt.inorder_str()}'

    #   0
    #  /    \
    # 1       2
    # /\     /  \
    # 3  4   N  6
    # /\ /\    / \
    # N N N N N N 7 8
    l = [0, 1, 2, 3, 4, None, 6, None, None, None, None, None, None, 7, 8]
    bt = BinaryTree()
    bt.construct_from_list(l)
    assert bt.inorder_str() == '01342678', f'bt.inorder_str():{bt.inorder_str()}'


if __name__ == '__main__':
    #test_binary_tree()
    test_construct_binary_tree()
