import operator

def person_lister(f):
    def inner(people):
        # Sort the list of people by age
        people.sort(key=lambda x: int(x[2]))
        
        # Format and store the sorted names in a list
        formatted_names = []
        for person in people:
            title = "Mr." if person[3] == "M" else "Ms."
            formatted_name = f"{title} {person[0]} {person[1]}"
            formatted_names.append(formatted_name)
        
        return formatted_names  # Return the list of formatted names
    
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    n = int(input())
    people = [input().split() for i in range(n)]
    formatted_names = name_format(people)
    
    # Print the formatted names with newlines in between
    print(*formatted_names, sep='\n')
