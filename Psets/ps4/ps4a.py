# Problem Set 4A
# Name: Santiago Ramirez
# Collaborators:
# Time Spent: 5:30
def string_to_list(word:str):
    """
    this function
    inputs
    word: str, the string to convert into list
    outputs
    ls_letters:list, the list with the letters of the string
    """
    ls_letters = []
    letter = ""
    for letter in word:
        ls_letters.append(letter)
    return ls_letters

def get_permutations(sequence:str):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    #covering the base case
    #if sequence has only 1 character or less
    if len(sequence) <= 1:
        return sequence
    else:
        #storing result
        list_permutations = []
        #go through the sequence
        #save one letter and save the remaining
        for i in range(0,len(sequence)):
            current_letter = sequence[i]
            remaining_letters = sequence[0:i]+sequence[i+1:]
            #loop over the function itself
            #now you are looping over a smaller sequence
            #this will output at the end a list or character(base case)
            for j in get_permutations(remaining_letters):
                list_permutations.append(current_letter + j)
    #the function returns the list of all cases
    return list_permutations
 
if __name__ == '__main__':
        # testing out solution
    examples = ['abc',"","e g"]
    results = [['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],"",['e g', 'eg ', ' eg', ' ge', 'ge ', 'g e']]
    #remember that enumerate gives you the index and the value of the iterable
    for index,example in enumerate(examples):
        print('Input:', example)
        print('Expected Output:', results[index])
        print('Actual Output:', get_permutations(example))
        
