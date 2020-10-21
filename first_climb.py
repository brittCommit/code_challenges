def first_climb(e):
  """
  Return the idx of first and last of a climb. A climb is when idx where i <= i + 1
  >>> first_climb([3, 2, 1, 0, 0, 1, 2, 2, 3, 5, 10, 10, 7, 15])
  [4, 10]
  """
  
  first = None
  last = None

  for idx in range(len(e)-2):
    if e[idx] < e[idx +1] and first is None:
      first = idx
    elif e[idx]  < e[idx + 1] and first is not None:
      last = idx + 1
    if e[idx] > e[idx + 1] and last is not None:
      break
  return [first, last]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')