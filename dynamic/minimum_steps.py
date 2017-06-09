def get_min_steps (num):
  """
  For any positive integer num, returns the amount of steps necessary to reduce
  the number to 1 given the following possible steps:

  1) Subtract 1
  2) Divide by 2
  3) Divide by 3

  >>>get_min_steps(15)
  4

  """

  if num <= 0 or type(num) != int: return None

  min_steps_list = [0] * (num + 1)
  for i in range(2, num + 1):
    print('\n')
    print('i = {0}'.format(i))
    print(dict(enumerate(min_steps_list)))

    # We can either -1, /2 or /3 -- this is the -1 step
    min_steps_list[i] = 1 + min_steps_list[i-1]

    # for any number i, we either take min_steps_list[i - i] + 1, or the number of steps
    # of its /2 or /3 factor (+1 because we have just added one more step)
    if i % 2 == 0:
      print('divisible by two')
      print('''min_steps_list[{0}] = {1} \n1 + min_steps_list[{2}] = {3}'''.format(i, min_steps_list[i], i/2, 1 + min_steps_list[i/2]))
      min_steps_list[i] = min( min_steps_list[i] , 1 + min_steps_list[i/2] )

    if i % 3 == 0:
      print('divisible by three')
      print('''min_steps_list[{0}] = {1} \n1 + min_steps_list[{2}] = {3}'''.format(i, min_steps_list[i], i/3, 1 + min_steps_list[i/3]))
      min_steps_list[i] = min( min_steps_list[i] , 1 + min_steps_list[i/3] )

  return min_steps_list[num]

if __name__ == '__main__':
  print(get_min_steps(8))
  # print(get_min_steps(247))

def fib(n):
  if n == 1: return 1
  return fib(n-1) + fib(n-2)

def min_steps_recursive(num):
  # if num == 1 return 1
  return min(min_steps_recursive(n-1) + min_steps_recursive(n/2) + min_steps_recursive(n/3))
