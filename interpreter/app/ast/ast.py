from app.token import OperatorToken, PLUS, MINUS, MULTIPLY, DIVIDE

class NullRoot(object):
    def __init__(self):
        self.value = None

    def __nonzero__(self):
        return False

    def __len__(self):
        return False


class AST(object):
    def __init__(self):
        self.root = NullRoot()
        self.current_node = self.root

    def feed(self, token):
        if token.is_operator():
            self._feed_operator(token)
        else:
            self._feed_number(token)

    def _feed_operator(self, operator: OperatorToken):
        """
            At the begining of this method the tree will look something like this
                -
                |
                |
            7<--+-->3

            This method will:
             - complete me!


            At the end of the method, here's how things will look:

                    +
                    |
                - <--+-->2
                |
                |
            7<--+-->3

        """

        if operator.is_a(MULTIPLY, DIVIDE):
            # we need to start at root and follow the right path until we are able to place this token below all plus and minus tokens

            operator.feed(self.root)
            self.root = operator
            self.current_node = operator
        else:
            operator.feed(self.root)
            self.root = operator
            self.current_node = operator

    

    def _feed_number(self, token):
        """
        feed the token to the current_operator (either an operator or AST root)
        """
        if self.root:
            self.root.feed(token)
        else:
            self.root = token

    @property
    def value(self):
        """
        kick off evaluation of the AST. If root is None, return that.
        """
        return self.root.value
