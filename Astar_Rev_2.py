class Arena:  # Description Arena
    def __init__(self, arena, width_arena, length_arena):
        self.arena = arena
        self.length = length_arena
        self.width = width_arena
        self.space_time = []

    def create_space_time_map(self):
        time = self.length*self.width*3
        for t in range(time):
            for x in range(self.length):
                for y in range(self.width):
                    if self.arena[y][x] == '1':
                        self.space_time.append({"coordinate": (x, y), "time": t, "value": 9})
                    else:
                        pass


def update_map(arena, bot):
    for t, _b in enumerate(bot.path):
        arena.space_time.append({"coordinate": _b["coordinate"], "time": t, "value": bot.id})
        if t == 0:
            continue
        arena.space_time.append({"coordinate": _b["coordinate"], "time": t-1, "value": bot.id})


class Bot:  # Description Bot
    def __init__(self, start_point, finish_point, _id):
        xs, ys = start_point.split(",")
        xf, yf = finish_point.split(",")
        self.start = (int(xs), int(ys))
        self.finish = (int(xf), int(yf))
        self.open_list = []
        self.closed_list = []
        self.path = []
        self.id = _id


def import_arena():  # return map as 2D array : map[y][x], x is axis, y is ordinate
    with open('Maps.txt', 'r') as _maps:  # import map from txt
        _path = [line.strip() for line in _maps.readlines()]
        width_arena = len(_path)
        length_arena = len(_path[0])

    arena = [[0]] * width_arena
    for y, line in enumerate(_path):
        arena[-y - 1] = tuple(list(line))
    print(f"Environment with length and width is {length_arena} x {width_arena}")
    return arena, width_arena, length_arena


def show_arena(arena):  # show maps in normal x and y
    with open('reservationTable.txt', 'w') as _txt:  # import map from txt
        for _space in arena.space_time:
            csv_sample = f"{_space['coordinate']},{_space['time']},{_space['value']}\n"
            _txt.writelines(csv_sample)


def bot_information():  # asking coordinate bot
    bot_start_point = input("input bot start coordinate (x,y): ")
    bot_finish_point = input("input bot finish coordinate (x,y): ")
    return bot_start_point, bot_finish_point


def check(bot, _xt, _yt, _maps, _t):
    if any(_map.get("coordinate", None) == (_xt, _yt) and _map.get("time", None) == _t for _map in
           _maps.space_time):  # check hit obstacle or not
        return False
    else:
        return True


def calc(bot, xd, yd, _t):
    for _close in bot.closed_list:
        if bot.open_list[-1]["parent"] == _close["coordinate"]:
            bot.open_list[-1].update({"gx": _close["gx"] + 1})
    hx = abs(xd - bot.finish[0]) + abs(yd - bot.finish[1])
    fx = hx + bot.open_list[-1]["gx"]
    bot.open_list[-1].update({"hx": hx, "fx": fx, "cost": fx - _t})


def plan(bot, arena, maximum_try):
    xc, yc = bot.start  # x and y start as first coordinate
    try_counter = 0
    time = 1  # time is 1 at first movement from start, same as real life should change it
    w = 0  # find another efficient way to find is any if got true or not
    bot.closed_list.append({"coordinate": (xc, yc), "gx": 0, "parent": 0, "time": 0})
    while xc != bot.finish[0] or yc != bot.finish[1]:  # until find the start
        try_counter += 1  # count as time too
        left_point = xc - 1
        right_point = xc + 1
        top_point = yc + 1
        bottom_point = yc - 1
        if left_point < 0:
            pass
        elif check(bot, left_point, yc, arena, time):
            bot.open_list.append({"coordinate": (left_point, yc), "parent": (xc, yc), "time": time})
            calc(bot, left_point, yc, time)
            w += 1
            # print("dari kiri")
        if right_point >= arena.length:
            pass
        elif check(bot, right_point, yc, arena, time):
            bot.open_list.append({"coordinate": (right_point, yc), "parent": (xc, yc), "time": time})
            calc(bot, right_point, yc, time)
            w += 1
            # print("dari kanan")
        if bottom_point < 0:
            pass
        elif check(bot, xc, bottom_point, arena, time):
            bot.open_list.append({"coordinate": (xc, bottom_point), "parent": (xc, yc), "time": time})
            calc(bot, xc, bottom_point, time)
            w += 1
            # print("dari bawah")
        if top_point >= arena.width:
            pass
        elif check(bot, xc, top_point, arena, time):
            bot.open_list.append({"coordinate": (xc, top_point), "parent": (xc, yc), "time": time})
            calc(bot, xc, top_point, time)
            w += 1
            # print("dari atas")
        if w == 0:
            if check(bot, xc, yc, arena, time):
                bot.open_list.append({"coordinate": (xc, yc), "parent": (xc, yc), "time": time})
                calc(bot, xc, yc, time)
        bot.open_list = sorted(bot.open_list, key=lambda k: k["cost"], reverse=True)
        time = bot.open_list[-1]["time"] + 1
        bot.closed_list.append(bot.open_list[-1])
        bot.open_list.pop()
        xc, yc = bot.closed_list[-1]["coordinate"]
        w = 0
        if try_counter > maximum_try:
            print("Maximum Try Reached")
            break
    print(f"With {try_counter} times exploration to reached the goal")


def path(bot):
    bot.path.append({"coordinate": bot.closed_list[-1]["coordinate"], "parent": bot.closed_list[-1]["parent"]})
    _t = bot.closed_list[-1]["time"] - 1
    while bot.path[0]["coordinate"] != bot.start:
        for _close in bot.closed_list:
            if _close["coordinate"] == bot.path[0]["parent"] and _close["time"] == _t:
                bot.path.insert(0, ({"coordinate": _close["coordinate"], "parent": _close["parent"]}))
                _t -= 1


#_environment, _width, _length = import_arena()  # map[y][x], width map, length map
#maze = Arena(_environment, _width, _length)
#maze.create_space_time_map()
#bot_start, bot_finish = bot_information()
#b1 = Bot(bot_start, bot_finish, 1)
#plan(b1, maze, 400)
#path(b1)
#print(b1.path)
#show_arena(maze)
#update_map(maze, b1)
#show_arena(maze)
#
