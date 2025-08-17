# 16994372 - Pyopyoroon

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Nashmau (ID: 53) |
| Block Size       | 688 bytes        |
| Total Events     | 13               |
| References Count | 41               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [275](#event-275)        | 0x0001       |    123 |             23 |
| [276](#event-276)        | 0x007C       |    133 |             23 |
| [277](#event-277)        | 0x0101       |      1 |              1 |
| [65535.1](#event-655351) | 0x0102       |     15 |              5 |
| [65535.2](#event-655352) | 0x0111       |     15 |              5 |
| [278](#event-278)        | 0x0120       |     40 |             12 |
| [279](#event-279)        | 0x0148       |      1 |              1 |
| [280](#event-280)        | 0x0149       |     25 |              9 |
| [281](#event-281)        | 0x0162       |      1 |              1 |
| [65535.3](#event-655353) | 0x0163       |     10 |              2 |
| [65535.4](#event-655354) | 0x016D       |     10 |              2 |
| [65535.5](#event-655355) | 0x0177       |     80 |             16 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x034B      |         843 |
|       1 | 0x2966      |       10598 |
|       2 | 0x001E      |          30 |
|       3 | 0x2967      |       10599 |
|       4 | 0x000F      |          15 |
|       5 | 0x0371      |         881 |
|       6 | 0x2968      |       10600 |
|       7 | 0x2969      |       10601 |
|       8 | 0x296A      |       10602 |
|       9 | 0x296B      |       10603 |
|      10 | 0x29E2      |       10722 |
|      11 | 0x296C      |       10604 |
|      12 | 0x296D      |       10605 |
|      13 | 0x000D      |          13 |
|      14 | 0x5976      |       22902 |
|      15 | 0x5DA0      |       23968 |
|      16 | 0x0000      |           0 |
|      17 | 0x5688      |       22152 |
|      18 | 0x5A55      |       23125 |
|      19 | 0x0903      |        2307 |
|      20 | 0x29EF      |       10735 |
|      21 | 0x032D      |         813 |
|      22 | 0x29F0      |       10736 |
|      23 | 0x29F6      |       10742 |
|      24 | 0x29F7      |       10743 |
|      25 | 0xFFFFEC97  |  4294962327 |
|      26 | 0xFFFF5969  |  4294924649 |
|      27 | 0x0466      |        1126 |
|      28 | 0xFFFFC523  |  4294952227 |
|      29 | 0xFFFF113B  |  4294906171 |
|      30 | 0x07CF      |        1999 |
|      31 | 0x0822      |        2082 |
|      32 | 0x0028      |          40 |
|      33 | 0xFFFFC727  |  4294952743 |
|      34 | 0xFFFF1899  |  4294908057 |
|      35 | 0x0078      |         120 |
|      36 | 0x003C      |          60 |
|      37 | 0xFFFFC9B9  |  4294953401 |
|      38 | 0xFFFF22EF  |  4294910703 |
|      39 | 0xFFFFDDBB  |  4294958523 |
|      40 | 0xFFFF2D6F  |  4294913391 |

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

### Event 275

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 123 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 70 6E 74 30   [..........pnt0
0010: 2B 44 50 03 01 01 80 23  5B 00 80 F8 FF FF 7F F8  +DP....#[.......
0020: FF FF 7F 70 6E 74 31 1C  02 80 2B 44 50 03 01 03  ...pnt1...+DP...
0030: 80 23 1E F0 FF FF 7F 6F  70 7B F8 FF FF 7F 1C 04  .#.....op{......
0040: 80 5B 05 80 F8 FF FF 7F  F8 FF FF 7F 75 72 61 30  .[..........ura0
0050: 2B 44 50 03 01 06 80 23  2B 44 50 03 01 07 80 23  +DP....#+DP....#
0060: 5B 00 80 F8 FF FF 7F F8  FF FF 7F 75 72 61 31 1C  [..........ura1.
0070: 02 80 2B 44 50 03 01 08  80 23 21 00              ..+DP....#!.    
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pnt0" with entities [EventEntity, EventEntity], work=843*
  1: 0x0010 [0x2B] Pyopyoroon (ID: 16994372/0x01035044) [10598*]:
    → "Girl that was here, turn to ghooost! Yooo knowing?"
  2: 0x0017 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0018 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pnt1" with entities [EventEntity, EventEntity], work=843*
  4: 0x0027 [0x1C] WAIT(30* ticks)
  5: 0x002A [0x2B] Pyopyoroon (ID: 16994372/0x01035044) [10599*]:
    → "Cooould it be!?"
  6: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0032 [0x1E] EventEntity looks at LocalPlayer and starts talking
  8: 0x0037 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x0038 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 10: 0x0039 [0x7B] EventEntity stops talking
 11: 0x003E [0x1C] WAIT(15* ticks)
 12: 0x0041 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ura0" with entities [EventEntity, EventEntity], work=881*
 13: 0x0050 [0x2B] Pyopyoroon (ID: 16994372/0x01035044) [10600*]:
    → "Bastoookan Blight?"
 14: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0058 [0x2B] Pyopyoroon (ID: 16994372/0x01035044) [10601*]:
    → "Life gooo bye, and become ghooost!"
 16: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0060 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ura1" with entities [EventEntity, EventEntity], work=843*
 18: 0x006F [0x1C] WAIT(30* ticks)
 19: 0x0072 [0x2B] Pyopyoroon (ID: 16994372/0x01035044) [10602*]:
    → "Blight painfoool. Painfoool death. Then become ghooost?"
 20: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x007A [0x21] END_EVENT
 22: 0x007B [0x00] END_REQSTACK()
```

### Event 276

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x007C    |
| Data Size    | 133 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      5B 00 80 F8              [...
0080: FF FF 7F F8 FF FF 7F 70  6E 74 30 2B 44 50 03 01  .......pnt0+DP..
0090: 01 80 23 5B 00 80 F8 FF  FF 7F F8 FF FF 7F 70 6E  ..#[..........pn
00A0: 74 31 1C 02 80 1E F0 FF  FF 7F 6F 70 1C 02 80 2B  t1........op...+
00B0: 44 50 03 01 09 80 23 5B  00 80 F8 FF FF 7F F8 FF  DP....#[........
00C0: FF 7F 61 6E 67 30 2B 44  50 03 01 0A 80 23 2B 44  ..ang0+DP....#+D
00D0: 50 03 01 0B 80 23 5B 05  80 F8 FF FF 7F F8 FF FF  P....#[.........
00E0: 7F 77 68 74 30 2B 44 50  03 01 0C 80 23 5B 05 80  .wht0+DP....#[..
00F0: F8 FF FF 7F F8 FF FF 7F  77 68 74 31 1C 02 80 21  ........wht1...!
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x007C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pnt0" with entities [EventEntity, EventEntity], work=843*
  1: 0x008B [0x2B] Pyopyoroon (ID: 16994372/0x01035044) [10598*]:
    → "Girl that was here, turn to ghooost! Yooo knowing?"
  2: 0x0092 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0093 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pnt1" with entities [EventEntity, EventEntity], work=843*
  4: 0x00A2 [0x1C] WAIT(30* ticks)
  5: 0x00A5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x00AA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x00AB [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x00AC [0x1C] WAIT(30* ticks)
  9: 0x00AF [0x2B] Pyopyoroon (ID: 16994372/0x01035044) [10603*]:
    → "Did yooo hear? Do yooo know? Girl that was here, now in Al Jibby!"
 10: 0x00B6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00B7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang0" with entities [EventEntity, EventEntity], work=843*
 12: 0x00C6 [0x2B] Pyopyoroon (ID: 16994372/0x01035044) [10722*]:
    → "Brrr. Brrr."
 13: 0x00CD [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x00CE [0x2B] Pyopyoroon (ID: 16994372/0x01035044) [10604*]:
    → "Pyopyoroon disappoooint. Pyopyoroon even kind of mad."
 15: 0x00D5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x00D6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wht0" with entities [EventEntity, EventEntity], work=881*
 17: 0x00E5 [0x2B] Pyopyoroon (ID: 16994372/0x01035044) [10605*]:
    → "But maybe Pyopyoroon want see her again? Can Pyopyoroon ever meet?"
 18: 0x00EC [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x00ED [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wht1" with entities [EventEntity, EventEntity], work=881*
 20: 0x00FC [0x1C] WAIT(30* ticks)
 21: 0x00FF [0x21] END_EVENT
 22: 0x0100 [0x00] END_REQSTACK()
```

### Event 277

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0101  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:    00                                              .              
```

#### Opcodes

```
  0: 0x0101 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0102   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:       32 0D 80 1F 00 0E  80 0F 80 10 80 1F 01 6F    2............o
0110: 00                                                .               
```

#### Opcodes

```
  0: 0x0102 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0105 [0x1F] MOVE_ENTITY: EventEntity moves to X=22.902*, Z=23.968*, Y=0.000*
  2: 0x010D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x010F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0110 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0111   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:    32 0D 80 1F 00 11 80  12 80 10 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0111 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0114 [0x1F] MOVE_ENTITY: EventEntity moves to X=22.152*, Z=23.125*, Y=0.000*
  2: 0x011C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x011E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x011F [0x00] END_REQSTACK()
```

### Event 278

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0120   |
| Data Size    | 40 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120: 1E F0 FF FF 7F 6F 70 03  03 10 13 80 2B 44 50 03  .....op.....+DP.
0130: 01 14 80 23 03 02 10 15  80 03 03 10 13 80 2B 44  ...#..........+D
0140: 50 03 01 16 80 23 21 00                           P....#!.        
```

#### Opcodes

```
  0: 0x0120 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0125 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0126 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0127 [0x03] Work_Zone[3] = 2307*
  4: 0x012C [0x2B] Pyopyoroon (ID: 16994372/0x01035044) [10735*]:
    → "Big, red, many-many wavy-wavy arm creature has $1! Yooo go to Wajaom or Bhaflau!"
  5: 0x0133 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0134 [0x03] Work_Zone[2] = 813*
  7: 0x0139 [0x03] Work_Zone[3] = 2307*
  8: 0x013E [0x2B] Pyopyoroon (ID: 16994372/0x01035044) [10736*]:
    → "If Pyopyoroon has $1, Pyopyoroon make yooo $3!"
  9: 0x0145 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0146 [0x21] END_EVENT
 11: 0x0147 [0x00] END_REQSTACK()
```

### Event 279

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0148  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                          00                               .       
```

#### Opcodes

```
  0: 0x0148 [0x00] END_REQSTACK()
```

### Event 280

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0149   |
| Data Size    | 25 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                             1E F0 FF FF 7F 6F 70           .....op
0150: 2B 44 50 03 01 17 80 23  2B 44 50 03 01 18 80 23  +DP....#+DP....#
0160: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0149 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x014E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x014F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0150 [0x2B] Pyopyoroon (ID: 16994372/0x01035044) [10742*]:
    → "Ooold smell is hard smell to make. But ghooost will smell, maybe cry?"
  4: 0x0157 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0158 [0x2B] Pyopyoroon (ID: 16994372/0x01035044) [10743*]:
    → "Yooo go west! Many rooocks, many stooones! Yooo find ghooost!"
  6: 0x015F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0160 [0x21] END_EVENT
  8: 0x0161 [0x00] END_REQSTACK()
```

### Event 281

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0162  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:       00                                            .             
```

#### Opcodes

```
  0: 0x0162 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0163   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:          37 19 80 1A 80  10 80 1B 80 00              7.........   
```

#### Opcodes

```
  0: 0x0163 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-4.969*, z=-42.647*, y=0.000*, direction=99.0°*
  1: 0x016C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                         37 1C 80               7..
0170: 1D 80 1E 80 1F 80 00                              .......         
```

#### Opcodes

```
  0: 0x016D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-15.069*, z=-61.125*, y=1.999*, direction=183.0°*
  1: 0x0176 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0177   |
| Data Size    | 80 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                      32  20 80 1F 00 21 80 22 80         2 ...!.".
0180: 1E 80 1F 01 1E 55 50 03  01 6F 70 1C 02 80 5B 05  .....UP..op...[.
0190: 80 44 50 03 01 44 50 03  01 75 72 61 30 1C 23 80  .DP..DP..ura0.#.
01A0: 5B 05 80 44 50 03 01 44  50 03 01 75 72 61 31 1C  [..DP..DP..ura1.
01B0: 24 80 1F 00 25 80 26 80  1E 80 1F 01 1F 00 27 80  $...%.&.......'.
01C0: 28 80 1E 80 1F 01 00                              (......         
```

#### Opcodes

```
  0: 0x0177 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x017A [0x1F] MOVE_ENTITY: EventEntity moves to X=-14.553*, Z=-59.239*, Y=1.999*
  2: 0x0182 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0184 [0x1E] EventEntity looks at Gessho (ID: 16994389/0x01035055) and starts talking
  4: 0x0189 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x018A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x018B [0x1C] WAIT(30* ticks)
  7: 0x018E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ura0" with entities [Pyopyoroon (ID: 16994372/0x01035044), Pyopyoroon (ID: 16994372/0x01035044)], work=881*
  8: 0x019D [0x1C] WAIT(120* ticks)
  9: 0x01A0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ura1" with entities [Pyopyoroon (ID: 16994372/0x01035044), Pyopyoroon (ID: 16994372/0x01035044)], work=881*
 10: 0x01AF [0x1C] WAIT(60* ticks)
 11: 0x01B2 [0x1F] MOVE_ENTITY: EventEntity moves to X=-13.895*, Z=-56.593*, Y=1.999*
 12: 0x01BA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 13: 0x01BC [0x1F] MOVE_ENTITY: EventEntity moves to X=-8.773*, Z=-53.905*, Y=1.999*
 14: 0x01C4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 15: 0x01C6 [0x00] END_REQSTACK()
```
