def answer(data):
  name = []
  parent = []
  for key1, value1 in data.items():
    for item in value1:
      for key2,value2 in item.items():
        if key2 == 'name':
          name.append(value2)
        if key2 == 'parent':
          parent.append(value2)
  name.pop(0)

  inputlist = list(map(str,input().split()))
  inputlist.pop(0)
  if(len(inputlist) == 3):
    input1,input2,input3 = inputlist[0],inputlist[1],inputlist[2]
    #print(input1,input2,input3)
  elif(len(inputlist) == 4):
    input1,input2,input3,input4 = inputlist[0],inputlist[1],inputlist[2],inputlist[3]
    #print(input1,input2,input3,input4)
  elif(len(inputlist) == 5):
    input1,input2,input3,input4,input5 = inputlist[0],inputlist[1],inputlist[2],inputlist[3],inputlist[4]
    #print(input1,input2,input3,input4,input5)
  else:
    print("total input not between 3 to 5")
    return

  
  if(len(inputlist) == 3):
    parent1 = []
    try:
      index1 = name.index(input1)
    except ValueError:
      print(input1 +' , '+ input2+' , '+input3+" Doesn't have a common leader")
      return
    while True:
      parent1.append(parent[index1])
      try:
        index1 = name.index(parent[index1])
      except ValueError:
        break

    parent3 = []
    try:
      index3 = name.index(input3)
    except ValueError:
      print(input1 +' , '+ input2+' , '+input3+" Doesn't have a common leader")
      return
    while True:
      parent3.append(parent[index3])
      try:
        index3 = name.index(parent[index3])
      except ValueError:
        break

    parent2 = []
    try:
      index2 = name.index(input2)
    except ValueError:
      print(input1 +' , '+ input2+' , '+input3+" Doesn't have a common leader")
      return

    while True:
      parent2.append(parent[index2])
      try:
        index2 = name.index(parent[index2])
      except ValueError:
        break

    f = False
    temp = ""
    for i in parent1:
      for j in parent2:
        for k in parent3:
          if (i == j and i == k):
            print(i)
            temp = i
            f = True
            break
        if f:
          break
      if f:
        break

    l1,l2,l3 = 0,0,0
    if f:
      for i in parent1:
        l1 += 1
        if (temp == i):
          print(i + " is " + str(l1) + " levels above than " + input1)
          break
      for i in parent2:
        l2 += 1
        if (temp == i):
          print(i + " is " + str(l2) + " levels above than " + input2)
          break
      for i in parent3:
        l3 += 1
        if (temp == i):
          print(i + " is " + str(l3) + " levels above than " + input3)
          break
    else:
      print(input1 +' , '+ input2+' , '+input3+" Doesn't have a common leader")
  elif (len(inputlist) == 4):
    parent1 = []
    try:
      index1 = name.index(input1)
    except ValueError:
      print(input1 +' , '+ input2+' , '+input3+' , '+ input4+" Doesn't have a common leader")
      return
    while True:
      parent1.append(parent[index1])
      try:
        index1 = name.index(parent[index1])
      except ValueError:
        break

    parent3 = []
    try:
      index3 = name.index(input3)
    except ValueError:
      print(input1 +' , '+ input2+' , '+input3+' , '+ input4+" Doesn't have a common leader")
      return
    while True:
      parent3.append(parent[index3])
      try:
        index3 = name.index(parent[index3])
      except ValueError:
        break

    parent2 = []
    try:
      index2 = name.index(input2)
    except ValueError:
      print(input1 +' , '+ input2+' , '+input3+' , '+ input4+" Doesn't have a common leader")
      return

    while True:
      parent2.append(parent[index2])
      try:
        index2 = name.index(parent[index2])
      except ValueError:
        break
    
    parent4 = []
    try:
      index4 = name.index(input4)
    except ValueError:
      print(input1 +' , '+ input2+' , '+input3+' , '+ input4+" Doesn't have a common leader")
      return

    while True:
      parent4.append(parent[index4])
      try:
        index4 = name.index(parent[index4])
      except ValueError:
        break 

    f = False
    temp = ""
    for i in parent1:
      for j in parent2:
        for k in parent3:
          for l in parent4:
            if (i == j and l == k and i == l):
              print(i)
              temp = i
              f = True
              break
          if f:
            break
        if f:
          break
      if f:
        break  

    l1,l2,l3,l4 = 0,0,0,0
    if f:
      for i in parent1:
        l1 += 1
        if (temp == i):
          print(i + " is " + str(l1) + " levels above than " + input1)
          break
      for i in parent2:
        l2 += 1
        if (temp == i):
          print(i + " is " + str(l2) + " levels above than " + input2)
          break
      for i in parent3:
        l3 += 1
        if (temp == i):
          print(i + " is " + str(l3) + " levels above than " + input3)
          break
      for i in parent4:
        l4 +=1 
        if (temp == i):
          print(i + " is " + str(l4) + " levels above than " + input4)
          break
    else:
      print(input1 +' , '+ input2+' , '+input3+' , '+ input4+" Doesn't have a common leader")  
  elif (len(inputlist) == 5):
    parent1 = []
    try:
      index1 = name.index(input1)
    except ValueError:
      print(input1 +' , '+ input2+' , '+input3+' , '+ input4+' , '+input5+" Doesn't have a common leader")
      return
    while True:
      parent1.append(parent[index1])
      try:
        index1 = name.index(parent[index1])
      except ValueError:
        break

    parent3 = []
    try:
      index3 = name.index(input3)
    except ValueError:
      print(input1 +' , '+ input2+' , '+input3+' , '+ input4+' , '+input5+" Doesn't have a common leader")
      return
    while True:
      parent3.append(parent[index3])
      try:
        index3 = name.index(parent[index3])
      except ValueError:
        break

    parent2 = []
    try:
      index2 = name.index(input2)
    except ValueError:
      print(input1 +' , '+ input2+' , '+input3+' , '+ input4+' , '+input5+" Doesn't have a common leader")
      return

    while True:
      parent2.append(parent[index2])
      try:
        index2 = name.index(parent[index2])
      except ValueError:
        break
    
    parent4 = []
    try:
      index4 = name.index(input4)
    except ValueError:
      print(input1 +' , '+ input2+' , '+input3+' , '+ input4+' , '+input5+" Doesn't have a common leader")
      return

    while True:
      parent4.append(parent[index4])
      try:
        index4 = name.index(parent[index4])
      except ValueError:
        break 
    
    parent5 = []
    try:
      index5 = name.index(input5)
    except ValueError:
      print(input1 +' , '+ input2+' , '+input3+' , '+ input4+' , '+input5+" Doesn't have a common leader")
      return

    while True:
      parent5.append(parent[index5])
      try:
        index5 = name.index(parent[index5])
      except ValueError:
        break


    f = False
    temp = ""
    for i in parent1:
      for j in parent2:
        for k in parent3:
          for l in parent4:
            for m in parent5:
              if (i == j and l == k and i == m):
                print(i)
                temp = i
                f = True
                break
            if f:
              break
          if f:
            break
        if f:
          break
      if f:
        break

    l1,l2,l3,l4,l5 = 0,0,0,0,0
    if f:
      for i in parent1:
        l1 += 1
        if (temp == i):
          print(i + " is " + str(l1) + " levels above than " + input1)
          break
      for i in parent2:
        l2 += 1
        if (temp == i):
          print(i + " is " + str(l2) + " levels above than " + input2)
          break
      for i in parent3:
        l3 += 1
        if (temp == i):
          print(i + " is " + str(l3) + " levels above than " + input3)
          break
      for i in parent4:
        l4 +=1 
        if (temp == i):
          print(i + " is " + str(l4) + " levels above than " + input4)
          break
      for i in parent5:
        l5 += 1 
        if (temp == i):
          print(i + " is " + str(l5) + " levels above than " + input5)
          break
    else:
      print(input1 +' , '+ input2+' , '+input3+' , '+ input4+' , '+input5+" Doesn't have a common leader")



# driver code
import json

with open('/content/sample_data/org.json') as f:
  data = json.load(f)

answer(data)
