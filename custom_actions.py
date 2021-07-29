from nle import nethack


_useful_actions = list(nethack.USEFUL_ACTIONS)
#print(len(_useful_actions))


rarely_useful_actions = (
nethack.Command.ADJUST,
#nethack.Command.APPLY,
nethack.Command.ATTRIBUTES,
nethack.Command.CALL,
#nethack.Command.CAST,
nethack.Command.CHAT,
nethack.Command.CLOSE,
nethack.Command.DIP,
#nethack.Command.DROP,
nethack.Command.DROPTYPE,
nethack.Command.ENGRAVE,
nethack.Command.ENHANCE,
nethack.Command.FIRE,
nethack.Command.FIGHT,
nethack.Command.INVENTORY,
nethack.Command.INVENTTYPE,
nethack.Command.INVOKE,
nethack.Command.JUMP,
nethack.Command.LOOK,
nethack.Command.MONSTER,
nethack.Command.MOVE,
nethack.Command.MOVEFAR,
nethack.Command.OFFER,
nethack.Command.PAY,
#nethack.Command.PRAY,
#nethack.Command.PUTON,
#nethack.Command.QUAFF,
nethack.Command.QUIVER,
#nethack.Command.READ,
#nethack.Command.REMOVE,
nethack.Command.RIDE,
nethack.Command.RUB,
nethack.Command.RUSH,
nethack.Command.RUSH2,
nethack.Command.SEETRAP,
nethack.Command.SIT,
nethack.Command.SWAP,
nethack.Command.TAKEOFF,
nethack.Command.TAKEOFFALL,
nethack.Command.THROW,
#nethack.Command.TIP,
nethack.Command.TURN,
nethack.Command.TWOWEAPON,
nethack.Command.UNTRAP,
nethack.Command.VERSIONSHORT,
#nethack.Command.WEAR,
#nethack.Command.WIELD,
#nethack.Command.WIPE,
#nethack.Command.ZAP,
)

for rua in rarely_useful_actions:
    _useful_actions.remove(rua)

#_useful_actions.remove(nethack.MiscDirection.DOWN)

print(_useful_actions)

CUSTOM_ACTION_SET = tuple(_useful_actions)

#print(_useful_actions)
#print(len(_useful_actions))
#print(tuple(list(nethack.TextCharacters)))
'''
CUSTOM_ACTION_SET = list(nethack.CompassCardinalDirection) + list(nethack.CompassIntercardinalDirection)

#print(type(nethack.TextCharacters.PLUS))
CUSTOM_ACTION_SET.append(nethack.MiscDirection.WAIT)
CUSTOM_ACTION_SET.append(nethack.MiscDirection.DOWN)
CUSTOM_ACTION_SET.append(nethack.MiscAction.MORE)

CUSTOM_ACTION_SET.append(nethack.Command.EAT)
CUSTOM_ACTION_SET.append(nethack.Command.ESC)
CUSTOM_ACTION_SET.append(nethack.Command.KICK)
CUSTOM_ACTION_SET.append(nethack.Command.OPEN)
CUSTOM_ACTION_SET.append(nethack.Command.SEARCH)

CUSTOM_ACTION_SET = tuple(CUSTOM_ACTION_SET)
'''
