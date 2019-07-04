class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """

        atom_counts = {}

        # Use stack to track which count there is
        # Use dictionary to keep track of coef distribution in parens
        stack = []
        atoms_in_parens = {}
        parens = []

        # To keep track of the current atom/count
        atom = []
        count = []

        length = len(formula)

        # to keep track of what came before
        num_prev = False
        seen_closing = False

        # Go through formula, back to front
        for i in range(len(formula)-1, -1, -1):
            cur = formula[i]

            # Check if alphanumeric (i.e. if not paranthesis)
            if cur.isalpha() or cur.isnumeric():
                # Check if digit, if it is, add to count
                if cur.isdigit():
                    if num_prev:
                        count.insert(0,cur)
                    elif len(count) == 0:
                        count.append(cur)
                    else:
                        stack.append(int(''.join(count)))
                        count = [cur]

                    num_prev = True
                else:
                    # If character is not a digit, add coefficient to stack
                    if len(count) > 0:
                        coef = int(''.join(count))
                        stack.append(coef)
                        count = []

                    if cur.islower():
                        # Check if character is lowercase
                        atom.append(cur)
                    else:
                        # If character is uppercase, it is an atom
                        atom.insert(0, cur)
                        a = ''.join(atom)

                        if len(parens) > 0:
                            atoms_in_parens[a] = 0

                        if num_prev:
                            atom_counts[a] = atom_counts.get(a, 0) + stack.pop()
                        else:
                            atom_counts[a] = atom_counts.get(a, 0) + 1

                        # Reset atom
                        atom = []
                        num_prev = False
            elif cur == ')':
                num_prev = False
                parens.append(')')
            elif cur == '(':
                parens.pop()
                if len(stack) > 0:
                    coef = stack.pop()
                    for a in atom_counts:
                        if a in atoms_in_parens:
                            atom_counts[a] = atom_counts[a]*coef
                    if len(parens) == 0:
                        atoms_in_parens = {}


        return ''.join([(a + str(count)) if count != 1 else a for a, count in sorted(atom_counts.items())])


                    
