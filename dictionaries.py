# dic={    // it is ordered
#     "key": "value",
#     "key1":"value1"
# }
# print(dic["key1"]);  // error if key not exist
# print(dic.get("key1"));  // print none if key not exist


# for ke in dic.keys():
#     print(f"the value corrosponding to key {key} is {info[key]}");

# for ke, val in dic.items():
#     print(f"the value of corrosponding key {ke} is {val}")


ep1={122: 45, 123: 89, 567: 69, 670: 69}
ep2={222: 67, 566: 90}

# ep1.update(ep2);
# print(ep1);

# ep1.clear();
# print(ep1) // {}

# ep1.pop(122);
# ep1.popitem();  // remove last item

# del ep1 