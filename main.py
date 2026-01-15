// --- Setup Arena and Players ---
scene.setBackgroundColor(9) // Light blue sky
tiles.setCurrentTilemap(tilemap`arena`) // Use a tilemap with a floor

let player1 = sprites.create(img`2`, SpriteKind.Player)
let player2 = sprites.create(img`3`, SpriteKind.Enemy)

// Position players and add gravity
player1.setPosition(40, 100)
player2.setPosition(120, 100)
player1.ay = 600
player2.ay = 600

// --- Controls ---
controller.moveSprite(player1, 100, 0) // Horizontal move only

controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (player1.isHittingTile(CollisionDirection.Bottom)) {
        player1.vy = -200 // Jump
    }
})

// --- Melee Attack (Player 1) ---
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    let hitbox = sprites.create(img`1`, SpriteKind.Projectile)
    hitbox.setPosition(player1.x + 10, player1.y)
    hitbox.lifespan = 100 // Exists briefly
    
    // Check if hitbox hits Player 2
    if (hitbox.overlapsWith(player2)) {
        info.changeScoreBy(1)
        player2.sayText("Ouch!", 500)
    }
})

// --- Basic AI for Player 2 ---
game.onUpdateInterval(1000, function() {
    if (player2.x > player1.x) {
        player2.vx = -40
    } else {
        player2.vx = 40
    }
})

