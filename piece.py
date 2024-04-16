from random import randint


class Tshape:
    rotation = [[[0,1,0],
                 [1,1,1],
                 [0,0,0]],

                [[0,1,0],
                 [0,1,1],
                 [0,1,0]],

                [[0,0,0],
                 [1,1,1],
                 [0,1,0]],
                
                [[0,1,0],
                 [1,1,0],
                 [0,1,0]]]
    
    code = 'T'


class Sshape:
    rotation = [[[0,1,1],
                 [1,1,0],
                 [0,0,0]],

                [[0,1,0],
                 [0,1,1],
                 [0,0,1]],

                [[0,0,0],
                 [0,1,1],
                 [1,1,0]],
                
                [[1,0,0],
                 [1,1,0],
                 [0,1,0]]]

    code = 'S'


class Zshape:
    rotation = [[[1,1,0],
                 [0,1,1],
                 [0,0,0]],

                [[0,0,1],
                 [0,1,1],
                 [0,1,0]],

                [[0,0,0],
                 [1,1,0],
                 [0,1,1]],
                
                [[0,1,0],
                 [1,1,0],
                 [1,0,0]]]
    
    code = 'Z'


class Lshape:
    rotation = [[[0,0,1],
                 [1,1,1],
                 [0,0,0]],

                [[0,1,0],
                 [0,1,0],
                 [0,1,1]],

                [[0,0,0],
                 [1,1,1],
                 [1,0,0]],
                
                [[1,1,0],
                 [0,1,0],
                 [0,1,0]]]
    
    code = 'L'


class Jshape:
    rotation = [[[0,0,0],
                 [1,1,1],
                 [0,0,1]],

                [[0,1,0],
                 [0,1,0],
                 [1,1,0]],

                [[1,0,0],
                 [1,1,1],
                 [0,0,0]],
                
                [[0,1,1],
                 [0,1,0],
                 [0,1,0]]]

    code = 'J'


class Oshape:
    rotation = [[[0,1,1,0],
                 [0,1,1,0],
                 [0,0,0,0]],

                [[0,1,1,0],
                 [0,1,1,0],
                 [0,0,0,0]],

                [[0,1,1,0],
                 [0,1,1,0],
                 [0,0,0,0]],
                
                [[0,1,1,0],
                 [0,1,1,0],
                 [0,0,0,0]]]
    
    code = 'O'


class Ishape:
    rotation = [[[0,0,0,0],
                 [1,1,1,1],
                 [0,0,0,0],
                 [0,0,0,0]],

                [[0,0,1,0],
                 [0,0,1,0],
                 [0,0,1,0],
                 [0,0,1,0]],

                [[0,0,0,0],
                 [0,0,0,0],
                 [1,1,1,1],
                 [0,0,0,0]],
                
                [[0,1,0,0],
                 [0,1,0,0],
                 [0,1,0,0],
                 [0,1,0,0]]]

    code = 'I'


class Choice():
    def __init__(self):
        self.pool = []
        self.queue = []
        self.fill_queue()


    def get_piece(self) -> object:
        '''
        Returns a random shape.\n
        The shapes that are selected are removed from the choice pool. When all shapes are removed, the pool is reset.
        '''
        if not self.pool:
            self.pool = [Tshape, Sshape, Zshape, Lshape, Jshape, Ishape, Oshape]

        return self.pool.pop(randint(0, len(self.pool)-1))


    def fill_queue(self):
        '''Adds new random shapes to the queue if there are less than 4 shapes in the queue.'''
        while len(self.queue) < 4:
            self.queue.append(self.get_piece())


    def dequeue(self) -> object:
        '''Returns the first shape in the queue.'''
        shape = self.queue.pop(0)
        self.fill_queue()
        return shape


    def reset_queue(self):
        self.pool = []
        self.queue = []
        self.fill_queue()




if __name__ == '__main__':

    bag = Choice()

    print(bag.dequeue().code)


    ...
    