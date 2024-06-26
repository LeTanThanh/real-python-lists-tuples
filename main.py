if __name__ == "__main__":
  # Python Lists

  a = ["foo", "bar", "baz", "qux"]
  print(a)

  # Lists Are Ordered

  a = ["foo", "bar", "baz", "qux"]
  b = ["baz", "qux", "bar", "foo"]
  print(a)
  print(b)
  print(a == b)
  print(a is b)
  print([1, 2, 3, 4] == [4, 1, 3, 2])

  # Lists Can Contain Arbitrary Objects

  a = [2, 4, 6, 8]
  print(a)

  a = [21.42, "foobar", 3, 4, "bark", False, 3.14159]
  print(a)

  import math

  def foo():
    pass

  print(int)
  print(len)
  print(foo)
  print(math)

  a = [int, len, foo, math]
  print(a)

  a = []
  print(a)

  a = ["foo"]
  print(a)

  a = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100
  ]
  print(a)

  a = ["bark", "meow", "woof", "bark", "cheep", "bark"]
  print(a)

  # List Elements Can Be Accessed by Index

  a = ["foo", "bar", "baz", "quz", "quux", "corge"]
  print(a)
  print(a[0])
  print(a[2])
  print(a[5])
  print(a[-1])
  print(a[-2])
  print(a[-5])

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a[2:5])
  print(a[-5:-2])
  print(a[1:4])
  print(a[-5:-2] == a[1:4])

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a[:4], a[0:4])
  print(a[2:], a[2: len(a)])
  print(a[:4] + a[4:])
  print(a[:4] + a[4:] == a)

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a[0:6:2])
  print(a[1:6:2])
  print(a[6:0:-2])

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a[::-1])

  s = "foobar"
  print(s[:])
  print(s[:] is s)

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a[:])
  print(a[:] is a)

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print("qux" in a)
  print("thud" not in a)

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a + ["grault", "garply"])
  print(a * 2)

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(len(a))
  print(min(a))
  print(max(a))

  # Lists Can Be Nested

  x = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", ["hh", "ii"], "j"]
  print(x)
  print(x[0], x[2], x[4])
  print(x[1])
  print(x[3])

  # Modifying a Single List Value

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a)
  a[2] = 10
  print(a)
  a[-1] = 20
  print(a)

  # s = "foobarbaz"
  # s[2] = "x"
  # TypeError

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a)
  del a[3]
  print(a)

  # Modifying Multiple List Values

  """
  a[m:n] = <iterable>
  """

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a)
  a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
  print(a)
  a[1:6] = ["Bark!"]
  print(a)

  a = [1, 2, 3]
  print(a)
  a[1:2] = [2.1, 2.2, 2.3]
  print(a)

  a = [1, 2, 3]
  print(a)
  a[1] = [2.1, 2.2, 2.3]
  print(a)

  a = [1, 2, 7, 8]
  print(a)
  a[2:2] = [3, 4, 5, 6]
  print(a)

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a)
  a[1:5] = []
  print(a)

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a)
  del a[1:5]
  print(a)

  # Prepending or Appending Items to a List

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a)
  a += ["grault", "garply"]
  print(a)

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a)
  a = [10, 20] + a
  print(a)

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a)
  # a += 20
  # TypeError

  a += [20]
  print(a)

  a = ["foo", "bar", "baz", "qux", "quux"]
  print(a)
  a += "corge"
  print(a)

  a = ["foo", "bar", "baz", "qux", "quux"]
  print(a)
  a += ["corge"]
  print(a)

  # Methods That Modify a List

  s = "foobar"
  t = s.upper()
  print(s, t)

  ## a.append(<obj>)

  """
  Appends an object to a list.

  a.append(<obj>) appends object <obj> to the end of list a:
  """

  a = ["a", "b"]
  print(a)
  a.append(123)
  print(a)

  a = ["a", "b"]
  print(a)
  a += [1, 2, 3]
  print(a)

  a = ["a", "b"]
  print(a)
  a.append([1, 2, 3])
  print(a)

  a = ["a", "b"]
  print(a)
  a.append("foo")
  print(a)

  ## a.extend(<iterable>)

  """
  Extends a list which the objects from an iterable.
  """

  a = ["a", "b"]
  print(a)
  a.extend([1, 2, 3])
  print(a)

  a = ["a", "b"]
  print(a)
  a += [1, 2, 3]
  print(a)

  ## a.insert(<index>, <obj>)

  """
  Inserts an object into a list.
  """

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a)
  a.insert(3, 3.15159)
  print(a)

  ## a.remove(<obj>)

  """
  Removes an object from a list.
  """

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a)
  a.remove("baz")
  print(a)

  # a.remove("Bark!")
  # ValueError

  ## a.pop(index = -1)

  """
  Removes an element from a list.
  """

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a)
  a.pop()
  print(a)
  a.pop()
  print(a)

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a)
  a.pop(1)
  print(a)
  a.pop(-3)
  print(a)

  # Lists Are Dynamic

  a = ["foo", "bar", "baz", "qux", "quux", "corge"]
  print(a)
  a[2:2] = [1, 2, 3]
  print(a)
  a += [3.14159]
  print(a)

  a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
  print(a)

  a[2:3] = []
  print(a)

  del a[0]
  print(a)

  # Python Tuples

  # Defining and Using Tuples

  t = ("foo", "bar", "baz", "qux", "quux", "corge")
  print(t)
  print(t[0])
  print(t[-1])
  print(t[1:2])
  print(t[::-1])

  # t[2] = "Bark!"
  # TypeError

  t = ()
  print(t)
  print(type(t))

  t = (1, 2)
  print(t)
  print(type(t))

  t = (1, 2, 3, 4, 5)
  print(t)
  print(type(t))

  t = (2,)
  print(t)
  print(type(t))

  # Tuple Assignment, Packing, and Unpacking

  t = ("foo", "bar", "baz", "qux")
  print(t)
  print(t[0])
  print(t[-1])

  (s1, s2, s3, s4) = t
  print(s1)
  print(s2)
  print(s3)
  print(s4)

  # (s1, s2, s3) = t
  # ValueError

  (s1, s2, s3, s4) = ("foo", "bar", "baz", "qux")
  print(s1)
  print(s2)
  print(s3)
  print(s4)

  # (s1, s2, s3, s4, s5) = ("foo", "bar", "baz", "qux")
  # ValueError

  t = 1, 2, 3
  print(t)
  print(type(t))

  x1, x2, x3 = t
  print(x1)
  print(x2)
  print(x3)

  x1, x2, x3 = 4, 5, 6
  print(x1)
  print(x2)
  print(x3)

  t = 2,
  print(t)
  print(type(t))

  a = "foo"
  b = "bar"
  print((a, b))

  # We need to define a temp variable to accomplish the swap.
  temp = a
  a = b
  b = temp
  print((a, b))

  a = "foo"
  b = "bar"
  print((a, b))

  a, b = b, a
  print((a, b))
