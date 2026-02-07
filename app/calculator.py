class Calculator:
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

        
        
    def calculate(self, exp : str):
        op = "+-*/"
        liste_digit = self.convert_string_to_array_digit(exp, op)
        liste_opperator = self.convert_string_to_array_operator(exp, op)
        result = 0
        if(len(liste_digit) == len(liste_opperator) and liste_opperator[0] =="-" ):
            liste_digit.insert(0,0)
        for i in range(len(liste_digit)-1):
            for opp in liste_opperator:
                match opp:
                    case "+":
                        result += liste_digit[i] + liste_digit[i+1]
                    case "-":
                        result += liste_digit[i] - liste_digit[i+1]

                    case "*":
                        result += liste_digit[i] * liste_digit[i+1]

                    case "/":
                        try:
                            result += liste_digit[i] / liste_digit[i+1]
                        except ZeroDivisionError:
                            raise "Division par 0 !"
        return result
                    
        
    
        