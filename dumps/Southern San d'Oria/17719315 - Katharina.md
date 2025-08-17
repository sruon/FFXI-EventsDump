# 17719315 - Katharina

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 188 bytes                     |
| Total Events     | 7                             |
| References Count | 11                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [532](#event-532)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      9 |              3 |
| [65535.2](#event-655352) | 0x000B       |     19 |              5 |
| [65535.3](#event-655353) | 0x001E       |     25 |              5 |
| [65535.4](#event-655354) | 0x0037       |     25 |              5 |
| [65535.5](#event-655355) | 0x0050       |     17 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFFFDD5BB  |  4294825403 |
|       2 | 0x838A      |       33674 |
|       3 | 0xFFFFF449  |  4294964297 |
|       4 | 0x000A      |          10 |
|       5 | 0x1EBA      |        7866 |
|       6 | 0x1EBD      |        7869 |
|       7 | 0xFFFDC9B1  |  4294822321 |
|       8 | 0x60F7      |       24823 |
|       9 | 0xFFFFF448  |  4294964296 |
|      10 | 0x001E      |          30 |

## String References

- **7866**: Maybe it's the weather, but we've been selling mulsum so fast, we can't keep up! We need another cask as soon as possible!
- **7869**: Oh... Well, I have to get back now, but could you bring another one extra quick? Thanks!

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

### Event 532

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       2F 00 13 60 0E 01  22 00 00                   /..`.."..     
```

#### Opcodes

```
  0: 0x0002 [0x2F] Katharina (ID: 17719315/0x010E6013)->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0008 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 00 80 1F 00             2....
0010: 01 80 02 80 03 80 1F 01  1E 12 60 0E 01 00        ..........`...  
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-141.893*, Z=33.674*, Y=-2.999*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x1E] EventEntity looks at Raimbroy (ID: 17719314/0x010E6012) and starts talking
  4: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 25 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            66 04                f.
0020: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1D 05 80  .........tlk0...
0030: 23 5E 69 64 6C 30 00                              #^idl0.         
```

#### Opcodes

```
  0: 0x001E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
  1: 0x002D [0x1D] PRINT_EVENT_MESSAGE(message_id=7866*)
    → "Maybe it's the weather, but we've been selling mulsum so fast, we can't keep up! We need another cask as soon as possible!"
  2: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0031 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  4: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 25 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      66  04 80 F8 FF FF 7F F8 FF         f........
0040: FF 7F 74 6C 6B 30 1D 06  80 23 5E 69 64 6C 30 00  ..tlk0...#^idl0.
```

#### Opcodes

```
  0: 0x0037 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
  1: 0x0046 [0x1D] PRINT_EVENT_MESSAGE(message_id=7869*)
    → "Oh... Well, I have to get back now, but could you bring another one extra quick? Thanks!"
  2: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x004A [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  4: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 32 00 80 1F 00 07 80 08  80 09 80 1F 01 1C 0A 80  2...............
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0050 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0053 [0x1F] MOVE_ENTITY: EventEntity moves to X=-144.975*, Z=24.823*, Y=-3.000*
  2: 0x005B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005D [0x1C] WAIT(30* ticks)
  4: 0x0060 [0x00] END_REQSTACK()
```
