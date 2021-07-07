The first attempt is easy:
Multiply up the whole array and divide for every entry in the return array the corresponding value of the input array

```
calc_products_of_all_others: (arr:[int]) -> [int]

returns an array of the same size of arr, where every entry is the product of all values in arr except the one at the corresponding index
```

the solution would something like this 
```
calc_products_of_all_others([int] arr, int arr_size) -> [int]:
  total_product:int = 1
  for_each elem in arr:
    total_product *= elem 

  products_of_all_others:[int] = init
  for (i=0; i<arr_size; i++):
    product_of_all_others[i] = total_product / arr[i];

  return product_of_all_others 
```

#### Follow-up: what if you can't use division?
Here we need some precalculations and some extra space to hold them:
We need two precalculation of the growing product for each running direction.
For every entry we calculate the result with the predecessor of the forward precalculated products array, and the successor of the backward precalculated products. It is better to show this an example:
Example: `arr = [2, 3, 4, 5] -> [60, 40, 30, 24]`
```
forward : [2 ,2*3, 2*3*4, 2*3*4*5] = [  2,  6, 24, 120]
backward: [5*4*3*2, 5*4*3 ,5*4 ,5] = [120, 60, 20,   5]
```
Just arrange them with the right offset and pend them at the right place with the production identity.
```
        1,[  2,   6,  24, 120]
                *
[120,  60,  20,   5],  1, 
                =
      [60,  40,  30,  24]
```
Notice, that we can drop the total_product and it will become:
```
forward  = [ 1, 2, 6,24]
backward = [60,20, 5, 1] 
```
In pseudo code:
```
forward_products  = int[arr_size]
forward_products[0] = 1
for (i=0; i < arr_size-1; i++):
  forward_products[i+1] = forward_products[i] * arr[i]

backward_products = int[arr_size]
backward_products[arr_size-1] = 1
for (i=arr_size-1; i > 0; i--):
  backward_products[i-1] = backward_products[i] * arr[i]

products_of_all_others = int[arr_size]
for (i=0; i < arr_size; i++):
  products_of_all_others[i] = backward_products[i]*forward_products[i]

return products_of_all_others
``` 

We could save some space and time, if we calculate the backward_products direct with the forward_products into the resulting value. this save us one loop `(T(n) space and memory)`, and we have less similar code;
```
backward_products = initialize like above

products_of_all_others = int[arr_size]
forward_product = 1
for (i=0; i < arr_size-1; i++):
  products_of_all_others[i] = backward_products[i]*forward_product;
  forward_product *= arr[i];

return products_of_all_others
```

language: python
[code](solution.py)

not trivial cases, that are considered: 
- input is an empty array -> empty array back
- input has just one entry -> array with 1 as only entry
- input is null / None
not considered cases, but should be discussed:
- input wrong type -> assert / raise an error (this is not easy in python and against the duck typing. Classic array of a single type are hard to type check in python -> so I decided, that the static typing notation is here enough, but python does no check)
- the absolute of the products is too big for the precision of the used integer type / overflow (not a problem with python)

run `python -m doctest -v test.doctest`
