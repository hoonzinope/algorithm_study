# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    temp_list = []
    def dfs(self, n_list):
        result = []
        if n_list.isInteger():
            result.append(n_list.getInteger())
        else:
            if n_list.getInteger() != None:
                result.append(n_list.getInteger())
            for nest in n_list.getList():
                result.extend(self.dfs(nest))
        return result
    
    def __init__(self, nestedList: [NestedInteger]):
        self.temp_list = []
        for nest in nestedList:
            if nest.isInteger():
                self.temp_list.append(nest.getInteger())
            else:
                self.temp_list.extend(self.dfs(nest))
        
    
    def next(self) -> int:
        return self.temp_list.pop(0)
    
    def hasNext(self) -> bool:
        if len(self.temp_list) == 0:
            return False
        else:
            return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())