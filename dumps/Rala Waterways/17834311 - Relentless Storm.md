# 17834311 - Relentless Storm

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Rala Waterways (ID: 258) |
| Block Size       | 188 bytes                |
| Total Events     | 5                        |
| References Count | 13                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [2500](#event-2500)      | 0x0001       |     43 |              9 |
| [323](#event-323)        | 0x002C       |      7 |              2 |
| [65535.1](#event-655351) | 0x0033       |     34 |              8 |
| [65535.2](#event-655352) | 0x0055       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0045      |          69 |
|       1 | 0x1FBD      |        8125 |
|       2 | 0x0028      |          40 |
|       3 | 0xFFFB5BF5  |  4294663157 |
|       4 | 0xFFFB1BE3  |  4294646755 |
|       5 | 0xFFFFFC18  |  4294966296 |
|       6 | 0xFFFB619C  |  4294664604 |
|       7 | 0xFFFB178D  |  4294645645 |
|       8 | 0xFFFB5F47  |  4294664007 |
|       9 | 0xFFFAF657  |  4294637143 |
|      10 | 0x000D      |          13 |
|      11 | 0xFFFB4A12  |  4294658578 |
|      12 | 0xFFFADD76  |  4294630774 |

## String References

- **8125**: You stand at the Peacekeepers' Coalition's outpost in Rala Waterways. I, Relentless Storm, am in charge of our operations in the area.

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

### Event 2500

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 66 00 80 F8 FF  ...tlk0...#f....
0020: FF 7F F8 FF FF 7F 74 6C  6B 31 21 00              ......tlk1!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=69*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=8125*)
    → "You stand at the Peacekeepers' Coalition's outpost in Rala Waterways. I, Relentless Storm, am in charge of our operations in the area."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=69*
  7: 0x002A [0x21] END_EVENT
  8: 0x002B [0x00] END_REQSTACK()
```

### Event 323

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002C  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      92 01 F8 FF              ....
0030: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x002C [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          32 02 80 1F 00  03 80 04 80 05 80 1F 01     2............
0040: 1F 00 06 80 07 80 05 80  1F 01 1F 00 08 80 09 80  ................
0050: 05 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0033 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=-304.139*, Z=-320.541*, Y=-1.000*
  2: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0040 [0x1F] MOVE_ENTITY: EventEntity moves to X=-302.692*, Z=-321.651*, Y=-1.000*
  4: 0x0048 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x004A [0x1F] MOVE_ENTITY: EventEntity moves to X=-303.289*, Z=-330.153*, Y=-1.000*
  6: 0x0052 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                32 0A 80  1F 00 0B 80 0C 80 05 80       2..........
0060: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0055 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0058 [0x1F] MOVE_ENTITY: EventEntity moves to X=-308.718*, Z=-336.522*, Y=-1.000*
  2: 0x0060 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0062 [0x00] END_REQSTACK()
```
