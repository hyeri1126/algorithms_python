# dfs : 모든 경우의 수를 깊이 들어가며 탐색

# dfs 활용 용도
# 1. 트리 -> 이진 트리를 구성하며 탐색하는 방법도 dfs를 통해 구현할 수 있다. 즉 트리 순회의 한 방법으로 dfs를 사용할 수 있음
# 2. 그래프 -> 그래프에서 모든 vertex를 순회하는 경우도 dfs를 통해 구현할 수 있다. 

# -------- 트리 ----------
# 트리 순회 - dfs
# 트리를 순회하는 방법에서 dfs를 사용하면 전위순회,중위순회,후위순회가 가능하다.
# 스택 혹은 재귀를 통해 구현 가능
# 트리 순회에서 알아두어야 할 것은 모든 노드를 순회할 때, 접근과 방문이 다르다. 접근은 두번,세번 하지만 방문은 딱 한번만
# 접근은 left child부터 깊게 하거나 혹은 right child부터 깊게하거나!
# 방문은 preorder, inorder, postorder가 있으며 방문 코드의 순서에 따라 정해짐


# 트리 탐색 기본 코드(재귀/dfs)
# dfs 역할: root의 서브트리에 속한 모든 노드들에 방문
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def dfs (root):
    if root is None: # 탈출 조건 : 리프 노드를 만났을 때
        return
    dfs(root.left)
    dfs(root.right)
    print(root.val, end=" ") # 후위순회(postorder):아래노드부터 방문.

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.right.right=TreeNode(4)

dfs(root)

# dfs 기본 문제 유형
# 1. Lowest Common Ancestor of a Binary Tree, 가장 낮은 공통 조상 구하기
