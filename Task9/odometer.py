from functools import reduce
from pymonad.maybe import Maybe

lst = [15,1,25,2,30,3,10,5]

def get_time_diffs (arr: list[int]):
    times = arr[1::2]
    delta_times = map(lambda t: t[0] - t[1], zip(times, [0] + times[:-1]))
    
    return zip(arr[::2], delta_times)
    
get_dist = lambda spd_and_tim: map(lambda s_t: s_t[0] * s_t[1], spd_and_tim)
get_route_len = lambda dist: sum(dist)

odometer = lambda data: (Maybe.insert(data).then(get_time_diffs)
                                           .then(get_dist)
                                           .then(get_route_len)
                                           .value)

print(odometer(lst)) # 90
