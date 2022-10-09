class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        arrK =[]

        for i in range(len(arr),1,-1):
            indexOfi=arr.index(i)
            
            if indexOfi==0 :
                y=arr[0:i]
                y.reverse()
                y.extend(arr[i:])
                arr=y
                arrK.append(i)
                continue
                
            if indexOfi+1 != i:
                
                x=arr[0:indexOfi+1]
                x.reverse()
                x.extend(arr[indexOfi+1:])
                arr=x
                arrK.append(indexOfi+1)
                
                y=arr[0:i]
                y.reverse()
                y.extend(arr[i:])
                arr=y
                arrK.append(i)
                
        return arrK

