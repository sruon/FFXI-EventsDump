# 17764366 - Gomada-Vulmada

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 208 bytes                |
| Total Events     | 9                        |
| References Count | 13                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     19 |              3 |
| [65535.3](#event-655353) | 0x0024       |      9 |              3 |
| [65535.4](#event-655354) | 0x002D       |     35 |              8 |
| [65535.5](#event-655355) | 0x0050       |     15 |              5 |
| [11](#event-11)          | 0x005F       |      1 |              1 |
| [367](#event-367)        | 0x0060       |      1 |              1 |
| [65535.6](#event-655356) | 0x0061       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0055      |          85 |
|       1 | 0x001E      |          30 |
|       2 | 0x3458      |       13400 |
|       3 | 0xFFFF4958  |  4294920536 |
|       4 | 0x07CF      |        1999 |
|       5 | 0x0EF5      |        3829 |
|       6 | 0x0015      |          21 |
|       7 | 0x4FAA      |       20394 |
|       8 | 0xFFFF5850  |  4294924368 |
|       9 | 0x43DD      |       17373 |
|      10 | 0xFFFF9FF4  |  4294942708 |
|      11 | 0x054A      |        1354 |
|      12 | 0x20AB      |        8363 |

## String References

- **8363**: He\`y, don't run so fasty-wasty!

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 6A 6D 70 30   [..........jmp0
0020: 1C 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0011 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "jmp0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0020 [0x1C] WAIT(30* ticks)
  2: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             5E 69 64 6C  30 1C 01 80 00               ^idl0....   
```

#### Opcodes

```
  0: 0x0024 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0029 [0x1C] WAIT(30* ticks)
  2: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 35 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         37 02 80               7..
0030: 03 80 04 80 05 80 4E 00  0E 10 0F 01 32 06 80 1F  ......N.....2...
0040: 00 07 80 08 80 04 80 1F  01 6F 1E 0F 10 0F 01 00  .........o......
```

#### Opcodes

```
  0: 0x002D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=13.400*, z=-46.760*, y=1.999*, direction=336.5°*
  1: 0x0036 [0x4E] SET_ENTITY_HIDE_FLAG: Show Gomada-Vulmada (ID: 17764366/0x010F100E)
  2: 0x003C [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  3: 0x003F [0x1F] MOVE_ENTITY: EventEntity moves to X=20.394*, Z=-42.928*, Y=1.999*
  4: 0x0047 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0049 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x004A [0x1E] EventEntity looks at Nanaa Mihgo (ID: 17764367/0x010F100F) and starts talking
  7: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 32 06 80 1F 00 09 80 0A  80 0B 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0050 [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  1: 0x0053 [0x1F] MOVE_ENTITY: EventEntity moves to X=17.373*, Z=-24.588*, Y=1.354*
  2: 0x005B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x005E [0x00] END_REQSTACK()
```

### Event 11

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

### Event 367

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

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0061  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    1D 0C 80 23 00                                  ...#.          
```

#### Opcodes

```
  0: 0x0061 [0x1D] PRINT_EVENT_MESSAGE(message_id=8363*)
    → "He`y, don't run so fasty-wasty!"
  1: 0x0064 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0065 [0x00] END_REQSTACK()
```
