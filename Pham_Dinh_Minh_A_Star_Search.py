import numpy as np
size = 8
matrix = np.zeros((int(size),int(size)))
f = open("matran.txt")
ds = f.readlines()
tap_dinh = ['S','A','B','C','D','E','F','G','H']
# id = dict({'S': 0, 'A': 1, 'B': 2, 'C': 3, 'D' : 4, 'E': 5, 'F': 6, 'G' : 7 , 'H' : 8})
i = 0
id = {}
bool_check = {}
for dinh in tap_dinh:
    id[dinh] = i
    bool_check[dinh] = 0
    i+=1
# bool_check = dict({'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D' : 0, 'E': 0, 'F': 0, 'G' : 0 , 'H' : 0})


h = dict({'S': 10,
          'A': 8,
          'B': 9,
          'C': 7,
          'D': 4,
          'E': 3,
          'F': 0,
          'G': 6,
          'H': 6,})

for i in range(size):
    ans = ds[i].split("\t")
    for j in range(size):
        matrix[i][j] = float(ans[j])
f.close()
output = ""
start = 'S'
end = 'F'
open = dict({f"{start}" : 10})
G = {}
F = {}
truoc = {}
solution = []
step = []

# del(open['S'])
def find_way(truoc,start,end,solution):
    if end == start:
        solution.append(end)
        return
    solution.append(end)
    find_way(truoc,start,truoc[end],solution)

while True:
    
    if open == {}:
        output = "not found solution!"
        print(output)
        break

    min_value = min(open.items(), key = lambda x:x[1])
    
   
    # u = min_value[0]
    
         
    if len(open) == 1:
        u = min_value[0]
    else:
        u = None
        dem = 0 
        for key,value in open.items():
            if  key != min_value[0] and open[key] == min_value[1]:
                dem += 1
                gmin = min((G[key]),(G[min_value[0]]))
                print("gmin = ",gmin)
                if G[key] == gmin:
                    u = key
                else:
                    u = min_value[0]
        if dem == 0:
                u = min_value[0]
    
    try:
        if min_value[0] == start:
            pass
        else:
            next[end]
            u = end
    except KeyError:
        pass
    # hàm try thực hiện xét đỉnh u, nếu đỉnh u nối tới end thì xác định luôn u tiếp theo chính là end

    print("u = ",u)
    if u != end:
        open.pop(u)
    bool_check[u] = 1
    step.append(u)
    
    next = {}
    for i in range (size):
        if matrix[id[f"{u}"]][i] != 0:
            for key in id.keys():
                if i == id[key]:
                    next[key] = h[key]
                    if bool_check[key] == 0:
                        truoc[key] = u
                    break
    print("next  ",next)
    print("truoc = ",truoc)
    g = {}
    for key, value in next.items():
        g[key] = 0
        G[key] = 0
        if u == start:
                G[key] = matrix[id[u]][id[key]]
                g[key] = matrix[id[u]][id[key]]
                
        else: 
            # for i in range(0,len(step)):
            #     if step[i] == step[-1]:
            #         G[key] += matrix[id[step[i]]][id[key]]
            #         break
            #     # print("i = ",i)
            #     print(matrix[id[step[i]]][id[step[i+1]]])
            #     G[key] += matrix[id[step[i]]][id[step[i+1]]]
            solution_temp =[]
            find_way(truoc,start,key,solution_temp)
            for i in range(len(solution_temp)-1,0,-1):
                if i != 0 :
                    G[key] += matrix [id[solution_temp[i]]] [id[solution_temp[i-1]]]
                    g[key] += matrix [id[solution_temp[i]]] [id[solution_temp[i-1]]]

        F[key] = g[key] + h[key]
        if bool_check[key] == 0:
            open[key] = F[key]
            

    print("g = ", g)
    print("F = ",F)
    print("open = ",open)
    print("--------------------")
    if u == end:
        break



print(f"so dinh xet la: {len(step)}")
if output == "":
    find_way(truoc,start,end,solution)
    chiphi = 0
    print(f"duong di tim thay: ",end="")

    for i in range(len(solution)-1,0,-1):
        if i !=0 :
            chiphi += matrix[id[solution[i]]][id[solution[i-1]]]
            print(f"{solution[i]} -> ",end="")
    print(end)
    print(f"chi phi di chuyen la: {chiphi}")

print(f"step = {step}")


