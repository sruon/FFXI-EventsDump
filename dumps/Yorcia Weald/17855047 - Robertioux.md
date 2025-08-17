# 17855047 - Robertioux

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Yorcia Weald (ID: 263) |
| Block Size       | 424 bytes              |
| Total Events     | 17                     |
| References Count | 29                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [116](#event-116)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     14 |              4 |
| [65535.2](#event-655352)   | 0x0010       |     14 |              4 |
| [118](#event-118)          | 0x001E       |      1 |              1 |
| [65535.3](#event-655353)   | 0x001F       |     14 |              4 |
| [65535.4](#event-655354)   | 0x002D       |     14 |              4 |
| [120](#event-120)          | 0x003B       |      1 |              1 |
| [65535.5](#event-655355)   | 0x003C       |     14 |              4 |
| [65535.6](#event-655356)   | 0x004A       |     14 |              4 |
| [122](#event-122)          | 0x0058       |     21 |              2 |
| [65535.7](#event-655357)   | 0x006D       |     14 |              4 |
| [123](#event-123)          | 0x007B       |     21 |              2 |
| [65535.8](#event-655358)   | 0x0090       |     14 |              4 |
| [125](#event-125)          | 0x009E       |     21 |              2 |
| [65535.9](#event-655359)   | 0x00B3       |     21 |              2 |
| [65535.10](#event-6553510) | 0x00C8       |     21 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x437F7     |      276471 |
|       2 | 0x4D97      |       19863 |
|       3 | 0x00EF      |         239 |
|       4 | 0x44953     |      280915 |
|       5 | 0x4E81      |       20097 |
|       6 | 0x00F2      |         242 |
|       7 | 0x26D92     |      159122 |
|       8 | 0xA677      |       42615 |
|       9 | 0x0000      |           0 |
|      10 | 0x0028      |          40 |
|      11 | 0x25247     |      152135 |
|      12 | 0xA65E      |       42590 |
|      13 | 0x00BF      |         191 |
|      14 | 0xFFFF1720  |  4294907680 |
|      15 | 0xFFFE5676  |  4294858358 |
|      16 | 0x0C10      |        3088 |
|      17 | 0xFFFF1F3C  |  4294909756 |
|      18 | 0xFFFE4682  |  4294854274 |
|      19 | 0x08BC      |        2236 |
|      20 | 0x0003      |           3 |
|      21 | 0x000C      |          12 |
|      22 | 0x00E9      |         233 |
|      23 | 0x008F      |         143 |
|      24 | 0x0017      |          23 |
|      25 | 0x2639D     |      156573 |
|      26 | 0xA19B      |       41371 |
|      27 | 0x27680     |      161408 |
|      28 | 0xAA93      |       43667 |

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 32 00 80 1F 00 04 80 05  80 06 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0010 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0013 [0x1F] MOVE_ENTITY: EventEntity moves to X=280.915*, Z=20.097*, Y=0.242*
  2: 0x001B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001D [0x00] END_REQSTACK()
```

### Event 118

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            00                   . 
```

#### Opcodes

```
  0: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               32                 2
0020: 00 80 1F 00 07 80 08 80  09 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=159.122*, Z=42.615*, Y=0.000*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         32 0A 80               2..
0030: 1F 00 0B 80 0C 80 0D 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x002D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=152.135*, Z=42.590*, Y=0.191*
  2: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003A [0x00] END_REQSTACK()
```

### Event 120

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   00                         .    
```

#### Opcodes

```
  0: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      32 00 80 1F              2...
0040: 00 0E 80 0F 80 10 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x003C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003F [0x1F] MOVE_ENTITY: EventEntity moves to X=-59.616*, Z=-108.938*, Y=3.088*
  2: 0x0047 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                32 00 80 1F 00 11            2.....
0050: 80 12 80 13 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x004A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004D [0x1F] MOVE_ENTITY: EventEntity moves to X=-57.540*, Z=-113.022*, Y=2.236*
  2: 0x0055 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0057 [0x00] END_REQSTACK()
```

### Event 122

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          B6 0B 14 80 15 80 16 80          ........
0060: 17 80 18 80 17 80 17 80  09 80 09 80 00           .............   
```

#### Opcodes

```
  0: 0x0058 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=12*, head=233*, body=143*, hands=23*, legs=143*, feet=143*, main=0*, sub=0*)
  1: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         32 0A 80               2..
0070: 1F 00 19 80 1A 80 09 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x006D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0070 [0x1F] MOVE_ENTITY: EventEntity moves to X=156.573*, Z=41.371*, Y=0.000*
  2: 0x0078 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007A [0x00] END_REQSTACK()
```

### Event 123

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   B6 0B 14 80 15             .....
0080: 80 16 80 17 80 18 80 17  80 17 80 09 80 09 80 00  ................
```

#### Opcodes

```
  0: 0x007B [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=12*, head=233*, body=143*, hands=23*, legs=143*, feet=143*, main=0*, sub=0*)
  1: 0x008F [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0090   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: 32 00 80 1F 00 1B 80 1C  80 09 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0090 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0093 [0x1F] MOVE_ENTITY: EventEntity moves to X=161.408*, Z=43.667*, Y=0.000*
  2: 0x009B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009D [0x00] END_REQSTACK()
```

### Event 125

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            B6 0B                ..
00A0: 14 80 15 80 16 80 17 80  18 80 17 80 17 80 09 80  ................
00B0: 09 80 00                                          ...             
```

#### Opcodes

```
  0: 0x009E [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=12*, head=233*, body=143*, hands=23*, legs=143*, feet=143*, main=0*, sub=0*)
  1: 0x00B2 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B3   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          B6 0B 14 80 15  80 16 80 17 80 18 80 17     .............
00C0: 80 17 80 09 80 09 80 00                           ........        
```

#### Opcodes

```
  0: 0x00B3 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=12*, head=233*, body=143*, hands=23*, legs=143*, feet=143*, main=0*, sub=0*)
  1: 0x00C7 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C8   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                          B6 0B 14 80 15 80 09 80          ........
00D0: 17 80 18 80 17 80 17 80  09 80 09 80 00           .............   
```

#### Opcodes

```
  0: 0x00C8 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=12*, head=0*, body=143*, hands=23*, legs=143*, feet=143*, main=0*, sub=0*)
  1: 0x00DC [0x00] END_REQSTACK()
```
