import random

class snake:

    def __init__(self,body,size):
        self.body = body
        self.board_size = size
        self.is_alive = True

    def get_body(self):
        return self.body

    def move(self,direction):
        new_head = [0,0]
        new_head[0] = (self.body[0][0] + direction[0])%self.board_size
        new_head[1] = (self.body[0][1] + direction[1])%self.board_size
        last = self.body[-1]
        old_head = self.body[0]
        #self.body = [tuple(new_head)]+self.body[:-1]
        return new_head,old_head,last
        

class board:

    def __init__(self,size,snake):
        self.size = size
        self.config = [ [" " for i in range(size)] for i in range(size)]
        #start = (size/2, size/2)
        self.snake = snake
        self.direcion = (1,0)
        self.is_fruit = True
        self.available_board = []
        self.n_fruits = 0

        for i in range(size):
            for j in range(size):
                self.available_board.append((i,j))

    def clear_board(self):
        self.config = [ [" " for i in range(size)] for i in range(size)]

    def put_snake_on_board(self):
        snake_body = self.snake.get_body()
        head = snake_body[0]
        self.config[head[0]][head[1]] = '@'
        self.available_board.remove((head[0],head[1]))
        for item in snake_body[1:]:
            self.config[item[0]][item[1]]='0'
            self.available_board.remove((item[0],item[1]))
            
        
    def move_snake_on_board(self,direction):
        
        new_head,old_head,last = self.snake.move(direction)
        
        if(self.config[new_head[0]][new_head[1]] == "0"):
            self.kill_snake()
            
        elif(self.config[new_head[0]][new_head[1]] == "$"):
            self.n_fruits += 1
            self.config[new_head[0]][new_head[1]] = '@'
            self.available_board.remove((new_head[0],new_head[1]))
            
            self.config[old_head[0]][old_head[1]] = '0'
            
            self.snake.body = [tuple(new_head)]+self.snake.body
            self.is_fruit=False
        else:
            self.config[new_head[0]][new_head[1]] = '@'
            self.available_board.remove((new_head[0],new_head[1]))
            
            self.config[old_head[0]][old_head[1]] = '0'
            
            self.config[last[0]][last[1]] = ' '
            self.available_board.append((last[0],last[1]))
            self.snake.body = [tuple(new_head)]+self.snake.body[:-1]

    def kill_snake(self):
        self.snake.is_alive = False
        print("Your collected {0} dollars".format(self.n_fruits))
        print("The snake died! Game Over")
        
    def render(self):
        print("_"*(self.size+2))
        for l in self.config:
            st = "".join(l)
            print("|" +st+"|")
        print("_"*(self.size+2))

        print('#'*50)
        print('#'*50)
        print('#'*50)

    def generate_fruit(self):
        position = random.choice(self.available_board)
        self.config[position[0]][position[1]]='$'
        

    def play(self):
        while(self.snake.is_alive):
            self.render()
            next_dir = input("Next direction ?")
            if(next_dir == 'w'):
                self.direction = (-1,0)
            elif(next_dir == 's'):
                self.direction = (1,0)
            elif(next_dir == 'a'):
                self.direction = (0,-1)
            elif(next_dir == 'd'):
                self.direction = (0,1)
            elif(next_dir == 'q'):
                print("Quit game")
                print("Your collected {0} dollars".format(self.n_fruits))
                return

            self.move_snake_on_board(self.direction)
            if(self.is_fruit == False):
                self.generate_fruit()
                self.is_fruit = True



def start_game():
    print("Snake Money")
    print()
    print("Instructions")
    print("The snake looks like this : @000000")
    print("The money looks like this : $")
    print("Use w,a,s,d keys to move UP,LEFT,DOWN,RIGHT respectively")
    print("COllect as much money as you can")
    print("Press s to start the game")
    print("You can press q at any time to close the game")
    inp = input()
    if( inp == 's'):
        sn = snake([(2,2),(2,3),(3,3),(3,4),(3,5),(3,6),(2,6)],20)
        b = board(20,sn)
        b.put_snake_on_board()
        b.generate_fruit()
        b.play()
    elif( inp != 's'):
        return

start_game()
        

    
    
        
                


