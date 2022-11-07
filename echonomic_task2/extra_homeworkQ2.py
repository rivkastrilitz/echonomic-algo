from doctest import testmod

def is_leximin_better(x: list, y: list )->bool:
    '''
          This function finds which vector is leximin better
          returns true if x is leximin better and false otherwise.
          Define input and expected output:

           >>> is_leximin_better(x = [1, 2, 4, 5], y= [1, 3, 4, 5])
           False
           >>> is_leximin_better(x = [1, 3, 4, 5], y= [1, 2, 4, 5])
           True
           >>> is_leximin_better(x = [1, 3, 5, 5], y= [1, 3, 4, 5])
           True
           >>> is_leximin_better(x = [1, 3, 5, 5], y= [1, 3, 5, 5])
           False
           >>> is_leximin_better(x = [1, 9, 3, 2], y= [1, 3, 5, 5])
           False

      '''
    sorted_x = sorted(x)
    sorted_y = sorted(y)
    for i in range(len(sorted_x)):
        if sorted_x > sorted_y :
            return True
    return False

if __name__ == '__main__':
    l1 = [1, 3, 4, 5]
    l2 = [1, 2, 5, 9]
    l3 = [1, 2, 5, 9]
    print(is_leximin_better(l1, l2))
    print(is_leximin_better(l2, l1))
    print(is_leximin_better(l2, l3))
    testmod(name='is_leximin_better', verbose=True)