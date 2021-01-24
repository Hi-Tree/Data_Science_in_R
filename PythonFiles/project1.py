import numpy as np

def calculate(list):
  if len(list) < 9:
      raise ValueError("List must be 9 digits long")
  s = np.array(list, dtype = float).reshape(3,3)
  axis1 = [np.mean(s, axis = 0).tolist(), np.var(s, axis = 0).tolist(), np.std(s, axis = 0).tolist(), np.max(s,axis =0).tolist(), np.min(s, axis = 0).tolist(), np.sum(s, axis = 0).tolist()]
  axis2 = [np.mean(s, axis = 1).tolist(), np.var(s, axis = 1).tolist(), np.std(s, axis = 1).tolist(), np.max(s,axis =1).tolist(), np.min(s, axis = 1).tolist(), np.sum(s, axis = 1).tolist()]
  flattened = [np.mean(list).tolist(), np.var(list).tolist(), np.std(list).tolist(), np.max(list).tolist(), np.min(list).tolist(), np.sum(list).tolist()]
  calculations = {"mean": [axis1[0], axis2[0], flattened[0]],
                  "variance": [axis1[1], axis2[1], flattened[1]],
                  "standard deviation": [axis1[2], axis2[2], flattened[2]],
                  "max": [axis1[3], axis2[3], flattened[3]],
                  "min": [axis1[4], axis2[4], flattened[4]],
                  "sum": [axis1[5], axis2[5], flattened[5]] } 

  return calculations
list1 = [1,2,3,4,5,6,7,8]
print(calculate(list1))
