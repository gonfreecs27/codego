def komento_statement(parser):
    """
    Parses a comment from the token stream.

    This method expects to find a comment token and consumes it, returning a 
    structured representation of the comment.

    Returns:
        dict: A parsed representation of the comment, including:
              - 'type': The type of token ('comment').
              - 'text': The text of the comment, stripped of the leading '#' character.
    """

    # Expect and consume the comment token
    comment = parser.eat('COMMENT')  

    return {
        'type': 'comment',
        'text': comment[1]
    }