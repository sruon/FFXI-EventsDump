# 17412784 - Leki Shameene

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Castle Zvahl Keep [S] (ID: 155) |
| Block Size       | 232 bytes                       |
| Total Events     | 10                              |
| References Count | 15                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [16](#event-16)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |      4 |              2 |
| [65535.2](#event-655352) | 0x000C       |     22 |              6 |
| [65535.3](#event-655353) | 0x0022       |     14 |              4 |
| [17](#event-17)          | 0x0030       |      7 |              2 |
| [65535.4](#event-655354) | 0x0037       |     22 |              6 |
| [65535.5](#event-655355) | 0x004D       |     13 |              3 |
| [18](#event-18)          | 0x005A       |      7 |              2 |
| [65535.6](#event-655356) | 0x0061       |     19 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0028      |          40 |
|       2 | 0x1E8EB     |      125163 |
|       3 | 0x27D2F     |      163119 |
|       4 | 0x039A      |         922 |
|       5 | 0x001E      |          30 |
|       6 | 0x208BC     |      133308 |
|       7 | 0x29B30     |      170800 |
|       8 | 0x0183      |         387 |
|       9 | 0xFFFA5CE8  |  4294597864 |
|      10 | 0xFFFE73C5  |  4294865861 |
|      11 | 0xFFFF34E1  |  4294915297 |
|      12 | 0x000C      |          12 |
|      13 | 0xFFFA6026  |  4294598694 |
|      14 | 0xFFFE7B33  |  4294867763 |

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
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      32 01 80 1F              2...
0010: 00 02 80 03 80 04 80 1F  01 1E B6 B2 09 01 1C 05  ................
0020: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x000C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=125.163*, Z=163.119*, Y=0.922*
  2: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0019 [0x1E] EventEntity looks at Klara (ID: 17412790/0x0109B2B6) and starts talking
  4: 0x001E [0x1C] WAIT(30* ticks)
  5: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       32 01 80 1F 00 06  80 07 80 08 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0022 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=133.308*, Z=170.800*, Y=0.387*
  2: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002F [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0030  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0030 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      32  01 80 1F 00 09 80 0A 80         2........
0040: 0B 80 1F 01 1E B3 B2 09  01 1C 05 80 00           .............   
```

#### Opcodes

```
  0: 0x0037 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003A [0x1F] MOVE_ENTITY: EventEntity moves to X=-369.432*, Z=-101.435*, Y=-51.999*
  2: 0x0042 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0044 [0x1E] EventEntity looks at Allenberge (ID: 17412787/0x0109B2B3) and starts talking
  4: 0x0049 [0x1C] WAIT(30* ticks)
  5: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         6E B0 B2               n..
0050: 09 01 0C 80 99 B0 B2 09  01 00                    ..........      
```

#### Opcodes

```
  0: 0x004D [0x6E] Leki Shameene (ID: 17412784/0x0109B2B0) uses emote 12*
  1: 0x0054 [0x99] Wait for Leki Shameene (ID: 17412784/0x0109B2B0) animation to complete
  2: 0x0059 [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                92 01 F8 FF FF 7F            ......
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x005A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    32 01 80 1F 00 0D 80  0E 80 0B 80 1F 01 1E AC   2..............
0070: B2 09 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0061 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0064 [0x1F] MOVE_ENTITY: EventEntity moves to X=-368.602*, Z=-99.533*, Y=-51.999*
  2: 0x006C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006E [0x1E] EventEntity looks at Volker (ID: 17412780/0x0109B2AC) and starts talking
  4: 0x0073 [0x00] END_REQSTACK()
```
