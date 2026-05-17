#find maximum key of the dict

dict={"A":50,"B":30,"C":70}
max_key=max(dict,key=dict.get)
print(max_key)

#find minimum key of the dict
min_key=min(dict,key=dict.get)
print(min_key)