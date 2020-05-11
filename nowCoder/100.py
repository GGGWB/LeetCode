count=0
for i in range(0,5):
    for j in range(0,11):
        for k in range(0,21):
            if 5*i+2*j+k==20:
                count+=1
print(count)