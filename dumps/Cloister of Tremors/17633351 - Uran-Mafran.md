# 17633351 - Uran-Mafran

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Cloister of Tremors (ID: 209) |
| Block Size       | 260 bytes                     |
| Total Events     | 10                            |
| References Count | 13                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |     16 |              2 |
| [65535.4](#event-655354) | 0x0037       |     50 |              5 |
| [65535.5](#event-655355) | 0x0069       |      1 |              1 |
| [65535.6](#event-655356) | 0x006A       |     10 |              2 |
| [65535.7](#event-655357) | 0x0074       |     10 |              2 |
| [65535.8](#event-655358) | 0x007E       |     16 |              5 |
| [32000](#event-32000)    | 0x008E       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x003C      |          60 |
|       2 | 0x002E      |          46 |
|       3 | 0x002A      |          42 |
|       4 | 0x6354      |       25428 |
|       5 | 0x7F68      |       32616 |
|       6 | 0xFFFFB7E3  |  4294948835 |
|       7 | 0x0560      |        1376 |
|       8 | 0x585E      |       22622 |
|       9 | 0x747E      |       29822 |
|      10 | 0xFFFFB8FF  |  4294949119 |
|      11 | 0x0620      |        1568 |
|      12 | 0x000D      |          13 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(60* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      66  02 80 F8 FF FF 7F F8 FF         f........
0030: FF 7F 00 FE FE FE 00                              .......         
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler 0xFEFEFE00 with entities [EventEntity, EventEntity], work=46*
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 50 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      81  00 F8 FF FF 7F 66 03 80         ......f..
0040: 47 10 0D 01 47 10 0D 01  77 6F 6E 32 66 02 80 F8  G...G...won2f...
0050: FF FF 7F F8 FF FF 7F 6D  67 63 30 53 F8 FF FF 7F  .......mgc0S....
0060: F8 FF FF 7F 6D 67 63 30  00                       ....mgc0.       
```

#### Opcodes

```
  0: 0x0037 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x003D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "won2" with entities [Uran-Mafran (ID: 17633351/0x010D1047), Uran-Mafran (ID: 17633351/0x010D1047)], work=42*
  2: 0x004C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "mgc0" with entities [EventEntity, EventEntity], work=46*
  3: 0x005B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "mgc0" with entities [EventEntity, EventEntity]
  4: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.5

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

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                37 04 80 05 80 06            7.....
0070: 80 07 80 00                                       ....            
```

#### Opcodes

```
  0: 0x006A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=25.428*, z=32.616*, y=-18.461*, direction=120.9°*
  1: 0x0073 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0074   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             37 08 80 09  80 0A 80 0B 80 00            7.........  
```

#### Opcodes

```
  0: 0x0074 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=22.622*, z=29.822*, y=-18.177*, direction=137.8°*
  1: 0x007D [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            22 00                ".
0080: 32 0C 80 1F 00 08 80 09  80 0A 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x007E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0080 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0083 [0x1F] MOVE_ENTITY: EventEntity moves to X=22.622*, Z=29.822*, Y=-18.177*
  3: 0x008B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x008D [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008E  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            92 01                ..
0090: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x008E [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0094 [0x00] END_REQSTACK()
```
