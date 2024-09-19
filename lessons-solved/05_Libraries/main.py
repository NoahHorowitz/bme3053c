from mymodule.math_operations import add,subtract,multiply,divide

print(f'3+3={add(3,3)}')
print(f'3*3={multiply(3,3)}')
print(f'3-3={subtract(3,3)}')
print(f'3/3={divide(3,3,)}')


try:
    print(divide(10,0))
except ValueError as e:
    print(e)