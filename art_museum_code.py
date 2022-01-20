import heapq

n=int(input())
heights = []
for i in range(n):
    heights.append(int(input()))
    
#print(heights)
#arrays to organize at which indexes is the height increasing or decreasing
increasing = [0]*n
decreasing = [0]*n
#arrays to store at which index could a mountain potentially end or could potentially start
index_end = []
index_start = []
heapq.heapify(index_end)
heapq.heapify(index_start)

for i in range(0, n-1): 
    #start-increasing
    if heights[i] <= heights[i+1]: 
        increasing[i]+=1
        
for i in range(1, n):
    #end-decreasing
    if heights[i] <= heights[i-1]: 
        decreasing[i]+=1

for i in range(0, n-1):
    #add the last consecutive decreasing index because that will maximize the width
    if decreasing[i] != decreasing[i+1] and decreasing[i]==1:
        heapq.heappush(index_end, i)
        
for i in range(1, n): 
    #add the first consecutive increasing index because that will maximize the width
    if increasing[i] != increasing[i-1] and increasing[i]==1: 
        heapq.heappush(index_start, i)

if (len(index_end)==0 or len(index_start)==0): #there are no changed in increasing heights or decreasing heights, which means that there is only one mountain 
    print(n)
    
else: 
    max_width = heapq.heappop(index_end)+1

    for i in range(len(index_end)): 
        max_width = max(max_width, (heapq.heappop(index_end)-heapq.heappop(index_start)+1))
    
    max_width = max(max_width, n - heapq.heappop(index_start))
    print(max_width)
