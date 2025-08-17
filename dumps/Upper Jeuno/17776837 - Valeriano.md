# 17776837 - Valeriano

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 296 bytes             |
| Total Events     | 14                    |
| References Count | 19                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10139](#event-10139)    | 0x0001       |      7 |              2 |
| [10214](#event-10214)    | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     22 |              6 |
| [65535.2](#event-655352) | 0x0025       |     14 |              4 |
| [65535.3](#event-655353) | 0x0033       |     37 |              7 |
| [65535.4](#event-655354) | 0x0058       |     14 |              4 |
| [10151](#event-10151)    | 0x0066       |      1 |              1 |
| [10209](#event-10209)    | 0x0067       |      1 |              1 |
| [10210](#event-10210)    | 0x0068       |      1 |              1 |
| [10211](#event-10211)    | 0x0069       |      1 |              1 |
| [65535.5](#event-655355) | 0x006A       |     22 |              6 |
| [65535.6](#event-655356) | 0x0080       |      5 |              2 |
| [65535.7](#event-655357) | 0x0085       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFF2364  |  4294910820 |
|       2 | 0x18E08     |      101896 |
|       3 | 0x0000      |           0 |
|       4 | 0x001E      |          30 |
|       5 | 0xFFFF0FE8  |  4294905832 |
|       6 | 0x1A4FB     |      107771 |
|       7 | 0xFFFA8AA6  |  4294609574 |
|       8 | 0xFFFD561A  |  4294792730 |
|       9 | 0xFFFFD8EE  |  4294957294 |
|      10 | 0x0005      |           5 |
|      11 | 0xFFFA808D  |  4294606989 |
|      12 | 0xFFFD3C1A  |  4294786074 |
|      13 | 0xFFFFD6FB  |  4294956795 |
|      14 | 0xFFFF26B6  |  4294911670 |
|      15 | 0x19360     |      103264 |
|      16 | 0x0043      |          67 |
|      17 | 0xFFFE8DB7  |  4294872503 |
|      18 | 0x29B49     |      170825 |

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

### Event 10139

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

### Event 10214

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               32                 2
0010: 00 80 1F 00 01 80 02 80  03 80 1F 01 1E BD 40 0F  ..............@.
0020: 01 1C 04 80 00                                    .....           
```

#### Opcodes

```
  0: 0x000F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=-56.476*, Z=101.896*, Y=0.000*
  2: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001C [0x1E] EventEntity looks at Laila (ID: 17776829/0x010F40BD) and starts talking
  4: 0x0021 [0x1C] WAIT(30* ticks)
  5: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                32 00 80  1F 00 05 80 06 80 03 80       2..........
0030: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0025 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0028 [0x1F] MOVE_ENTITY: EventEntity moves to X=-61.464*, Z=107.771*, Y=0.000*
  2: 0x0030 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 37 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          32 00 80 1F 00  07 80 08 80 09 80 1F 01     2............
0040: 1E 33 40 0F 01 1C 04 80  66 0A 80 C5 40 0F 01 C5  .3@.....f...@...
0050: 40 0F 01 74 6C 62 30 00                           @..tlb0.        
```

#### Opcodes

```
  0: 0x0033 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=-357.722*, Z=-174.566*, Y=-10.002*
  2: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0040 [0x1E] EventEntity looks at Balkehr (ID: 17776691/0x010F4033) and starts talking
  4: 0x0045 [0x1C] WAIT(30* ticks)
  5: 0x0048 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [Valeriano (ID: 17776837/0x010F40C5), Valeriano (ID: 17776837/0x010F40C5)], work=5*
  6: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          32 00 80 1F 00 0B 80 0C          2.......
0060: 80 0D 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0058 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005B [0x1F] MOVE_ENTITY: EventEntity moves to X=-360.307*, Z=-181.222*, Y=-10.501*
  2: 0x0063 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0065 [0x00] END_REQSTACK()
```

### Event 10151

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0066  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   00                                    .         
```

#### Opcodes

```
  0: 0x0066 [0x00] END_REQSTACK()
```

### Event 10209

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0067  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      00                                  .        
```

#### Opcodes

```
  0: 0x0067 [0x00] END_REQSTACK()
```

### Event 10210

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0068  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          00                               .       
```

#### Opcodes

```
  0: 0x0068 [0x00] END_REQSTACK()
```

### Event 10211

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0069  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             00                             .      
```

#### Opcodes

```
  0: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                32 00 80 1F 00 0E            2.....
0070: 80 0F 80 03 80 1F 01 1E  BD 40 0F 01 1C 04 80 00  .........@......
```

#### Opcodes

```
  0: 0x006A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006D [0x1F] MOVE_ENTITY: EventEntity moves to X=-55.626*, Z=103.264*, Y=0.000*
  2: 0x0075 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0077 [0x1E] EventEntity looks at Laila (ID: 17776829/0x010F40BD) and starts talking
  4: 0x007C [0x1C] WAIT(30* ticks)
  5: 0x007F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0080  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: B6 0A 10 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0080 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Ranged, value=67*)
  1: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                32 00 80  1F 00 11 80 12 80 03 80       2..........
0090: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0085 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0088 [0x1F] MOVE_ENTITY: EventEntity moves to X=-94.793*, Z=170.825*, Y=0.000*
  2: 0x0090 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0092 [0x00] END_REQSTACK()
```
