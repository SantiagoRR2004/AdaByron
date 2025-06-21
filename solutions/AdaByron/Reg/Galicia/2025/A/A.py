# Largest Rectangle in Histogram

nBlocks = int(input())

while nBlocks:

    heights = [int(x) for x in input().split()]

    stack = []
    maxArea = 0
    n = len(heights)

    # Include an extra iteration for the end of the histogram
    for i in range(n + 1):
        # Use 0 for the end of the histogram
        currentHeight = heights[i] if i < n else 0

        # Maintain the stack in increasing order of heights
        while stack and currentHeight < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            area = height * width
            maxArea = max(maxArea, area)

        stack.append(i)

    print(maxArea)

    nBlocks = int(input())
