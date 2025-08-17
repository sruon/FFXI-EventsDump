# 16982139 - Rujen-Gorgen

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 564 bytes                     |
| Total Events     | 9                             |
| References Count | 28                            |

## List of Events

| Event ID                  | Entrypoint   |   Size |   Instructions |
|---------------------------|--------------|--------|----------------|
| [65535](#event-65535)     | 0x0000       |      1 |              1 |
| [667](#event-667)         | 0x0001       |    288 |             43 |
| [594](#event-594)         | 0x0121       |      1 |              1 |
| [774](#event-774)         | 0x0122       |      7 |              2 |
| [3220](#event-3220)       | 0x0129       |     16 |              3 |
| [859](#event-859)         | 0x0139       |      7 |              2 |
| [872](#event-872)         | 0x0140       |      7 |              2 |
| [65535.1](#event-65535-1) | 0x0147       |     38 |              9 |
| [65535.2](#event-65535-2) | 0x016D       |     34 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0028      |          40 |
|       2 | 0x18E8      |        6376 |
|       3 | 0x18E9      |        6377 |
|       4 | 0x0000      |           0 |
|       5 | 0x0022      |          34 |
|       6 | 0x18EA      |        6378 |
|       7 | 0x0001      |           1 |
|       8 | 0x18EB      |        6379 |
|       9 | 0x18EC      |        6380 |
|      10 | 0x18ED      |        6381 |
|      11 | 0x18EE      |        6382 |
|      12 | 0x0002      |           2 |
|      13 | 0x18EF      |        6383 |
|      14 | 0xFFFE3DBC  |  4294852028 |
|      15 | 0xFFFFD261  |  4294955617 |
|      16 | 0x03F5      |        1013 |
|      17 | 0x00F0      |         240 |
|      18 | 0xFFFE6AE2  |  4294863586 |
|      19 | 0x2041      |        8257 |
|      20 | 0x0305      |         773 |
|      21 | 0x000D      |          13 |
|      22 | 0xFFFE6682  |  4294862466 |
|      23 | 0x3280      |       12928 |
|      24 | 0x0671      |        1649 |
|      25 | 0x003C      |          60 |
|      26 | 0x1C73      |        7283 |
|      27 | 0x1C74      |        7284 |

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

### Event 667

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 288 bytes |
| Instructions | 43        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F   ........f......
0010: F8 FF FF 7F 74 68 6B 31  1D 02 80 23 66 01 80 F8  ....thk1...#f...
0020: FF FF 7F F8 FF FF 7F 74  68 6B 32 24 03 80 04 80  .......thk2$....
0030: 04 80 25 02 00 10 04 80  00 60 00 66 05 80 F8 FF  ..%......`.f....
0040: FF 7F F8 FF FF 7F 73 79  75 30 1D 06 80 23 66 05  ......syu0...#f.
0050: 80 F8 FF FF 7F F8 FF FF  7F 73 79 75 31 01 1C 01  .........syu1...
0060: 02 00 10 07 80 00 1C 01  66 05 80 F8 FF FF 7F F8  ........f.......
0070: FF FF 7F 74 6C 62 30 1D  08 80 23 66 05 80 F8 FF  ...tlb0...#f....
0080: FF 7F F8 FF FF 7F 74 6C  62 31 24 09 80 04 80 04  ......tlb1$.....
0090: 80 25 02 00 10 04 80 00  BF 00 66 01 80 F8 FF FF  .%........f.....
00A0: 7F F8 FF FF 7F 74 68 6B  31 1D 0A 80 23 66 01 80  .....thk1...#f..
00B0: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 01 19 01 02  ........thk2....
00C0: 00 10 07 80 00 EC 00 66  01 80 F8 FF FF 7F F8 FF  .......f........
00D0: FF 7F 74 68 6B 31 1D 0B  80 23 66 01 80 F8 FF FF  ..thk1...#f.....
00E0: 7F F8 FF FF 7F 74 68 6B  32 01 19 01 02 00 10 0C  .....thk2.......
00F0: 80 00 19 01 66 01 80 F8  FF FF 7F F8 FF FF 7F 74  ....f..........t
0100: 68 6B 31 1D 0D 80 23 66  01 80 F8 FF FF 7F F8 FF  hk1...#f........
0110: FF 7F 74 68 6B 32 01 19  01 01 1C 01 1C 00 80 21  ..thk2.........!
0120: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=6376*)
    → "Howdy-dowdy!\u0007Have you figured out this town's ward system yet?\u007F1\u0000\u0007"
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
  6: 0x002B [0x24] CREATE_DIALOG(message_id=6377*, default_option=0*, option_flags=0*)
    → "Are you an expert on wards?\u0007\u000BYes, I know everything.\u0007No, can you explain?\u007F1\u0000\u0007"
  7: 0x0032 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0033 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0060
  9: 0x003B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "syu0" with entities [EventEntity, EventEntity], work=34*
 10: 0x004A [0x1D] PRINT_EVENT_MESSAGE(message_id=6378*)
    → "Well, that's one fewer worry-dorry you'll have to deal with!\u0007Off on your way-day, now! You don't want the Immortals to set their sights on you!\u007F1\u0000\u0007"
 11: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x004E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "syu1" with entities [EventEntity, EventEntity], work=34*
 13: 0x005D [0x01] GOTO 0x011C
 14: 0x0060 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x011C
 15: 0x0068 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=34*
 16: 0x0077 [0x1D] PRINT_EVENT_MESSAGE(message_id=6379*)
    → "No problem-doblem!\u0007What would you like to know?\u007F1\u0000\u0007"
 17: 0x007A [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x007B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=34*
 19: 0x008A [0x24] CREATE_DIALOG(message_id=6380*, default_option=0*, option_flags=0*)
    → "Ask about which ward?\u0007\u000BCommoners' Ward.\u0007Merchants' Ward.\u0007Imperial Ward.\u007F1\u0000\u0007"
 20: 0x0091 [0x25] WAIT_DIALOG_SELECT()
 21: 0x0092 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00BF
 22: 0x009A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
 23: 0x00A9 [0x1D] PRINT_EVENT_MESSAGE(message_id=6381*)
    → "Those who have been stripped-dipped of their citizenship and those who never had it in the first place live in the Commoners' Ward. It's a relatively new area.\u007F1\u0000\u0007"
 24: 0x00AC [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x00AD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
 26: 0x00BC [0x01] GOTO 0x0119
 27: 0x00BF [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00EC
 28: 0x00C7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
 29: 0x00D6 [0x1D] PRINT_EVENT_MESSAGE(message_id=6382*)
    → "People who have come from other nations and the merchants who sell to them live in the Merchants' Ward. It's a smorgasbord of sights and smells. There are also two ports that allow Aht Urhgan Whitegate to serve as the main \u00072gate\u00073 to West Aht Urhgan.\u007F1\u0000\u0007"
 30: 0x00D9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x00DA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
 32: 0x00E9 [0x01] GOTO 0x0119
 33: 0x00EC [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0119
 34: 0x00F4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
 35: 0x0103 [0x1D] PRINT_EVENT_MESSAGE(message_id=6383*)
    → "The Imperial Ward lies beyond those towering ivory walls. It houses the Imperial palace, facilities for the Imperial Army, and the residences of the Imperial family. People like us aren't even allowed to enter.\u007F1\u0000\u0007"
 36: 0x0106 [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x0107 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
 38: 0x0116 [0x01] GOTO 0x0119

SUBROUTINE_0119:
 39: 0x0119 [0x01] GOTO 0x011C

SUBROUTINE_011C:
 40: 0x011C [0x1C] WAIT(30* ticks)
 41: 0x011F [0x21] END_EVENT
 42: 0x0120 [0x00] END_REQSTACK()
```

### Event 594

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0121  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:    00                                              .              
```

#### Opcodes

```
  0: 0x0121 [0x00] END_REQSTACK()
```

### Event 774

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0122  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x0122 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0128 [0x00] END_REQSTACK()
```

### Event 3220

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0129   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                             92 01 F8 FF FF 7F 37           ......7
0130: 0E 80 0F 80 04 80 10 80  00                       .........       
```

#### Opcodes

```
  0: 0x0129 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x012F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-115.268*, z=-11.679*, y=0.000*, direction=89.0°*
  2: 0x0138 [0x00] END_REQSTACK()
```

### Event 859

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0139  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                             92 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x0139 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x013F [0x00] END_REQSTACK()
```

### Event 872

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0140  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0140 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0146 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0147   |
| Data Size    | 38 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                      1C  11 80 22 00 37 12 80 13         ...".7...
0150: 80 04 80 14 80 80 F8 FF  FF 7F 32 15 80 1F 00 16  ..........2.....
0160: 80 17 80 04 80 1F 01 1E  6C 20 03 01 00           ........l ...   
```

#### Opcodes

```
  0: 0x0147 [0x1C] WAIT(240* ticks)
  1: 0x014A [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x014C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-103.710*, z=8.257*, y=0.000*, direction=67.9°*
  3: 0x0155 [0x80] LOAD_WAIT(entity=EventEntity)
  4: 0x015A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x015D [0x1F] MOVE_ENTITY: EventEntity moves to X=-104.830*, Z=12.928*, Y=0.000*
  6: 0x0165 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0167 [0x1E] EventEntity looks at Zyfhil (ID: 16982124/0x0103206C) and starts talking
  8: 0x016C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016D   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                         4B 7B 20               K{ 
0170: 03 01 18 80 1C 19 80 1D  1A 80 23 66 01 80 7B 20  ..........#f..{ 
0180: 03 01 7B 20 03 01 7A 69  74 30 1D 1B 80 23 00     ..{ ..zit0...#. 
```

#### Opcodes

```
  0: 0x016D [0x4B] UPDATE_ENTITY_YAW(entity=Rujen-Gorgen (ID: 16982139/0x0103207B), yaw=9.1°*)
  1: 0x0174 [0x1C] WAIT(60* ticks)
  2: 0x0177 [0x1D] PRINT_EVENT_MESSAGE(message_id=7283*)
    → "All of a sudden I feel a bit lightaru.\u007F1\u0000\u0007"
  3: 0x017A [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x017B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "zit0" with entities [Rujen-Gorgen (ID: 16982139/0x0103207B), Rujen-Gorgen (ID: 16982139/0x0103207B)], work=40*
  5: 0x018A [0x1D] PRINT_EVENT_MESSAGE(message_id=7284*)
    → "Waaaaahhh! My gil pouch has been stolen, and with it my life savings!\u007F1\u0000\u0007"
  6: 0x018D [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x018E [0x00] END_REQSTACK()
```
