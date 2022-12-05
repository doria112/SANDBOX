from collections import defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # create a queue of supplies, use it to maintain available recipes
        # create a dictionary keyed by ingredients from recipes 
        # remove an ingredient if it's available 
        # when ingredient[i] is empty, added the created recipe to return value
        
        created = []
        available = deque(supplies)
        i_to_rs = defaultdict(list)
        r_to_is = defaultdict(list)
        for r, ingredients in zip(recipes, ingredients):
            r_to_is[r] = ingredients
            for ingredient in ingredients:
                i_to_rs[ingredient].append(r)

        while available:
            curr = available.popleft()
            recipes = i_to_rs[curr]
            for r in recipes:
                r_to_is[r].remove(curr)
                if not r_to_is[r]:
                    available.append(r)
                    created.append(r)

        return created
