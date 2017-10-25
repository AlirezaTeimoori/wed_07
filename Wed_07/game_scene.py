from scene import *
import ui

from splash_scene import *
from main_menu_scene import *

class GameScene(Scene):
    def setup(self):
        #this method is called when user moves to this scene
        self.center_of_screen=self.size/2
        self.left_button_down=False
        self.right_button_down=False
        self.ship_move_speed= 20.0
        self.missiles = []
        #add background color
        
        self.background=SpriteNode(position=self.size/2,
                                   color= ('black'),
                                   parent=self,
                                   size=self.size)
                                   
        space_ship_position=self.size/2
        space_ship_position.y=100
        
        self.space_ship=SpriteNode('./assets/sprites/spaceship.png',
                                   position=space_ship_position,
                                   parent=self)
                                   
        left_button_position=self.center_of_screen
        left_button_position.x = 100
        left_button_position.y = 100
        self.left_button = SpriteNode('./assets/sprites/left_button.png',
                                      parent = self,
                                      position=left_button_position,
                                      alpha=0.5)
                                      
        right_button_position=self.center_of_screen
        right_button_position.x = 300
        right_button_position.y = 100
        self.right_button = SpriteNode('./assets/sprites/right_button.png',
                                       parent = self,
                                       position=right_button_position,
                                       alpha=0.5)
                                       
        fire_button_position=self.size
        fire_button_position.x = fire_button_position.x - 100
        fire_button_position.y = 100
        self.fire_button = SpriteNode('./assets/sprites/red_button.png',
                                      parent = self,
                                      position=fire_button_position,
                                      alpha=0.5)
                                      
        #back_button_position=self.size
        #back_button_position.y=back_button_position.y + 580
        #back_button_position.x=100
        #self.back_button=SpriteNode('./assets/sprites/back_button.png',
        #                            parent=self,
        #                            position=back_button_position)
        #                            
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        #move spaceship if button down
        
        if self.left_button_down == True:
            self.space_ship.run_action(Action.move_by(-1*self.ship_move_speed,0.0,0.1))
        if self.right_button_down == True:
            self.space_ship.run_action(Action.move_by(self.ship_move_speed,0.0,0.1))
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        # Check if left or right button is down
        
        if self.left_button.frame.contains_point(touch.location):
            self.left_button_down = True
            
        if self.right_button.frame.contains_point(touch.location):
            self.right_button_down = True
            
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        self.right_button_down = False
        self.left_button_down = False
        
        if self.fire_button.frame.contains_point(touch.location):
            self.create_new_missile()
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
    def create_new_missile(self):
        # when the user touches the fire button
        
        missile_start_position = self.space_ship.position
        missile_start_position.y = 100
        
        missile_end_position = self.size
        missile_end_position.x = missile_start_position.x
        
        self.missiles.append(SpriteNode('./assets/sprites/missile.png',
                             position = missile_start_position,
                             parent = self))
                             
        # make missile move forward
        
        missileMoveAction = Action.move_to(missile_end_position.x,
                                           missile_end_position.y+0,
                                           5.0)
                                           
        self.missiles[len(self.missiles)-1].run_action(missileMoveAction)
        
