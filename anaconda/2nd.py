def min_operations_to_same_parity(t, test_cases):
    results = []
    
    for case in test_cases:
        n = case[0]
        a = case[1]
        
        even_count = sum(1 for x in a if x % 2 == 0)
        odd_count = n - even_count
        
        results.append(min(even_count, odd_count))
    
    return results
