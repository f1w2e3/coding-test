import time 

a = 0
start_time = time.time()  

for _ in range(100):
    for _ in range(100):
        a = a + 1 

end_time = time.time()  


print("실행 시간:", end_time - start_time, "초")
