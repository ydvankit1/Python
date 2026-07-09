# s={2, 4, 2, 6};
# print(s);

# ankit=set()
# print(type(ankit));


# set function

s1={1,2,5,6};
s2={3,6,7};
print(s1.union(s2)); # similarly intersection, difference
print(s1,s2);
s1.update(s2);  # s1 get updated  1,2,3,5,6,7
print(s1,s2);

# print(s1.isdisjoint(s2)) // true if no entry common

# s1.add(10)  // to add value in set

# s1.update(s2) // add s2 set into s1

# s1.remove(7)  // raise error if element not present
# s1.discar(7)  // never raise error

# cities={"ab","cd","ef"}
# itm=cities.pop()   // pop random value
# print(itm);

# del(cities) // delete entire set and clear used to delete all item set still remain





