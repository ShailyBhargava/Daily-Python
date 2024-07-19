def eval_expr(a):
    stack =[]
    operator = ['*','-','+','/','%']

    for item in a:
      if item not in operator:
         stack.append((item))

      else:
         first = int(stack.pop())
         sec = int(stack.pop())

         if (item =="+"):
            stack.append(sec + first)

         if (item =="-"):
            stack.append(sec - first)

         if (item =="/"):
            stack.append(sec / first)

         if (item =="*"):
            stack.append(sec * first)

         if (item =="%"):
            stack.append(sec % first)
        
    return stack[-1]

a= ["2","3","+","3","*"]   

print(eval_expr(a))         