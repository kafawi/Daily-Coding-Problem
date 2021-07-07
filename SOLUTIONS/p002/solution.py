def calc_products_of_all_others(arr: list[int]) -> list[int]:
  """Calculate a new array with each entry at index i is a product of all numbers in the original array except the one at i."""
  if arr is None: raise TypeError("'None' is not allowed for input")

  backward_products = [1]*len(arr)
  for i in range(len(arr)-1 , 0, -1):
    backward_products[i-1] = backward_products[i] * arr[i]

  products_of_all_others = [1]*len(arr)
  forward_product = 1
  for i in range(0, len(arr)):
    products_of_all_others[i] = backward_products[i]*forward_product;
    forward_product *= arr[i];

  return products_of_all_others
  