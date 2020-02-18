init offset = 1

### CHARACTER DEFINITIONS ###
#############################

# Gio's note:
# Snowbound blood uses its own pre-rendered textboxes.
# Making your own characters is usually easier than this!
define !secily = Character("SECILY", kind=hiveswap, image="secily", window_background="{{assets}}/gui/textbox_secily.png", show_blood="#0989A0",)

# N.B.
# SBB uses "GothamHTF-Black.otf" for the character font.
# To replicate this, we can create our own style here.
# Todo.

### CHARACTER SPRITES ##
########################

image !secily = Image("{{assets}}/images/secily_idle.png", yanchor=860)
image !secily speak = Image("{{assets}}/images/secily_idle_speak.png", yanchor=860)
image !secily annoyed = Image("{{assets}}/images/secily_annoyed.png", yanchor=860)
image !secily engarde = Image("{{assets}}/images/secily_en_garde.png", yanchor=860)
image !secily lunge = Image("{{assets}}/images/secily_lunge.png", yanchor=860)
image !secily menacing = Image("{{assets}}/images/secily_menacing.png", yanchor=860)
image !secily menacing speak = Image("{{assets}}/images/secily_menacing_speak.png", yanchor=860)
image !secily parry = Image("{{assets}}/images/secily_parry.png", yanchor=860)
image !secily sword hold = Image("{{assets}}/images/secily_sword_hold.png", yanchor=860)
image !secily sword hold speak = Image("{{assets}}/images/secily_sword_hold_speak.png", yanchor=860)
image !secily gun = Image("{{assets}}/images/secily_then_perish.png", yanchor=860)
image !secily unamused = Image("{{assets}}/images/secily_unamused.png", yanchor=860)
image !secily unamused speak = Image("{{assets}}/images/secily_unamused_speak.png", yanchor=860)
image !secily young = Image("{{assets}}/images/secily_young.png", yanchor=860)

image background !warehouse = Image("{{assets}}/images/warehouse.png")
