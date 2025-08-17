# 17855048 - Frondeaubaire

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Yorcia Weald (ID: 263) |
| Block Size       | 484 bytes              |
| Total Events     | 16                     |
| References Count | 44                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [116](#event-116)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     14 |              4 |
| [65535.2](#event-655352)   | 0x0010       |     26 |              6 |
| [65535.3](#event-655353)   | 0x002A       |     14 |              4 |
| [118](#event-118)          | 0x0038       |      1 |              1 |
| [65535.4](#event-655354)   | 0x0039       |     14 |              4 |
| [120](#event-120)          | 0x0047       |      1 |              1 |
| [65535.5](#event-655355)   | 0x0048       |     17 |              5 |
| [65535.6](#event-655356)   | 0x0059       |     14 |              4 |
| [125](#event-125)          | 0x0067       |     21 |              2 |
| [65535.7](#event-655357)   | 0x007C       |     24 |              6 |
| [65535.8](#event-655358)   | 0x0094       |     21 |              2 |
| [131](#event-131)          | 0x00A9       |      7 |              2 |
| [65535.9](#event-655359)   | 0x00B0       |     30 |              8 |
| [65535.10](#event-6553510) | 0x00CE       |     22 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x437F7     |      276471 |
|       2 | 0x4D97      |       19863 |
|       3 | 0x00EF      |         239 |
|       4 | 0x42DF4     |      273908 |
|       5 | 0x473C      |       18236 |
|       6 | 0x023B      |         571 |
|       7 | 0x001E      |          30 |
|       8 | 0x44953     |      280915 |
|       9 | 0x4E81      |       20097 |
|      10 | 0x00F2      |         242 |
|      11 | 0x27738     |      161592 |
|      12 | 0xA19D      |       41373 |
|      13 | 0x0000      |           0 |
|      14 | 0xFFFF1DA2  |  4294909346 |
|      15 | 0xFFFE31BD  |  4294848957 |
|      16 | 0x01A9      |         425 |
|      17 | 0xFFFF2230  |  4294910512 |
|      18 | 0xFFFE234B  |  4294845259 |
|      19 | 0x017F      |         383 |
|      20 | 0x0004      |           4 |
|      21 | 0x0001      |           1 |
|      22 | 0x0014      |          20 |
|      23 | 0x008F      |         143 |
|      24 | 0x0017      |          23 |
|      25 | 0xFFFD6CBD  |  4294798525 |
|      26 | 0x604F2     |      394482 |
|      27 | 0x0215      |         533 |
|      28 | 0xFFFD6440  |  4294796352 |
|      29 | 0x60F34     |      397108 |
|      30 | 0x00FD      |         253 |
|      31 | 0x0003      |           3 |
|      32 | 0x0007      |           7 |
|      33 | 0x0028      |          40 |
|      34 | 0x194F6     |      103670 |
|      35 | 0xEABA      |       60090 |
|      36 | 0xFFFFF952  |  4294965586 |
|      37 | 0x1A1F8     |      107000 |
|      38 | 0xEC54      |       60500 |
|      39 | 0xFFFFFD26  |  4294966566 |
|      40 | 0x000F      |          15 |
|      41 | 0x1C264     |      115300 |
|      42 | 0xE9FC      |       59900 |
|      43 | 0x0384      |         900 |

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

### Event 116

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=276.471*, Z=19.863*, Y=0.239*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 26 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 32 00 80 1F 00 04 80 05  80 06 80 1F 01 4A 46 72  2............JFr
0020: 10 01 48 72 10 01 1C 07  80 00                    ..Hr......      
```

#### Opcodes

```
  0: 0x0010 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0013 [0x1F] MOVE_ENTITY: EventEntity moves to X=273.908*, Z=18.236*, Y=0.571*
  2: 0x001B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001D [0x4A] Erfimia (ID: 17855046/0x01107246) looks at Frondeaubaire (ID: 17855048/0x01107248)
  4: 0x0026 [0x1C] WAIT(30* ticks)
  5: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                32 00 80 1F 00 08            2.....
0030: 80 09 80 0A 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x002A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=280.915*, Z=20.097*, Y=0.242*
  2: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0037 [0x00] END_REQSTACK()
```

### Event 118

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0038  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          00                               .       
```

#### Opcodes

```
  0: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             32 00 80 1F 00 0B 80           2......
0040: 0C 80 0D 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0039 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=161.592*, Z=41.373*, Y=0.000*
  2: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0046 [0x00] END_REQSTACK()
```

### Event 120

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0047  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      00                                  .        
```

#### Opcodes

```
  0: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          32 00 80 1F 00 0E 80 0F          2.......
0050: 80 10 80 1F 01 1C 07 80  00                       .........       
```

#### Opcodes

```
  0: 0x0048 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=-57.950*, Z=-118.339*, Y=0.425*
  2: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0055 [0x1C] WAIT(30* ticks)
  4: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             32 00 80 1F 00 11 80           2......
0060: 12 80 13 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0059 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=-56.784*, Z=-122.037*, Y=0.383*
  2: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0066 [0x00] END_REQSTACK()
```

### Event 125

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      B6  0B 14 80 15 80 16 80 17         .........
0070: 80 18 80 17 80 17 80 0D  80 0D 80 00              ............    
```

#### Opcodes

```
  0: 0x0067 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=4*, hair=1*, head=20*, body=143*, hands=23*, legs=143*, feet=143*, main=0*, sub=0*)
  1: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      32 00 80 1F              2...
0080: 00 19 80 1A 80 1B 80 1F  01 1F 00 1C 80 1D 80 1E  ................
0090: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x007C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007F [0x1F] MOVE_ENTITY: EventEntity moves to X=-168.771*, Z=394.482*, Y=0.533*
  2: 0x0087 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0089 [0x1F] MOVE_ENTITY: EventEntity moves to X=-170.944*, Z=397.108*, Y=0.253*
  4: 0x0091 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             B6 0B 1F 80  20 80 16 80 17 80 18 80      .... .......
00A0: 17 80 17 80 0D 80 0D 80  00                       .........       
```

#### Opcodes

```
  0: 0x0094 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=7*, head=20*, body=143*, hands=23*, legs=143*, feet=143*, main=0*, sub=0*)
  1: 0x00A8 [0x00] END_REQSTACK()
```

### Event 131

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A9  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             92 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x00A9 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00AF [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B0   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 32 21 80 1F 00 22 80 23  80 24 80 1F 01 1F 00 25  2!...".#.$.....%
00C0: 80 26 80 27 80 1F 01 1C  28 80 39 0D 80 00        .&.'....(.9...  
```

#### Opcodes

```
  0: 0x00B0 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00B3 [0x1F] MOVE_ENTITY: EventEntity moves to X=103.670*, Z=60.090*, Y=-1.710*
  2: 0x00BB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BD [0x1F] MOVE_ENTITY: EventEntity moves to X=107.000*, Z=60.500*, Y=-0.730*
  4: 0x00C5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00C7 [0x1C] WAIT(15* ticks)
  6: 0x00CA [0x39] SET_ENTITY_DIRECTION(direction=0.0°*)
  7: 0x00CD [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CE   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            32 00                2.
00D0: 80 1F 00 29 80 2A 80 2B  80 1F 01 1C 28 80 1E 3A  ...).*.+....(..:
00E0: 72 10 01 00                                       r...            
```

#### Opcodes

```
  0: 0x00CE [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00D1 [0x1F] MOVE_ENTITY: EventEntity moves to X=115.300*, Z=59.900*, Y=0.900*
  2: 0x00D9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00DB [0x1C] WAIT(15* ticks)
  4: 0x00DE [0x1E] EventEntity looks at Nashu (ID: 17855034/0x0110723A) and starts talking
  5: 0x00E3 [0x00] END_REQSTACK()
```
