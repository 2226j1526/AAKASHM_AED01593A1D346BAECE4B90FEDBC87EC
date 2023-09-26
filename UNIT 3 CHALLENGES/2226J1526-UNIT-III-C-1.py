def linear_SearchProduct(productlist, targetProduct):
  indices = []
  
  for index, product in  enumerate(productlist):
    if product == targetProduct:
      indices.append(index)
  return indices

      
  
# Example usage:
products = ["Apple", "Banana", "Orange", "Apple", "Grape","Apple"]
target = "Apple"
target2 = "shoes"
result = linear_SearchProduct(products, target)

#print(result)

print("Indices of '{}' in the list: {}".format(target, result))