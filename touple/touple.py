newTouple = ("apple","banana","cherry")

print(type(newTouple))
a = len(newTouple)
#print(len(newTouple))
print(type(a))


newList = ["apple","multa"]
newTouple = ("apple","multa")
newSet = {"apple", "nadim"}



set1 = {"a","b","c"}
set2 = {1,2,3}

set3 = set2.union(set1)
print(set3)

set4 = {"n","a","d","u"}

set5 = set3.union(set4)

print(set5)


x = {"a","b","c"}
y= {"s","t","a"}

z = x.intersection(y)

print(z)


newDic = {
  "name":"nadu",
  "age":"22",
  "sex":"male"
}
#name = "nadu"
print(type(newDic["name"]))
