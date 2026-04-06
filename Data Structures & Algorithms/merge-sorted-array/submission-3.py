class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #since nums1 has empty space at the back, we start at the back
        #we will maintain 3 pointers
        #last valid from list 1, last valid from list 2, and last slot in list 1

        p1 = m-1
        p2 = n-1
        p_write= m+n-1

        while p2 >=0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                    nums1[p_write] = nums1[p1]
                    p1 -= 1
            else:
                nums1[p_write] = nums2[p2]
                p2 -= 1
            p_write -=1