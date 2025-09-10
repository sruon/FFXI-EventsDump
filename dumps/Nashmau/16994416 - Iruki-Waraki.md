# 16994416 - Iruki-Waraki

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Nashmau (ID: 53) |
| Block Size       | 760 bytes        |
| Total Events     | 24               |
| References Count | 51               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [290](#event-290)          | 0x0001       |      1 |              1 |
| [291](#event-291)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0003       |     14 |              3 |
| [65535.2](#event-655352)   | 0x0011       |     21 |              7 |
| [65535.3](#event-655353)   | 0x0026       |     23 |              5 |
| [65535.4](#event-655354)   | 0x003D       |     10 |              2 |
| [65535.5](#event-655355)   | 0x0047       |     14 |              4 |
| [65535.6](#event-655356)   | 0x0055       |     14 |              3 |
| [65535.7](#event-655357)   | 0x0063       |      4 |              2 |
| [65535.8](#event-655358)   | 0x0067       |     28 |              6 |
| [65535.9](#event-655359)   | 0x0083       |      5 |              2 |
| [65535.10](#event-6553510) | 0x0088       |     10 |              3 |
| [65535.11](#event-6553511) | 0x0092       |     10 |              2 |
| [65535.12](#event-6553512) | 0x009C       |     23 |              5 |
| [65535.13](#event-6553513) | 0x00B3       |     11 |              3 |
| [65535.14](#event-6553514) | 0x00BE       |     10 |              2 |
| [65535.15](#event-6553515) | 0x00C8       |      9 |              3 |
| [65535.16](#event-6553516) | 0x00D1       |     92 |             15 |
| [65535.17](#event-6553517) | 0x012D       |     10 |              2 |
| [65535.18](#event-6553518) | 0x0137       |     11 |              3 |
| [65535.19](#event-6553519) | 0x0142       |     99 |              9 |
| [65535.20](#event-6553520) | 0x01A5       |     10 |              2 |
| [65535.21](#event-6553521) | 0x01AF       |     11 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFE88D  |  4294961293 |
|       1 | 0xFFFF6B59  |  4294929241 |
|       2 | 0x0000      |           0 |
|       3 | 0x0DB5      |        3509 |
|       4 | 0x0016      |          22 |
|       5 | 0x000D      |          13 |
|       6 | 0xFFFFDC5F  |  4294958175 |
|       7 | 0xFFFF6820  |  4294928416 |
|       8 | 0x4C22      |       19490 |
|       9 | 0xFFFF336E  |  4294914926 |
|      10 | 0x0AA7      |        2727 |
|      11 | 0x4533      |       17715 |
|      12 | 0xFFFF46E2  |  4294919906 |
|      13 | 0xFFFFE43D  |  4294960189 |
|      14 | 0xFFFF60F1  |  4294926577 |
|      15 | 0x0D94      |        3476 |
|      16 | 0xFFFFBB75  |  4294949749 |
|      17 | 0xFFFF79FF  |  4294932991 |
|      18 | 0x00A9      |         169 |
|      19 | 0xFFFFE06A  |  4294959210 |
|      20 | 0xFFFF7270  |  4294931056 |
|      21 | 0x0EEE      |        3822 |
|      22 | 0x005A      |          90 |
|      23 | 0x001E      |          30 |
|      24 | 0x0007      |           7 |
|      25 | 0x4F28      |       20264 |
|      26 | 0xFFFF133D  |  4294906685 |
|      27 | 0x0BDF      |        3039 |
|      28 | 0x4F47      |       20295 |
|      29 | 0xFFFF194D  |  4294908237 |
|      30 | 0x4A6F      |       19055 |
|      31 | 0xFFFF39E4  |  4294916580 |
|      32 | 0x0A60      |        2656 |
|      33 | 0x2B44      |       11076 |
|      34 | 0x0078      |         120 |
|      35 | 0x0046      |          70 |
|      36 | 0x0041      |          65 |
|      37 | 0x003C      |          60 |
|      38 | 0x2131      |        8497 |
|      39 | 0xFFFF73E8  |  4294931432 |
|      40 | 0x0754      |        1876 |
|      41 | 0x1D42      |        7490 |
|      42 | 0xFFFF72E5  |  4294931173 |
|      43 | 0x0023      |          35 |
|      44 | 0x0088      |         136 |
|      45 | 0x034B      |         843 |
|      46 | 0xFFFFFD1E  |  4294966558 |
|      47 | 0xFFFF8535  |  4294935861 |
|      48 | 0x03FA      |        1018 |
|      49 | 0xFFFFFE98  |  4294966936 |
|      50 | 0xFFFF58F3  |  4294924531 |

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

### Event 290

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 291

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 14 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          37 00 80 01 80  02 80 03 80 B6 03 04 80     7............
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0003 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-6.003*, z=-38.055*, y=0.000*, direction=308.4°*
  1: 0x000C [0xB6] ENTITY_APPEARANCE_HANDLER(case=Head, value=22*)
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 05 80 1F 00 06 80  07 80 02 80 1F 01 1E 6D   2.............m
0020: 50 03 01 6F 70 00                                 P..op.          
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-9.121*, Z=-38.880*, Y=0.000*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x1E] EventEntity looks at Yafahb (ID: 16994413/0x0103506D) and starts talking
  4: 0x0023 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0024 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   37 08  80 09 80 02 80 0A 80 32        7........2
0030: 05 80 1F 00 0B 80 0C 80  02 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x0026 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=19.490*, z=-52.370*, y=0.000*, direction=239.7°*
  1: 0x002F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0032 [0x1F] MOVE_ENTITY: EventEntity moves to X=17.715*, Z=-47.390*, Y=0.000*
  3: 0x003A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         37 0D 80               7..
0040: 0E 80 02 80 0F 80 00                              .......         
```

#### Opcodes

```
  0: 0x003D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-7.107*, z=-40.719*, y=0.000*, direction=305.5°*
  1: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      32  05 80 1F 00 10 80 11 80         2........
0050: 02 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0047 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004A [0x1F] MOVE_ENTITY: EventEntity moves to X=-17.547*, Z=-34.305*, Y=0.000*
  2: 0x0052 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 14 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                B6 03 12  80 37 13 80 14 80 02 80       ....7......
0060: 15 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0055 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Head, value=169*)
  1: 0x0059 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-8.086*, z=-36.240*, y=0.000*, direction=335.9°*
  2: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          1C 16 80 00                                 ....         
```

#### Opcodes

```
  0: 0x0063 [0x1C] WAIT(90* ticks)
  1: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 28 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      1C  17 80 6E 70 50 03 01 18         ...npP...
0070: 80 99 70 50 03 01 99 70  50 03 01 27 09 70 50 03  ..pP...pP..'.pP.
0080: 01 09 00                                          ...             
```

#### Opcodes

```
  0: 0x0067 [0x1C] WAIT(30* ticks)
  1: 0x006A [0x6E] Iruki-Waraki (ID: 16994416/0x01035070) uses emote 7*
  2: 0x0071 [0x99] Wait for Iruki-Waraki (ID: 16994416/0x01035070) animation to complete
  3: 0x0076 [0x99] Wait for Iruki-Waraki (ID: 16994416/0x01035070) animation to complete
  4: 0x007B [0x27] REQ_SET(priority=0x09, entity_id=Iruki-Waraki (ID: 16994416/0x01035070), tag_num=0x09)
  5: 0x0082 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0083  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:          B6 03 02 80 00                              .....        
```

#### Opcodes

```
  0: 0x0083 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Head, value=0*)
  1: 0x0087 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0088   |
| Data Size    | 10 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          B6 03 12 80 80 F8 FF FF          ........
0090: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0088 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Head, value=169*)
  1: 0x008C [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0091 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       37 19 80 1A 80 02  80 1B 80 00                7.........    
```

#### Opcodes

```
  0: 0x0092 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=20.264*, z=-60.611*, y=0.000*, direction=267.1°*
  1: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      32 05 80 1F              2...
00A0: 00 1C 80 1D 80 02 80 1F  01 4A 70 50 03 01 6D 50  .........JpP..mP
00B0: 03 01 00                                          ...             
```

#### Opcodes

```
  0: 0x009C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x009F [0x1F] MOVE_ENTITY: EventEntity moves to X=20.295*, Z=-59.059*, Y=0.000*
  2: 0x00A7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A9 [0x4A] Iruki-Waraki (ID: 16994416/0x01035070) looks at Yafahb (ID: 16994413/0x0103506D)
  4: 0x00B2 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B3   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          1F 00 1E 80 1F  80 02 80 1F 01 00           ...........  
```

#### Opcodes

```
  0: 0x00B3 [0x1F] MOVE_ENTITY: EventEntity moves to X=19.055*, Z=-50.716*, Y=0.000*
  1: 0x00BB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00BD [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BE   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                            37 0B                7.
00C0: 80 0C 80 02 80 20 80 00                           ..... ..        
```

#### Opcodes

```
  0: 0x00BE [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=17.715*, z=-47.390*, y=0.000*, direction=233.4°*
  1: 0x00C7 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C8  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                          2B 6F 50 03 01 21 80 23          +oP..!.#
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00C8 [0x2B] Elisabeth (ID: 16994415/0x0103506F) [11076*]:
    → "And you're supposed to be one of the top puppetmasters on Urhguum? Don't make me laugh!"
  1: 0x00CF [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00D0 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D1   |
| Data Size    | 92 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:    79 00 F0 FF FF 7F 6D  50 03 01 1C 22 80 79 00   y.....mP...".y.
00E0: F0 FF FF 7F 6F 50 03 01  1C 23 80 79 00 F0 FF FF  ....oP...#.y....
00F0: 7F 6D 50 03 01 1C 22 80  79 00 F0 FF FF 7F 6F 50  .mP...".y.....oP
0100: 03 01 1C 24 80 79 00 F0  FF FF 7F 6D 50 03 01 1C  ...$.y.....mP...
0110: 22 80 79 00 F0 FF FF 7F  6F 50 03 01 1C 25 80 79  ".y.....oP...%.y
0120: 00 F0 FF FF 7F 6D 50 03  01 1C 16 80 00           .....mP......   
```

#### Opcodes

```
  0: 0x00D1 [0x79] LocalPlayer looks at Yafahb (ID: 16994413/0x0103506D) (Basic look)
  1: 0x00DB [0x1C] WAIT(120* ticks)
  2: 0x00DE [0x79] LocalPlayer looks at Elisabeth (ID: 16994415/0x0103506F) (Basic look)
  3: 0x00E8 [0x1C] WAIT(70* ticks)
  4: 0x00EB [0x79] LocalPlayer looks at Yafahb (ID: 16994413/0x0103506D) (Basic look)
  5: 0x00F5 [0x1C] WAIT(120* ticks)
  6: 0x00F8 [0x79] LocalPlayer looks at Elisabeth (ID: 16994415/0x0103506F) (Basic look)
  7: 0x0102 [0x1C] WAIT(65* ticks)
  8: 0x0105 [0x79] LocalPlayer looks at Yafahb (ID: 16994413/0x0103506D) (Basic look)
  9: 0x010F [0x1C] WAIT(120* ticks)
 10: 0x0112 [0x79] LocalPlayer looks at Elisabeth (ID: 16994415/0x0103506F) (Basic look)
 11: 0x011C [0x1C] WAIT(60* ticks)
 12: 0x011F [0x79] LocalPlayer looks at Yafahb (ID: 16994413/0x0103506D) (Basic look)
 13: 0x0129 [0x1C] WAIT(90* ticks)
 14: 0x012C [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                         37 26 80               7&.
0130: 27 80 02 80 28 80 00                              '...(..         
```

#### Opcodes

```
  0: 0x012D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=8.497*, z=-35.864*, y=0.000*, direction=164.9°*
  1: 0x0136 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0137   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                      1F  00 29 80 2A 80 02 80 1F         ..).*....
0140: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0137 [0x1F] MOVE_ENTITY: EventEntity moves to X=7.490*, Z=-36.123*, Y=0.000*
  1: 0x013F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0141 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0142   |
| Data Size    | 99 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:       55 2B 80 F8 FF FF  7F F8 FF FF 7F 73 32 39    U+.........s29
0150: 7A 5C 00 2C 80 5C 01 2C  80 5B 2D 80 32 50 03 01  z\.,.\.,.[-.2P..
0160: 32 50 03 01 68 61 70 30  5B 2D 80 3A 50 03 01 3A  2P..hap0[-.:P..:
0170: 50 03 01 68 61 70 30 5B  2D 80 3B 50 03 01 3B 50  P..hap0[-.;P..;P
0180: 03 01 68 61 70 30 5B 2D  80 3E 50 03 01 3E 50 03  ..hap0[-.>P..>P.
0190: 01 68 61 70 30 5B 2D 80  42 50 03 01 42 50 03 01  .hap0[-.BP..BP..
01A0: 68 61 70 30 00                                    hap0.           
```

#### Opcodes

```
  0: 0x0142 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s29z" with entities [EventEntity, EventEntity], work=35*
  1: 0x0151 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 136*
  2: 0x0155 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 136*
  3: 0x0159 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hap0" with entities [Buburoon (ID: 16994354/0x01035032), Buburoon (ID: 16994354/0x01035032)], work=843*
  4: 0x0168 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hap0" with entities [Tsotsoroon (ID: 16994362/0x0103503A), Tsotsoroon (ID: 16994362/0x0103503A)], work=843*
  5: 0x0177 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hap0" with entities [Sisiroon (ID: 16994363/0x0103503B), Sisiroon (ID: 16994363/0x0103503B)], work=843*
  6: 0x0186 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hap0" with entities [Jojoroon (ID: 16994366/0x0103503E), Jojoroon (ID: 16994366/0x0103503E)], work=843*
  7: 0x0195 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hap0" with entities [Tsutsuroon (ID: 16994370/0x01035042), Tsutsuroon (ID: 16994370/0x01035042)], work=843*
  8: 0x01A4 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A5   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                37 2E 80  2F 80 02 80 30 80 00          7../...0.. 
```

#### Opcodes

```
  0: 0x01A5 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.738*, z=-31.435*, y=0.000*, direction=89.5°*
  1: 0x01AE [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01AF   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                               1F                 .
01B0: 00 31 80 32 80 02 80 1F  01 00                    .1.2......      
```

#### Opcodes

```
  0: 0x01AF [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.360*, Z=-42.765*, Y=0.000*
  1: 0x01B7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x01B9 [0x00] END_REQSTACK()
```
