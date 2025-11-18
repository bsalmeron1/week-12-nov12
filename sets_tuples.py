#sets and tuples examples
set1={1, 2, 3, 4, 5}
print(set1)
print(type(set1))
set1.add(6)
print(set1)
set1.remove(2)
print(set1)
set1.add(6) #wont actually add another 6 because sets remove duplicates
print(set1)

#sets are unordered, doesnt allow dupes but can be edited eventually
#lists gave brackets and are editable after creation (.append or .remove), ordered, allows dupes
#tuples have parenthesis and are not editabel, ordered, allows dupes
ssn=(1233444, 444333555, 5444455)
print(ssn)
