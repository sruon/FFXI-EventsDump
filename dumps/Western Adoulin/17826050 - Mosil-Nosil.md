# 17826050 - Mosil-Nosil

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 324 bytes                 |
| Total Events     | 10                        |
| References Count | 21                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [513](#event-513)        | 0x0001       |     47 |             11 |
| [2](#event-2)            | 0x0030       |      1 |              1 |
| [65535.1](#event-655351) | 0x0031       |     15 |              5 |
| [65535.2](#event-655352) | 0x0040       |     15 |              5 |
| [65535.3](#event-655353) | 0x004F       |     15 |              5 |
| [65535.4](#event-655354) | 0x005E       |     15 |              5 |
| [65535.5](#event-655355) | 0x006D       |     24 |              3 |
| [65535.6](#event-655356) | 0x0085       |     24 |              3 |
| [65535.7](#event-655357) | 0x009D       |     24 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x2633      |        9779 |
|       2 | 0x0022      |          34 |
|       3 | 0x2634      |        9780 |
|       4 | 0x000D      |          13 |
|       5 | 0x26A7      |        9895 |
|       6 | 0x0825      |        2085 |
|       7 | 0x0000      |           0 |
|       8 | 0xFFFDB610  |  4294817296 |
|       9 | 0xFFFFB5C8  |  4294948296 |
|      10 | 0x0F9F      |        3999 |
|      11 | 0xFFFFB1E0  |  4294947296 |
|      12 | 0xFFFFAEF2  |  4294946546 |
|      13 | 0x0002      |           2 |
|      14 | 0x0001      |           1 |
|      15 | 0x0023      |          35 |
|      16 | 0x001C      |          28 |
|      17 | 0x0066      |         102 |
|      18 | 0x0007      |           7 |
|      19 | 0x0009      |           9 |
|      20 | 0x0005      |           5 |

## String References

- **9779**: The risks involved in reaching Adoulin without using waypoints send shiver-wivers down my spine! Not to mention the expenses! The merchant in me is already vomitaruing at the thought!
- **9780**: Why won't someone from the high and mightaruy Twelve Orders show some kindness for once and throw us a bone? Especially that rascal Chero-Machero! I'm sick and tired of being bamboozle-woozled by him!

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

### Event 513

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
0010: FF FF 7F 74 68 6B 31 1D  01 80 23 66 02 80 F8 FF  ...thk1...#f....
0020: FF 7F F8 FF FF 7F 74 68  6B 32 1D 03 80 23 21 00  ......thk2...#!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=9779*)
    → "The risks involved in reaching Adoulin without using waypoints send shiver-wivers down my spine! Not to mention the expenses! The merchant in me is already vomitaruing at the thought!"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=34*
  7: 0x002A [0x1D] PRINT_EVENT_MESSAGE(message_id=9780*)
    → "Why won't someone from the high and mightaruy Twelve Orders show some kindness for once and throw us a bone? Especially that rascal Chero-Machero! I'm sick and tired of being bamboozle-woozled by him!"
  8: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002E [0x21] END_EVENT
 10: 0x002F [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0030  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    32 04 80 1F 00 05 80  06 80 07 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0031 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0034 [0x1F] MOVE_ENTITY: EventEntity moves to X=9.895*, Z=2.085*, Y=0.000*
  2: 0x003C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 32 04 80 1F 00 08 80 09  80 0A 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0040 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0043 [0x1F] MOVE_ENTITY: EventEntity moves to X=-150.000*, Z=-19.000*, Y=3.999*
  2: 0x004B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               32                 2
0050: 04 80 1F 00 08 80 0B 80  0A 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x004F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0052 [0x1F] MOVE_ENTITY: EventEntity moves to X=-150.000*, Z=-20.000*, Y=3.999*
  2: 0x005A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            32 04                2.
0060: 80 1F 00 08 80 0C 80 0A  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x005E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0061 [0x1F] MOVE_ENTITY: EventEntity moves to X=-150.000*, Z=-20.750*, Y=3.999*
  2: 0x0069 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 24 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         B6 0B 0D               ...
0070: 80 0E 80 07 80 0F 80 10  80 11 80 11 80 07 80 07  ................
0080: 80 C0 0E 80 00                                    .....           
```

#### Opcodes

```
  0: 0x006D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=2*, hair=1*, head=0*, body=35*, hands=28*, legs=102*, feet=102*, main=0*, sub=0*)
  1: 0x0081 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 24 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                B6 0B 12  80 0D 80 07 80 13 80 13       ...........
0090: 80 13 80 13 80 07 80 07  80 C0 0E 80 00           .............   
```

#### Opcodes

```
  0: 0x0085 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=2*, head=0*, body=9*, hands=9*, legs=9*, feet=9*, main=0*, sub=0*)
  1: 0x0099 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 24 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         B6 0B 14               ...
00A0: 80 0E 80 07 80 0F 80 10  80 11 80 11 80 07 80 07  ................
00B0: 80 C0 0E 80 00                                    .....           
```

#### Opcodes

```
  0: 0x009D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=1*, head=0*, body=35*, hands=28*, legs=102*, feet=102*, main=0*, sub=0*)
  1: 0x00B1 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x00B4 [0x00] END_REQSTACK()
```
