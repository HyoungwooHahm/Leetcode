class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        intv=[]
        while 1:
            if i==len(firstList) or j==len(secondList) :
                break
                    
            if firstList[i][0] < secondList[j][0]:
                if firstList[i][1] >= secondList[j][0]:
                    if firstList[i][1] < secondList[j][1]:
                        temp=[]
                        temp.append(secondList[j][0])
                        temp.append(firstList[i][1])
                        intv.append(temp)
                        i+=1
                        continue
                    if firstList[i][1] == secondList[j][1]:
                        intv.append(secondList[j])
                        i+=1
                        j+=1
                        continue
                    if firstList[i][1] > secondList[j][1]:
                        intv.append(secondList[j])
                        j+=1
                        continue
                    
                else:
                    i+=1
                    continue
                                
            if firstList[i][0] > secondList[j][0]:
                if secondList[j][1] >= firstList[i][0]:
                    if secondList[j][1] < firstList[i][1]:
                        temp=[]
                        temp.append(firstList[i][0])
                        temp.append(secondList[j][1])
                        intv.append(temp)
                        j+=1
                        continue
                    if secondList[j][1] == firstList[i][1]:
                        intv.append(firstList[i])
                        i+=1
                        j+=1
                        continue
                    if secondList[j][1] > firstList[i][1]:
                        intv.append(firstList[i])
                        i+=1
                        continue
                    
                else:
                    j+=1
                    continue
                    
            if firstList[i][0] == secondList[j][0]:
                if firstList[i][1] >secondList[j][1]:
                    temp=[]
                    temp.append(firstList[i][0])
                    temp.append(secondList[j][1])
                    intv.append(temp)
                    j+=1
                    continue
                    
                if firstList[i][1] == secondList[j][1]:
                    intv.append(firstList[i])
                    i+=1
                    j+=1
                    continue
                                     
                else :
                    temp=[]
                    temp.append(secondList[j][0])
                    temp.append(firstList[i][1])
                    intv.append(temp)
                    i+=1
            
        return intv
           
      
                
                                    
                                    
            
        