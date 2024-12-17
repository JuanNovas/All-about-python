# s[i] = x: item i of s is replaced by x
# s[i:j] = t: slice of s from i to j is replaced by the contents of t
# del s[i:j]: same as s[i:j] = []
# s[i:j:k] = t: elements of s[i:j:k] are replaced by those of t
# del s[i:j:k]: removes the elements of s[i:j:k]
# s.append(x): appends x to the end of s (same as s[len(s):len(s)] = [x])
# s.clear(): removes all items from s (same as del s[:])
# s.copy(): creates a shallow copy of s (same as s[:])
# s.extend(t) or s += t: extends s with the contents of t (similar to s[len(s):len(s)] = t)
# s *= n: updates s with its contents repeated n times
# s.insert(i, x): inserts x into s at index i (same as s[i:i] = [x])
# s.pop() or s.pop(i): retrieves the item at i and removes it from s
# s.remove(x): removes the first item in s where s[i] equals x
# s.reverse(): reverses the items of s in place