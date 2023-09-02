controller.player4.onEvent(ControllerEvent.Connected, function () {
    greenCrewmate = sprites.create(assets.image`greenCrewmate1`, SpriteKind.Player)
    greenCrewmate.setPosition(146, 105)
    greenCrewmate.setStayInScreen(true)
    controller.player4.moveSprite(greenCrewmate, 0, 100)
    playersRemaining += 1
    gameStarted = 1
})
controller.player3.onEvent(ControllerEvent.Disconnected, function () {
    sprites.destroy(yellowCrewmate)
})
controller.player4.onEvent(ControllerEvent.Disconnected, function () {
    sprites.destroy(greenCrewmate)
})
controller.player1.onEvent(ControllerEvent.Disconnected, function () {
    sprites.destroy(redCrewmate)
})
controller.player2.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    blueCrewmate.setImage(assets.image`blueCrewmate2`)
    music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.InBackground)
    blueLaser = sprites.create(assets.image`blueLaser`, SpriteKind.Projectile)
    blueLaser.setPosition(130, blueCrewmate.y)
    blueLaser.setFlag(SpriteFlag.AutoDestroy, true)
    blueLaser.setVelocity(-200, 0)
    pause(100)
    blueCrewmate.setImage(assets.image`blueCrewmate1`)
    pause(fireDelay)
})
function initializeGame () {
    scene.setBackgroundImage(assets.image`spaceBackground`)
    info.setScore(0)
    playersRemaining = 0
    gameStarted = 0
    game.setGameOverEffect(true, effects.none)
    game.setGameOverMessage(true, "GAME OVER!")
}
controller.player3.onEvent(ControllerEvent.Connected, function () {
    yellowCrewmate = sprites.create(assets.image`yellowCrewmate1`, SpriteKind.Player)
    yellowCrewmate.setPosition(146, 75)
    yellowCrewmate.setStayInScreen(true)
    controller.player3.moveSprite(yellowCrewmate, 0, 100)
    playersRemaining += 1
    gameStarted = 1
})
controller.player2.onEvent(ControllerEvent.Disconnected, function () {
    sprites.destroy(blueCrewmate)
})
controller.player4.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    greenCrewmate.setImage(assets.image`greenCrewmate2`)
    music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.InBackground)
    greenLaser = sprites.create(assets.image`greenLaser`, SpriteKind.Projectile)
    greenLaser.setPosition(130, greenCrewmate.y)
    greenLaser.setFlag(SpriteFlag.AutoDestroy, true)
    greenLaser.setVelocity(-200, 0)
    pause(100)
    greenCrewmate.setImage(assets.image`greenCrewmate1`)
    pause(fireDelay)
})
controller.player1.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    redCrewmate.setImage(assets.image`redCrewmate2`)
    music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.InBackground)
    redLaser = sprites.create(assets.image`redLaser`, SpriteKind.Projectile)
    redLaser.setPosition(130, redCrewmate.y)
    redLaser.setFlag(SpriteFlag.AutoDestroy, true)
    redLaser.setVelocity(-200, 0)
    pause(100)
    redCrewmate.setImage(assets.image`redCrewmate1`)
    pause(fireDelay)
})
controller.player3.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    yellowCrewmate.setImage(assets.image`yellowCrewmate2`)
    music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.InBackground)
    yellowLaser = sprites.create(assets.image`yellowLaser`, SpriteKind.Projectile)
    yellowLaser.setPosition(130, yellowCrewmate.y)
    yellowLaser.setFlag(SpriteFlag.AutoDestroy, true)
    yellowLaser.setVelocity(-200, 0)
    pause(100)
    yellowCrewmate.setImage(assets.image`yellowCrewmate1`)
    pause(fireDelay)
})
controller.player2.onEvent(ControllerEvent.Connected, function () {
    blueCrewmate = sprites.create(assets.image`blueCrewmate1`, SpriteKind.Player)
    blueCrewmate.setPosition(146, 45)
    blueCrewmate.setStayInScreen(true)
    controller.player2.moveSprite(blueCrewmate, 0, 100)
    playersRemaining += 1
    gameStarted = 1
})
sprites.onDestroyed(SpriteKind.Enemy, function (sprite) {
    if (sprite.x >= 160) {
        game.gameOver(true)
    }
})
controller.player1.onEvent(ControllerEvent.Connected, function () {
    redCrewmate = sprites.create(assets.image`redCrewmate1`, SpriteKind.Player)
    redCrewmate.setPosition(146, 15)
    redCrewmate.setStayInScreen(true)
    controller.player1.moveSprite(redCrewmate, 0, 100)
    playersRemaining += 1
    gameStarted = 1
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(sprite)
    sprites.destroy(otherSprite, effects.disintegrate, 50)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(sprite, effects.disintegrate, 100)
    sprites.destroy(otherSprite, effects.disintegrate, 100)
    playersRemaining += -1
})
let asteroidSmall: Sprite = null
let yellowLaser: Sprite = null
let redLaser: Sprite = null
let greenLaser: Sprite = null
let blueLaser: Sprite = null
let blueCrewmate: Sprite = null
let redCrewmate: Sprite = null
let yellowCrewmate: Sprite = null
let gameStarted = 0
let playersRemaining = 0
let greenCrewmate: Sprite = null
let fireDelay = 0
fireDelay = 100
initializeGame()
game.onUpdateInterval(500, function () {
    if (playersRemaining == 0 && gameStarted == 1) {
        game.gameOver(true)
    }
    for (let index = 0; index < Math.round(playersRemaining / 2); index++) {
        asteroidSmall = sprites.create(assets.image`asteroidSmall`, SpriteKind.Enemy)
        asteroidSmall.setFlag(SpriteFlag.AutoDestroy, true)
        asteroidSmall.setPosition(0, randint(8, 112))
        asteroidSmall.setVelocity(50, 0)
    }
})
