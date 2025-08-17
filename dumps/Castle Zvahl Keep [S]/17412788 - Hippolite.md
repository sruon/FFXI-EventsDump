# 17412788 - Hippolite

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Castle Zvahl Keep [S] (ID: 155) |
| Block Size       | 252 bytes                       |
| Total Events     | 10                              |
| References Count | 17                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [16](#event-16)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |      4 |              2 |
| [65535.2](#event-655352) | 0x000C       |     22 |              6 |
| [65535.3](#event-655353) | 0x0022       |     22 |              6 |
| [65535.4](#event-655354) | 0x0038       |     22 |              6 |
| [65535.5](#event-655355) | 0x004E       |     13 |              3 |
| [17](#event-17)          | 0x005B       |      7 |              2 |
| [18](#event-18)          | 0x0062       |      7 |              2 |
| [65535.6](#event-655356) | 0x0069       |     22 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0028      |          40 |
|       2 | 0x1B491     |      111761 |
|       3 | 0x2776A     |      161642 |
|       4 | 0x04E1      |        1249 |
|       5 | 0x001E      |          30 |
|       6 | 0x1DC22     |      121890 |
|       7 | 0x27A64     |      162404 |
|       8 | 0x03E7      |         999 |
|       9 | 0xFFFA5583  |  4294595971 |
|      10 | 0xFFFE8290  |  4294869648 |
|      11 | 0xFFFF34E1  |  4294915297 |
|      12 | 0x0024      |          36 |
|      13 | 0x000F      |          15 |
|      14 | 0x0021      |          33 |
|      15 | 0xFFFA5E36  |  4294598198 |
|      16 | 0xFFFE7632  |  4294866482 |

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
0010: 00 02 80 03 80 04 80 1F  01 1E B3 B2 09 01 1C 05  ................
0020: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x000C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=111.761*, Z=161.642*, Y=1.249*
  2: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0019 [0x1E] EventEntity looks at Allenberge (ID: 17412787/0x0109B2B3) and starts talking
  4: 0x001E [0x1C] WAIT(30* ticks)
  5: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       32 01 80 1F 00 06  80 07 80 08 80 1F 01 1E    2.............
0030: B6 B2 09 01 1C 05 80 00                           ........        
```

#### Opcodes

```
  0: 0x0022 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=121.890*, Z=162.404*, Y=0.999*
  2: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002F [0x1E] EventEntity looks at Klara (ID: 17412790/0x0109B2B6) and starts talking
  4: 0x0034 [0x1C] WAIT(30* ticks)
  5: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          32 01 80 1F 00 09 80 0A          2.......
0040: 80 0B 80 1F 01 1E AC B2  09 01 1C 05 80 00        ..............  
```

#### Opcodes

```
  0: 0x0038 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003B [0x1F] MOVE_ENTITY: EventEntity moves to X=-371.325*, Z=-97.648*, Y=-51.999*
  2: 0x0043 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0045 [0x1E] EventEntity looks at Volker (ID: 17412780/0x0109B2AC) and starts talking
  4: 0x004A [0x1C] WAIT(30* ticks)
  5: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            6E B4                n.
0050: B2 09 01 0C 80 99 B4 B2  09 01 00                 ...........     
```

#### Opcodes

```
  0: 0x004E [0x6E] Hippolite (ID: 17412788/0x0109B2B4) uses emote 36*
  1: 0x0055 [0x99] Wait for Hippolite (ID: 17412788/0x0109B2B4) animation to complete
  2: 0x005A [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005B  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   92 01 F8 FF FF             .....
0060: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x005B [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0061 [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0062  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x0062 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             1C 0D 80 32 0E 80 1F           ...2...
0070: 00 0F 80 10 80 0B 80 1F  01 1E AC B2 09 01 00     ............... 
```

#### Opcodes

```
  0: 0x0069 [0x1C] WAIT(15* ticks)
  1: 0x006C [0x32] ExtData[1]->MainSpeed = 33* * 0.1
  2: 0x006F [0x1F] MOVE_ENTITY: EventEntity moves to X=-369.098*, Z=-100.814*, Y=-51.999*
  3: 0x0077 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0079 [0x1E] EventEntity looks at Volker (ID: 17412780/0x0109B2AC) and starts talking
  5: 0x007E [0x00] END_REQSTACK()
```
