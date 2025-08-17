# 17412787 - Allenberge

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Castle Zvahl Keep [S] (ID: 155) |
| Block Size       | 264 bytes                       |
| Total Events     | 11                              |
| References Count | 19                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [16](#event-16)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |      4 |              2 |
| [65535.2](#event-655352) | 0x000C       |     15 |              5 |
| [65535.3](#event-655353) | 0x001B       |     18 |              6 |
| [65535.4](#event-655354) | 0x002D       |     15 |              5 |
| [17](#event-17)          | 0x003C       |      7 |              2 |
| [65535.5](#event-655355) | 0x0043       |     22 |              6 |
| [65535.6](#event-655356) | 0x0059       |     13 |              3 |
| [18](#event-18)          | 0x0066       |      7 |              2 |
| [65535.7](#event-655357) | 0x006D       |     19 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0028      |          40 |
|       2 | 0x1DB2F     |      121647 |
|       3 | 0x285A9     |      165289 |
|       4 | 0x03E7      |         999 |
|       5 | 0x000D      |          13 |
|       6 | 0xFFFC31E4  |  4294717924 |
|       7 | 0x1349B     |       79003 |
|       8 | 0xFFFF34E0  |  4294915296 |
|       9 | 0x001E      |          30 |
|      10 | 0xFFFC2406  |  4294714374 |
|      11 | 0x11AC9     |       72393 |
|      12 | 0xFFFA501D  |  4294594589 |
|      13 | 0xFFFE7C77  |  4294868087 |
|      14 | 0xFFFF34E1  |  4294915297 |
|      15 | 0x0007      |           7 |
|      16 | 0x0023      |          35 |
|      17 | 0xFFFA5966  |  4294596966 |
|      18 | 0xFFFE717F  |  4294865279 |

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

### Event 16

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          C0 00 80 00                      ....    
```

#### Opcodes

```
  0: 0x0008 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      32 01 80 1F              2...
0010: 00 02 80 03 80 04 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x000C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=121.647*, Z=165.289*, Y=0.999*
  2: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0019 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   32 05 80 1F 00             2....
0020: 06 80 07 80 08 80 1F 01  6F 1C 09 80 00           ........o....   
```

#### Opcodes

```
  0: 0x001B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001E [0x1F] MOVE_ENTITY: EventEntity moves to X=-249.372*, Z=79.003*, Y=-52.000*
  2: 0x0026 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0029 [0x1C] WAIT(30* ticks)
  5: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         32 05 80               2..
0030: 1F 00 0A 80 0B 80 08 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x002D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=-252.922*, Z=72.393*, Y=-52.000*
  2: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x003B [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      92 01 F8 FF              ....
0040: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x003C [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          32 01 80 1F 00  0C 80 0D 80 0E 80 1F 01     2............
0050: 1E AC B2 09 01 1C 09 80  00                       .........       
```

#### Opcodes

```
  0: 0x0043 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0046 [0x1F] MOVE_ENTITY: EventEntity moves to X=-372.707*, Z=-99.209*, Y=-51.999*
  2: 0x004E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0050 [0x1E] EventEntity looks at Volker (ID: 17412780/0x0109B2AC) and starts talking
  4: 0x0055 [0x1C] WAIT(30* ticks)
  5: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             6E B3 B2 09 01 0F 80           n......
0060: 99 B3 B2 09 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0059 [0x6E] Allenberge (ID: 17412787/0x0109B2B3) uses emote 7*
  1: 0x0060 [0x99] Wait for Allenberge (ID: 17412787/0x0109B2B3) animation to complete
  2: 0x0065 [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0066  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   92 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x0066 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         32 10 80               2..
0070: 1F 00 11 80 12 80 0E 80  1F 01 1E AC B2 09 01 00  ................
```

#### Opcodes

```
  0: 0x006D [0x32] ExtData[1]->MainSpeed = 35* * 0.1
  1: 0x0070 [0x1F] MOVE_ENTITY: EventEntity moves to X=-370.330*, Z=-102.017*, Y=-51.999*
  2: 0x0078 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007A [0x1E] EventEntity looks at Volker (ID: 17412780/0x0109B2AC) and starts talking
  4: 0x007F [0x00] END_REQSTACK()
```
