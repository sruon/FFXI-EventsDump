# 17826122 - Polished Pebble

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 1008 bytes                |
| Total Events     | 15                        |
| References Count | 45                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [174](#event-174)          | 0x0001       |     28 |             10 |
| [173](#event-173)          | 0x001D       |    361 |             63 |
| [5201](#event-5201)        | 0x0186       |     28 |             10 |
| [5200](#event-5200)        | 0x01A2       |      7 |              2 |
| [65535.1](#event-655351)   | 0x01A9       |     44 |             10 |
| [65535.2](#event-655352)   | 0x01D5       |     34 |              8 |
| [65535.3](#event-655353)   | 0x01F7       |     33 |              3 |
| [65535.4](#event-655354)   | 0x0218       |     33 |              3 |
| [65535.5](#event-655355)   | 0x0239       |     33 |              3 |
| [65535.6](#event-655356)   | 0x025A       |     33 |              3 |
| [65535.7](#event-655357)   | 0x027B       |     33 |              3 |
| [65535.8](#event-655358)   | 0x029C       |     33 |              3 |
| [65535.9](#event-655359)   | 0x02BD       |     33 |              3 |
| [65535.10](#event-6553510) | 0x02DE       |     16 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2DAA      |       11690 |
|       1 | 0x001A      |          26 |
|       2 | 0x2DA4      |       11684 |
|       3 | 0x003C      |          60 |
|       4 | 0x0045      |          69 |
|       5 | 0x2DA5      |       11685 |
|       6 | 0x2DA6      |       11686 |
|       7 | 0x00C8      |         200 |
|       8 | 0x0000      |           0 |
|       9 | 0x01E0      |         480 |
|      10 | 0x0050      |          80 |
|      11 | 0x188DF     |      100575 |
|      12 | 0xFFFEED4C  |  4294896972 |
|      13 | 0xFFFFFD77  |  4294966647 |
|      14 | 0x19B58     |      105304 |
|      15 | 0xFFFED157  |  4294889815 |
|      16 | 0x18A6B     |      100971 |
|      17 | 0xFFFEC257  |  4294885975 |
|      18 | 0xFFFFFD76  |  4294966646 |
|      19 | 0x171B6     |       94646 |
|      20 | 0xFFFEC55C  |  4294886748 |
|      21 | 0x002D      |          45 |
|      22 | 0x0265      |         613 |
|      23 | 0x007F      |         127 |
|      24 | 0x012C      |         300 |
|      25 | 0x19E3F     |      106047 |
|      26 | 0xFFFECCDF  |  4294888671 |
|      27 | 0x1847F     |       99455 |
|      28 | 0xFFFEED5C  |  4294896988 |
|      29 | 0x17C21     |       97313 |
|      30 | 0xFFFEEA68  |  4294896232 |
|      31 | 0x000F      |          15 |
|      32 | 0x0083      |         131 |
|      33 | 0x2DA7      |       11687 |
|      34 | 0x2DA8      |       11688 |
|      35 | 0x0016      |          22 |
|      36 | 0x2DA9      |       11689 |
|      37 | 0x001E      |          30 |
|      38 | 0x2EF8      |       12024 |
|      39 | 0x00D1      |         209 |
|      40 | 0x0053      |          83 |
|      41 | 0x0060      |          96 |
|      42 | 0x0064      |         100 |
|      43 | 0x0018      |          24 |
|      44 | 0x006E      |         110 |

## String References

- **11684**: Yeesh! This looks to be quite the fixer-upper.
- **11685**: I'll see what I can do. I don't think I'll have any problems with it, but you never know.
- **11686**: Wait here, I'll be right back.
- **11687**: Here you go.
- **11688**: Sorry, but this is the best I could do. All that rust proved a bit much for me.
- **11689**: I guess you could always hang it in your Mog House or something. At least I'm not going to charge you for not fixing it.
- **11690**: Some of us at the Inventors' Coalition like to say that our craft is realizing people's dreams. I'm a little more direct, though. I just say I fix stuff up.
- **12024**: Treat your tools with the proper respect, and they'll serve you well for years to come.

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

### Event 174

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 28 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  4A F0 FF FF 7F F8 FF FF   .....opJ.......
0010: 7F 6F 76 F0 FF FF 7F 1D  00 80 23 21 00           .ov.......#!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x4A] LocalPlayer looks at EventEntity
  4: 0x0011 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0012 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
  6: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=11690*)
    → "Some of us at the Inventors' Coalition like to say that our craft is realizing people's dreams. I'm a little more direct, though. I just say I fix stuff up."
  7: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001B [0x21] END_EVENT
  9: 0x001C [0x00] END_REQSTACK()
```

### Event 173

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x001D    |
| Data Size    | 361 bytes |
| Instructions | 63        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         42 1E F0               B..
0020: FF FF 7F 6F 70 4A F0 FF  FF 7F F8 FF FF 7F 6F 76  ...opJ........ov
0030: F0 FF FF 7F 6E F8 FF FF  7F 01 80 99 F8 FF FF 7F  ....n...........
0040: 1D 02 80 23 1C 03 80 66  04 80 F8 FF FF 7F F8 FF  ...#...f........
0050: FF 7F 74 68 6B 31 1D 05  80 23 53 F8 FF FF 7F F8  ..thk1...#S.....
0060: FF FF 7F 74 68 6B 31 66  04 80 F8 FF FF 7F F8 FF  ...thk1f........
0070: FF 7F 74 68 6B 32 1D 06  80 23 53 F8 FF FF 7F F8  ..thk2...#S.....
0080: FF FF 7F 74 68 6B 32 45  07 80 F0 FF FF 7F F0 FF  ...thk2E........
0090: FF 7F 66 64 6F 31 08 80  55 07 80 F0 FF FF 7F F0  ..fdo1..U.......
00A0: FF FF 7F 66 64 6F 31 5D  08 80 09 80 32 0A 80 1F  ...fdo1]....2...
00B0: 00 0B 80 0C 80 0D 80 1F  01 1F 00 0E 80 0F 80 0D  ................
00C0: 80 1F 01 1F 00 10 80 11  80 12 80 1F 01 1F 00 13  ................
00D0: 80 14 80 12 80 1F 01 1C  15 80 45 16 80 F8 FF FF  ..........E.....
00E0: 7F F8 FF FF 7F 73 30 36  32 08 80 55 16 80 F8 FF  .....s062..U....
00F0: FF 7F F8 FF FF 7F 73 30  36 32 1C 15 80 5D 17 80  ......s062...]..
0100: 18 80 32 0A 80 1F 00 19  80 1A 80 12 80 1F 01 1F  ..2.............
0110: 00 1B 80 1C 80 0D 80 1F  01 1F 00 1D 80 1E 80 0D  ................
0120: 80 1F 01 1E F0 FF FF 7F  6F 70 55 16 80 F8 FF FF  ........opU.....
0130: 7F F8 FF FF 7F 73 30 36  32 1C 1F 80 45 07 80 F0  .....s062...E...
0140: FF FF 7F F0 FF FF 7F 66  64 69 31 08 80 66 20 80  .......fdi1..f .
0150: F8 FF FF 7F F8 FF FF 7F  70 61 73 30 1D 21 80 23  ........pas0.!.#
0160: 53 F8 FF FF 7F F8 FF FF  7F 70 61 73 30 1D 22 80  S........pas0.".
0170: 23 6E F8 FF FF 7F 23 80  99 F8 FF FF 7F 1D 24 80  #n....#.......$.
0180: 23 1C 25 80 21 00                                 #.%.!.          
```

#### Opcodes

```
  0: 0x001D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x001E [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0023 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0024 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0025 [0x4A] LocalPlayer looks at EventEntity
  5: 0x002E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x002F [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
  7: 0x0034 [0x6E] EventEntity uses emote 26*
  8: 0x003B [0x99] Wait for EventEntity animation to complete
  9: 0x0040 [0x1D] PRINT_EVENT_MESSAGE(message_id=11684*)
    → "Yeesh! This looks to be quite the fixer-upper."
 10: 0x0043 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0044 [0x1C] WAIT(60* ticks)
 12: 0x0047 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=69*
 13: 0x0056 [0x1D] PRINT_EVENT_MESSAGE(message_id=11685*)
    → "I'll see what I can do. I don't think I'll have any problems with it, but you never know."
 14: 0x0059 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x005A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
 16: 0x0067 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=69*
 17: 0x0076 [0x1D] PRINT_EVENT_MESSAGE(message_id=11686*)
    → "Wait here, I'll be right back."
 18: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x007A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
 20: 0x0087 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 21: 0x0098 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 22: 0x00A7 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=480*)
 23: 0x00AC [0x32] ExtData[1]->MainSpeed = 80* * 0.1
 24: 0x00AF [0x1F] MOVE_ENTITY: EventEntity moves to X=100.575*, Z=-70.324*, Y=-0.649*
 25: 0x00B7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 26: 0x00B9 [0x1F] MOVE_ENTITY: EventEntity moves to X=105.304*, Z=-77.481*, Y=-0.649*
 27: 0x00C1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 28: 0x00C3 [0x1F] MOVE_ENTITY: EventEntity moves to X=100.971*, Z=-81.321*, Y=-0.650*
 29: 0x00CB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 30: 0x00CD [0x1F] MOVE_ENTITY: EventEntity moves to X=94.646*, Z=-80.548*, Y=-0.650*
 31: 0x00D5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 32: 0x00D7 [0x1C] WAIT(45* ticks)
 33: 0x00DA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s062" with entities [EventEntity, EventEntity], work=[613*, 0*]
 34: 0x00EB [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s062" with entities [EventEntity, EventEntity], work=613*
 35: 0x00FA [0x1C] WAIT(45* ticks)
 36: 0x00FD [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=300*)
 37: 0x0102 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
 38: 0x0105 [0x1F] MOVE_ENTITY: EventEntity moves to X=106.047*, Z=-78.625*, Y=-0.650*
 39: 0x010D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 40: 0x010F [0x1F] MOVE_ENTITY: EventEntity moves to X=99.455*, Z=-70.308*, Y=-0.649*
 41: 0x0117 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 42: 0x0119 [0x1F] MOVE_ENTITY: EventEntity moves to X=97.313*, Z=-71.064*, Y=-0.649*
 43: 0x0121 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 44: 0x0123 [0x1E] EventEntity looks at LocalPlayer and starts talking
 45: 0x0128 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 46: 0x0129 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 47: 0x012A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s062" with entities [EventEntity, EventEntity], work=613*
 48: 0x0139 [0x1C] WAIT(15* ticks)
 49: 0x013C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 50: 0x014D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=131*
 51: 0x015C [0x1D] PRINT_EVENT_MESSAGE(message_id=11687*)
    → "Here you go."
 52: 0x015F [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x0160 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 54: 0x016D [0x1D] PRINT_EVENT_MESSAGE(message_id=11688*)
    → "Sorry, but this is the best I could do. All that rust proved a bit much for me."
 55: 0x0170 [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x0171 [0x6E] EventEntity uses emote 22*
 57: 0x0178 [0x99] Wait for EventEntity animation to complete
 58: 0x017D [0x1D] PRINT_EVENT_MESSAGE(message_id=11689*)
    → "I guess you could always hang it in your Mog House or something. At least I'm not going to charge you for not fixing it."
 59: 0x0180 [0x23] WAIT_FOR_DIALOG_INTERACTION
 60: 0x0181 [0x1C] WAIT(30* ticks)
 61: 0x0184 [0x21] END_EVENT
 62: 0x0185 [0x00] END_REQSTACK()
```

### Event 5201

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0186   |
| Data Size    | 28 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                   1E F0  FF FF 7F 6F 70 4A F0 FF        .....opJ..
0190: FF 7F F8 FF FF 7F 6F 76  F0 FF FF 7F 1D 26 80 23  ......ov.....&.#
01A0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0186 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x018B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x018C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x018D [0x4A] LocalPlayer looks at EventEntity
  4: 0x0196 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0197 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
  6: 0x019C [0x1D] PRINT_EVENT_MESSAGE(message_id=12024*)
    → "Treat your tools with the proper respect, and they'll serve you well for years to come."
  7: 0x019F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x01A0 [0x21] END_EVENT
  9: 0x01A1 [0x00] END_REQSTACK()
```

### Event 5200

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01A2  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x01A2 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x01A8 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A9   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                             32 0A 80 1F 00 0B 80           2......
01B0: 0C 80 0D 80 1F 01 1F 00  0E 80 0F 80 0D 80 1F 01  ................
01C0: 1F 00 10 80 11 80 12 80  1F 01 1F 00 13 80 14 80  ................
01D0: 12 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x01A9 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x01AC [0x1F] MOVE_ENTITY: EventEntity moves to X=100.575*, Z=-70.324*, Y=-0.649*
  2: 0x01B4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01B6 [0x1F] MOVE_ENTITY: EventEntity moves to X=105.304*, Z=-77.481*, Y=-0.649*
  4: 0x01BE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x01C0 [0x1F] MOVE_ENTITY: EventEntity moves to X=100.971*, Z=-81.321*, Y=-0.650*
  6: 0x01C8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x01CA [0x1F] MOVE_ENTITY: EventEntity moves to X=94.646*, Z=-80.548*, Y=-0.650*
  8: 0x01D2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x01D4 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D5   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                32 0A 80  1F 00 19 80 1A 80 12 80       2..........
01E0: 1F 01 1F 00 1B 80 1C 80  0D 80 1F 01 1F 00 1D 80  ................
01F0: 1E 80 0D 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x01D5 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x01D8 [0x1F] MOVE_ENTITY: EventEntity moves to X=106.047*, Z=-78.625*, Y=-0.650*
  2: 0x01E0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01E2 [0x1F] MOVE_ENTITY: EventEntity moves to X=99.455*, Z=-70.308*, Y=-0.649*
  4: 0x01EA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x01EC [0x1F] MOVE_ENTITY: EventEntity moves to X=97.313*, Z=-71.064*, Y=-0.649*
  6: 0x01F4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x01F6 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01F7   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                      5F  06 20 80 F8 FF FF 7F F8         _. ......
0200: FF FF 7F 70 61 73 30 07  80 5F 07 F8 FF FF 7F F8  ...pas0.._......
0210: FF FF 7F 70 61 73 30 00                           ...pas0.        
```

#### Opcodes

```
  0: 0x01F7 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=131*, entity1=EventEntity, entity2=EventEntity, string="pas0", extra=200*)
  1: 0x0209 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0217 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0218   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                          5F 06 27 80 F8 FF FF 7F          _.'.....
0220: F8 FF FF 7F 74 6C 6B 30  28 80 5F 07 F8 FF FF 7F  ....tlk0(._.....
0230: F8 FF FF 7F 74 6C 6B 30  00                       ....tlk0.       
```

#### Opcodes

```
  0: 0x0218 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=209*, entity1=EventEntity, entity2=EventEntity, string="tlk0", extra=83*)
  1: 0x022A [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0238 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0239   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:                             5F 06 27 80 F8 FF FF           _.'....
0240: 7F F8 FF FF 7F 74 6C 6B  31 29 80 5F 07 F8 FF FF  .....tlk1)._....
0250: 7F F8 FF FF 7F 74 6C 6B  31 00                    .....tlk1.      
```

#### Opcodes

```
  0: 0x0239 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=209*, entity1=EventEntity, entity2=EventEntity, string="tlk1", extra=96*)
  1: 0x024B [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0259 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x025A   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0250:                                5F 06 04 80 F8 FF            _.....
0260: FF 7F F8 FF FF 7F 74 6C  6B 30 2A 80 5F 07 F8 FF  ......tlk0*._...
0270: FF 7F F8 FF FF 7F 74 6C  6B 30 00                 ......tlk0.     
```

#### Opcodes

```
  0: 0x025A [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=69*, entity1=EventEntity, entity2=EventEntity, string="tlk0", extra=100*)
  1: 0x026C [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x027A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x027B   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:                                   5F 06 04 80 F8             _....
0280: FF FF 7F F8 FF FF 7F 74  6C 6B 31 2A 80 5F 07 F8  .......tlk1*._..
0290: FF FF 7F F8 FF FF 7F 74  6C 6B 31 00              .......tlk1.    
```

#### Opcodes

```
  0: 0x027B [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=69*, entity1=EventEntity, entity2=EventEntity, string="tlk1", extra=100*)
  1: 0x028D [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x029B [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x029C   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0290:                                      5F 06 04 80              _...
02A0: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 2A 80 5F 07  ........thk1*._.
02B0: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 00           ........thk1.   
```

#### Opcodes

```
  0: 0x029C [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=69*, entity1=EventEntity, entity2=EventEntity, string="thk1", extra=100*)
  1: 0x02AE [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x02BC [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02BD   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:                                         5F 06 04               _..
02C0: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 32 2A 80 5F  .........thk2*._
02D0: 07 F8 FF FF 7F F8 FF FF  7F 74 68 6B 32 00        .........thk2.  
```

#### Opcodes

```
  0: 0x02BD [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=69*, entity1=EventEntity, entity2=EventEntity, string="thk2", extra=100*)
  1: 0x02CF [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x02DD [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02DE   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02D0:                                            6E F8                n.
02E0: FF FF 7F 2B 80 99 F8 FF  FF 7F 1C 2C 80 00        ...+.......,..  
```

#### Opcodes

```
  0: 0x02DE [0x6E] EventEntity uses emote 24*
  1: 0x02E5 [0x99] Wait for EventEntity animation to complete
  2: 0x02EA [0x1C] WAIT(110* ticks)
  3: 0x02ED [0x00] END_REQSTACK()
```
