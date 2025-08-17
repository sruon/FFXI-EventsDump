# 17719396 - Anxaberoute

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 256 bytes                     |
| Total Events     | 7                             |
| References Count | 15                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [503](#event-503)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [65535.2](#event-655352) | 0x000C       |     63 |             14 |
| [886](#event-886)        | 0x004B       |     65 |             11 |
| [957](#event-957)        | 0x008C       |      9 |              3 |
| [991](#event-991)        | 0x0095       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFED6E2  |  4294891234 |
|       1 | 0xFFFFA19C  |  4294943132 |
|       2 | 0xFFFFDF32  |  4294958898 |
|       3 | 0x0A10      |        2576 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFED1D8  |  4294889944 |
|       6 | 0xFFFFA6FF  |  4294944511 |
|       7 | 0xFFFFE31A  |  4294959898 |
|       8 | 0x0015      |          21 |
|       9 | 0xFFFEA987  |  4294879623 |
|      10 | 0xFFFFCF03  |  4294954755 |
|      11 | 0x0014      |          20 |
|      12 | 0x205B      |        8283 |
|      13 | 0x205C      |        8284 |
|      14 | 0x205D      |        8285 |

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

### Event 503

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-76.062*, z=-24.164*, y=-8.398*, direction=226.4°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 63 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      32 04 80 1F              2...
0010: 00 05 80 06 80 07 80 1F  01 6F 1E 61 60 0E 01 6F  .........o.a`..o
0020: 70 66 08 80 F8 FF FF 7F  F8 FF FF 7F 73 6C 30 30  pf..........sl00
0030: 53 F8 FF FF 7F F8 FF FF  7F 73 6C 30 30 1F 00 09  S........sl00...
0040: 80 0A 80 07 80 1F 01 6F  22 01 00                 .......o"..     
```

#### Opcodes

```
  0: 0x000C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-77.352*, Z=-22.785*, Y=-7.398*
  2: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0019 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001A [0x1E] EventEntity looks at Endracion (ID: 17719393/0x010E6061) and starts talking
  5: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0021 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sl00" with entities [EventEntity, EventEntity], work=21*
  8: 0x0030 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sl00" with entities [EventEntity, EventEntity]
  9: 0x003D [0x1F] MOVE_ENTITY: EventEntity moves to X=-87.673*, Z=-12.541*, Y=-7.398*
 10: 0x0045 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x0047 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 12: 0x0048 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
 13: 0x004A [0x00] END_REQSTACK()
```

### Event 886

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 65 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   4A 64 60 0E 01             Jd`..
0050: F0 FF FF 7F 66 0B 80 F8  FF FF 7F F8 FF FF 7F 74  ....f..........t
0060: 6C 6B 30 2B 64 60 0E 01  0C 80 23 2B 64 60 0E 01  lk0+d`....#+d`..
0070: 0D 80 23 2B 64 60 0E 01  0E 80 23 66 0B 80 F8 FF  ..#+d`....#f....
0080: FF 7F F8 FF FF 7F 74 6C  6B 31 21 00              ......tlk1!.    
```

#### Opcodes

```
  0: 0x004B [0x4A] Anxaberoute (ID: 17719396/0x010E6064) looks at LocalPlayer
  1: 0x0054 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  2: 0x0063 [0x2B] Anxaberoute (ID: 17719396/0x010E6064) [8283*]:
    → "Nothing to report...as usual. Although I suppose having nothing to report is a good thing."
  3: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x006B [0x2B] Anxaberoute (ID: 17719396/0x010E6064) [8284*]:
    → "It is quite a far cry from the days when our kingdom was under siege by the Orcish Bloodwing Horde led by the merciless Doggvdegg."
  5: 0x0072 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0073 [0x2B] Anxaberoute (ID: 17719396/0x010E6064) [8285*]:
    → "I still get weak in the knees when I recall the thunderous din raised by the footsteps of Doggvdegg's mighty bugard mount."
  7: 0x007A [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x007B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  9: 0x008A [0x21] END_EVENT
 10: 0x008B [0x00] END_REQSTACK()
```

### Event 957

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008C  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      2F 00 64 60              /.d`
0090: 0E 01 22 00 00                                    .."..           
```

#### Opcodes

```
  0: 0x008C [0x2F] Anxaberoute (ID: 17719396/0x010E6064)->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0092 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x0094 [0x00] END_REQSTACK()
```

### Event 991

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0095  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                00                                      .          
```

#### Opcodes

```
  0: 0x0095 [0x00] END_REQSTACK()
```
