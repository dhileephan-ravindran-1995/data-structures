class Solution:
    def removeStars(self, s: str) -> str:

        def stackLogic():
            print("******stack Logic********")
            k = []
            for i in s:
                if(i!='*'):
                    k.append(i)
                else:
                    k.pop()
            #print(''.join(k))
            return ''.join(k)
        
        def stringLogic():
            print("******string Logic*******")
            k = ''
            for i in s:
                if(i != '*'):
                    k= k + i
                else:
                    k = k[0:-1]
                #print(k)
            return k


        return stackLogic()
        #return stringLogic()

if __name__ == "__main__":
    s = "leet**cod*e"
    print("input: ", s)
    sol = Solution()
    output = sol.removeStars(s)
    print("output: ", output)

        