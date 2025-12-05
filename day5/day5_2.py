def add_interval_to_disjoint_set(new_interval, interval_set):
    result = []
    current_start, current_end = new_interval[0], new_interval[1]

    for interval in interval_set:
        if current_end < interval[0]: # New interval is before current interval, no overlap
            result.append([current_start, current_end])
            current_start, current_end = interval[0], interval[1] # Process current interval as a new one
        elif current_start > interval[1]: # New interval is after current interval, no overlap
            result.append(interval)
        else: # Overlap, merge intervals
            current_start = min(current_start, interval[0])
            current_end = max(current_end, interval[1])
    
    result.append([current_start, current_end])
    return sorted(result) # Return sorted merged intervals

        
interval_set  = []               
line = input().strip()
while len(line) > 0:
    x, y = (int(x) for x in line.split('-'))
    interval_set = add_interval_to_disjoint_set([x, y], interval_set)
    line = input()

print(sum([y - x + 1 for [x, y] in interval_set]))
