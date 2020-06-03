'''
977. Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

Given an array of integers A sorted in non-decreasing order, 
return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
'''

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        p1, p2 = 0, len(A) - 1
        
        num_1, num_2 = A[p1], A[p2]
        res = []
        while p1 <= p2:
            if abs(num_1) > abs(num_2):
                res.append(num_1**2)
                p1 += 1
                num_1 = A[p1]
            else:
                res.append(num_2**2)
                p2 -= 1
                num_2 = A[p2]
                
        res.reverse()
        
        return res