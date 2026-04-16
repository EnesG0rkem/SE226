def remove_duplicates(data_list):
    seen = []
    for d in data_list:
        if d not in seen:
            seen.append(d)

    return seen

def strip_whitespaces(string_list):
    return [s.strip() for s in string_list]
    
