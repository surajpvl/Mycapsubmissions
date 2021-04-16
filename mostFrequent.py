def most_frequent(str):
  dict = {}
  for i in str:
    if i not in dict:
      dict[i]=1
    else:
      dict[i] +=1
   dict = reversed(sorted(dict.items(),key=lamda kv:(kv[1],kv[0])))
  for i in dict:
    print(i[0],"=",i[1])
 inp = input()
most_frequent(inp)
