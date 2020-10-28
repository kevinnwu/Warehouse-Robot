import Astar_Rev_2 as ar2
import Reverse_Astar as ra

_environment, _width, _length = ar2.import_arena()
maze = ar2.Arena(_environment, _width, _length)
maze.create_space_time_map()

_environment, _width, _length = ra.import_arena()
maze_reverse = ra.Arena(_environment, _width, _length)
maze_reverse.create_space_time_map()


b1 = ar2.Bot("2,5", "2,0", 1)
b2 = ar2.Bot("5,3", "0,5", 2)
b1r = ra.Bot("2,0", "2,5", 1)
b2r = ra.Bot("0,5", "5,3", 2)


ar2.plan(b1, maze, 2000)
ar2.path(b1)
print(b1.path)
print(len(b1.path))
ar2.update_map(maze, b1)
ar2.show_arena(maze)
ar2.plan(b2, maze, 500)
ar2.path(b2)
print(b2.path)
print(len(b2.path))

#ra.plan(b1r, maze_reverse, 500)
#ra.path(b1r)
#print(b1r.path)
#ra.update_map(maze_reverse, b1r)
#ra.show_arena(maze_reverse)
#ra.plan(b2r, maze_reverse, 500)
#ra.path(b2r)
#print(b2r.path)


#time saat search dan saat jalan itu berbeda. kebalikan
#kalau ada stop nilai fx nya lebih baik dari jalan karena nilai hx (dari titik tujuan ke point yg mau diarah atau wait)
# nya lebih kecil daripada yg jalan

