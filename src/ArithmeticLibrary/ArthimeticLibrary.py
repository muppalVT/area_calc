def mathit(type,x,y):
  try:

    x_float = float(x);
    y_float = float(y);
    type = type.upper()

    if type == 'ADD':
      result = x_float + y_float   
    elif type == 'SUB':
       result = x_float - y_float   
    elif type == 'MULT':
       result = x_float * y_float 
    elif type == 'DIV': 
       result = x_float / y_float  
    
    print("Result: ",result)
  except ValueError:
    print("Invalid input(s)")
    return
  

# Testing / Examples
#mathit('add',';',4)
#mathit('sub',3,4)
#mathit('div',3,4)
#mathit('mult',3,4)