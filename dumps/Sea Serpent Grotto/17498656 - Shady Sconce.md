# 17498656 - Shady Sconce

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Sea Serpent Grotto (ID: 176) |
| Block Size       | 460 bytes                    |
| Total Events     | 3                            |
| References Count | 18                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [21](#event-21)       | 0x0001       |     39 |              8 |
| [22](#event-22)       | 0x0028       |    320 |             52 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1DA9      |        7593 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x00EA      |         234 |
|       4 | 0x0013      |          19 |
|       5 | 0xFFFD4D6C  |  4294790508 |
|       6 | 0x4211D     |      270621 |
|       7 | 0x6383      |       25475 |
|       8 | 0x0FA0      |        4000 |
|       9 | 0xFFFD48B0  |  4294789296 |
|      10 | 0x42A68     |      273000 |
|      11 | 0x03E8      |        1000 |
|      12 | 0x000F      |          15 |
|      13 | 0x001E      |          30 |
|      14 | 0x01D2      |         466 |
|      15 | 0x1DAB      |        7595 |
|      16 | 0x1DAD      |        7597 |
|      17 | 0x00C8      |         200 |

## String References

- **7593**: Hold out your hand? [Yes./No.]

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 39 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 24 00 80 01 80 02  80 25 02 00 10 02 80 00   B$......%......
0010: 26 00 45 03 80 F0 FF FF  7F F0 FF FF 7F 6B 75 70  &.E..........kup
0020: 6F 02 80 01 26 00 21 00                           o...&.!.        
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x24] CREATE_DIALOG(message_id=7593*, default_option=1*, option_flags=0*)
    → "Hold out your hand? [Yes./No.]"
  2: 0x0009 [0x25] WAIT_DIALOG_SELECT()
  3: 0x000A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0026
  4: 0x0012 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "kupo" with entities [LocalPlayer, LocalPlayer], work=[234*, 0*]
  5: 0x0023 [0x01] GOTO 0x0026

SUBROUTINE_0026:
  6: 0x0026 [0x21] END_EVENT
  7: 0x0027 [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0028    |
| Data Size    | 320 bytes |
| Instructions | 47        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          42 24 00 80 01 80 02 80          B$......
0030: 25 02 00 10 02 80 00 54  00 43 00 43 01 45 03 80  %......T.C.C.E..
0040: F0 FF FF 7F F0 FF FF 7F  6B 75 70 6F 02 80 01 61  ........kupo...a
0050: 00 01 61 00 02 00 10 01  80 00 61 00 21 00 01 61  ..a.......a.!..a
0060: 00 42 45 03 80 F0 FF FF  7F F0 FF FF 7F 6B 75 70  .BE..........kup
0070: 6F 02 80 1A 47 01 46 01  38 04 80 27 10 F0 FF FF  o...G.F.8..'....
0080: 7F 08 27 10 26 02 0B 01  03 BA F0 FF FF 7F 05 80  ..'.&...........
0090: 06 80 07 80 08 80 BA 26  02 0B 01 09 80 0A 80 07  .......&........
00A0: 80 0B 80 80 F0 FF FF 7F  80 26 02 0B 01 1C 0C 80  .........&......
00B0: 4A F0 FF FF 7F 26 02 0B  01 4A 26 02 0B 01 F0 FF  J....&...J&.....
00C0: FF 7F 6F 76 F0 FF FF 7F  6F 76 26 02 0B 01 1C 0D  ..ov....ov&.....
00D0: 80 45 0E 80 F0 FF FF 7F  F0 FF FF 7F 67 30 30 32  .E..........g002
00E0: 02 80 1A 26 01 2B 26 02  0B 01 0F 80 23 2B 26 02  ...&.+&.....#+&.
00F0: 0B 01 10 80 23 27 10 26  02 0B 01 05 52 0E 80 F0  ....#'.&....R...
0100: FF FF 7F F0 FF FF 7F 67  30 30 32 1A 47 01 1C 0D  .......g002.G...
0110: 80 46 00 45 11 80 F0 FF  FF 7F F0 FF FF 7F 66 64  .F.E..........fd
0120: 69 32 02 80 21 00 45 11  80 F0 FF FF 7F F0 FF FF  i2..!.E.........
0130: 7F 66 64 69 31 02 80 55  11 80 F0 FF FF 7F F0 FF  .fdi1..U........
0140: FF 7F 66 64 69 31 1B 45  11 80 F0 FF FF 7F F0 FF  ..fdi1.E........
0150: FF 7F 66 64 6F 31 02 80  55 11 80 F0 FF FF 7F F0  ..fdo1..U.......
0160: FF FF 7F 66 64 6F 31 1B                           ...fdo1.        
```

#### Opcodes

```
  0: 0x0028 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0029 [0x24] CREATE_DIALOG(message_id=7593*, default_option=1*, option_flags=0*)
    → "Hold out your hand? [Yes./No.]"
  2: 0x0030 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0031 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0054
  4: 0x0039 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x003B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x003D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "kupo" with entities [LocalPlayer, LocalPlayer], work=[234*, 0*]
  7: 0x004E [0x01] GOTO 0x0061

SUBROUTINE_0061:
  8: 0x0061 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x0062 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "kupo" with entities [LocalPlayer, LocalPlayer], work=[234*, 0*]
 10: 0x0073 [0x1A] CALL_SUBROUTINE(address=0x0147)
 11: 0x0076 [0x46] CAMERA_CONTROL: Disable user control
 12: 0x0078 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 13: 0x007B [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x08)
 14: 0x0082 [0x27] REQ_SET(priority=0x10, entity_id=Henchman Moogle (ID: 17498662/0x010B0226), tag_num=0x03)
 15: 0x0089 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-176.788*, pos_z=270.621*, pos_y=25.475*, direction=351.6°*)
 16: 0x0096 [0xBA] SET_ENTITY_POSITION(entity_id=Henchman Moogle (ID: 17498662/0x010B0226), pos_x=-178.000*, pos_z=273.000*, pos_y=25.475*, direction=87.9°*)
 17: 0x00A3 [0x80] LOAD_WAIT(entity=LocalPlayer)
 18: 0x00A8 [0x80] LOAD_WAIT(entity=Henchman Moogle (ID: 17498662/0x010B0226))
 19: 0x00AD [0x1C] WAIT(15* ticks)
 20: 0x00B0 [0x4A] LocalPlayer looks at Henchman Moogle (ID: 17498662/0x010B0226)
 21: 0x00B9 [0x4A] Henchman Moogle (ID: 17498662/0x010B0226) looks at LocalPlayer
 22: 0x00C2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 23: 0x00C3 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 24: 0x00C8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 25: 0x00C9 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Henchman Moogle (ID: 17498662/0x010B0226) Render.Flags0 and Render.Flags3 conditions are met
 26: 0x00CE [0x1C] WAIT(30* ticks)
 27: 0x00D1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "g002" with entities [LocalPlayer, LocalPlayer], work=[466*, 0*]
 28: 0x00E2 [0x1A] CALL_SUBROUTINE(address=0x0126)
 29: 0x00E5 [0x2B] Henchman Moogle (ID: 17498662/0x010B0226) [7595*]:
    → "Yer lookin' for the boss, y'say? Looks like it ain't your lucky day. He just left."
 30: 0x00EC [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x00ED [0x2B] Henchman Moogle (ID: 17498662/0x010B0226) [7597*]:
    → "I mean, if the boss caught me blabbin' to everyone 'n their uncle about his favorite huntin' spot past the Sahagins' ornamented door, I'd be cruisin' for a serious bruisin'. So scram!"
 32: 0x00F4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x00F5 [0x27] REQ_SET(priority=0x10, entity_id=Henchman Moogle (ID: 17498662/0x010B0226), tag_num=0x05)
 34: 0x00FC [0x52] END_LOAD_SCHEDULER: End scheduler "g002" with entities [LocalPlayer, LocalPlayer], work=466*
 35: 0x010B [0x1A] CALL_SUBROUTINE(address=0x0147)
 36: 0x010E [0x1C] WAIT(30* ticks)
 37: 0x0111 [0x46] CAMERA_CONTROL: Restore default settings
 38: 0x0113 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 39: 0x0124 [0x21] END_EVENT
 40: 0x0125 [0x00] END_REQSTACK()

SUBROUTINE_0126:
 41: 0x0126 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 42: 0x0137 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 43: 0x0146 [0x1B] RETURN

SUBROUTINE_0147:
 44: 0x0147 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 45: 0x0158 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 46: 0x0167 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0051 [0x01] GOTO 0x0061
     0x005E [0x01] GOTO 0x0061
```
