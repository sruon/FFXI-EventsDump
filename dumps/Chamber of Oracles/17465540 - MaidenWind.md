# 17465540 - MaidenWind

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Chamber of Oracles (ID: 168) |
| Block Size       | 268 bytes                    |
| Total Events     | 9                            |
| References Count | 14                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [0](#event-0)            | 0x0001       |     18 |              4 |
| [1](#event-1)            | 0x0013       |     16 |              3 |
| [65535.1](#event-655351) | 0x0023       |     12 |              3 |
| [65535.2](#event-655352) | 0x002F       |     31 |              3 |
| [65535.3](#event-655353) | 0x004E       |     49 |              7 |
| [65535.4](#event-655354) | 0x007F       |     12 |              3 |
| [65535.5](#event-655355) | 0x008B       |     10 |              2 |
| [65535.6](#event-655356) | 0x0095       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0050      |          80 |
|       3 | 0x00B4      |         180 |
|       4 | 0x023B      |         571 |
|       5 | 0x023D      |         573 |
|       6 | 0x003C      |          60 |
|       7 | 0x00D2      |         210 |
|       8 | 0x0060      |          96 |
|       9 | 0x010E      |         270 |
|      10 | 0x2E584     |      189828 |
|      11 | 0xBFF0      |       49136 |
|      12 | 0xFFFFEB0D  |  4294961933 |
|      13 | 0x01C3      |         451 |

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

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 2F 00 F8 FF FF  7F 6C F8 FF FF 7F 00 80   "./.....l......
0010: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0009 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0012 [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          2F 00 F8 FF FF  7F 6C F8 FF FF 7F 00 80     /.....l......
0020: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0013 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0019 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  2: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          22 00 6C F8 FF  FF 7F 02 80 03 80 00        ".l......... 
```

#### Opcodes

```
  0: 0x0023 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0025 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=80*, fade_time=180*)
  2: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 31 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               5B                 [
0030: 04 80 F8 FF FF 7F F8 FF  FF 7F 00 FE FE FE 5B 05  ..............[.
0040: 80 F8 FF FF 7F F8 FF FF  7F 00 FE FE FE 00        ..............  
```

#### Opcodes

```
  0: 0x002F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [EventEntity, EventEntity], work=571*
  1: 0x003E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [EventEntity, EventEntity], work=573*
  2: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 49 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            81 00                ..
0050: F8 FF FF 7F 5B 05 80 F8  FF FF 7F F8 FF FF 7F 69  ....[..........i
0060: 6E 72 30 1C 06 80 6C F8  FF FF 7F 00 80 07 80 6B  nr0...l........k
0070: 69 64 6C 30 F8 FF FF 7F  81 01 F8 FF FF 7F 00     idl0........... 
```

#### Opcodes

```
  0: 0x004E [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0054 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "inr0" with entities [EventEntity, EventEntity], work=573*
  2: 0x0063 [0x1C] WAIT(60* ticks)
  3: 0x0066 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=210*)
  4: 0x006F [0x6B] STOP_AND_IDLE: EventEntity stops current action and resets to idle (animation="idl0")
  5: 0x0078 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  6: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               22                 "
0080: 00 6C F8 FF FF 7F 08 80  09 80 00                 .l.........     
```

#### Opcodes

```
  0: 0x007F [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0081 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=96*, fade_time=270*)
  2: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   6C F8 FF FF 7F             l....
0090: 02 80 01 80 00                                    .....           
```

#### Opcodes

```
  0: 0x008B [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=80*, fade_time=1*)
  1: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                37 0A 80  0B 80 0C 80 0D 80 00          7......... 
```

#### Opcodes

```
  0: 0x0095 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=189.828*, z=49.136*, y=-5.363*, direction=39.6°*
  1: 0x009E [0x00] END_REQSTACK()
```
