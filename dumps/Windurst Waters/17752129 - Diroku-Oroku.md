# 17752129 - Diroku-Oroku

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 772 bytes                 |
| Total Events     | 8                         |
| References Count | 18                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |     16 |              2 |
| [65535.4](#event-655354) | 0x0037       |     22 |              4 |
| [65535.5](#event-655355) | 0x004D       |      9 |              3 |
| [420](#event-420)        | 0x0056       |    506 |             89 |
| [65535.6](#event-655356) | 0x0250       |     57 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0055      |          85 |
|       1 | 0x001E      |          30 |
|       2 | 0x00C8      |         200 |
|       3 | 0x0000      |           0 |
|       4 | 0x003C      |          60 |
|       5 | 0x0013      |          19 |
|       6 | 0x008A      |         138 |
|       7 | 0x2079      |        8313 |
|       8 | 0x207A      |        8314 |
|       9 | 0x207B      |        8315 |
|      10 | 0x0001      |           1 |
|      11 | 0x207C      |        8316 |
|      12 | 0x207D      |        8317 |
|      13 | 0x207E      |        8318 |
|      14 | 0x207F      |        8319 |
|      15 | 0x2089      |        8329 |
|      16 | 0x208A      |        8330 |
|      17 | 0x208B      |        8331 |

## String References

- **8313**: Oh, so you want to know a little about magic, huh?
- **8314**: Well, you've come to the right place. We can teach you the basics...
- **8315**: Listen to their explanation? [Decline./Accept.]
- **8316**: Well then, let us explain... There are basically two types of magic...white and black.
- **8317**: White magic is predominately used for healing. It is what white mages specialize in. White magic includes healing spells such as Cure, and Poisona, which removes poison status...
- **8318**: High-level white mages can use Raise to revive fallen comrades.
- **8319**: Then there's black magic...
- **8329**: Calm down, guys... Cool it!
- **8330**: So, how about it? Do you understand more about magic now? We're currently studying the basics here at the School of Magic.
- **8331**: Actually, there is one more type of magic that is forbidden now, but I guess that doesn't concern an adventurer such as yourself. Anyway, good luck with your magic studies. Bye-bye.

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5B  00 80 F8 FF FF 7F F8 FF         [........
0030: FF 7F 74 6C 6B 31 00                              ..tlk1.         
```

#### Opcodes

```
  0: 0x0027 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=85*
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0040: 74 6C 6B 31 5E 69 64 6C  30 1C 01 80 00           tlk1^idl0....   
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0049 [0x1C] WAIT(30* ticks)
  3: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004D  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         5E 69 64               ^id
0050: 6C 30 1C 01 80 00                                 l0....          
```

#### Opcodes

```
  0: 0x004D [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0052 [0x1C] WAIT(30* ticks)
  2: 0x0055 [0x00] END_REQSTACK()
```

### Event 420

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0056    |
| Data Size    | 506 bytes |
| Instructions | 89        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   42 46  01 45 02 80 F8 FF FF 7F        BF.E......
0060: F8 FF FF 7F 66 64 6F 31  03 80 1C 04 80 38 05 80  ....fdo1.....8..
0070: 29 0B F0 FF FF 7F 34 4A  F0 FF FF 7F 41 E0 0E 01  ).....4J....A...
0080: 45 06 80 F0 FF FF 7F F0  FF FF 7F 73 30 35 38 03  E..........s058.
0090: 80 45 02 80 F8 FF FF 7F  F8 FF FF 7F 66 64 69 31  .E..........fdi1
00A0: 03 80 1E F0 FF FF 7F 6F  70 29 08 41 E0 0E 01 01  .......op).A....
00B0: 1D 07 80 23 29 08 41 E0  0E 01 02 4A 42 E0 0E 01  ...#).A....JB...
00C0: 41 E0 0E 01 6F 76 42 E0  0E 01 4A 41 E0 0E 01 42  A...ovB...JA...B
00D0: E0 0E 01 6F 76 F8 FF FF  7F 1C 01 80 4A 41 E0 0E  ...ov.......JA..
00E0: 01 43 E0 0E 01 6F 76 F8  FF FF 7F 1C 01 80 4A 41  .C...ov.......JA
00F0: E0 0E 01 F0 FF FF 7F 6F  76 F8 FF FF 7F 29 08 41  .......ov....).A
0100: E0 0E 01 01 1D 08 80 23  29 08 41 E0 0E 01 02 24  .......#).A....$
0110: 09 80 03 80 03 80 25 02  00 10 03 80 00 27 01 03  ......%......'..
0120: 01 10 03 80 01 17 02 02  00 10 0A 80 00 17 02 45  ...............E
0130: 06 80 F0 FF FF 7F F0 FF  FF 7F 73 30 36 30 03 80  ..........s060..
0140: 03 01 10 0A 80 29 08 41  E0 0E 01 01 1D 0B 80 23  .....).A.......#
0150: 29 08 41 E0 0E 01 02 29  08 41 E0 0E 01 03 1D 0C  ).A....).A......
0160: 80 23 1D 0D 80 23 29 08  41 E0 0E 01 04 1D 0E 80  .#...#).A.......
0170: 23 4A 43 E0 0E 01 42 E0  0E 01 6F 76 43 E0 0E 01  #JC...B...ovC...
0180: 45 06 80 F0 FF FF 7F F0  FF FF 7F 73 30 35 39 03  E..........s059.
0190: 80 4A F0 FF FF 7F 42 E0  0E 01 4A 41 E0 0E 01 42  .J....B...JA...B
01A0: E0 0E 01 6F 76 F8 FF FF  7F 29 0B 42 E0 0E 01 0A  ...ov....).B....
01B0: 4A 43 E0 0E 01 F0 FF FF  7F 6F 76 43 E0 0E 01 4A  JC.......ovC...J
01C0: 42 E0 0E 01 43 E0 0E 01  6F 76 42 E0 0E 01 29 0B  B...C...ovB...).
01D0: 43 E0 0E 01 0C 4A 43 E0  0E 01 42 E0 0E 01 6F 76  C....JC...B...ov
01E0: 43 E0 0E 01 29 0B 42 E0  0E 01 0B 29 08 43 E0 0E  C...).B....).C..
01F0: 01 07 1C 01 80 45 06 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0200: 73 30 36 31 03 80 29 08  42 E0 0E 01 05 29 0B 41  s061..).B....).A
0210: E0 0E 01 07 01 17 02 45  02 80 F8 FF FF 7F F8 FF  .......E........
0220: FF 7F 66 64 6F 31 03 80  1C 04 80 29 08 42 E0 0E  ..fdo1.....).B..
0230: 01 06 29 08 43 E0 0E 01  08 46 00 45 02 80 F8 FF  ..).C....F.E....
0240: FF 7F F8 FF FF 7F 66 64  69 31 03 80 20 00 21 00  ......fdi1.. .!.
```

#### Opcodes

```
  0: 0x0056 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0057 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0059 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  3: 0x006A [0x1C] WAIT(60* ticks)
  4: 0x006D [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  5: 0x0070 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x34)
  6: 0x0077 [0x4A] LocalPlayer looks at Diroku-Oroku (ID: 17752129/0x010EE041)
  7: 0x0080 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s058" with entities [LocalPlayer, LocalPlayer], work=[138*, 0*]
  8: 0x0091 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  9: 0x00A2 [0x1E] EventEntity looks at LocalPlayer and starts talking
 10: 0x00A7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x00A8 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 12: 0x00A9 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Diroku-Oroku (ID: 17752129/0x010EE041), tag_num=0x01)
 13: 0x00B0 [0x1D] PRINT_EVENT_MESSAGE(message_id=8313*)
    → "Oh, so you want to know a little about magic, huh?"
 14: 0x00B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x00B4 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Diroku-Oroku (ID: 17752129/0x010EE041), tag_num=0x02)
 16: 0x00BB [0x4A] Pakesse-Myukesse (ID: 17752130/0x010EE042) looks at Diroku-Oroku (ID: 17752129/0x010EE041)
 17: 0x00C4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 18: 0x00C5 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Pakesse-Myukesse (ID: 17752130/0x010EE042) Render.Flags0 and Render.Flags3 conditions are met
 19: 0x00CA [0x4A] Diroku-Oroku (ID: 17752129/0x010EE041) looks at Pakesse-Myukesse (ID: 17752130/0x010EE042)
 20: 0x00D3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 21: 0x00D4 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
 22: 0x00D9 [0x1C] WAIT(30* ticks)
 23: 0x00DC [0x4A] Diroku-Oroku (ID: 17752129/0x010EE041) looks at Majiji (ID: 17752131/0x010EE043)
 24: 0x00E5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 25: 0x00E6 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
 26: 0x00EB [0x1C] WAIT(30* ticks)
 27: 0x00EE [0x4A] Diroku-Oroku (ID: 17752129/0x010EE041) looks at LocalPlayer
 28: 0x00F7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 29: 0x00F8 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
 30: 0x00FD [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Diroku-Oroku (ID: 17752129/0x010EE041), tag_num=0x01)
 31: 0x0104 [0x1D] PRINT_EVENT_MESSAGE(message_id=8314*)
    → "Well, you've come to the right place. We can teach you the basics..."
 32: 0x0107 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x0108 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Diroku-Oroku (ID: 17752129/0x010EE041), tag_num=0x02)
 34: 0x010F [0x24] CREATE_DIALOG(message_id=8315*, default_option=0*, option_flags=0*)
    → "Listen to their explanation? [Decline./Accept.]"
 35: 0x0116 [0x25] WAIT_DIALOG_SELECT()
 36: 0x0117 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0127
 37: 0x011F [0x03] Work_Zone[1] = 0*
 38: 0x0124 [0x01] GOTO 0x0217
 39: 0x0127 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0217
 40: 0x012F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s060" with entities [LocalPlayer, LocalPlayer], work=[138*, 0*]
 41: 0x0140 [0x03] Work_Zone[1] = 1*
 42: 0x0145 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Diroku-Oroku (ID: 17752129/0x010EE041), tag_num=0x01)
 43: 0x014C [0x1D] PRINT_EVENT_MESSAGE(message_id=8316*)
    → "Well then, let us explain... There are basically two types of magic...white and black."
 44: 0x014F [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x0150 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Diroku-Oroku (ID: 17752129/0x010EE041), tag_num=0x02)
 46: 0x0157 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Diroku-Oroku (ID: 17752129/0x010EE041), tag_num=0x03)
 47: 0x015E [0x1D] PRINT_EVENT_MESSAGE(message_id=8317*)
    → "White magic is predominately used for healing. It is what white mages specialize in. White magic includes healing spells such as Cure, and Poisona, which removes poison status..."
 48: 0x0161 [0x23] WAIT_FOR_DIALOG_INTERACTION
 49: 0x0162 [0x1D] PRINT_EVENT_MESSAGE(message_id=8318*)
    → "High-level white mages can use Raise to revive fallen comrades."
 50: 0x0165 [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x0166 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Diroku-Oroku (ID: 17752129/0x010EE041), tag_num=0x04)
 52: 0x016D [0x1D] PRINT_EVENT_MESSAGE(message_id=8319*)
    → "Then there's black magic..."
 53: 0x0170 [0x23] WAIT_FOR_DIALOG_INTERACTION
 54: 0x0171 [0x4A] Majiji (ID: 17752131/0x010EE043) looks at Pakesse-Myukesse (ID: 17752130/0x010EE042)
 55: 0x017A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 56: 0x017B [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Majiji (ID: 17752131/0x010EE043) Render.Flags0 and Render.Flags3 conditions are met
 57: 0x0180 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s059" with entities [LocalPlayer, LocalPlayer], work=[138*, 0*]
 58: 0x0191 [0x4A] LocalPlayer looks at Pakesse-Myukesse (ID: 17752130/0x010EE042)
 59: 0x019A [0x4A] Diroku-Oroku (ID: 17752129/0x010EE041) looks at Pakesse-Myukesse (ID: 17752130/0x010EE042)
 60: 0x01A3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 61: 0x01A4 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
 62: 0x01A9 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pakesse-Myukesse (ID: 17752130/0x010EE042), tag_num=0x0A)
 63: 0x01B0 [0x4A] Majiji (ID: 17752131/0x010EE043) looks at LocalPlayer
 64: 0x01B9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 65: 0x01BA [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Majiji (ID: 17752131/0x010EE043) Render.Flags0 and Render.Flags3 conditions are met
 66: 0x01BF [0x4A] Pakesse-Myukesse (ID: 17752130/0x010EE042) looks at Majiji (ID: 17752131/0x010EE043)
 67: 0x01C8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 68: 0x01C9 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Pakesse-Myukesse (ID: 17752130/0x010EE042) Render.Flags0 and Render.Flags3 conditions are met
 69: 0x01CE [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Majiji (ID: 17752131/0x010EE043), tag_num=0x0C)
 70: 0x01D5 [0x4A] Majiji (ID: 17752131/0x010EE043) looks at Pakesse-Myukesse (ID: 17752130/0x010EE042)
 71: 0x01DE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 72: 0x01DF [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Majiji (ID: 17752131/0x010EE043) Render.Flags0 and Render.Flags3 conditions are met
 73: 0x01E4 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pakesse-Myukesse (ID: 17752130/0x010EE042), tag_num=0x0B)
 74: 0x01EB [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Majiji (ID: 17752131/0x010EE043), tag_num=0x07)
 75: 0x01F2 [0x1C] WAIT(30* ticks)
 76: 0x01F5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s061" with entities [LocalPlayer, LocalPlayer], work=[138*, 0*]
 77: 0x0206 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pakesse-Myukesse (ID: 17752130/0x010EE042), tag_num=0x05)
 78: 0x020D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Diroku-Oroku (ID: 17752129/0x010EE041), tag_num=0x07)
 79: 0x0214 [0x01] GOTO 0x0217

SUBROUTINE_0217:
 80: 0x0217 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 81: 0x0228 [0x1C] WAIT(60* ticks)
 82: 0x022B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pakesse-Myukesse (ID: 17752130/0x010EE042), tag_num=0x06)
 83: 0x0232 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Majiji (ID: 17752131/0x010EE043), tag_num=0x08)
 84: 0x0239 [0x46] CAMERA_CONTROL: Restore default settings
 85: 0x023B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 86: 0x024C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 87: 0x024E [0x21] END_EVENT
 88: 0x024F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0250   |
| Data Size    | 57 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0250: 29 08 41 E0 0E 01 01 1D  0F 80 23 29 08 41 E0 0E  ).A.......#).A..
0260: 01 02 1E F0 FF FF 7F 6F  70 4A F0 FF FF 7F 41 E0  .......opJ....A.
0270: 0E 01 29 08 41 E0 0E 01  01 1D 10 80 23 1D 11 80  ..).A.......#...
0280: 23 29 08 41 E0 0E 01 02  00                       #).A.....       
```

#### Opcodes

```
  0: 0x0250 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Diroku-Oroku (ID: 17752129/0x010EE041), tag_num=0x01)
  1: 0x0257 [0x1D] PRINT_EVENT_MESSAGE(message_id=8329*)
    → "Calm down, guys... Cool it!"
  2: 0x025A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x025B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Diroku-Oroku (ID: 17752129/0x010EE041), tag_num=0x02)
  4: 0x0262 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0267 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0268 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0269 [0x4A] LocalPlayer looks at Diroku-Oroku (ID: 17752129/0x010EE041)
  8: 0x0272 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Diroku-Oroku (ID: 17752129/0x010EE041), tag_num=0x01)
  9: 0x0279 [0x1D] PRINT_EVENT_MESSAGE(message_id=8330*)
    → "So, how about it? Do you understand more about magic now? We're currently studying the basics here at the School of Magic."
 10: 0x027C [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x027D [0x1D] PRINT_EVENT_MESSAGE(message_id=8331*)
    → "Actually, there is one more type of magic that is forbidden now, but I guess that doesn't concern an adventurer such as yourself. Anyway, good luck with your magic studies. Bye-bye."
 12: 0x0280 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0281 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Diroku-Oroku (ID: 17752129/0x010EE041), tag_num=0x02)
 14: 0x0288 [0x00] END_REQSTACK()
```
