# 17105503 - Pattna-Ottna

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 184 bytes                        |
| Total Events     | 9                                |
| References Count | 11                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [63](#event-63)          | 0x0001       |      1 |              1 |
| [62](#event-62)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     20 |              6 |
| [65535.2](#event-655352) | 0x0017       |     15 |              5 |
| [89](#event-89)          | 0x0026       |      1 |              1 |
| [65535.3](#event-655353) | 0x0027       |     21 |              5 |
| [65535.4](#event-655354) | 0x003C       |     13 |              3 |
| [65535.5](#event-655355) | 0x0049       |     13 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x18358     |       99160 |
|       2 | 0xFFFF57A8  |  4294924200 |
|       3 | 0x03E7      |         999 |
|       4 | 0x1AAA5     |      109221 |
|       5 | 0xFFFF442B  |  4294919211 |
|       6 | 0x1DC97     |      122007 |
|       7 | 0x4368D     |      276109 |
|       8 | 0xFFFF158F  |  4294907279 |
|       9 | 0x012B      |         299 |
|      10 | 0x0002      |           2 |

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

### Event 63

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

### Event 62

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
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 6F 1E 5C 02 05 01 00                              o.\....         
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=99.160*, Z=-43.096*, Y=0.999*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0011 [0x1E] EventEntity looks at Tihl Midurhi (ID: 17105500/0x0105025C) and starts talking
  5: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      32  00 80 1F 00 04 80 05 80         2........
0020: 03 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0017 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=109.221*, Z=-48.085*, Y=0.999*
  2: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0024 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0025 [0x00] END_REQSTACK()
```

### Event 89

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0026  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   00                                    .         
```

#### Opcodes

```
  0: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      1F  00 06 80 07 80 08 80 1F         .........
0030: 01 6F 4A 5F 02 05 01 D4  02 05 01 00              .oJ_........    
```

#### Opcodes

```
  0: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=122.007*, Z=276.109*, Y=-60.017*
  1: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0031 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0032 [0x4A] Pattna-Ottna (ID: 17105503/0x0105025F) looks at Robel-Akbel (ID: 17105620/0x010502D4)
  4: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      6E F8 FF FF              n...
0040: 7F 09 80 99 F8 FF FF 7F  00                       .........       
```

#### Opcodes

```
  0: 0x003C [0x6E] EventEntity uses emote 299*
  1: 0x0043 [0x99] Wait for EventEntity animation to complete
  2: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             6E F8 FF FF 7F 0A 80           n......
0050: 99 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x0049 [0x6E] EventEntity uses emote 2*
  1: 0x0050 [0x99] Wait for EventEntity animation to complete
  2: 0x0055 [0x00] END_REQSTACK()
```
