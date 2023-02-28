class Solution(object):
  def findRightInterval(self, a):
    s,i = zip(*sorted([[x[0],i] for i,x in enumerate(a)] + [[float('inf'),-1]]))
    return [i[bisect_left(s,e-0.5)] for _,e in a]





   
