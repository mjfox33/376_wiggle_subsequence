from code_376_wiggle_subsequence import Solution

def test_example_1():
    s = Solution()
    nums = [1,7,4,9,2,5]
    output = 6
    assert s.wiggleMaxLength(nums) == output

def test_example_2():
    s = Solution()
    nums = [1,17,5,10,13,15,10,5,16,8]
    output = 7
    assert s.wiggleMaxLength(nums) == output

def test_example_3():
    s = Solution()
    nums = [1,2,3,4,5,6,7,8,9]
    output = 2
    assert s.wiggleMaxLength(nums) == output
