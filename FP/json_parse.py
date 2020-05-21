import json

worker={'addr':'127.0.0.1', 'port' : 9003}
with open('workers.conf','r+') as f:
    worker_ls = []
    try:
        conf = json.loads(f.read())
        worker_ls = conf
    except :
        pass
    worker_ls.append(worker)
    worker_str = json.dumps(worker_ls)
    f.seek(0)
    f.write(worker_str)
    f.truncate()

# worker={'addr':'127.0.0.1', 'port' : 9002}
# with open('workers.conf','r+') as f:
#     worker_ls = []
#     try:
#         conf = json.loads(f.read())
#         worker_ls = conf
#     except :
#         pass
#     worker_ls.append(worker)
#     worker_str = json.dumps(worker_ls)
#     f.seek(0)
#     f.write(worker_str)
#     f.truncate()

with open('workers.conf','r') as f:
    worker_ls = json.loads(f.read())
    print(worker_ls)



