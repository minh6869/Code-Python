import numpy as np
size = 7
matrix = np.zeros((int(size),int(size)))
f = open("matrixthuchanh.txt")
ds = f.readlines()
tap_dinh = ['A','B','C','D','E','F','H']
i = 0
id = {}
for dinh in tap_dinh:
    id[dinh] = i
    i+=1

h = dict({'A': 35,
          'B': 45,
          'C': 5,
          'D': 15,
          'E': 29,
          'F': 0,
          'H': 23,})

for i in range(size):
    ans = ds[i].split("\t")
    for j in range(size):
        matrix[i][j] = float(ans[j])
        

f.close()


start = 'B'
end = 'F'

def sort_dict(temp_dict):
    items = list(temp_dict.items())
    items.sort(key=lambda x: (x[1], x[0]))
    new_dict = dict(items)
    return new_dict

def find_way(truoc,start,end, solutions):
    if end == start:
        solutions.append(end)
        return
    solutions.append(end)
    find_way(truoc,start,truoc[end],solutions)

def BFS():
    solution = []
    queue = [f"{start}"]
    truoc = {}
    flag = {}
    step =[]
    for dinh in tap_dinh:
        flag[dinh] = 0
    while True:
        if queue == []:
           return "Not found solution!",None
        u = queue.pop(0)
        step.append(u)
        flag[u] = 1
        for i in range (size):
            if matrix[id[f"{u}"]][i] != 0:
                for key,value in id.items():
                    if id[key] == i and flag[key]==0:
                        queue.append(key)
                        truoc[key] = u
                        flag[key] = 1
                        break
        if u == end:
            find_way(truoc,start,end,solution)
            ans = ''
            for i in range(len(solution)-1,0,-1):
                if i !=0 :
                    ans += f"{solution[i]} -> "
            ans+=end
            return ans,step
        # print(f"{truoc}\n---------------")

def DFS():
    solution = []
    truoc = {}
    stack = [f"{start}"]
    flag = {}
    step =[]
    for dinh in tap_dinh:
        flag[dinh] = 0
    while True:
        if stack == []:
            return "Not found solution!",None

        u = stack.pop(0)
        step.append(u)
        flag[u] = 1
        ke = []
        for i in range(size):
            if matrix[id[f"{u}"]][i] != 0:
                for key,value in id.items():
                    if id[key] == i and flag[key] == 0:
                        ke.append(key)
                        ke.sort(key=lambda x:x[0])
                        truoc[key] = u
                        flag[key] = 1
                        break
        # print(f"{truoc}-----\n")
        stack = ke + stack
        # print(stack)
        if u == end:
            find_way(truoc,start,end,solution)
            ans = ''
            for i in range(len(solution)-1,0,-1):
                if i !=0 :
                    ans += f"{solution[i]} -> "
            ans+=end
            return ans,step

def Best_First_Search():
    global u
    solution = []
    truoc = {}
    open = dict({f"{start}": h[start]})
    flag = {}
    step = []
    for dinh in tap_dinh:
        flag[dinh] = 0
    while True:
        if open == {}:
            return "Not found solution!",None
        
        u = next(key for key in open.keys())
        if u != end:
            open.pop(u)
        flag[u] = 1
        step.append(u)
        for i in range (size):
            if matrix[id[f"{u}"]][i] != 0:
                for key,value in id.items():
                    if id[key] == i and flag[key] == 0:
                        open[key] = h[key]
                        if flag[key] == 0:
                            truoc[key] = u
                            flag[key] = 1
        open = sort_dict(open)
        # print(f"{truoc}-------\n")
        # print(step)
        if u == end:
            find_way(truoc,start,end,solution)
            ans = ''
            for i in range(len(solution)-1,0,-1):
                if i !=0 :
                    ans += f"{solution[i]} -> "
            ans+=end
            return ans,step

def Hill_Climbing_Search():
    global u
    solution = []
    truoc = {}
    open = dict({f"{start}": h[start]})
    
    flag = {}
    step = []
    for dinh in tap_dinh:
        flag[dinh] = 0
    while True:
        tmp_open = {}
        if open == {}:
            return "Not found solution!",None          
        
        u = next(key for key in open.keys())
        
        if u != end:
            open.pop(u)
        flag[u] = 1
        step.append(u)
        for i in range (size):
            if matrix[id[f"{u}"]][i] != 0:
                for key,value in id.items():
                    if id[key] == i and flag[key] == 0:
                        tmp_open[key] = h[key]
                        if flag[key] == 0:
                            truoc[key] = u
                            flag[key] = 1
        tmp_open = sort_dict(tmp_open)
        open = tmp_open|open
        # print(step)
        # print(open)
        # print(f"{truoc}-------\n")
        if u == end:
            find_way(truoc,start,end,solution)
            ans = ''
            for i in range(len(solution)-1,0,-1):
                if i !=0 :
                    ans += f"{solution[i]} -> "
            ans+=end
            return ans,step

        
ans,step = BFS()
if ans != "Not found solution!":
    print(f"duong di tim thay theo BFS la: {ans}\nthu tu duyet dinh la: {step}\n")
else:
    print(f"duyet theo BFS khong tim thay duong di")



ans,step = DFS()
if ans != "Not found solution!":
    print(f"duong di tim thay theo DFS la: {ans}\nthu tu duyet dinh la: {step}\n")
else:
    print(f"duyet theo DFS khong tim thay duong di")


ans,step = Best_First_Search()
if ans != "Not found solution!":
    print(f"duong di tim thay theo Best_First_Seach la: {ans}\nthu tu duyet dinh la: {step}\n")
else:
    print(f"duyet theo Best_First_Search khong tim thay duong di")



ans,step = Hill_Climbing_Search()
if ans != "Not found solution!":
    print(f"duong di tim thay theo Hill_Climbing_Search la: {ans}\nthu tu duyet dinh la: {step}\n")
else:
    print(f"duyet theo ill_Climbing_Search khong tim thay duong di")
