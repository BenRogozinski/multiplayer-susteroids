def on_player4_connected():
    global greenCrewmate, playersRemaining, gameStarted
    greenCrewmate = sprites.create(assets.image("""
        greenCrewmate1
    """), SpriteKind.player)
    greenCrewmate.set_position(146, 105)
    greenCrewmate.set_stay_in_screen(True)
    controller.player4.move_sprite(greenCrewmate, 0, 100)
    playersRemaining += 1
    gameStarted = 1
controller.player4.on_event(ControllerEvent.CONNECTED, on_player4_connected)

def on_player3_disconnected():
    sprites.destroy(yellowCrewmate)
controller.player3.on_event(ControllerEvent.DISCONNECTED, on_player3_disconnected)

def on_player4_disconnected():
    sprites.destroy(greenCrewmate)
controller.player4.on_event(ControllerEvent.DISCONNECTED, on_player4_disconnected)

def on_player1_disconnected():
    sprites.destroy(redCrewmate)
controller.player1.on_event(ControllerEvent.DISCONNECTED, on_player1_disconnected)

def on_player2_button_a_pressed():
    global blueLaser
    blueCrewmate.set_image(assets.image("""
        blueCrewmate2
    """))
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.IN_BACKGROUND)
    blueLaser = sprites.create(assets.image("""
        blueLaser
    """), SpriteKind.projectile)
    blueLaser.set_position(130, blueCrewmate.y)
    blueLaser.set_flag(SpriteFlag.AUTO_DESTROY, True)
    blueLaser.set_velocity(-250, 0)
    pause(100)
    blueCrewmate.set_image(assets.image("""
        blueCrewmate1
    """))
    pause(fireDelay)
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def initializeGame():
    global playersRemaining, gameStarted
    scene.set_background_image(assets.image("""
        spaceBackground
    """))
    info.set_score(0)
    playersRemaining = 0
    gameStarted = 0
    game.set_game_over_effect(True, effects.none)
    game.set_game_over_message(True, "GAME OVER!")

def on_player3_connected():
    global yellowCrewmate, playersRemaining, gameStarted
    yellowCrewmate = sprites.create(assets.image("""
        yellowCrewmate1
    """), SpriteKind.player)
    yellowCrewmate.set_position(146, 75)
    yellowCrewmate.set_stay_in_screen(True)
    controller.player3.move_sprite(yellowCrewmate, 0, 100)
    playersRemaining += 1
    gameStarted = 1
controller.player3.on_event(ControllerEvent.CONNECTED, on_player3_connected)

def on_on_overlap(sprite2, otherSprite):
    sprites.destroy(sprite2)
    sprites.destroy(otherSprite, effects.disintegrate, 50)
    info.change_score_by(1)
    pause(20)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite3, otherSprite2):
    global playersRemaining
    sprites.destroy(sprite3, effects.disintegrate, 100)
    sprites.destroy(otherSprite2, effects.disintegrate, 100)
    playersRemaining += -1
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

def on_player2_disconnected():
    sprites.destroy(blueCrewmate)
controller.player2.on_event(ControllerEvent.DISCONNECTED, on_player2_disconnected)

def on_player4_button_a_pressed():
    global greenLaser
    greenCrewmate.set_image(assets.image("""
        greenCrewmate2
    """))
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.IN_BACKGROUND)
    greenLaser = sprites.create(assets.image("""
        greenLaser
    """), SpriteKind.projectile)
    greenLaser.set_position(130, greenCrewmate.y)
    greenLaser.set_flag(SpriteFlag.AUTO_DESTROY, True)
    greenLaser.set_velocity(-250, 0)
    pause(100)
    greenCrewmate.set_image(assets.image("""
        greenCrewmate1
    """))
    pause(fireDelay)
controller.player4.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player4_button_a_pressed)

def on_player1_button_a_pressed():
    global redLaser
    redCrewmate.set_image(assets.image("""
        redCrewmate2
    """))
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.IN_BACKGROUND)
    redLaser = sprites.create(assets.image("""
        redLaser
    """), SpriteKind.projectile)
    redLaser.set_position(130, redCrewmate.y)
    redLaser.set_flag(SpriteFlag.AUTO_DESTROY, True)
    redLaser.set_velocity(-250, 0)
    pause(100)
    redCrewmate.set_image(assets.image("""
        redCrewmate1
    """))
    pause(fireDelay)
controller.player1.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player1_button_a_pressed)

def on_player3_button_a_pressed():
    global yellowLaser
    yellowCrewmate.set_image(assets.image("""
        yellowCrewmate2
    """))
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.IN_BACKGROUND)
    yellowLaser = sprites.create(assets.image("""
        yellowLaser
    """), SpriteKind.projectile)
    yellowLaser.set_position(130, yellowCrewmate.y)
    yellowLaser.set_flag(SpriteFlag.AUTO_DESTROY, True)
    yellowLaser.set_velocity(-250, 0)
    pause(100)
    yellowCrewmate.set_image(assets.image("""
        yellowCrewmate1
    """))
    pause(fireDelay)
controller.player3.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player3_button_a_pressed)

def on_player2_connected():
    global blueCrewmate, playersRemaining, gameStarted
    blueCrewmate = sprites.create(assets.image("""
        blueCrewmate1
    """), SpriteKind.player)
    blueCrewmate.set_position(146, 45)
    blueCrewmate.set_stay_in_screen(True)
    controller.player2.move_sprite(blueCrewmate, 0, 100)
    playersRemaining += 1
    gameStarted = 1
controller.player2.on_event(ControllerEvent.CONNECTED, on_player2_connected)

def on_on_destroyed(sprite):
    if sprite.x >= 160:
        game.game_over(True)
sprites.on_destroyed(SpriteKind.enemy, on_on_destroyed)

def on_player1_connected():
    global redCrewmate, playersRemaining, gameStarted
    redCrewmate = sprites.create(assets.image("""
        redCrewmate1
    """), SpriteKind.player)
    redCrewmate.set_position(146, 15)
    redCrewmate.set_stay_in_screen(True)
    controller.player1.move_sprite(redCrewmate, 0, 100)
    playersRemaining += 1
    gameStarted = 1
controller.player1.on_event(ControllerEvent.CONNECTED, on_player1_connected)

asteroidSmall: Sprite = None
yellowLaser: Sprite = None
redLaser: Sprite = None
greenLaser: Sprite = None
blueLaser: Sprite = None
blueCrewmate: Sprite = None
redCrewmate: Sprite = None
yellowCrewmate: Sprite = None
gameStarted = 0
playersRemaining = 0
greenCrewmate: Sprite = None
fireDelay = 0
fireDelay = 100
gameDifficultyMultiplier = 1
initializeGame()

def on_update_interval():
    global asteroidSmall
    if playersRemaining == 0 and gameStarted == 1:
        game.game_over(True)
    for index in range(Math.round(playersRemaining * gameDifficultyMultiplier)):
        asteroidSmall = sprites.create(assets.image("""
            asteroidSmall
        """), SpriteKind.enemy)
        asteroidSmall.set_flag(SpriteFlag.AUTO_DESTROY, True)
        asteroidSmall.set_position(0, randint(8, 112))
        asteroidSmall.set_velocity(50, 0)
game.on_update_interval(750, on_update_interval)
