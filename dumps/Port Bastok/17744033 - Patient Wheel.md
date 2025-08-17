# 17744033 - Patient Wheel

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Port Bastok (ID: 236) |
| Block Size       | 408 bytes             |
| Total Events     | 11                    |
| References Count | 26                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [322](#event-322)        | 0x0001       |      1 |              1 |
| [323](#event-323)        | 0x0002       |      1 |              1 |
| [325](#event-325)        | 0x0003       |     13 |              7 |
| [326](#event-326)        | 0x0010       |     58 |             10 |
| [327](#event-327)        | 0x004A       |     64 |             14 |
| [328](#event-328)        | 0x008A       |     13 |              7 |
| [65535.1](#event-655351) | 0x0097       |     10 |              2 |
| [65535.2](#event-655352) | 0x00A1       |     30 |              7 |
| [65535.3](#event-655353) | 0x00BF       |     33 |              8 |
| [354](#event-354)        | 0x00E0       |     18 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x23EF      |        9199 |
|       1 | 0x003C      |          60 |
|       2 | 0x23DD      |        9181 |
|       3 | 0x23DE      |        9182 |
|       4 | 0x23EA      |        9194 |
|       5 | 0x23EB      |        9195 |
|       6 | 0x23EC      |        9196 |
|       7 | 0x23F0      |        9200 |
|       8 | 0xFFFE670B  |  4294862603 |
|       9 | 0x5706      |       22278 |
|      10 | 0xFFFFF705  |  4294964997 |
|      11 | 0x0FFF      |        4095 |
|      12 | 0x000B      |          11 |
|      13 | 0xFFFE74AA  |  4294866090 |
|      14 | 0x577F      |       22399 |
|      15 | 0xFFFE6BAB  |  4294863787 |
|      16 | 0x575F      |       22367 |
|      17 | 0xFFFE65A4  |  4294862244 |
|      18 | 0x5CB5      |       23733 |
|      19 | 0xFFFFF6F2  |  4294964978 |
|      20 | 0xFFFE64C1  |  4294862017 |
|      21 | 0x6864      |       26724 |
|      22 | 0xFFFFFCAE  |  4294966446 |
|      23 | 0x2706      |        9990 |
|      24 | 0x001E      |          30 |
|      25 | 0x270B      |        9995 |

## String References

- **9181**: Five $1. It's a small price to pay for saving someone's life, but...
- **9182**: Where am I gonna get my hands on goods like that?
- **9194**: There have been rumors of some weird eddy of darkness in a cave near Selbina that can take you to the Tavnazian Archipelago...
- **9195**: They say a guy who entered that patch of Emptiness never returned.
- **9196**: That story is still the talk of the town in Selbina. When your friend hears how dangerous it is, she'll give up on the idea, I'd say.
- **9199**: What's an adventurer doing back here? Look buddy, I've got all these boxes to sort through. If you're looking for work, try someplace else.
- **9200**: $3N$3$3AcL$3$3b$3Z[$3W
- **9990**: <Player>'s badge flashes brightly.
- **9995**: What's an adventurer doing back here? Look, buddy, I've got all these boxes to sort through. If you're looking for work, you should go to the Near East.

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

### Event 322

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

### Event 323

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 325

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          1E F0 FF FF 7F  6F 70 1D 00 80 23 21 00     .....op...#!.
```

#### Opcodes

```
  0: 0x0003 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0008 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0009 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=9199*)
    → "What's an adventurer doing back here? Look buddy, I've got all these boxes to sort through. If you're looking for work, try someplace else."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x21] END_EVENT
  6: 0x000F [0x00] END_REQSTACK()
```

### Event 326

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 58 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 03 00 00 03 10 66 01 80  A1 C0 0E 01 A1 C0 0E 01  .....f..........
0020: 74 68 6B 31 1D 02 80 23  1D 03 80 23 66 01 80 A1  thk1...#...#f...
0030: C0 0E 01 A1 C0 0E 01 74  68 6B 32 53 A1 C0 0E 01  .......thk2S....
0040: A1 C0 0E 01 74 68 6B 32  21 00                    ....thk2!.      
```

#### Opcodes

```
  0: 0x0010 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
  1: 0x0015 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Patient Wheel (ID: 17744033/0x010EC0A1), Patient Wheel (ID: 17744033/0x010EC0A1)], work=60*
  2: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=9181*)
    → "Five $1. It's a small price to pay for saving someone's life, but..."
  3: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=9182*)
    → "Where am I gonna get my hands on goods like that?"
  5: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Patient Wheel (ID: 17744033/0x010EC0A1), Patient Wheel (ID: 17744033/0x010EC0A1)], work=60*
  7: 0x003B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [Patient Wheel (ID: 17744033/0x010EC0A1), Patient Wheel (ID: 17744033/0x010EC0A1)]
  8: 0x0048 [0x21] END_EVENT
  9: 0x0049 [0x00] END_REQSTACK()
```

### Event 327

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 64 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                1E F0 FF FF 7F 6F            .....o
0050: 70 66 01 80 A1 C0 0E 01  A1 C0 0E 01 74 6C 6B 30  pf..........tlk0
0060: 1D 04 80 23 1D 05 80 23  1D 06 80 23 66 01 80 A1  ...#...#...#f...
0070: C0 0E 01 A1 C0 0E 01 74  6C 6B 31 53 A1 C0 0E 01  .......tlk1S....
0080: A1 C0 0E 01 74 6C 6B 31  21 00                    ....tlk1!.      
```

#### Opcodes

```
  0: 0x004A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x004F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0050 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0051 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Patient Wheel (ID: 17744033/0x010EC0A1), Patient Wheel (ID: 17744033/0x010EC0A1)], work=60*
  4: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=9194*)
    → "There have been rumors of some weird eddy of darkness in a cave near Selbina that can take you to the Tavnazian Archipelago..."
  5: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0064 [0x1D] PRINT_EVENT_MESSAGE(message_id=9195*)
    → "They say a guy who entered that patch of Emptiness never returned."
  7: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0068 [0x1D] PRINT_EVENT_MESSAGE(message_id=9196*)
    → "That story is still the talk of the town in Selbina. When your friend hears how dangerous it is, she'll give up on the idea, I'd say."
  9: 0x006B [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x006C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Patient Wheel (ID: 17744033/0x010EC0A1), Patient Wheel (ID: 17744033/0x010EC0A1)], work=60*
 11: 0x007B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [Patient Wheel (ID: 17744033/0x010EC0A1), Patient Wheel (ID: 17744033/0x010EC0A1)]
 12: 0x0088 [0x21] END_EVENT
 13: 0x0089 [0x00] END_REQSTACK()
```

### Event 328

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                1E F0 FF FF 7F 6F            .....o
0090: 70 1D 07 80 23 21 00                              p...#!.         
```

#### Opcodes

```
  0: 0x008A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x008F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0090 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0091 [0x1D] PRINT_EVENT_MESSAGE(message_id=9200*)
    → "$3N$3$3AcL$3$3b$3Z[$3W"
  4: 0x0094 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0095 [0x21] END_EVENT
  6: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      37  08 80 09 80 0A 80 0B 80         7........
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x0097 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-104.693*, z=22.278*, y=-2.299*, direction=359.9°*
  1: 0x00A0 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A1   |
| Data Size    | 30 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:    79 00 F8 FF FF 7F 07  C0 0E 01 32 0C 80 1F 00   y.........2....
00B0: 0D 80 0E 80 0A 80 1F 01  6F 1E 07 C0 0E 01 00     ........o...... 
```

#### Opcodes

```
  0: 0x00A1 [0x79] EventEntity looks at Kagetora (ID: 17743879/0x010EC007) (Basic look)
  1: 0x00AB [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  2: 0x00AE [0x1F] MOVE_ENTITY: EventEntity moves to X=-101.206*, Z=22.399*, Y=-2.299*
  3: 0x00B6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00B8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x00B9 [0x1E] EventEntity looks at Kagetora (ID: 17743879/0x010EC007) and starts talking
  6: 0x00BE [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BF   |
| Data Size    | 33 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               1F                 .
00C0: 00 0F 80 10 80 0A 80 1F  01 1F 00 11 80 12 80 13  ................
00D0: 80 1F 01 33 01 5A 00 14  80 15 80 16 80 5A 01 00  ...3.Z.......Z..
```

#### Opcodes

```
  0: 0x00BF [0x1F] MOVE_ENTITY: EventEntity moves to X=-103.509*, Z=22.367*, Y=-2.299*
  1: 0x00C7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00C9 [0x1F] MOVE_ENTITY: EventEntity moves to X=-105.052*, Z=23.733*, Y=-2.318*
  3: 0x00D1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00D3 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  5: 0x00D5 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-105.279*, Z=26.724*, Y=-0.850*
  6: 0x00DD [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  7: 0x00DF [0x00] END_REQSTACK()
```

### Event 354

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E0   |
| Data Size    | 18 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 42 48 17 80 1E F0 FF FF  7F 1C 18 80 1D 19 80 23  BH.............#
00F0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x00E0 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00E1 [0x48] [System] [9990*]:
    → "<Player>'s badge flashes brightly."
  2: 0x00E4 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x00E9 [0x1C] WAIT(30* ticks)
  4: 0x00EC [0x1D] PRINT_EVENT_MESSAGE(message_id=9995*)
    → "What's an adventurer doing back here? Look, buddy, I've got all these boxes to sort through. If you're looking for work, you should go to the Near East."
  5: 0x00EF [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00F0 [0x21] END_EVENT
  7: 0x00F1 [0x00] END_REQSTACK()
```
