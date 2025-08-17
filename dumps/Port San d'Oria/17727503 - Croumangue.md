# 17727503 - Croumangue

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 212 bytes                 |
| Total Events     | 8                         |
| References Count | 16                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [523](#event-523)        | 0x0001       |     36 |             10 |
| [500](#event-500)        | 0x0025       |      1 |              1 |
| [65535.1](#event-655351) | 0x0026       |      1 |              1 |
| [65535.2](#event-655352) | 0x0027       |     23 |              5 |
| [65535.3](#event-655353) | 0x003E       |     33 |              7 |
| [792](#event-792)        | 0x005F       |      1 |              1 |
| [793](#event-793)        | 0x0060       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x1D4F      |        7503 |
|       2 | 0x001E      |          30 |
|       3 | 0xB798      |       47000 |
|       4 | 0xFFFF48CC  |  4294920396 |
|       5 | 0xFFFFFC18  |  4294966296 |
|       6 | 0x0758      |        1880 |
|       7 | 0x000D      |          13 |
|       8 | 0x80E8      |       33000 |
|       9 | 0xFFFF3544  |  4294915396 |
|      10 | 0x6590      |       26000 |
|      11 | 0xFFFF2734  |  4294911796 |
|      12 | 0x0400      |        1024 |
|      13 | 0xFFFEEAA8  |  4294896296 |
|      14 | 0xFFFFF061  |  4294963297 |
|      15 | 0xFFFFF060  |  4294963296 |

## String References

- **7503**: Greetings, traveler! (Shop Menu)

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

### Event 523

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 5E 69 64 6C 30  ...tlk0...#^idl0
0020: 1C 02 80 21 00                                    ...!.           
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7503*)
    → "Greetings, traveler! (Shop Menu)"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0020 [0x1C] WAIT(30* ticks)
  8: 0x0023 [0x21] END_EVENT
  9: 0x0024 [0x00] END_REQSTACK()
```

### Event 500

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0025  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                00                                      .          
```

#### Opcodes

```
  0: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.1

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

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      37  03 80 04 80 05 80 06 80         7........
0030: 32 07 80 1F 00 08 80 09  80 05 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0027 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=47.000*, z=-46.900*, y=-1.000*, direction=165.2°*
  1: 0x0030 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0033 [0x1F] MOVE_ENTITY: EventEntity moves to X=33.000*, Z=-51.900*, Y=-1.000*
  3: 0x003B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 33 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            37 0A                7.
0040: 80 0B 80 05 80 0C 80 32  07 80 1F 00 0A 80 0D 80  .......2........
0050: 0E 80 1F 01 1F 00 08 80  0D 80 0F 80 1F 01 00     ............... 
```

#### Opcodes

```
  0: 0x003E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=26.000*, z=-55.500*, y=-1.000*, direction=90.0°*
  1: 0x0047 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x004A [0x1F] MOVE_ENTITY: EventEntity moves to X=26.000*, Z=-71.000*, Y=-3.999*
  3: 0x0052 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0054 [0x1F] MOVE_ENTITY: EventEntity moves to X=33.000*, Z=-71.000*, Y=-4.000*
  5: 0x005C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x005E [0x00] END_REQSTACK()
```

### Event 792

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               00                 .
```

#### Opcodes

```
  0: 0x005F [0x00] END_REQSTACK()
```

### Event 793

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0060  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0060 [0x00] END_REQSTACK()
```
