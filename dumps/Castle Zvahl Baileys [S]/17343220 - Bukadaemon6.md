# 17343220 - Bukadaemon6

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Castle Zvahl Baileys [S] (ID: 138) |
| Block Size       | 248 bytes                          |
| Total Events     | 10                                 |
| References Count | 19                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [14](#event-14)          | 0x0002       |      1 |              1 |
| [3](#event-3)            | 0x0003       |      1 |              1 |
| [65535.1](#event-655351) | 0x0004       |     14 |              4 |
| [65535.2](#event-655352) | 0x0012       |     14 |              4 |
| [65535.3](#event-655353) | 0x0020       |     14 |              4 |
| [65535.4](#event-655354) | 0x002E       |     47 |              7 |
| [65535.5](#event-655355) | 0x005D       |     10 |              2 |
| [65535.6](#event-655356) | 0x0067       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x19FB      |        6651 |
|       2 | 0xFFFFF1E6  |  4294963686 |
|       3 | 0xFFFFD91F  |  4294957343 |
|       4 | 0x0044      |          68 |
|       5 | 0x467D      |       18045 |
|       6 | 0x7C48      |       31816 |
|       7 | 0xFFFFD8DB  |  4294957275 |
|       8 | 0x0028      |          40 |
|       9 | 0xFFFFFF94  |  4294967188 |
|      10 | 0x0001      |           1 |
|      11 | 0xFFFFD8F0  |  4294957296 |
|      12 | 0x002D      |          45 |
|      13 | 0xFFFA9D25  |  4294614309 |
|      14 | 0x60D1      |       24785 |
|      15 | 0xFFFF76AC  |  4294932140 |
|      16 | 0x0000      |           0 |
|      17 | 0x003C      |          60 |
|      18 | 0x0080      |         128 |

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

### Event 1

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

### Event 14

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

### Event 3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             32 00 80 1F  00 01 80 02 80 03 80 1F      2...........
0010: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0004 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0007 [0x1F] MOVE_ENTITY: EventEntity moves to X=6.651*, Z=-3.610*, Y=-9.953*
  2: 0x000F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       32 04 80 1F 00 05  80 06 80 07 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0012 [0x32] ExtData[1]->MainSpeed = 68* * 0.1
  1: 0x0015 [0x1F] MOVE_ENTITY: EventEntity moves to X=18.045*, Z=31.816*, Y=-10.021*
  2: 0x001D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 32 08 80 1F 00 09 80 0A  80 0B 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0020 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0023 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.108*, Z=0.001*, Y=-10.000*
  2: 0x002B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 47 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            32 0C                2.
0030: 80 1F 00 0D 80 0E 80 0F  80 1F 01 CD 00 80 F8 A2  ................
0040: 08 01 F8 A2 08 01 73 30  30 31 10 80 1C 11 80 2C  ......s001.....,
0050: F4 A2 08 01 F4 A2 08 01  64 65 61 64 00           ........dead.   
```

#### Opcodes

```
  0: 0x002E [0x32] ExtData[1]->MainSpeed = 45* * 0.1
  1: 0x0031 [0x1F] MOVE_ENTITY: EventEntity moves to X=-352.987*, Z=24.785*, Y=-35.156*
  2: 0x0039 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003B [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "s001" with entities [04 (ID: 17343224/0x0108A2F8), 04 (ID: 17343224/0x0108A2F8)], work=[13*, 0*]
  4: 0x004C [0x1C] WAIT(60* ticks)
  5: 0x004F [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dead" with entities [Bukadaemon6 (ID: 17343220/0x0108A2F4), Bukadaemon6 (ID: 17343220/0x0108A2F4)]
  6: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         6C F4 A2               l..
0060: 08 01 10 80 0A 80 00                              .......         
```

#### Opcodes

```
  0: 0x005D [0x6C] FADE_ENTITY_COLOR(entity_id=Bukadaemon6 (ID: 17343220/0x0108A2F4), end_alpha=0*, fade_time=1*)
  1: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      6C  F4 A2 08 01 12 80 0A 80         l........
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0067 [0x6C] FADE_ENTITY_COLOR(entity_id=Bukadaemon6 (ID: 17343220/0x0108A2F4), end_alpha=128*, fade_time=1*)
  1: 0x0070 [0x00] END_REQSTACK()
```
