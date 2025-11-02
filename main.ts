namespace SpriteKind {
    export const Treasure = SpriteKind.create()
    export const Victim = SpriteKind.create()
    export const Theif = SpriteKind.create()
}
function enterHouse () {
    tiles.setCurrentTilemap(tilemap`house1`)
    myVictim = sprites.create(assets.image`myVictimSleep`, SpriteKind.Victim)
    treasure = sprites.create(assets.image`treasure`, SpriteKind.Treasure)
    tiles.placeOnRandomTile(myRogue, assets.tile`entry`)
    tiles.placeOnRandomTile(myVictim, assets.tile`bed`)
    tiles.placeOnRandomTile(treasure, assets.tile`stand`)
    scene.cameraFollowSprite(myRogue)
}
sprites.onOverlap(SpriteKind.Theif, SpriteKind.Victim, function (sprite, otherSprite) {
    sprite.x += -10
    sprite.y += -10
    otherSprite.x += 10
    otherSprite.y += 10
    info.changeLifeBy(-1)
})
scene.onOverlapTile(SpriteKind.Theif, assets.tile`houseA`, function (sprite, location) {
    leaveVillage()
    enterHouse()
})
scene.onOverlapTile(SpriteKind.Theif, assets.tile`exit`, function (sprite, location) {
    leaveHouse()
    enterVillage()
})
sprites.onOverlap(SpriteKind.Theif, SpriteKind.Treasure, function (sprite, otherSprite) {
    sprites.destroy(otherSprite)
    info.changeScoreBy(1)
})
function leaveVillage () {
    sprites.setDataNumber(myRogue, "villageCol", myRogue.tilemapLocation().column)
    sprites.setDataNumber(myRogue, "villageRow", myRogue.tilemapLocation().row)
}
function leaveHouse () {
    sprites.destroyAllSpritesOfKind(SpriteKind.Treasure)
    sprites.destroyAllSpritesOfKind(SpriteKind.Victim)
}
function enterVillage () {
    tiles.setCurrentTilemap(tilemap`valleyVillage`)
    tiles.placeOnTile(myRogue, tiles.getTileLocation(sprites.readDataNumber(myRogue, "villageCol"), sprites.readDataNumber(myRogue, "villageRow")))
}
let treasure: Sprite = null
let myVictim: Sprite = null
let myRogue: Sprite = null
myRogue = sprites.create(assets.image`myRogue`, SpriteKind.Theif)
sprites.setDataBoolean(myRogue, "moving", false)
controller.moveSprite(myRogue)
info.setScore(0)
info.setLife(3)
scene.cameraFollowSprite(myRogue)
sprites.setDataNumber(myRogue, "villageCol", 1)
sprites.setDataNumber(myRogue, "villageRow", 1)
enterVillage()
game.onUpdate(function () {
    if (controller.left.isPressed() || (controller.right.isPressed() || (controller.up.isPressed() || controller.down.isPressed()))) {
        sprites.setDataBoolean(myRogue, "moving", true)
        myRogue.setImage(assets.image`myRogue`)
    } else {
        sprites.setDataBoolean(myRogue, "moving", false)
        myRogue.setImage(assets.image`myRogueCloak`)
    }
})
