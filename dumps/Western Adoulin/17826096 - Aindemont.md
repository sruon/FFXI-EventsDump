# 17826096 - Aindemont

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 336 bytes                 |
| Total Events     | 10                        |
| References Count | 24                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [569](#event-569)        | 0x0001       |     47 |             11 |
| [2](#event-2)            | 0x0030       |      1 |              1 |
| [65535.1](#event-655351) | 0x0031       |     24 |              3 |
| [65535.2](#event-655352) | 0x0049       |     15 |              5 |
| [65535.3](#event-655353) | 0x0058       |     15 |              5 |
| [65535.4](#event-655354) | 0x0067       |     24 |              3 |
| [65535.5](#event-655355) | 0x007F       |     15 |              5 |
| [65535.6](#event-655356) | 0x008E       |     15 |              5 |
| [65535.7](#event-655357) | 0x009D       |     24 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x2686      |        9862 |
|       2 | 0x2687      |        9863 |
|       3 | 0x0001      |           1 |
|       4 | 0x000D      |          13 |
|       5 | 0x0000      |           0 |
|       6 | 0x0005      |           5 |
|       7 | 0x0028      |          40 |
|       8 | 0x65859     |      415833 |
|       9 | 0xFFFFAAC9  |  4294945481 |
|      10 | 0x0F9F      |        3999 |
|      11 | 0xFFFCAC70  |  4294749296 |
|      12 | 0xFFFF9E58  |  4294942296 |
|      13 | 0x0FA0      |        4000 |
|      14 | 0x0002      |           2 |
|      15 | 0xFFFE7960  |  4294867296 |
|      16 | 0xFFFFA240  |  4294943296 |
|      17 | 0x015E      |         350 |
|      18 | 0xFFFDB610  |  4294817296 |
|      19 | 0xFFFFB1E0  |  4294947296 |
|      20 | 0x0003      |           3 |
|      21 | 0x0156      |         342 |
|      22 | 0x0140      |         320 |
|      23 | 0x00EF      |         239 |

## String References

- **9862**: You would be sorely misinformed were you to believe that everyone in Adoulin supports the colonization effort.
- **9863**: A famous example would be the leader of the Peacekeepers' Coalition, Gratzigg. I personally think that his views on the topic are outdated and overly conservative, but to each his own.

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

### Event 569

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
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=9862*)
    → "You would be sorely misinformed were you to believe that everyone in Adoulin supports the colonization effort."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=9863*)
    → "A famous example would be the leader of the Peacekeepers' Coalition, Gratzigg. I personally think that his views on the topic are outdated and overly conservative, but to each his own."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
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
| Data Size    | 24 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    B6 0B 03 80 04 80 05  80 06 80 06 80 06 80 06   ...............
0040: 80 05 80 05 80 C0 03 80  00                       .........       
```

#### Opcodes

```
  0: 0x0031 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=13*, head=0*, body=5*, hands=5*, legs=5*, feet=5*, main=0*, sub=0*)
  1: 0x0045 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             32 07 80 1F 00 08 80           2......
0050: 09 80 0A 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0049 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x004C [0x1F] MOVE_ENTITY: EventEntity moves to X=415.833*, Z=-21.815*, Y=3.999*
  2: 0x0054 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0056 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          32 04 80 1F 00 0B 80 0C          2.......
0060: 80 0D 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0058 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005B [0x1F] MOVE_ENTITY: EventEntity moves to X=-218.000*, Z=-25.000*, Y=4.000*
  2: 0x0063 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0065 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 24 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      B6  0B 03 80 0E 80 05 80 00         .........
0070: 80 00 80 00 80 00 80 05  80 05 80 C0 03 80 00     ............... 
```

#### Opcodes

```
  0: 0x0067 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=2*, head=0*, body=20*, hands=20*, legs=20*, feet=20*, main=0*, sub=0*)
  1: 0x007B [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               32                 2
0080: 04 80 1F 00 0F 80 10 80  11 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x007F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0082 [0x1F] MOVE_ENTITY: EventEntity moves to X=-100.000*, Z=-24.000*, Y=0.350*
  2: 0x008A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x008C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x008D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008E   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            32 04                2.
0090: 80 1F 00 12 80 13 80 0A  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x008E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0091 [0x1F] MOVE_ENTITY: EventEntity moves to X=-150.000*, Z=-20.000*, Y=3.999*
  2: 0x0099 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x009C [0x00] END_REQSTACK()
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
00A0: 80 04 80 15 80 15 80 16  80 15 80 17 80 05 80 05  ................
00B0: 80 C0 03 80 00                                    .....           
```

#### Opcodes

```
  0: 0x009D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=13*, head=342*, body=342*, hands=320*, legs=342*, feet=239*, main=0*, sub=0*)
  1: 0x00B1 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x00B4 [0x00] END_REQSTACK()
```
