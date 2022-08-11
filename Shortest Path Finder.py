
import curses
from curses import wrapper
import queue
import time


maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]
# O is the start point and x is the end 


#---- PrintMaze----#
def PrintMaze(maze,stdscr,path=[]):
    BLUE=curses.color_pair(1)
    RED=curses.color_pair(2)
   
    for i ,row in enumerate(maze):
        for j ,value in enumerate(row):
            if  (i,j) in path:
               stdscr.addstr(i,j*2,"X",RED)

            else:   
             stdscr.addstr(i,j*2,value,BLUE)


#---- to find the start point ----#            

def FindStart(maze,start):
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if value == start:
                return i,j
    return None            

#---- find path aligrithem ----#
def FindPath(maze,stdscr):
    start="O"
    end="X"
    start_point=FindStart(maze,start)
    q=queue.Queue()
    
    q.put((start_point,[start_point])) # the first one is for pross the nod and the 2nd one is for know the path 
    visited=set() # this set is to all nod are be prossed 

    while not q.empty():
        current_pos,path=q.get()
        row,col=current_pos

        stdscr.clear()
        PrintMaze(maze,stdscr,path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col]==end:
            return path 

        neighbbors=find_neighbors(maze,row,col)
        for neighbor in neighbbors:
            if neighbor in visited:
                continue

            r,c=neighbor
            if maze[r][c]=="#":
                continue

            new_path=path+[neighbor]
            q.put((neighbor,new_path))
            visited.add(neighbor)

    


def find_neighbors(maze,row,col):
    neighbors=[]

    if row > 0 : # UP
        neighbors.append((row-1,col))
    if row +1< len(maze): # DOWN
        neighbors.append((row+1,col))
    if col >0: #LEFT
        neighbors.append((row,col-1))
    if col +1< len(maze[0]): # RIGHT
        neighbors.append((row,col+1))

    return neighbors    
    


def main(stdscr):
    # init the color 
     curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
     curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
     
     
     FindPath(maze,stdscr)
     stdscr.getch()


wrapper(main)