# 17834312 - Soltargan

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Rala Waterways (ID: 258) |
| Block Size       | 284 bytes                |
| Total Events     | 8                        |
| References Count | 19                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [313](#event-313)        | 0x0001       |     47 |             11 |
| [323](#event-323)        | 0x0030       |      7 |              2 |
| [65535.1](#event-655351) | 0x0037       |     34 |              8 |
| [65535.2](#event-655352) | 0x0059       |     14 |              4 |
| [325](#event-325)        | 0x0067       |      7 |              2 |
| [65535.3](#event-655353) | 0x006E       |     14 |              4 |
| [326](#event-326)        | 0x007C       |     33 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0009      |           9 |
|       1 | 0x1FBE      |        8126 |
|       2 | 0x1FBF      |        8127 |
|       3 | 0x0028      |          40 |
|       4 | 0xFFFB5BF5  |  4294663157 |
|       5 | 0xFFFB1BE3  |  4294646755 |
|       6 | 0xFFFFFC18  |  4294966296 |
|       7 | 0xFFFB619C  |  4294664604 |
|       8 | 0xFFFB178D  |  4294645645 |
|       9 | 0xFFFB5F47  |  4294664007 |
|      10 | 0xFFFAF657  |  4294637143 |
|      11 | 0x000D      |          13 |
|      12 | 0xFFFB4A12  |  4294658578 |
|      13 | 0xFFFADD76  |  4294630774 |
|      14 | 0xFFFADB60  |  4294630240 |
|      15 | 0xFFFB403C  |  4294656060 |
|      16 | 0x001E      |          30 |
|      17 | 0x1F52      |        8018 |
|      18 | 0x1F53      |        8019 |

## String References

- **8018**: Please forgive us for the raptor incident.
- **8019**: That being said, shouldn't you be heading back to the Mummers' Coalition to let them know the raptors are safe and unharmed?
- **8126**: I wouldn't go past the gates if I were you...but if you're determined, make sure you're prepared for the dangers within.
- **8127**: And I don't just mean the monsters. Which gates are opening depends on the day and time, so if you aren't careful, you may find yourself in trouble should you need to beat a hasty retreat!

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

### Event 313

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 23 66  ...tlk0...#...#f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 21 00  ..........tlk1!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=9*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=8126*)
    → "I wouldn't go past the gates if I were you...but if you're determined, make sure you're prepared for the dangers within."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=8127*)
    → "And I don't just mean the monsters. Which gates are opening depends on the day and time, so if you aren't careful, you may find yourself in trouble should you need to beat a hasty retreat!"
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=9*
  9: 0x002E [0x21] END_EVENT
 10: 0x002F [0x00] END_REQSTACK()
```

### Event 323

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0030  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0030 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      32  03 80 1F 00 04 80 05 80         2........
0040: 06 80 1F 01 1F 00 07 80  08 80 06 80 1F 01 1F 00  ................
0050: 09 80 0A 80 06 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x0037 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003A [0x1F] MOVE_ENTITY: EventEntity moves to X=-304.139*, Z=-320.541*, Y=-1.000*
  2: 0x0042 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0044 [0x1F] MOVE_ENTITY: EventEntity moves to X=-302.692*, Z=-321.651*, Y=-1.000*
  4: 0x004C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x004E [0x1F] MOVE_ENTITY: EventEntity moves to X=-303.289*, Z=-330.153*, Y=-1.000*
  6: 0x0056 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             32 0B 80 1F 00 0C 80           2......
0060: 0D 80 06 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0059 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=-308.718*, Z=-336.522*, Y=-1.000*
  2: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0066 [0x00] END_REQSTACK()
```

### Event 325

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0067  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x0067 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x006D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            32 0B                2.
0070: 80 1F 00 0E 80 0F 80 06  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x006E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0071 [0x1F] MOVE_ENTITY: EventEntity moves to X=-337.056*, Z=-311.236*, Y=-1.000*
  2: 0x0079 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007B [0x00] END_REQSTACK()
```

### Event 326

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      1E F0 FF FF              ....
0080: 7F 1C 10 80 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ....f..........t
0090: 6C 6B 30 1D 11 80 23 1D  12 80 23 21 00           lk0...#...#!.   
```

#### Opcodes

```
  0: 0x007C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0081 [0x1C] WAIT(30* ticks)
  2: 0x0084 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=9*
  3: 0x0093 [0x1D] PRINT_EVENT_MESSAGE(message_id=8018*)
    → "Please forgive us for the raptor incident."
  4: 0x0096 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0097 [0x1D] PRINT_EVENT_MESSAGE(message_id=8019*)
    → "That being said, shouldn't you be heading back to the Mummers' Coalition to let them know the raptors are safe and unharmed?"
  6: 0x009A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x009B [0x21] END_EVENT
  8: 0x009C [0x00] END_REQSTACK()
```
