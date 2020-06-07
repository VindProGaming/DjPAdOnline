import arcade
import typing
import random

BUTTON_SIZE = 80

SCREEN_WIDTH = 600
SCREEN_HIEGT = 600

SCREEN_TITLE = "Launchpad.exe - Funny Sounds Prank"

x = [
        0,
        250,
        160,
        70,
        250,
        160,
        70,
        250,
        160,
        70
    ]

y = [
        0,
        250,
        250,
        250,
        160,
        160,
        160,
        70,
        70,
        70
    ]

sounds_name = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9
]

class SoundButton (arcade.SpriteSolidColor):
    def __init__(self, sound_file, pan, volume):
        super.__init__(BUTTON_SIZE, BUTTON_SIZE, arcade.color.WHITE)
        self.sound = arcade.Sound(sound_file)
        self.pan = pan
        self.volume = volume

    def play(self):
        self.sound.play( pan= self.pan, volume= self.volume)

class AudioStreamButton (arcade.SpriteSolidColor):
    def __init__(self, sound_file, pan, volume):
        super().__init__(BUTTON_SIZE, BUTTON_SIZE, arcade.color.WHITE)
        self.sound = arcade.Sound(sound_file)
        self.pan = pan
        self.volume = volume

    def play(self):
        self.sound.play( pan= self.pan, volume= self.volume)

    def volume_up(self):
        vol = self.sound.get_volume()
        self.sound.set_volume(vol + 0.1)
        print(f"Volumen: {self.sound.get_volume()}")

    def straem_position(self):
        print(f"Curent Position: {self.sound.get_stream_position()}")

class MyGame(arcade.Window):
    def __init__ ( self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
        self.button_sprites = None

    def setup(self):
        self.button_sprites = arcade.SpriteList()

        self.vpg = arcade.load_texture("image/icon.png")

        for i in range(1, 10):
            volume = 10
            button = AudioStreamButton("sounds/00" + str(sounds_name[i]) +".wav", pan = 0, volume = volume)
            button.center_x = SCREEN_WIDTH // 2 - x[i]
            button.center_y = SCREEN_HIEGT // 2 + y[i]
            self.button_sprites.append(button)

    def on_draw(self):
        arcade.start_render()
        self.button_sprites.draw()
        for i in range(1, 10):
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2 - x[i], SCREEN_HIEGT // 2 + y[i], BUTTON_SIZE, BUTTON_SIZE, self.vpg)

    def on_update(self, delta_time):
        self.button_sprites.update()

    def on_mouse_press(self, x, y, button, key_modifiers):
        hit_sprites = arcade.get_sprites_at_point((x, y), self.button_sprites)
        for sprite in hit_sprites:
            button_sprites = typing.cast(SoundButton, sprite)
            if button == arcade.MOUSE_BUTTON_LEFT:
                button_sprites.play()
            elif button == arcade.MOUSE_BUTTON_RIGHT:
                if button_sprites.sound.voice_handle:
                    button_sprites.volume_up()
                    button_sprites.stream_position()

def main():
    my_game = MyGame(SCREEN_WIDTH, SCREEN_HIEGT, SCREEN_TITLE)
    my_game.setup()
    arcade.run()

if __name__ == "__main__":
    main()