n, w, L = map(int, input().split())
truck = list(map(int, input().split()))
bridge = [0]*w
T = 0
cur_weight=0
while truck or cur_weight>0:
    T += 1
    cur_weight-=bridge.pop(0)

    if truck and cur_weight+truck[0]<=L:
        cur_truck = truck.pop(0)
        bridge.append(cur_truck)
        cur_weight+=cur_truck
    else:
        bridge.append(0)

    # print("다리: ", bridge)
    # print("남은 트럭: ", truck)

print(T)
