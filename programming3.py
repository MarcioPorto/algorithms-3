""" ------------------------------------------------------------------------
File: BSTClass.py
Author: Susan Fox
Date: September 2014

This file contains an implementation of the BST Abstract Data Type, using
classes to represent the tree. Each tree object has a boolean for whether or
not it is an empty tree. If it is not empty, then there are three other data
values: the node value, and the left and right children. For the sake of
demonstrating trees more broadly, this implementation includes other binary
tree algorithms, like traversal and height-calculation.

NOTES: 
  * this doesn't do much error-checking, to keep the code simple to read
  * print statements are Python 3 style, remove parens for Python 2
----------------------------------------------------------------------------
"""

"""
  Comp 221 F14 
  Programming Assignment #4 
  Marcio Porto
"""

import random

class BST:
    """Implements a typical Binary Search Tree that does no balancing. It also includes
    several general binary tree algorithms, just so you can see them."""


    def __init__(self, initialNode = None):
        """Makes a tree.  If no input is given, then the tree is empty. Otherwise,
        the input node is set as the root of the tree."""

        self.leftChild = None
        self.rightChild = None
        if initialNode == None:
            self.nodeValue = None
            self.emptyTree = True
        else:
            self.nodeValue = initialNode
            self.emptyTree = False
 
    # -------------------------------------------------------------
    # The section that follows has basic tree utility functions, accessors for node values 
    # and children, functions to check the kind of tree and its properties, and to add or modify
    # elements of the tree
 
    def isEmpty(self):
        """Returns True if the tree is empty, and False otherwise."""
        return self.emptyTree
 
 
    def getNodeValue(self):
        """Returns the root node's value, or None if the tree is empty"""
        if self.isEmpty():
            return None
        else:
            return self.nodeValue
 
     

    def getLeftChild(self):
        """Returns the left subtree."""
        return self.leftChild


    def getRightChild(self):
        """Returns the right subtree."""
        return self.rightChild

    
    
    def isLeaf(self):
        """Returns True if it has no children."""
        return (not self.emptyTree)\
               and (self.leftChild == None) \
               and (self.rightChild == None)
    
    
    def setNodeValue(self, newValue):
        """Takes in a new node value, and changes the node value for 
        the root of the tree to the new one."""
        if self.isEmpty():        
            print("Empty tree, can't change node value")
        else:
            self.nodeValue = newValue
            
            
    def hasLeftChild(self):
        """Returns True if it has a left child and False otherwise."""
        return (not self.emptyTree) and (self.leftChild != None)
    
    def hasRightChild(self):
        """Returns True if it has a right child and False otherwise."""
        return (not self.emptyTree) and (self.rightChild != None)


    def setLeftChild(self, childTree):
        """Takes in a subtree.  Changes the left child to the new
        subtree. Can be used to delete the left child by passing
        an empty tree as the child tree"""
        if self.emptyTree:
            print("Cannot set child on empty tree")
        elif childTree == None or childTree.isEmpty():
            self.leftChild = None
        else:
            self.leftChild = childTree

            
    def setRightChild(self, childTree):
        """Takes in a subtree.  Changes the left child to the new
        subtree. Can be used to delete the left child by passing
        an empty tree as the child tree"""
        if self.emptyTree:
            print("Cannot set child on empty tree")
        elif childTree == None or childTree.isEmpty():
            self.rightChild = None
        else:
            self.rightChild = childTree
           
         
     
    # -------------------------------------------------------------
    # The section that follows has more complex operations.  Computing the height,
    # traversing the tree in various orders, inserting, searching, and deleting.  The 
    # last three operations are not fully defined here; should be added to in a subclass.
 
 
    def getHeight(self):
        """Computes and returns the height of the tree.  Note that an empty tree
        is defined to have a height of -1, and a single-node tree has a
        heigh of zero."""
        if self.isEmpty():
            return -1
        elif self.isLeaf():
            return 0
        else:      
            leftHgt = self.leftChild.getHeight()
            rightHgt = self.rightChild.getHeight()
            return max(leftHgt, rightHgt) + 1



    def preorderTraverse(self, nodeFn = None):
        """Takes in a tree and an optional function, which may be used to
        update/modify the node values of the tree. If the function is not there,
        then the node values are printed. This function performs preorder
        traversal, meaning the root is touched, then the left child is traversed,
        and finally the right child is traversed."""
        if self.isEmpty():
            return
        else:
            # touch the root node
            if nodeFn == None:
                print(self.nodeValue)
            else:
                self.setNodeValue(nodeFn(self.nodeValue))

        # recur on left and right children, if they exist
        if self.hasLeftChild():
            self.leftChild.preorderTraverse(nodeFn)
        if self.hasRightChild():
            self.rightChild.preorderTraverse(nodeFn)


    def postorderTraverse(self, nodeFn = None):
        """Takes in a tree and an optional function, which may be used to
        update/modify the node values of the tree. If the function is not there,
        then the node values are printed. This function performs postorder
        traversal, meaning the left child is traversed, then the right child is
        traversed, and finally the root value is touched."""
        # handle the empty tree case
        if self.isEmpty():
            return
        else:
            # recur on left and right children, if they exist
            if self.hasLeftChild():
                self.leftChild.preorderTraverse(nodeFn)
            if self.hasRightChild():
                self.rightChild.preorderTraverse(nodeFn)

            # touch the root node
            if nodeFn == None:
                print(self.nodeValue)
            else:
                self.setNodeValue(nodeFn(self.nodeValue))




    def inorderTraverse(self, nodeFn = None):
        """Takes in a tree and an optional function, which may be used to
        update/modify the node values of the tree. If the function is not there,
        then the node values are printed. This function performs inorder
        traversal, meaning the left child is traversed, then the root value is
        touched, and finally the right child is traversed."""
        # handle the empty tree case
        if self.isEmpty():
            return
        else:
            # recur on left and right children, if they exist
            if self.hasLeftChild():
                self.leftChild.preorderTraverse(nodeFn)

            # touch the root node
            if nodeFn == None:
                print(self.nodeValue)
            else:
                self.setNodeValue(nodeFn(self.nodeValue))

            if self.hasRightChild():
                self.rightChild.preorderTraverse(nodeFn)
            
        

    def printTree(self):
        """Takes in a tree and prints it, printing first left subtree and then right,
        and using indentation to indicate the level in the tree."""
        if self.isEmpty():
            print("Tree is empty")
        else:   
            self._printRecurDepth(0)
        
        
    def _printRecurDepth(self, depth):
        """prints the tree, using depth to track the levels"""
        indent = " " * depth
        indentPlus = ' ' * (depth + 5)
        if self.isLeaf():
            print(indent + "Leaf: " + str(self.nodeValue))
        else:   
            print(indent + "Node: " + str(self.nodeValue))
            if self.hasLeftChild():
                print(indentPlus + "LEFT:")
                self.leftChild._printRecurDepth(depth + 5)
            else:
                print(indentPlus + "LEFT:  no left child")
            
            if self.hasRightChild():
                print(indentPlus + "RIGHT:")
                self.rightChild._printRecurDepth(depth + 5)
            else:       
                print(indentPlus + "RIGHT:  no right child")



    def search(self, value):
        """Find the value in the tree and return True if it is there, False otherwise. Performs typical BST search."""
        if self.isEmpty():
            return False
        elif value == self.nodeValue:
            return True
        elif (value < self.nodeValue) and self.hasLeftChild():
            return self.leftChild.search(value)
        elif (value >= self.nodeValue) and self.hasRightChild():
            return self.rightChild.search(value)
        else:   
            return False
      
         
         
    def insert(self, newValue):
        """Given a new value, add a node to the tree somewhere to add the new value. This performs the typical BST insertion algorithm."""
        if self.isEmpty():
            self.emptyTree = False
            self.nodeValue = newValue
            self.leftChild = None
            self.rightChild = None
        elif newValue < self.nodeValue:
            if self.hasLeftChild():
                self.leftChild.insert(newValue)
            else:  
                self.setLeftChild(BST(newValue))
        else:
            if self.hasRightChild():
                self.rightChild.insert(newValue)
            else:
                self.setRightChild(BST(newValue))
             
             
    def delete(self, value):
        """Find value in the tree and delete its node from the tree. Performs typical unbalanced BST deletion."""
        if self.isEmpty():
            print("Cannot remove value from an empty tree")
            return
        else:
            result = self._deleteRec(value)
            if result != None:
                # deleting the original root is a special case, need
                # to handle tree going empty or root value changing
                print("ROOT VALUE CHANGED")
                if result.isEmpty():
                    self.emptyTree = True
                    self.nodeValue = None
                    self.leftChild = None
                    self.rightChild = None
                else:
                    self.setNodeValue(result.getNodeValue())
                    self.setLeftChild(result.getLeftChild())
                    self.setRightChild(result.getRightChild())
                
    def getBalance(self):
        leftHeight = self.getLeftChild.getHeight()
        rightHeight = self.getRightChild.getHeight()
        return rightHeight-leftHeight



    def _deleteRec(self, value):
        """Takes a value and removes one occurrence of the value from the 
        tree. Checks if this node is the one to be changed. Returns None
        if the parent node does not have to change anything, or it
        returns the new tree if the parent node does have to change."""
        if value == self.nodeValue:
            if self.isLeaf():
                return BST()          # this node is going away, replace by empty tree
            elif not self.hasLeftChild():
                return self.rightChild     # right child is taking this node's place
            elif not self.hasRightChild():
                return self.leftChild      # left child is taking this node's place
            else:   # Node has two children, most complicated case
                replaceValue = self.leftChild._findMaxValue()
                self.setNodeValue(replaceValue)
                result = self.leftChild._deleteRec(replaceValue)
                if result != None:
                    self.setLeftChild(result)           # update this node's left child
                return None                                # this node stays, so return None
        elif value < self.nodeValue:
            if self.hasLeftChild():
                result = self.leftChild._deleteRec(value)    # update this node's left child
                if result != None:
                    self.setLeftChild(result)
            return None                                # this node stays, so return None
        else:  # value >= getNodeValue(tree)    
            if self.hasRightChild(): 
                result = self.rightChild._deleteRec(value) # update this node's right child
                if result != None:
                    self.setRightChild(result)
            return None                               # this node stays so return None
                
                    
    def _findMaxValue(self):
        """Finds the maximum value in this subtree.  If there is a right child, then it 
        follows the path down to the right child.  If no right child, then this node is the
        maximum."""
        if self.isLeaf() or (not self.hasRightChild()):
            return self.nodeValue
        else:
            return self.rightChild._findMaxValue()
        
        

