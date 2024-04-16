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
    
    color_code = 'T'


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

    color_code = 'S'


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
    
    color_code = 'Z'


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
    
    color_code = 'L'


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

    color_code = 'J'


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
    
    color_code = 'O'


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

    color_code = 'I'


class PieceBag():
    bag = []

    def get_piece(self):
        if not self.bag:
            self.bag = [Tshape, Sshape, Zshape, Lshape, Jshape, Ishape, Oshape]

        return self.bag.pop(randint(0, len(self.bag)-1))


if __name__ == '__main__':

    bag = PieceBag()

    print(bag.get_piece())
    print(bag.get_piece())
    print(bag.get_piece())
    print(bag.get_piece())
    print(bag.get_piece())
    print(bag.get_piece())
    print(bag.get_piece())

    print(bag.get_piece())


    ...
    