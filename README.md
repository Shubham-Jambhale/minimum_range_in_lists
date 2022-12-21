# minimum_range_in_lists

# Question

An XYZ shipping company, At the conclusion of each quarter, releases a list of the routes that
received the most deliveries during that quarter. At the end of the year, we’ll have four lists, one
for each quarter. The shipping company wants to use these lists to show the board of directors
the smallest range that includes at least one element from each of the four quarters so that they
can use it to market their company with the fewest amount of resources possible and try to open
a new warehouse in that range. For simplicity all lists would be in sorted order. Expected time
complexity is O(nlogM) where n is the total number of elements present in M lists.


# Example 1

Input :[[ 3, 6, 8, 10, 15],[ 1, 5, 12 ],[ 4, 8, 15, 16 ],[ 2, 6 ]]

Output: The minimum range is (4,6)

# Example 2

Input: [[ 2, 3, 4, 8, 10, 15 ],[ 1, 5, 12 ],[ 7, 8, 15, 16 ],[ 3, 6 ]]

Output: The minimum range is (4,7)
