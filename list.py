# l=[3,"ankit","true"];  // list is mutable
# print(l);

# print(l[0]); // 3
# print(l[-3])  //3

# if "ankit" in marks:
#     print("yes");
#   else:
#     print("No")

# similarly for string

# if "nki" in "ankit":
#     print("yes");
# else:
#     print("No");

# print(l[0,2,2]) //3,"true"


l=[2, 6, 8, 9,6, 8,6];
l.append(13);
l.sort();
l.sort(reverse=True);
print(l.index(1));
print(l.count(6));
m=l; # reference of l change to m
m.insert(1, 55)  #index, value
l.extend(m) # add list m to end of l 
k=l+m; # concatenate l and m

