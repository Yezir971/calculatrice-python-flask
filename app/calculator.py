from app.node import Node
class Calculator(Node):
    """
    Une classe simple de calculatrice fournissant les opérations arithmétiques de base.
    """
    

    def add(self, a, b):
        """
        Additionne deux nombres.

        Args:
            a: Premier nombre
            b: Deuxième nombre

        Returns:
            La somme de a et b
        """
        return a + b

    def subtract(self, a, b):
        """
        Soustrait b de a.

        Args:
            a: Premier nombre
            b: Deuxième nombre

        Returns:
            La différence entre a et b
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiplie deux nombres.

        Args:
            a: Premier nombre
            b: Deuxième nombre

        Returns:
            Le produit de a et b
        """
        return a * b

    def divide(self, a, b):
        """
        Divise a par b.

        Args:
            a: Numérateur
            b: Dénominateur

        Returns:
            Le quotient de a divisé par b

        Raises:
            ZeroDivisionError: Si b est égal à zéro
        """
        if b == 0:
            raise ZeroDivisionError("Division par zéro impossible")
        return a / b
    def power(self, a, b):
        """
        Calcule a^b. Retourner 1 pour 0^0.
        """
        if a == 0 and b == 0:
            return 1
        return a**b 
    def sqrt(self, a):
        """
        Racine carrée. Lever ValueError si a < 0.
        """
        if a < 0:
            raise ValueError('a ne peux pas etre négatif !')
        return a**0.5
    def modulo(self, a, b):
        """
        Reste de division. Lever ZeroDivisionError si b = 0.
        """
        if type(a) == str or type(b) == str:
            raise ValueError('b = 0')
            
        if int(b) == 0:
            raise ZeroDivisionError('b = 0')
        return int(a)%int(b) 
    
    
    def convert_string_to_array_digit(self,exp: str, opperator: str) -> list[int | float]:
        """Converti une chaine de caractère en tableau de float ou int""" 
        # supprime les espaces entre les chiffres #mercisandra
        exp_digit = exp[:].replace(" ", "")
        tab_number = exp_digit.replace('+', ";").replace('-', ";").replace('*', ";").replace('/', ";")
        return [int(element) for element in tab_number.strip(";").split(';')]
    
    def convert_string_to_array_operator(self,exp: str, opperator: str) -> list[int | float]:
        """Converti une chaine de caractère en tableau d'oppérateur """ 
        # supprime les espaces entre les chiffres #mercisandra
        exp_op = exp[:].replace(" ", "")
        return [element for element in exp_op if element in opperator] 

    # def order_by_priority(self, digit, opperator):
    #     for i in range(len(opperator)):
    #         if opperator[i] == "*" or opperator[i] == "/":
    #             digit1 = digit[i]
    #             digit2 = digit[i+1]
    #             op = opperator[i]
    #             del digit[i]
    #             del digit[i+1]
    #             del opperator[i]
    #             opperator.insert(0, op) 
    #             digit.insert(0,digit1)
    #             digit.insert(1,digit2)
    #     return [digit, opperator]
            

        
    # def calculate(self, exp: str):
    #     op_symbols = "+-*/"
    #     # liste_digit = self.convert_string_to_array_digit(exp, op_symbols)
    #     # liste_opperator = self.convert_string_to_array_operator(exp, op_symbols)
    #     liste_digit,liste_opperator = self.order_by_priority(self.convert_string_to_array_digit(exp, op_symbols),self.convert_string_to_array_operator(exp, op_symbols) )
    #     if len(liste_digit) < len(liste_opperator):
    #         return "Il manque un chiffre"
    #     if(len(liste_digit) == len(liste_opperator) and liste_opperator[0] == "-"):
    #         liste_digit.insert(0, 0)
    #     result = liste_digit[0]
    #     print(liste_digit, liste_opperator)
    #     print(len(liste_opperator))

    #     for i in range(len(liste_opperator)):

    #         opp = liste_opperator[i]
    #         next_val = liste_digit[i+1]

    #         match opp:
    #             case "+":
    #                 result += next_val
    #             case "-":
    #                 result -= next_val
    #             case "*":
    #                 result *= next_val
    #             case "/":
    #                 if next_val == 0:
    #                     raise ZeroDivisionError("Division par 0 !")
    #                 result /= next_val
    #     print(result)  
    #     return result
    def build_tree(self, digits, operators):
        # S'il n'y a plus d'opérateurs, c'est juste un nombre (une feuille)
        if not operators:
            return Node(digits[0])

        # On cherche l'opérateur le MOINS prioritaire en partant de la droite
        # car dans 10 - 5 + 2, le '+' est fait après le '-'
        index_to_split = -1
        
        # 1. On cherche d'abord + ou - (priorité basse)
        for i in range(len(operators) - 1, -1, -1):
            if operators[i] in "+-":
                index_to_split = i
                break
                
        # 2. Si on n'a pas trouvé, on cherche * ou /
        if index_to_split == -1:
            for i in range(len(operators) - 1, -1, -1):
                if operators[i] in "*/":
                    index_to_split = i
                    break

        # On crée le nœud avec l'opérateur trouvé
        op = operators[index_to_split]
        
        # On sépare les listes en deux pour la gauche et la droite
        left_digits = digits[:index_to_split + 1]
        left_ops = operators[:index_to_split]
        
        right_digits = digits[index_to_split + 1:]
        right_ops = operators[index_to_split + 1:]

        return Node(
            value=op,
            left=self.build_tree(left_digits, left_ops),
            right=self.build_tree(right_digits, right_ops)
        )
        
    def calculate(self, exp: str):
        
        op_symbols = "+-*/"
            
        # Tes fonctions actuelles
        digits = self.convert_string_to_array_digit(exp, op_symbols)
        operators = self.convert_string_to_array_operator(exp, op_symbols)
        if len(digits) == 1 :
            raise ValueError('Erreur de logique !')
        if(len(operators) == len(digits) and operators[0] == "-"):
            digits.insert(0, 0)
        
        # Construction de l'arbre
        root_node = self.build_tree(digits, operators)
        
        # Évaluation récursive
        result = root_node.evaluate()
        print(f"Calcul pour '{exp}' terminé.")
        return result
    
        