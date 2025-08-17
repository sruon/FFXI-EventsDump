# 17494799 - Enkelados

## Common Data

| Field            | Value                                |
|------------------|--------------------------------------|
| Zone             | The Eldieme Necropolis [S] (ID: 175) |
| Block Size       | 244 bytes                            |
| Total Events     | 10                                   |
| References Count | 14                                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [48](#event-48)          | 0x0001       |      7 |              2 |
| [49](#event-49)          | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     42 |             10 |
| [65535.2](#event-655352) | 0x0039       |      7 |              3 |
| [65535.3](#event-655353) | 0x0040       |      7 |              3 |
| [65535.4](#event-655354) | 0x0047       |     16 |              2 |
| [65535.5](#event-655355) | 0x0057       |     14 |              2 |
| [65535.6](#event-655356) | 0x0065       |     16 |              2 |
| [65535.7](#event-655357) | 0x0075       |     14 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFC2194  |  4294713748 |
|       1 | 0x2070D     |      132877 |
|       2 | 0x00EB      |         235 |
|       3 | 0xFFFC0D2F  |  4294708527 |
|       4 | 0x2271E     |      141086 |
|       5 | 0x005B      |          91 |
|       6 | 0xFFFC0580  |  4294706560 |
|       7 | 0x24261     |      148065 |
|       8 | 0x0027      |          39 |
|       9 | 0xFFFC0826  |  4294707238 |
|      10 | 0x27585     |      161157 |
|      11 | 0x0001      |           1 |
|      12 | 0x0000      |           0 |
|      13 | 0x05AD      |        1453 |

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

### Event 48

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

### Event 49

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
| Data Size    | 42 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               1F                 .
0010: 00 00 80 01 80 02 80 1F  01 1F 00 03 80 04 80 05  ................
0020: 80 1F 01 1F 00 06 80 07  80 08 80 1F 01 1F 00 09  ................
0030: 80 0A 80 02 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-253.548*, Z=132.877*, Y=0.235*
  1: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=-258.769*, Z=141.086*, Y=0.091*
  3: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0023 [0x1F] MOVE_ENTITY: EventEntity moves to X=-260.736*, Z=148.065*, Y=0.039*
  5: 0x002B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=-260.058*, Z=161.157*, Y=0.235*
  7: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0037 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0039  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             AB 03 AC 01 0B 80 00           .......
```

#### Opcodes

```
  0: 0x0039 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x003B [0xAC] EventEntity->StatusEvent = 1*
  2: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0040  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: AC 01 0C 80 AB 04 00                              .......         
```

#### Opcodes

```
  0: 0x0040 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x0044 [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      5B  0D 80 F8 FF FF 7F F8 FF         [........
0050: FF 7F 64 72 61 32 00                              ..dra2.         
```

#### Opcodes

```
  0: 0x0047 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dra2" with entities [EventEntity, EventEntity], work=1453*
  1: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0060: 64 72 61 32 00                                    dra2.           
```

#### Opcodes

```
  0: 0x0057 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dra2" with entities [EventEntity, EventEntity]
  1: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                5B 0D 80  F8 FF FF 7F F8 FF FF 7F       [..........
0070: 64 72 6D 30 00                                    drm0.           
```

#### Opcodes

```
  0: 0x0065 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "drm0" with entities [EventEntity, EventEntity], work=1453*
  1: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                53 F8 FF  FF 7F F8 FF FF 7F 64 72       S........dr
0080: 6D 30 00                                          m0.             
```

#### Opcodes

```
  0: 0x0075 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "drm0" with entities [EventEntity, EventEntity]
  1: 0x0082 [0x00] END_REQSTACK()
```
