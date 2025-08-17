# 17195651 - Millechairale

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
| Block Size       | 188 bytes                   |
| Total Events     | 9                           |
| References Count | 9                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |     16 |              3 |
| [65535.1](#event-655351) | 0x0011       |      6 |              2 |
| [65535.2](#event-655352) | 0x0017       |      6 |              2 |
| [65535.3](#event-655353) | 0x001D       |      6 |              2 |
| [65535.4](#event-655354) | 0x0023       |      6 |              2 |
| [65535.5](#event-655355) | 0x0029       |     14 |              4 |
| [65535.6](#event-655356) | 0x0037       |     14 |              4 |
| [65535.7](#event-655357) | 0x0045       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFBAE95  |  4294684309 |
|       1 | 0x1786F     |       96367 |
|       2 | 0x5C69      |       23657 |
|       3 | 0x02F2      |         754 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFBAD34  |  4294683956 |
|       6 | 0x17D64     |       97636 |
|       7 | 0x5DA0      |       23968 |
|       8 | 0x0014      |          20 |

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    94 01 F8 FF FF 7F 37  00 80 01 80 02 80 03 80   ......7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-282.987*, z=96.367*, y=23.657*, direction=66.3°*
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    1E F0 FF FF 7F 00                               ......         
```

#### Opcodes

```
  0: 0x0011 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0017  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      1E  81 62 06 01 00                  ..b...   
```

#### Opcodes

```
  0: 0x0017 [0x1E] EventEntity looks at Vijartal (ID: 17195649/0x01066281) and starts talking
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         1E 82 62               ..b
0020: 06 01 00                                          ...             
```

#### Opcodes

```
  0: 0x001D [0x1E] EventEntity looks at Roido (ID: 17195650/0x01066282) and starts talking
  1: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0023  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          1E 80 62 06 01  00                          ..b...       
```

#### Opcodes

```
  0: 0x0023 [0x1E] EventEntity looks at Elmemague (ID: 17195648/0x01066280) and starts talking
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             32 04 80 1F 00 05 80           2......
0030: 06 80 07 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0029 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x002C [0x1F] MOVE_ENTITY: EventEntity moves to X=-283.340*, Z=97.636*, Y=23.968*
  2: 0x0034 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      32  04 80 1F 00 00 80 01 80         2........
0040: 02 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0037 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003A [0x1F] MOVE_ENTITY: EventEntity moves to X=-282.987*, Z=96.367*, Y=23.657*
  2: 0x0042 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                66 08 80  F8 FF FF 7F F8 FF FF 7F       f..........
0050: 70 61 73 30 53 F8 FF FF  7F F8 FF FF 7F 70 61 73  pas0S........pas
0060: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0045 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
  1: 0x0054 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  2: 0x0061 [0x00] END_REQSTACK()
```
