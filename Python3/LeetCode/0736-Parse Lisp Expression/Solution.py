import collections

class Solution:
     
     def evaluate(self, expression: str) -> int:

          # 題目的括弧是連著的, split 分不開
          expression = expression.replace('(', ' ( ')
          expression = expression.replace(')', ' ) ')

          # python list 是 dynamic array, list.pop(0) 時間複雜度 : O(N)
          # double-ended-queue 可以安心的 deque.popleft() 時間複雜度 : O(1)
          tokens = collections.deque(expression.split())
          
          # variables 紀錄參數的值, 會是個 stack 
          variables = collections.defaultdict(list)

          return self.recur(tokens, variables)

     def recur(self, tokens: collections, variables: list) -> int:
          
          # 每 1 次 call recur 就等於讀(pop)最左邊的 tokens
          command = tokens.popleft()

          # 如果不是前括弧, 代表不是 int 就是 variables, 所以直接回傳
          if command != '(':
               try: return int(command)
               except: return variables[command][-1]

          # 如果是前括弧, 就再 pop 一次捨棄掉前括弧
          command = tokens.popleft()
          
          # let 的情況
          if command == 'let':
               
               # 由於程式是從左到右讀取, 但計算是括弧內先計算
               # (let x 2 (let x 3 x)), variables 會先是 x = 2 => x = 3
               # 括弧內計算完就要把 x = 3 pop 掉
               stack = []
               while tokens:

                    # 遇到新括弧或結尾, recur 到底會算出答案
                    # 之後就可以把這層在 variables 存的值 pop 掉
                    if tokens[0] == '(' or tokens[1] == ')':
                         value = self.recur(tokens, variables)
                         tokens.popleft()
                         while stack : variables[stack.pop()].pop()
                         return value

                    # 第一個 popleft 會是參數, 不會有括弧
                    # 第二個 popleft 會有括弧, call recur
                    # 用 stack 記錄這層存的值
                    var = tokens.popleft()
                    value = self.recur(tokens, variables)
                    stack.append(var)
                    variables[var].append(value)
                    
          
          # add 或 multi 的情況
          # call 2 次 recur 並 將結果相加或相乘
          # 最後把後括弧 pop 掉 並 回傳結果
          else :
               if command == 'add' : result = self.recur(tokens, variables) + self.recur(tokens, variables)
               else : result = self.recur(tokens, variables) * self.recur(tokens, variables)
               tokens.popleft()
               return result


