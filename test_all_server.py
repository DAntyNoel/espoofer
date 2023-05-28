import os, time
for i in range(15):
    print(f'正在进行第{i+1}次尝试...\n\n')
    os.system(f'python espoofer.py -id server_a{i+1}')
    time.sleep(60)
    print('=' * 50)