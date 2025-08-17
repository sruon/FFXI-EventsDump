# 16822497 - Brakobrik

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Oldton Movalpolos (ID: 11) |
| Block Size       | 660 bytes                  |
| Total Events     | 16                         |
| References Count | 42                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [2](#event-2)            | 0x0001       |     67 |             22 |
| [3](#event-3)            | 0x0044       |     19 |             10 |
| [4](#event-4)            | 0x0057       |    222 |             66 |
| [6](#event-6)            | 0x0135       |      1 |              1 |
| [65535.1](#event-655351) | 0x0136       |     10 |              2 |
| [65535.2](#event-655352) | 0x0140       |     15 |              5 |
| [65535.3](#event-655353) | 0x014F       |     15 |              5 |
| [65535.4](#event-655354) | 0x015E       |     15 |              5 |
| [57](#event-57)          | 0x016D       |      1 |              1 |
| [65535.5](#event-655355) | 0x016E       |     10 |              2 |
| [65535.6](#event-655356) | 0x0178       |     29 |              7 |
| [67](#event-67)          | 0x0195       |      1 |              1 |
| [69](#event-69)          | 0x0196       |      1 |              1 |
| [70](#event-70)          | 0x0197       |      1 |              1 |
| [72](#event-72)          | 0x0198       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E2D      |        7725 |
|       1 | 0x1E2E      |        7726 |
|       2 | 0x1E2F      |        7727 |
|       3 | 0x0000      |           0 |
|       4 | 0x0001      |           1 |
|       5 | 0x0002      |           2 |
|       6 | 0x1E30      |        7728 |
|       7 | 0x1E31      |        7729 |
|       8 | 0x1E32      |        7730 |
|       9 | 0x1E33      |        7731 |
|      10 | 0x1E34      |        7732 |
|      11 | 0x1E35      |        7733 |
|      12 | 0x1E36      |        7734 |
|      13 | 0x0006      |           6 |
|      14 | 0x1E39      |        7737 |
|      15 | 0x1E37      |        7735 |
|      16 | 0x0005      |           5 |
|      17 | 0x1E3B      |        7739 |
|      18 | 0x1E3C      |        7740 |
|      19 | 0x1E38      |        7736 |
|      20 | 0x0003      |           3 |
|      21 | 0x0004      |           4 |
|      22 | 0x28CAF     |      167087 |
|      23 | 0xFFFF5170  |  4294922608 |
|      24 | 0x36AC      |       13996 |
|      25 | 0x08C4      |        2244 |
|      26 | 0x000D      |          13 |
|      27 | 0x27238     |      160312 |
|      28 | 0xFFFF5943  |  4294924611 |
|      29 | 0x369C      |       13980 |
|      30 | 0x2763D     |      161341 |
|      31 | 0xFFFF5781  |  4294924161 |
|      32 | 0x2863D     |      165437 |
|      33 | 0xFFFF4F63  |  4294922083 |
|      34 | 0x36AF      |       13999 |
|      35 | 0xFFF8E553  |  4294501715 |
|      36 | 0x7823      |       30755 |
|      37 | 0x1DC8F     |      121999 |
|      38 | 0x059A      |        1434 |
|      39 | 0x0080      |         128 |
|      40 | 0xFFF8DFEA  |  4294500330 |
|      41 | 0x72D6      |       29398 |

## String References

- **7725**: This place being for garbage. No fires. No bombs.
- **7726**: Stupid people. You don't getting what I'm saying.
- **7727**: How do you respond? [Huh?/I getting you.]
- **7728**: Do you really getting me? Okay. Killing bombs. Bringing $1.
- **7729**: Five is being too many. No more than four. Can't having fires around here.
- **7730**: Killing bombs. Bringing $1.
- **7731**: You bringing it! This being perfect! You not being so stupid after all.
- **7732**: Now what? You wanting something from me? I guess I should giving you a reward.
- **7733**: You can having this. Looking like garbage, but it being important to us Moblins.
- **7734**: Take it? [I'll take it./No thanks.]
- **7735**: Good, good. You being smart. Very, very clever.
- **7736**: Taking it, taking it. You being very stupid. You saying stupid things.
- **7737**: Stupid people. You already having one. You don't needing two of the same thing.
- **7739**: ... You figuring it out?
- **7740**: Okay, okay. Don't being mad. You can having my treasure. It being very shiny. Very pretty.

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

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 67 bytes |
| Instructions | 22       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 1D 01 80 23   .....op...#...#
0010: 24 02 80 03 80 03 80 25  02 00 10 03 80 00 28 00  $......%......(.
0020: 03 01 10 04 80 01 40 00  02 00 10 04 80 00 40 00  ......@.......@.
0030: 03 01 10 05 80 1D 06 80  23 1D 07 80 23 01 40 00  ........#...#.@.
0040: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7725*)
    → "This place being for garbage. No fires. No bombs."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x1D] PRINT_EVENT_MESSAGE(message_id=7726*)
    → "Stupid people. You don't getting what I'm saying."
  6: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0010 [0x24] CREATE_DIALOG(message_id=7727*, default_option=0*, option_flags=0*)
    → "How do you respond? [Huh?/I getting you.]"
  8: 0x0017 [0x25] WAIT_DIALOG_SELECT()
  9: 0x0018 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0028
 10: 0x0020 [0x03] Work_Zone[1] = 1*
 11: 0x0025 [0x01] GOTO 0x0040
 12: 0x0028 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0040
 13: 0x0030 [0x03] Work_Zone[1] = 2*
 14: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=7728*)
    → "Do you really getting me? Okay. Killing bombs. Bringing $1."
 15: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=7729*)
    → "Five is being too many. No more than four. Can't having fires around here."
 17: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x003D [0x01] GOTO 0x0040

SUBROUTINE_0040:
 19: 0x0040 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 20: 0x0042 [0x21] END_EVENT
 21: 0x0043 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             1E F0 FF FF  7F 6F 70 1D 08 80 23 1D      .....op...#.
0050: 07 80 23 20 00 21 00                              ..# .!.         
```

#### Opcodes

```
  0: 0x0044 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0049 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x004A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=7730*)
    → "Killing bombs. Bringing $1."
  4: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=7729*)
    → "Five is being too many. No more than four. Can't having fires around here."
  6: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0053 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0055 [0x21] END_EVENT
  9: 0x0056 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0057    |
| Data Size    | 222 bytes |
| Instructions | 52        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      42  1E F0 FF FF 7F 6F 70 1D         B.....op.
0060: 09 80 23 1D 0A 80 23 1D  0B 80 23 24 0C 80 03 80  ..#...#...#$....
0070: 03 80 25 02 00 10 03 80  00 9A 00 02 06 10 04 80  ..%.............
0080: 00 93 00 03 01 10 0D 80  1D 0E 80 23 20 00 21 00  ...........# .!.
0090: 01 97 00 1D 0F 80 23 01  F1 00 02 00 10 04 80 00  ......#.........
00A0: F1 00 02 05 10 04 80 00  D2 00 02 06 10 04 80 00  ................
00B0: B5 00 01 BE 00 03 01 10  04 10 43 00 43 01 03 01  ..........C.C...
00C0: 10 10 80 1D 11 80 23 1D  12 80 23 20 00 21 00 01  ......#...# .!..
00D0: EE 00 02 06 10 04 80 00  EA 00 03 01 10 0D 80 1D  ................
00E0: 0E 80 23 20 00 21 00 01  EE 00 1D 13 80 23 01 F1  ..# .!.......#..
00F0: 00 02 04 10 04 80 80 01  01 03 01 10 04 80 01 31  ...............1
0100: 01 02 04 10 05 80 80 11  01 03 01 10 05 80 01 31  ...............1
0110: 01 02 04 10 14 80 80 21  01 03 01 10 14 80 01 31  .......!.......1
0120: 01 02 04 10 15 80 80 31  01 03 01 10 15 80 01 31  .......1.......1
0130: 01 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0057 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0058 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x005D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x005E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x005F [0x1D] PRINT_EVENT_MESSAGE(message_id=7731*)
    → "You bringing it! This being perfect! You not being so stupid after all."
  5: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0063 [0x1D] PRINT_EVENT_MESSAGE(message_id=7732*)
    → "Now what? You wanting something from me? I guess I should giving you a reward."
  7: 0x0066 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=7733*)
    → "You can having this. Looking like garbage, but it being important to us Moblins."
  9: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x006B [0x24] CREATE_DIALOG(message_id=7734*, default_option=0*, option_flags=0*)
    → "Take it? [I'll take it./No thanks.]"
 11: 0x0072 [0x25] WAIT_DIALOG_SELECT()
 12: 0x0073 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x009A
 13: 0x007B [0x02] IF !(Work_Zone[6] == 1*) GOTO 0x0093
 14: 0x0083 [0x03] Work_Zone[1] = 6*
 15: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=7737*)
    → "Stupid people. You already having one. You don't needing two of the same thing."
 16: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x008C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 18: 0x008E [0x21] END_EVENT
 19: 0x008F [0x00] END_REQSTACK()

SUBROUTINE_0097:
 20: 0x0097 [0x01] GOTO 0x00F1
 21: 0x009A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00F1
 22: 0x00A2 [0x02] IF !(Work_Zone[5] == 1*) GOTO 0x00D2
 23: 0x00AA [0x02] IF !(Work_Zone[6] == 1*) GOTO 0x00B5
 24: 0x00B2 [0x01] GOTO 0x00BE
 25: 0x00B5 [0x03] Work_Zone[1] = Work_Zone[4]
 26: 0x00BA [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 27: 0x00BC [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)

SUBROUTINE_00BE:
 28: 0x00BE [0x03] Work_Zone[1] = 5*
 29: 0x00C3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7739*)
    → "... You figuring it out?"
 30: 0x00C6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x00C7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7740*)
    → "Okay, okay. Don't being mad. You can having my treasure. It being very shiny. Very pretty."
 32: 0x00CA [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x00CB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 34: 0x00CD [0x21] END_EVENT
 35: 0x00CE [0x00] END_REQSTACK()

SUBROUTINE_00EE:
 36: 0x00EE [0x01] GOTO 0x00F1

SUBROUTINE_00F1:
 37: 0x00F1 [0x02] IF !(Work_Zone[4] == 1*) GOTO 0x0101
 38: 0x00F9 [0x03] Work_Zone[1] = 1*
 39: 0x00FE [0x01] GOTO 0x0131
 40: 0x0101 [0x02] IF !(Work_Zone[4] == 2*) GOTO 0x0111
 41: 0x0109 [0x03] Work_Zone[1] = 2*
 42: 0x010E [0x01] GOTO 0x0131
 43: 0x0111 [0x02] IF !(Work_Zone[4] == 3*) GOTO 0x0121
 44: 0x0119 [0x03] Work_Zone[1] = 3*
 45: 0x011E [0x01] GOTO 0x0131
 46: 0x0121 [0x02] IF !(Work_Zone[4] == 4*) GOTO 0x0131
 47: 0x0129 [0x03] Work_Zone[1] = 4*
 48: 0x012E [0x01] GOTO 0x0131

SUBROUTINE_0131:
 49: 0x0131 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 50: 0x0133 [0x21] END_EVENT
 51: 0x0134 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0090 [0x01] GOTO 0x0097
# Dead code (unreachable instructions):
     0x00CF [0x01] GOTO 0x00EE
     0x00E7 [0x01] GOTO 0x00EE
```

### Event 6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0135  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                00                                      .          
```

#### Opcodes

```
  0: 0x0135 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0136   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                   37 16  80 17 80 18 80 19 80 00        7.........
```

#### Opcodes

```
  0: 0x0136 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=167.087*, z=-44.688*, y=13.996*, direction=197.2°*
  1: 0x013F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0140   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140: 32 1A 80 1F 00 1B 80 1C  80 1D 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0140 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0143 [0x1F] MOVE_ENTITY: EventEntity moves to X=160.312*, Z=-42.685*, Y=13.980*
  2: 0x014B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x014D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x014E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                               32                 2
0150: 1A 80 1F 00 1E 80 1F 80  1D 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x014F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0152 [0x1F] MOVE_ENTITY: EventEntity moves to X=161.341*, Z=-43.135*, Y=13.980*
  2: 0x015A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x015C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x015D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015E   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                            32 1A                2.
0160: 80 1F 00 20 80 21 80 22  80 1F 01 6F 00           ... .!."...o.   
```

#### Opcodes

```
  0: 0x015E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0161 [0x1F] MOVE_ENTITY: EventEntity moves to X=165.437*, Z=-45.213*, Y=13.999*
  2: 0x0169 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x016B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x016C [0x00] END_REQSTACK()
```

### Event 57

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x016D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                         00                     .  
```

#### Opcodes

```
  0: 0x016D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                            37 23                7#
0170: 80 24 80 25 80 26 80 00                           .$.%.&..        
```

#### Opcodes

```
  0: 0x016E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-465.581*, z=30.755*, y=121.999*, direction=126.0°*
  1: 0x0177 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0178   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                          32 1A 80 6C F8 FF FF 7F          2..l....
0180: 27 80 04 80 1F 00 28 80  29 80 25 80 1F 01 6F 1E  '.....(.).%...o.
0190: 08 B1 00 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0178 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x017B [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  2: 0x0184 [0x1F] MOVE_ENTITY: EventEntity moves to X=-466.966*, Z=29.398*, Y=121.999*
  3: 0x018C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x018E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x018F [0x1E] EventEntity looks at Jabbos (ID: 16822536/0x0100B108) and starts talking
  6: 0x0194 [0x00] END_REQSTACK()
```

### Event 67

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0195  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                00                                      .          
```

#### Opcodes

```
  0: 0x0195 [0x00] END_REQSTACK()
```

### Event 69

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0196  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                   00                                    .         
```

#### Opcodes

```
  0: 0x0196 [0x00] END_REQSTACK()
```

### Event 70

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0197  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                      00                                  .        
```

#### Opcodes

```
  0: 0x0197 [0x00] END_REQSTACK()
```

### Event 72

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0198  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                          00                               .       
```

#### Opcodes

```
  0: 0x0198 [0x00] END_REQSTACK()
```