# Testing code for testing the basic Tree and BST operations.
if __name__ == '__main__':
    # Note that some of these tests violate the rules of the BST,
    # which you can do if you don't use insert, delete, and search
    # to build the tree.
    print("---------Tree----------")
    tree = BST()
    print("is empty?", tree.isEmpty(), "tree height", tree.getHeight())
    tree.inorderTraverse()
    tree.printTree()
    tree.insert(3)
    print("---------Tree after insert:")
    tree.printTree()
    print("New height", tree.getHeight())
    t2 = BST(1234)
    print("--------T2:")
    t2.printTree()
    print("children?", t2.hasLeftChild(), t2.hasRightChild())
    tree.setLeftChild(t2)
    tree.setRightChild(BST(101))
    tree.printTree()
    t2.printTree()
    print("tree isleaf?", tree.isLeaf(), "t2 is leaf?", t2.isLeaf(), "height", tree.getHeight())
    tree.inorderTraverse()
    tree.preorderTraverse()
    tree.postorderTraverse()
    
    newT = BST()
    valList =[]
    for i in range(20):
        val = random.randrange(100)
        valList.append(val)
        newT.insert(val)
        print("Inserted value", val)
    newT.printTree()
    extraList = [random.randrange(100) for x in range(10)]
    random.shuffle(valList)
    print("==========Searching for values in tree:")
    for v in valList:
        print("Searching for value", v)
        print(newT.search(v))
    print("==========Searching for extra values (likely not in tree):")
    for v in extraList:
        print("Searching for value", v)
        print(newT.search(v))

    random.shuffle(valList)
    print("==========Deleting values from tree:")
    for v in valList:
        print("Deleting value", v)
        newT.delete(v)
        newT.printTree()

        

def AVLInsertion(B, k):
    """ Performs AVL Insertion """
    if B.isEmpty():
        node = B.insert(k)
        return "height-increase"
    else if B.getNodeValue() >= k:
        res = B.getLeftChild.insert(k)
        if res.equal("height-increase"):
            #decrement node B's balance
            if B.getBalance == 0:
                return "height-balanced"
            else if B.getBalance == -1:
                return "height-increase"
            else:
                if B.getLeftChild.getBalance() == -1:
                    #if left also left-heavy
                    #perform single right rotation
                else:
                    #perform double left-right rotation
        else:
            return "height-balanced"
    else:
        res = B.getRightChild.insert(k)
        if res.equal("height-increase"):
            #increment node B's balance
            if B.getBalance()==0:
                return "height-balanced"
            else if B.getBalance()==1:
                return "height-increase"
            else:
                if B.getRightChild.getBalance() == 1:
                    #perform single left rotation
                else:
                    #perform double right left rotation
        else:
            return "height-balanced"
            
