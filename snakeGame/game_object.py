from pyglet import sprite

# class GameObject():
#     def __init__(self, x, y):
#         # Set Initial Position of Object
#         self.x = x
#         self.y = y


class Ball():
    def __init__(self, x, y, resource):
        # Ball attribute
        self.sprite = sprite.Sprite(resource, x, y)

    def draw(self):
        self.sprite.draw()
    
    @property
    def x(self):
        return self.sprite.position[0]
    
    @property
    def y(self):
        return self.sprite.position[1]
    
    def update_position(self, x=None, y=None):
        self.sprite.update(x, y)

