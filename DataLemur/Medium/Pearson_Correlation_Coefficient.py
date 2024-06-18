def corr(x, y):
  d_xy=[]
  mean_x=sum(x)/len(x)
  mean_y=sum(y)/len(y)
  
  sd_x=(sum((i-mean_x)**2 for i in x) / len(x))**0.5
  sd_y=(sum((i-mean_y)**2 for i in x) / len(y))**0.5
  
  for i in range(len(x)):
    d_x=x[i]-mean_x
    d_y=y[i]-mean_y
    d_xy.append(d_x*d_y)
    
  mean_d_xy=sum(d_xy)/len(d_xy)
  return mean_d_xy/(sd_x*sd_y)
