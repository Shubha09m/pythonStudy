import copy


class Format:
    def __init__(self,t):
       self.temp=t

    def MaxReducedString(self):

        flag=True
        while flag:
            flag=False
            for i in range(1,len(self.temp)):
                if self.temp[i]==self.temp[i-1]:
                    self.temp=self.temp[0:i-1]+self.temp[i+1:]
                    flag=True
                    break
        if len(self.temp)==0:
            print("empty string")
        else:
            print(self.temp)

f=Format('abccddd')
f.MaxReducedString()



