import sys
# class for solving equation
class solve:

    def __init__(self, num):
        self.num = num
    # arrange bracket arguments in queue    
    def brack_queue(self,val1,val2,eq):
        queue=[eq[i] for i in range(val1+1,val2-1)]
        return queue
    # argument that are not in bracket
    def without_brack_queue(self,val1,val2,eq):
        queue=[eq[i] for i in range(val1,val2)]
        return queue
    # solve accouding to DMAS RULE
    def DMAS_queue(self,queue):
        operators_queue=[]
        for i in queue:
            if i=='^':
                operators_queue.append(i)
        for i in queue:
            if i=='/':
                operators_queue.append(i)
        for i in queue:
            if i=='*':
                operators_queue.append(i)
        for i in queue:
            if i=='+':
                operators_queue.append(i)
        for i in queue:
            if i=='-':
                operators_queue.append(i)
        return operators_queue
    
    # priority arrange based on DMAS rule
    def priority_arrange(self,operator_queue,eq):
        queue_arr=[]
        count=operator_queue.count('^')
        while count>0:
            Index=eq.index('^')
            new=float(eq[Index-1])**float(eq[Index+1])
            eq[Index-1]=new
            for i in range(0,2):
                eq.pop(Index)
            count=count-1
            
        count=operator_queue.count('/')
        while count>0:
            Index=eq.index('/')
            v1=float(eq[Index-1])
            v2=float(eq[Index+1])
            new=v1/v2
            eq[Index-1]=new
            for i in range(0,2):
                eq.pop(Index)
            count=count-1
            
        count=operator_queue.count('*')
        while count>0:
            Index=eq.index('*')
            new=float(eq[Index-1])*float(eq[Index+1])
            eq[Index-1]=new
            for i in range(0,2):
                eq.pop(Index)
            count=count-1
        
        count=operator_queue.count('+')
        while count>0:
            Index=eq.index('+')
            new=float(eq[Index-1])+float(eq[Index+1])
            eq[Index-1]=new
            for i in range(0,2):
                eq.pop(Index)
            count=count-1
        count=operator_queue.count('-')
        while count>0:
            Index=eq.index('-')
            new=float(eq[Index-1])-float(eq[Index+1])
            eq[Index-1]=new
            for i in range(0,2):
                eq.pop(Index)
            count=count-1

        return eq
            
        
    # bracket will be solved first    
    def solve_brack(self,val1,val2,eq):
        obj=solve(0)
        queue=list(obj.brack_queue(val1,val2,eq))
        operator=list(obj.DMAS_queue(eq))
        arr=list(obj.priority_arrange(operator,queue))  
        self.num=arr[0]
        return str(self.num)


def simplify_eq(eq):
    Count=eq.count('(')
    queue=[i for i in eq]
    while(Count>0):
        
        Index=queue.index('(')
        val=Index
        temp=[]
        while True:
            temp.append(queue[Index])
            Index=Index+1
            if queue[Index]=='(':
                temp=[]
                val=Index
                temp.append(queue[Index])
            elif queue[Index]==')':
                temp.append(queue[Index])
                value=solve(0)
                new=value.solve_brack(0,len(temp),temp)
                queue[val]=new
                Value=Index-val
                for i in range(Value):
                    queue.pop(val+1)
                Count=Count-1
                break
    return queue

def final_solve(val1,val2,eq):
    obj=solve(0)
    operator=list(obj.DMAS_queue(eq))
    arr=list(obj.priority_arrange(operator,eq))  
    return str(arr[0])


m=sys.argv[1]

n=simplify_eq(m)
ans=final_solve(0,len(n),n)
print(ans)
