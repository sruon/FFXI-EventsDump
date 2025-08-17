# 17723422 - Oiheaurese

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 212 bytes                     |
| Total Events     | 7                             |
| References Count | 13                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65](#event-65)          | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     17 |              6 |
| [65535.2](#event-655352) | 0x001C       |     19 |              3 |
| [65535.3](#event-655353) | 0x002F       |     29 |              3 |
| [65535.4](#event-655354) | 0x004C       |     19 |              3 |
| [16](#event-16)          | 0x005F       |     18 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x18048     |       98376 |
|       1 | 0x1D6D3     |      120531 |
|       2 | 0x0000      |           0 |
|       3 | 0x03B8      |         952 |
|       4 | 0x000D      |          13 |
|       5 | 0x18350     |       99152 |
|       6 | 0x1C990     |      117136 |
|       7 | 0x0019      |          25 |
|       8 | 0x005A      |          90 |
|       9 | 0x003C      |          60 |
|      10 | 0x1E81E     |      124958 |
|      11 | 0x1B4DA     |      111834 |
|      12 | 0x0A21      |        2593 |

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

### Event 65

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=98.376*, z=120.531*, y=0.000*, direction=83.7°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 17 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   22 00 32 04 80             ".2..
0010: 1F 00 05 80 06 80 02 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x000B [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x000D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0010 [0x1F] MOVE_ENTITY: EventEntity moves to X=99.152*, Z=117.136*, Y=0.000*
  3: 0x0018 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x001A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x001B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      5B 07 80 F8              [...
0020: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1C 08 80 00     .......tlk0.... 
```

#### Opcodes

```
  0: 0x001C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=25*
  1: 0x002B [0x1C] WAIT(90* ticks)
  2: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               5B                 [
0030: 07 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 53 F8  ..........tlk1S.
0040: FF FF 7F F8 FF FF 7F 74  6C 6B 31 00              .......tlk1.    
```

#### Opcodes

```
  0: 0x002F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=25*
  1: 0x003E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      5B 07 80 F8              [...
0050: FF FF 7F F8 FF FF 7F 74  68 6B 30 1C 09 80 00     .......thk0.... 
```

#### Opcodes

```
  0: 0x004C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk0" with entities [EventEntity, EventEntity], work=25*
  1: 0x005B [0x1C] WAIT(60* ticks)
  2: 0x005E [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               22                 "
0060: 00 92 01 F8 FF FF 7F 37  0A 80 0B 80 02 80 0C 80  .......7........
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x005F [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0061 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0067 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=124.958*, z=111.834*, y=0.000*, direction=227.9°*
  3: 0x0070 [0x00] END_REQSTACK()
```
