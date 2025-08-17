# 17801275 - Romaa Mihgo

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 420 bytes        |
| Total Events     | 15               |
| References Count | 28               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [263](#event-263)        | 0x0001       |     15 |              8 |
| [306](#event-306)        | 0x0010       |     23 |             12 |
| [266](#event-266)        | 0x0027       |     24 |             13 |
| [267](#event-267)        | 0x003F       |     15 |              8 |
| [276](#event-276)        | 0x004E       |     23 |             12 |
| [295](#event-295)        | 0x0065       |      9 |              3 |
| [65535.1](#event-655351) | 0x006E       |     10 |              2 |
| [296](#event-296)        | 0x0078       |     19 |             10 |
| [297](#event-297)        | 0x008B       |      9 |              3 |
| [65535.2](#event-655352) | 0x0094       |     10 |              2 |
| [65535.3](#event-655353) | 0x009E       |     15 |              5 |
| [65535.4](#event-655354) | 0x00AD       |     15 |              5 |
| [65535.5](#event-655355) | 0x00BC       |     15 |              5 |
| [298](#event-298)        | 0x00CB       |     27 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x271E      |       10014 |
|       1 | 0x271F      |       10015 |
|       2 | 0x2720      |       10016 |
|       3 | 0x2721      |       10017 |
|       4 | 0x28F0      |       10480 |
|       5 | 0x28F1      |       10481 |
|       6 | 0x28F2      |       10482 |
|       7 | 0x28F3      |       10483 |
|       8 | 0x27B4      |       10164 |
|       9 | 0x27B5      |       10165 |
|      10 | 0x27B6      |       10166 |
|      11 | 0x6DC4      |       28100 |
|      12 | 0xFFFD4E28  |  4294790696 |
|      13 | 0xFFFFD109  |  4294955273 |
|      14 | 0x0FA1      |        4001 |
|      15 | 0x29F8      |       10744 |
|      16 | 0x29F9      |       10745 |
|      17 | 0x7080      |       28800 |
|      18 | 0xFFFD4E8C  |  4294790796 |
|      19 | 0x0C3D      |        3133 |
|      20 | 0x000D      |          13 |
|      21 | 0xFFFD5098  |  4294791320 |
|      22 | 0xFFFD4AA4  |  4294789796 |
|      23 | 0xFFFD5080  |  4294791296 |
|      24 | 0x2A12      |       10770 |
|      25 | 0x2A13      |       10771 |
|      26 | 0x2A14      |       10772 |
|      27 | 0x2A0E      |       10766 |

## String References

- **10014**: ...
- **10015**: ...
- **10016**: A familiarrr scent clings to you, adventurer. The aroma of rich earth, and a fresh breeze...it brings me back to long ago.
- **10017**: ...But these are merely the rrramblings of one whose days in the sun have long since passed. Be safe in your travels, adventurer.
- **10164**: ... The $1...
- **10165**: If you want to relieve your hands of the Tonberries' currrse, you must, with your $1, light the four lanterns on a darkened Altar of Rancor.
- **10166**: But be ready, for when all four lanterns are lit...
- **10480**: ... Rukususu...
- **10481**: She said she was looking for a cerrrtain Iru-Kuiru...
- **10482**: This Iru-Kuiru was banished to the Temple of Uggalepih years ago. If you want to find Rukususu, that is where you should start searching.
- **10483**: If you want to find Rukususu, go to the Temple of Uggalepih. That is all I have to tell you.
- **10744**: Go to the hill overlooking the waterfall in the east of the Yuhtunga Jungle...
- **10745**: You will see that he doesn't employ the help of other adventurers, or use any other devious tactics...
- **10766**: If you give the guard at the door $1, $2, and $3, you should be allowed to ask a few questions.
- **10770**: In the ancient past, the god that abides within the crystal of darkness awoke...
- **10771**: The deity was led again into slumber by the light of a certain box.
- **10772**: Tales of this box will surely be known to Kamui, the aged officer that attends Gilgamesh...

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

### Event 263

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 20 00 21 00   .....op...# .!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=10014*)
    → "..."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x000E [0x21] END_EVENT
  7: 0x000F [0x00] END_REQSTACK()
```

### Event 306

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 23 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 1E F0 FF FF 7F 6F 70 1D  01 80 23 1D 02 80 23 1D  .....op...#...#.
0020: 03 80 23 20 00 21 00                              ..# .!.         
```

#### Opcodes

```
  0: 0x0010 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0015 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0016 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=10015*)
    → "..."
  4: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=10016*)
    → "A familiarrr scent clings to you, adventurer. The aroma of rich earth, and a fresh breeze...it brings me back to long ago."
  6: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=10017*)
    → "...But these are merely the rrramblings of one whose days in the sun have long since passed. Be safe in your travels, adventurer."
  8: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0023 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0025 [0x21] END_EVENT
 11: 0x0026 [0x00] END_REQSTACK()
```

### Event 266

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 24 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      42  1E F0 FF FF 7F 6F 70 1D         B.....op.
0030: 04 80 23 1D 05 80 23 1D  06 80 23 20 00 21 00     ..#...#...# .!. 
```

#### Opcodes

```
  0: 0x0027 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0028 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x002D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x002E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=10480*)
    → "... Rukususu..."
  5: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=10481*)
    → "She said she was looking for a cerrrtain Iru-Kuiru..."
  7: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=10482*)
    → "This Iru-Kuiru was banished to the Temple of Uggalepih years ago. If you want to find Rukususu, that is where you should start searching."
  9: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x003B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x003D [0x21] END_EVENT
 12: 0x003E [0x00] END_REQSTACK()
```

### Event 267

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 15 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               1E                 .
0040: F0 FF FF 7F 6F 70 1D 07  80 23 20 00 21 00        ....op...# .!.  
```

#### Opcodes

```
  0: 0x003F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0044 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0045 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0046 [0x1D] PRINT_EVENT_MESSAGE(message_id=10483*)
    → "If you want to find Rukususu, go to the Temple of Uggalepih. That is all I have to tell you."
  4: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x004A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x004C [0x21] END_EVENT
  7: 0x004D [0x00] END_REQSTACK()
```

### Event 276

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 23 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            1E F0                ..
0050: FF FF 7F 6F 70 1D 08 80  23 1D 09 80 23 1D 0A 80  ...op...#...#...
0060: 23 20 00 21 00                                    # .!.           
```

#### Opcodes

```
  0: 0x004E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0053 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0054 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0055 [0x1D] PRINT_EVENT_MESSAGE(message_id=10164*)
    → "... The $1..."
  4: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0059 [0x1D] PRINT_EVENT_MESSAGE(message_id=10165*)
    → "If you want to relieve your hands of the Tonberries' currrse, you must, with your $1, light the four lanterns on a darkened Altar of Rancor."
  6: 0x005C [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x005D [0x1D] PRINT_EVENT_MESSAGE(message_id=10166*)
    → "But be ready, for when all four lanterns are lit..."
  8: 0x0060 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0061 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0063 [0x21] END_EVENT
 11: 0x0064 [0x00] END_REQSTACK()
```

### Event 295

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0065  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                94 01 F8  FF FF 7F A4 01 00             .........  
```

#### Opcodes

```
  0: 0x0065 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x006B [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  2: 0x006D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            37 0B                7.
0070: 80 0C 80 0D 80 0E 80 00                           ........        
```

#### Opcodes

```
  0: 0x006E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=28.100*, z=-176.600*, y=-12.023*, direction=351.6°*
  1: 0x0077 [0x00] END_REQSTACK()
```

### Event 296

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          1E F0 FF FF 7F 6F 70 1D          .....op.
0080: 0F 80 23 1D 10 80 23 20  00 21 00                 ..#...# .!.     
```

#### Opcodes

```
  0: 0x0078 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x007D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x007E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x007F [0x1D] PRINT_EVENT_MESSAGE(message_id=10744*)
    → "Go to the hill overlooking the waterfall in the east of the Yuhtunga Jungle..."
  4: 0x0082 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0083 [0x1D] PRINT_EVENT_MESSAGE(message_id=10745*)
    → "You will see that he doesn't employ the help of other adventurers, or use any other devious tactics..."
  6: 0x0086 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0087 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0089 [0x21] END_EVENT
  9: 0x008A [0x00] END_REQSTACK()
```

### Event 297

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008B  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   94 01 F8 FF FF             .....
0090: 7F A4 01 00                                       ....            
```

#### Opcodes

```
  0: 0x008B [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0091 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  2: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             37 11 80 12  80 0D 80 13 80 00            7.........  
```

#### Opcodes

```
  0: 0x0094 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=28.800*, z=-176.500*, y=-12.023*, direction=275.4°*
  1: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            32 14                2.
00A0: 80 1F 00 11 80 15 80 0D  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x009E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00A1 [0x1F] MOVE_ENTITY: EventEntity moves to X=28.800*, Z=-175.976*, Y=-12.023*
  2: 0x00A9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         32 14 80               2..
00B0: 1F 00 11 80 16 80 0D 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x00AD [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00B0 [0x1F] MOVE_ENTITY: EventEntity moves to X=28.800*, Z=-177.500*, Y=-12.023*
  2: 0x00B8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00BB [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      32 14 80 1F              2...
00C0: 00 11 80 17 80 0D 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x00BC [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00BF [0x1F] MOVE_ENTITY: EventEntity moves to X=28.800*, Z=-176.000*, Y=-12.023*
  2: 0x00C7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00CA [0x00] END_REQSTACK()
```

### Event 298

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CB   |
| Data Size    | 27 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                   1E F0 FF FF 7F             .....
00D0: 6F 70 1D 18 80 23 1D 19  80 23 1D 1A 80 23 1D 1B  op...#...#...#..
00E0: 80 23 20 00 21 00                                 .# .!.          
```

#### Opcodes

```
  0: 0x00CB [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00D0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00D1 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00D2 [0x1D] PRINT_EVENT_MESSAGE(message_id=10770*)
    → "In the ancient past, the god that abides within the crystal of darkness awoke..."
  4: 0x00D5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00D6 [0x1D] PRINT_EVENT_MESSAGE(message_id=10771*)
    → "The deity was led again into slumber by the light of a certain box."
  6: 0x00D9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00DA [0x1D] PRINT_EVENT_MESSAGE(message_id=10772*)
    → "Tales of this box will surely be known to Kamui, the aged officer that attends Gilgamesh..."
  8: 0x00DD [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00DE [0x1D] PRINT_EVENT_MESSAGE(message_id=10766*)
    → "If you give the guard at the door $1, $2, and $3, you should be allowed to ask a few questions."
 10: 0x00E1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00E2 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x00E4 [0x21] END_EVENT
 13: 0x00E5 [0x00] END_REQSTACK()
```
