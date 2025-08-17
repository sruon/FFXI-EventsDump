# 16982246 - Bharifhal

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 216 bytes                     |
| Total Events     | 10                            |
| References Count | 14                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [3140](#event-3140)      | 0x0001       |      7 |              2 |
| [3215](#event-3215)      | 0x0008       |      1 |              1 |
| [65535.1](#event-655351) | 0x0009       |     22 |              6 |
| [65535.2](#event-655352) | 0x001F       |     22 |              6 |
| [3216](#event-3216)      | 0x0035       |      1 |              1 |
| [65535.3](#event-655353) | 0x0036       |     23 |              7 |
| [65535.4](#event-655354) | 0x004D       |     22 |              6 |
| [65535.5](#event-655355) | 0x0063       |      1 |              1 |
| [65535.6](#event-655356) | 0x0064       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x0411      |        1041 |
|       2 | 0xBFE0      |       49120 |
|       3 | 0x0000      |           0 |
|       4 | 0x001E      |          30 |
|       5 | 0x05F2      |        1522 |
|       6 | 0xC65E      |       50782 |
|       7 | 0x000B      |          11 |
|       8 | 0x052B      |        1323 |
|       9 | 0xBFC3      |       49091 |
|      10 | 0x000A      |          10 |
|      11 | 0x04D9      |        1241 |
|      12 | 0xC3F5      |       50165 |
|      13 | 0x0491      |        1169 |

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

### Event 3140

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

### Event 3215

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          00                               .       
```

#### Opcodes

```
  0: 0x0008 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0009   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             32 00 80 1F 00 01 80           2......
0010: 02 80 03 80 1F 01 1E F0  FF FF 7F 1C 04 80 00     ............... 
```

#### Opcodes

```
  0: 0x0009 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000C [0x1F] MOVE_ENTITY: EventEntity moves to X=1.041*, Z=49.120*, Y=0.000*
  2: 0x0014 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0016 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x001B [0x1C] WAIT(30* ticks)
  5: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               32                 2
0020: 00 80 1F 00 05 80 06 80  03 80 1F 01 1E F0 FF FF  ................
0030: 7F 1C 04 80 00                                    .....           
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.522*, Z=50.782*, Y=0.000*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0031 [0x1C] WAIT(30* ticks)
  5: 0x0034 [0x00] END_REQSTACK()
```

### Event 3216

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0035  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                00                                      .          
```

#### Opcodes

```
  0: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   32 07  80 1F 00 08 80 09 80 03        2.........
0040: 80 1F 01 6F 1E F0 FF FF  7F 1C 04 80 00           ...o.........   
```

#### Opcodes

```
  0: 0x0036 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0039 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.323*, Z=49.091*, Y=0.000*
  2: 0x0041 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0043 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0044 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0049 [0x1C] WAIT(30* ticks)
  6: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         32 0A 80               2..
0050: 1F 00 0B 80 0C 80 03 80  1F 01 6F 4B F8 FF FF 7F  ..........oK....
0060: 0D 80 00                                          ...             
```

#### Opcodes

```
  0: 0x004D [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x0050 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.241*, Z=50.165*, Y=0.000*
  2: 0x0058 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x005B [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=6.4°*)
  5: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          00                                          .            
```

#### Opcodes

```
  0: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0064  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             00                                        .           
```

#### Opcodes

```
  0: 0x0064 [0x00] END_REQSTACK()
```
