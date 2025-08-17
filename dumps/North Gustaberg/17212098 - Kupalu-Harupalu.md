# 17212098 - Kupalu-Harupalu

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | North Gustaberg (ID: 106) |
| Block Size       | 164 bytes                 |
| Total Events     | 6                         |
| References Count | 8                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [256](#event-256)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     12 |              3 |
| [65535.2](#event-655352) | 0x000E       |     24 |              5 |
| [65535.3](#event-655353) | 0x0026       |     27 |              3 |
| [65535.4](#event-655354) | 0x0041       |     27 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFA8E6B  |  4294610539 |
|       1 | 0xFFFE6FC2  |  4294864834 |
|       2 | 0x390B      |       14603 |
|       3 | 0x00D8      |         216 |
|       4 | 0x0000      |           0 |
|       5 | 0x0001      |           1 |
|       6 | 0x0080      |         128 |
|       7 | 0x0026      |          38 |

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

### Event 256

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       33 01 37 00 80 01  80 02 80 03 80 00          3.7.........  
```

#### Opcodes

```
  0: 0x0002 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-356.757*, z=-102.462*, y=14.603*, direction=19.0°*
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 24 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            22 00                ".
0010: 2F 00 F8 FF FF 7F 92 01  F8 FF FF 7F 6C F8 FF FF  /...........l...
0020: 7F 04 80 05 80 00                                 ......          
```

#### Opcodes

```
  0: 0x000E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0010 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0016 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x001C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  4: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   6C F8  FF FF 7F 06 80 05 80 9F        l.........
0030: 07 80 F8 FF FF 7F F8 FF  FF 7F 6D 61 69 6E 04 80  ..........main..
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0026 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x002F [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[38*, 0*]
  2: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    6C F8 FF FF 7F 04 80  05 80 9F 07 80 F8 FF FF   l..............
0050: 7F F8 FF FF 7F 73 74 6F  70 04 80 00              .....stop...    
```

#### Opcodes

```
  0: 0x0041 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x004A [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "stop" with entities [EventEntity, EventEntity], work=[38*, 0*]
  2: 0x005B [0x00] END_REQSTACK()
```
