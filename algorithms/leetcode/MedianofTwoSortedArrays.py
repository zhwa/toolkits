class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def med(arr):
            n = len(arr)
            if n == 0: return 0
            elif n == 1: return arr[0]
            else:
                if n % 2 == 1: return arr[n/2]
                else: return 0.5 * (arr[n/2] + arr[n/2-1])

        def locat(array, e):
            n = len(array)
            if n == 0: return 0
            if n == 1: return 0 if e < array[0] else 1
            else:
                if array[n/2] > e: return locat(array[:n/2], e)
                else: return 1 + n/2 + locat(array[n/2+1:], e)
        
        def dq(arr1, arr2, rank):
            if len(arr1) == 0: return med(arr2)
            if len(arr2) == 0: return med(arr1)
            if rank == 0:
                if arr1[0] < arr2[0]: return arr1[0]
                else: return arr2[0]
            elif rank == 1:
                if arr1[0] < arr2[0]: return arr2[0]
                else: return arr1[0]
            else:
                [m1, m2] = map(med, [arr1, arr2])
                [l1, l2] = map(len, [arr1, arr2])
                if m1 > m2: 
                    a2, a1 = arr1, arr2
                    m2, m1 = m1, m2
                    l2, l1 = l1, l2
                else: a1, a2 = arr1, arr2
                m = locat(a1, m1)
                if m1 <= a2[0] and m < rank: return dq(a1[m:], a2, rank-m)
                elif m1 <= a2[0] and m >= rank: return a1[rank]
                else:
                    n = locat(a2, m1)
                    if m + n >= rank: return dq(a1[:m], a2[:n], rank)
                    else: return dq(a1[m:], a2[n:], rank-m-n)
        
        
        m = len(nums1)
        n = len(nums2)
        rank = (m + n) / 2 - 1
        if m == 0: return med(nums2)
        if n == 0: return med(nums1)
        if (m + n) % 2 == 0:
            if nums1[0] < nums2[0]:
                med1 = dq(nums1, nums2, rank)
                med2 = dq(nums1[1:], nums2, rank-1)
            else:
                med1 = dq(nums1, nums2, rank)
                med2 = dq(nums1, nums2[1:], rank-1)
            return 0.5 * (med1 + med2)
        else:
            return dq(nums1, nums2, (m+n)/2)

nums1 = [2,2,2]
nums2 = [2,2,2,2]
import pdb
s = Solution()
print s.findMedianSortedArrays(nums1, nums2)
