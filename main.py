@namespace
class SpriteKind:
    Treasure = SpriteKind.create()
    Victim = SpriteKind.create()
    Theif = SpriteKind.create()
def enterHouse():
    global myVictim, treasure
    tiles.set_current_tilemap(tilemap("""
        house1
        """))
    myVictim = sprites.create(assets.image("""
            myVictimSleep
            """),
        SpriteKind.Victim)
    treasure = sprites.create(assets.image("""
        treasure
        """), SpriteKind.Treasure)
    tiles.place_on_random_tile(myRogue, assets.tile("""
        transparency16
        """))
    tiles.place_on_random_tile(myVictim, assets.tile("""
        transparency16
        """))
    tiles.place_on_random_tile(treasure, assets.tile("""
        transparency16
        """))
    scene.camera_follow_sprite(myRogue)

def on_on_overlap(sprite, otherSprite):
    sprite.x += -10
    sprite.y += -10
    otherSprite.x += 10
    otherSprite.y += 10
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.Theif, SpriteKind.Victim, on_on_overlap)

def on_overlap_tile(sprite2, location):
    leaveVillage()
    enterHouse()
scene.on_overlap_tile(SpriteKind.Theif,
    assets.tile("""
        houseA
        """),
    on_overlap_tile)

def on_on_overlap2(sprite3, otherSprite2):
    sprites.destroy(otherSprite2)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.Theif, SpriteKind.Treasure, on_on_overlap2)

def leaveVillage():
    sprites.set_data_number(myRogue, "villageCol", myRogue.tilemap_location().column)
    sprites.set_data_number(myRogue, "villageRow", myRogue.tilemap_location().row)
def leaveHouse():
    sprites.destroy_all_sprites_of_kind(SpriteKind.Treasure)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Victim)
def enterVillage():
    tiles.set_current_tilemap(tilemap("""
        valleyVillage
        """))
    tiles.place_on_tile(myRogue,
        tiles.get_tile_location(sprites.read_data_number(myRogue, "villageCol"),
            sprites.read_data_number(myRogue, "villageRow")))

def on_overlap_tile2(sprite4, location2):
    leaveHouse()
    enterVillage()
scene.on_overlap_tile(SpriteKind.Theif,
    assets.tile("""
        transparency16
        """),
    on_overlap_tile2)

treasure: Sprite = None
myVictim: Sprite = None
myRogue: Sprite = None
myRogue = sprites.create(assets.image("""
    myRogue
    """), SpriteKind.Theif)
sprites.set_data_boolean(myRogue, "moving", False)
controller.move_sprite(myRogue)
info.set_score(0)
info.set_life(3)
scene.camera_follow_sprite(myRogue)
sprites.set_data_number(myRogue, "villageCol", 1)
sprites.set_data_number(myRogue, "villageRow", 1)
enterVillage()

def on_on_update():
    if controller.player1.is_pressed(ControllerButton.LEFT) or (controller.player1.is_pressed(ControllerButton.RIGHT) or (controller.player1.is_pressed(ControllerButton.UP) or controller.player1.is_pressed(ControllerButton.DOWN))):
        sprites.set_data_boolean(myRogue, "moving", True)
        myRogue.set_image(assets.image("""
            myRogue
            """))
    else:
        sprites.set_data_boolean(myRogue, "moving", False)
        myRogue.set_image(assets.image("""
            myRogueCloak
            """))
game.on_update(on_on_update)
