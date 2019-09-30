def permutation(word):
   if len(word) == 1:
     return [word]

   permutations = [] # store all the permutations
   for letter in word:
     remaining_letters = [x for x in word if x != letter]
     # Find the permutations of the remaining elements
     remaining_permutations = permutation(remaining_letters)

     for sub_word in remaining_permutations:
       permutations.append([letter] + sub_word)

   return permutations

print(permutation('dbef'))
