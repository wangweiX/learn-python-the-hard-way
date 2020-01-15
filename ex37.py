## Keywords ##

#del removes a specific index:
>>> a = [3, 2, 2, 1]
>>> del a[1]
[3, 2, 1]

#remove removes the first matching value, not a specific index:
>>> a = [0, 2, 2, 3]
>>> a.remove(2)
>>> a
[0, 2, 3]

# and pop returns the removed element:
>>> a = [4, 3, 5]
>>> a.pop(1)
3
>>> a
[4, 5]


# as
# he as clause is generally used as an assignment operator for various builtin types.
> with ContextManager as instance:
> import foo as bar
> catch Exception as exc:
