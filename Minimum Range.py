import heapq

def minimum_range ( lists ):
    #list to store results
    main_elements = []
    pop_first = []
    max_element = -10000000000000
    #taking the first element from each list and finding the minimum using heap 
    for i in range(len(lists)):
        heapq.heappush(pop_first,(lists[i][0],i,0))
        #finding the max of 3 elements
        max_element = max(max_element,lists[i][0])
        
    main_element =[pop_first[0][0],max_element]
    
    #Looping over heap and comparing the elements with main list(result are stored in this list) 
    while pop_first:
        value,i,j = heapq.heappop(pop_first)
        
        if max_element - value < main_element[1] -main_element[0]:
            main_element = [value,max_element]
        
        #if reaching end of any list we are stopping the loop
        if j+1 == len(lists[i]):
            return tuple(main_element)
        #pushing the next element from the popped list.
        heapq.heappush(pop_first,(lists[i][j+1],i,j+1))
        
        max_element = max(max_element,lists[i][j+1])