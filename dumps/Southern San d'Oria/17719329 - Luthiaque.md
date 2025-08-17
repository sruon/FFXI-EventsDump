# 17719329 - Luthiaque

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 604 bytes                     |
| Total Events     | 7                             |
| References Count | 27                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [658](#event-658)     | 0x0001       |    262 |             62 |
| [549](#event-549)     | 0x0107       |     56 |             11 |
| [544](#event-544)     | 0x013F       |     54 |             12 |
| [550](#event-550)     | 0x0175       |     74 |             18 |
| [993](#event-993)     | 0x01BF       |      1 |              1 |
| [3526](#event-3526)   | 0x01C0       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0008      |           8 |
|       1 | 0x0014      |          20 |
|       2 | 0x20F3      |        8435 |
|       3 | 0x20F4      |        8436 |
|       4 | 0x0000      |           0 |
|       5 | 0xFFFFFFFB  |  4294967291 |
|       6 | 0x20F5      |        8437 |
|       7 | 0x001E      |          30 |
|       8 | 0x20F6      |        8438 |
|       9 | 0x0001      |           1 |
|      10 | 0x20F7      |        8439 |
|      11 | 0x2ECA      |       11978 |
|      12 | 0x0002      |           2 |
|      13 | 0x2EE9      |       12009 |
|      14 | 0x2EEA      |       12010 |
|      15 | 0x2EEB      |       12011 |
|      16 | 0x2EFC      |       12028 |
|      17 | 0x2EFD      |       12029 |
|      18 | 0x208D      |        8333 |
|      19 | 0x208E      |        8334 |
|      20 | 0x208F      |        8335 |
|      21 | 0x2090      |        8336 |
|      22 | 0x2091      |        8337 |
|      23 | 0x2092      |        8338 |
|      24 | 0x2093      |        8339 |
|      25 | 0x2094      |        8340 |
|      26 | 0x2095      |        8341 |

## String References

- **8333**: Hmm... Now where did I put it?
- **8334**: Oh, I'm sorry. I'm looking for something. Come back later.
- **8335**: I'm sorry, but that's all for today. Someone stole my dagger.
- **8336**: I'm Luthiaque. I travel hither and thither, bringing entertainment everywhere!
- **8337**: Juggling is my specialty, but not mere balls or dishes... No, I juggle daggers!
- **8338**: Did you bring me my dagger?
- **8339**: Well, did you? [Yes, I did./No, not yet.]
- **8340**: This is just the one! Thank you so much!
- **8341**: Oh...
- **8435**: Finding your way around Southern San d'Oria? You can look at my map if you'd like.
- **8436**: Look at the map? [Yes./No.]
- **8437**: Here in the center lies Victory Square. West is Pikeman's Way and Watchdog Alley, where you'll find the Tanners' Guild and Taumila's Sundries.
- **8438**: East is Cavalry Way and Squire Alley, with armor and weapons shops, and a tavern. The gate at the end leads to the housing area.
- **8439**: Is that so? Pity.
- **11978**: Ask if this person is the chick's owner? [Yes./No.]
- **12009**: You...you have my chocobo?
- **12010**: May Altana's blessings be upon you! I was teaching the little one to find his way home when I lost the poor creature.
- **12011**: You are raising a chocobo yourself, are you not? In that case, let me teach you a story I often tell my chocobo...
- **12028**: You say you have my chocobo?
- **12029**: My chocobo would never get lost. I trained him to find his way home all by himself!

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

### Event 658

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 262 bytes |
| Instructions | 62        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    38 00 80 1E F0 FF FF  7F 6F 70 66 01 80 F8 FF   8.......opf....
0010: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 02 80 23 5E 69  ......tlk0...#^i
0020: 64 6C 30 24 03 80 04 80  04 80 25 02 00 10 04 80  dl0$......%.....
0030: 00 4D 00 8D 05 80 04 80  1D 06 80 23 1C 07 80 1D  .M.........#....
0040: 08 80 23 1C 07 80 8A 1C  07 80 01 73 00 02 00 10  ..#........s....
0050: 09 80 00 73 00 66 01 80  F8 FF FF 7F F8 FF FF 7F  ...s.f..........
0060: 74 6C 6B 30 1D 0A 80 23  5E 69 64 6C 30 1C 07 80  tlk0...#^idl0...
0070: 01 73 00 03 01 10 09 80  43 00 43 01 02 03 10 04  .s......C.C.....
0080: 80 00 8C 00 03 01 10 04  80 01 05 01 42 24 0B 80  ............B$..
0090: 09 80 04 80 25 02 00 10  04 80 00 F5 00 03 01 10  ....%...........
00A0: 0C 80 43 00 43 01 02 03  10 09 80 00 DB 00 1D 0D  ..C.C...........
00B0: 80 23 66 01 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  .#f..........tlk
00C0: 30 1D 0E 80 23 66 01 80  F8 FF FF 7F F8 FF FF 7F  0...#f..........
00D0: 74 6C 6B 31 1D 0F 80 23  01 F2 00 1D 10 80 23 66  tlk1...#......#f
00E0: 01 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1D 11  ..........tlk0..
00F0: 80 23 01 05 01 02 00 10  09 80 00 05 01 03 01 10  .#..............
0100: 04 80 01 05 01 21 00                              .....!.         
```

#### Opcodes

```
  0: 0x0001 [0x38] SET_CLIENT_EVENT_MODE(mode=8*)
  1: 0x0004 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0009 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x000A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x000B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  5: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=8435*)
    → "Finding your way around Southern San d'Oria? You can look at my map if you'd like."
  6: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  8: 0x0023 [0x24] CREATE_DIALOG(message_id=8436*, default_option=0*, option_flags=0*)
    → "Look at the map? [Yes./No.]"
  9: 0x002A [0x25] WAIT_DIALOG_SELECT()
 10: 0x002B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004D
 11: 0x0033 [0x8D] OPEN_MAP_WITH_PROPERTIES(map_id=4294967291*, properties=0*)
 12: 0x0038 [0x1D] PRINT_EVENT_MESSAGE(message_id=8437*)
    → "Here in the center lies Victory Square. West is Pikeman's Way and Watchdog Alley, where you'll find the Tanners' Guild and Taumila's Sundries."
 13: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x003C [0x1C] WAIT(30* ticks)
 15: 0x003F [0x1D] PRINT_EVENT_MESSAGE(message_id=8438*)
    → "East is Cavalry Way and Squire Alley, with armor and weapons shops, and a tavern. The gate at the end leads to the housing area."
 16: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0043 [0x1C] WAIT(30* ticks)
 18: 0x0046 [0x8A] CLOSE_MAP()
 19: 0x0047 [0x1C] WAIT(30* ticks)
 20: 0x004A [0x01] GOTO 0x0073
 21: 0x004D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0073
 22: 0x0055 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 23: 0x0064 [0x1D] PRINT_EVENT_MESSAGE(message_id=8439*)
    → "Is that so? Pity."
 24: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0068 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 26: 0x006D [0x1C] WAIT(30* ticks)
 27: 0x0070 [0x01] GOTO 0x0073

SUBROUTINE_0073:
 28: 0x0073 [0x03] Work_Zone[1] = 1*
 29: 0x0078 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 30: 0x007A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 31: 0x007C [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x008C
 32: 0x0084 [0x03] Work_Zone[1] = 0*
 33: 0x0089 [0x01] GOTO 0x0105
 34: 0x008C [0x42] SET_CLI_EVENT_CANCEL_DATA()
 35: 0x008D [0x24] CREATE_DIALOG(message_id=11978*, default_option=1*, option_flags=0*)
    → "Ask if this person is the chick's owner? [Yes./No.]"
 36: 0x0094 [0x25] WAIT_DIALOG_SELECT()
 37: 0x0095 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00F5
 38: 0x009D [0x03] Work_Zone[1] = 2*
 39: 0x00A2 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 40: 0x00A4 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 41: 0x00A6 [0x02] IF !(Work_Zone[3] == 1*) GOTO 0x00DB
 42: 0x00AE [0x1D] PRINT_EVENT_MESSAGE(message_id=12009*)
    → "You...you have my chocobo?"
 43: 0x00B1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x00B2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 45: 0x00C1 [0x1D] PRINT_EVENT_MESSAGE(message_id=12010*)
    → "May Altana's blessings be upon you! I was teaching the little one to find his way home when I lost the poor creature."
 46: 0x00C4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x00C5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 48: 0x00D4 [0x1D] PRINT_EVENT_MESSAGE(message_id=12011*)
    → "You are raising a chocobo yourself, are you not? In that case, let me teach you a story I often tell my chocobo..."
 49: 0x00D7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 50: 0x00D8 [0x01] GOTO 0x00F2
 51: 0x00DB [0x1D] PRINT_EVENT_MESSAGE(message_id=12028*)
    → "You say you have my chocobo?"
 52: 0x00DE [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x00DF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 54: 0x00EE [0x1D] PRINT_EVENT_MESSAGE(message_id=12029*)
    → "My chocobo would never get lost. I trained him to find his way home all by himself!"
 55: 0x00F1 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00F2:
 56: 0x00F2 [0x01] GOTO 0x0105
 57: 0x00F5 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0105
 58: 0x00FD [0x03] Work_Zone[1] = 0*
 59: 0x0102 [0x01] GOTO 0x0105

SUBROUTINE_0105:
 60: 0x0105 [0x21] END_EVENT
 61: 0x0106 [0x00] END_REQSTACK()
```

### Event 549

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0107   |
| Data Size    | 56 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                      13  00 00 09 80 02 00 00 09         .........
0110: 80 00 2A 01 66 04 80 F8  FF FF 7F F8 FF FF 7F 74  ..*.f..........t
0120: 68 6B 31 1D 12 80 23 01  3D 01 66 04 80 F8 FF FF  hk1...#.=.f.....
0130: 7F F8 FF FF 7F 74 6C 6B  32 1D 13 80 23 21 00     .....tlk2...#!. 
```

#### Opcodes

```
  0: 0x0107 [0x13] ExtData[1]->WorkLocal[0] = rand() % 1*
  1: 0x010C [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x012A
  2: 0x0114 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=0*
  3: 0x0123 [0x1D] PRINT_EVENT_MESSAGE(message_id=8333*)
    → "Hmm... Now where did I put it?"
  4: 0x0126 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0127 [0x01] GOTO 0x013D
  6: 0x012A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=0*
  7: 0x0139 [0x1D] PRINT_EVENT_MESSAGE(message_id=8334*)
    → "Oh, I'm sorry. I'm looking for something. Come back later."
  8: 0x013C [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_013D:
  9: 0x013D [0x21] END_EVENT
 10: 0x013E [0x00] END_REQSTACK()
```

### Event 544

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013F   |
| Data Size    | 54 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                               1E                 .
0140: F0 FF FF 7F 66 04 80 F8  FF FF 7F F8 FF FF 7F 74  ....f..........t
0150: 6C 6B 31 1D 14 80 23 66  04 80 F8 FF FF 7F F8 FF  lk1...#f........
0160: FF 7F 74 6C 6B 30 1D 15  80 23 1D 16 80 23 03 01  ..tlk0...#...#..
0170: 10 09 80 21 00                                    ...!.           
```

#### Opcodes

```
  0: 0x013F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0144 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=0*
  2: 0x0153 [0x1D] PRINT_EVENT_MESSAGE(message_id=8335*)
    → "I'm sorry, but that's all for today. Someone stole my dagger."
  3: 0x0156 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0157 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
  5: 0x0166 [0x1D] PRINT_EVENT_MESSAGE(message_id=8336*)
    → "I'm Luthiaque. I travel hither and thither, bringing entertainment everywhere!"
  6: 0x0169 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x016A [0x1D] PRINT_EVENT_MESSAGE(message_id=8337*)
    → "Juggling is my specialty, but not mere balls or dishes... No, I juggle daggers!"
  8: 0x016D [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x016E [0x03] Work_Zone[1] = 1*
 10: 0x0173 [0x21] END_EVENT
 11: 0x0174 [0x00] END_REQSTACK()
```

### Event 550

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0175   |
| Data Size    | 74 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                1E F0 FF  FF 7F 66 04 80 F8 FF FF       .....f.....
0180: 7F F8 FF FF 7F 74 6C 6B  32 1D 17 80 23 24 18 80  .....tlk2...#$..
0190: 04 80 04 80 25 02 00 10  04 80 00 A9 01 1D 19 80  ....%...........
01A0: 23 03 01 10 04 80 01 BD  01 02 00 10 09 80 00 BD  #...............
01B0: 01 1D 1A 80 23 03 01 10  09 80 01 BD 01 21 00     ....#........!. 
```

#### Opcodes

```
  0: 0x0175 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x017A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=0*
  2: 0x0189 [0x1D] PRINT_EVENT_MESSAGE(message_id=8338*)
    → "Did you bring me my dagger?"
  3: 0x018C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x018D [0x24] CREATE_DIALOG(message_id=8339*, default_option=0*, option_flags=0*)
    → "Well, did you? [Yes, I did./No, not yet.]"
  5: 0x0194 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0195 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01A9
  7: 0x019D [0x1D] PRINT_EVENT_MESSAGE(message_id=8340*)
    → "This is just the one! Thank you so much!"
  8: 0x01A0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x01A1 [0x03] Work_Zone[1] = 0*
 10: 0x01A6 [0x01] GOTO 0x01BD
 11: 0x01A9 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01BD
 12: 0x01B1 [0x1D] PRINT_EVENT_MESSAGE(message_id=8341*)
    → "Oh..."
 13: 0x01B4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x01B5 [0x03] Work_Zone[1] = 1*
 15: 0x01BA [0x01] GOTO 0x01BD

SUBROUTINE_01BD:
 16: 0x01BD [0x21] END_EVENT
 17: 0x01BE [0x00] END_REQSTACK()
```

### Event 993

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01BF  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                               00                 .
```

#### Opcodes

```
  0: 0x01BF [0x00] END_REQSTACK()
```

### Event 3526

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01C0  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0: 00                                                .               
```

#### Opcodes

```
  0: 0x01C0 [0x00] END_REQSTACK()
```
