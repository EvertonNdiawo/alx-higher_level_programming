## PYTHON-MORE_DATA-STRUCTURES

                >>> a `|` b

                {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'} //Result of letters in a or b or both

                >>> a `&` b

                {'a', 'c'} //Result of letters in both a and b

                >>> a `^` b

                {'r', 'd', 'b', 'm', 'z', 'l'} //Result of letters in a or b but not both

        ```

- Similar to lists, `set comprehensions` are also supported:

        ```
                a = {X for X in 'abracadabra' if X `not in` 'abc'}

                >>> a

                {'r', 'd'} //Result of all letters found in `abracadabra` where the letters are not in contained in `a, b or c`.
