# 17850926 - Choubollet

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Foret de Hennetiel (ID: 262) |
| Block Size       | 876 bytes                    |
| Total Events     | 21                           |
| References Count | 30                           |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     47 |              5 |
| [65535.2](#event-655352)   | 0x0030       |     16 |              2 |
| [65535.3](#event-655353)   | 0x0040       |     14 |              2 |
| [65535.4](#event-655354)   | 0x004E       |     16 |              2 |
| [65535.5](#event-655355)   | 0x005E       |     14 |              2 |
| [65535.6](#event-655356)   | 0x006C       |     16 |              2 |
| [65535.7](#event-655357)   | 0x007C       |     14 |              2 |
| [65535.8](#event-655358)   | 0x008A       |     16 |              2 |
| [65535.9](#event-655359)   | 0x009A       |     14 |              2 |
| [65535.10](#event-6553510) | 0x00A8       |     29 |              3 |
| [65535.11](#event-6553511) | 0x00C5       |      9 |              3 |
| [65535.12](#event-6553512) | 0x00CE       |     16 |              4 |
| [65535.13](#event-6553513) | 0x00DE       |     16 |              4 |
| [2560](#event-2560)        | 0x00EE       |     31 |             10 |
| [2561](#event-2561)        | 0x010D       |    101 |             27 |
| [2562](#event-2562)        | 0x0172       |     45 |             14 |
| [2576](#event-2576)        | 0x019F       |    115 |             21 |
| [2577](#event-2577)        | 0x0212       |     30 |             11 |
| [2563](#event-2563)        | 0x0230       |     67 |             17 |
| [2564](#event-2564)        | 0x0273       |     26 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001D      |          29 |
|       1 | 0x0032      |          50 |
|       2 | 0x00A9      |         169 |
|       3 | 0x005B      |          91 |
|       4 | 0x001E      |          30 |
|       5 | 0x0007      |           7 |
|       6 | 0x000E      |          14 |
|       7 | 0x086D      |        2157 |
|       8 | 0x1D5E      |        7518 |
|       9 | 0x0350      |         848 |
|      10 | 0x0F5F      |        3935 |
|      11 | 0x0F5B      |        3931 |
|      12 | 0x1D5F      |        7519 |
|      13 | 0x1D60      |        7520 |
|      14 | 0x1D61      |        7521 |
|      15 | 0x1D62      |        7522 |
|      16 | 0x1D63      |        7523 |
|      17 | 0x1D64      |        7524 |
|      18 | 0x00C8      |         200 |
|      19 | 0x0000      |           0 |
|      20 | 0x003C      |          60 |
|      21 | 0x1D65      |        7525 |
|      22 | 0x1D66      |        7526 |
|      23 | 0x1D67      |        7527 |
|      24 | 0x1D68      |        7528 |
|      25 | 0x1D6B      |        7531 |
|      26 | 0x1D6C      |        7532 |
|      27 | 0x1D6D      |        7533 |
|      28 | 0x00C9      |         201 |
|      29 | 0x1D6E      |        7534 |

## String References

- **7518**: You think I would have some work to do for one of your ilk? Bah. I only deal with those who have $6 from the Pioneers' Coalition in Western Adoulin.
- **7519**: You are a pioneer, are you not? Surely you must have laid eyes on the noxious fumes rising up from the Zoldeff River while on duty!
- **7520**: They pose an obstacle, though not an unsurmountable one, for pioneer expeditions in the area. In fact, the Inventors' Coalition has devised portable boats to aid in crossing the river.
- **7521**: Yet all things come with a price. In this case, you will have to procure the materials yourself. Do that, and I will create such a device to assist you in traversing the toxic tributary.
- **7522**: Three $0 and one $1 and $2 each should be sufficient.
- **7523**: Do this for me, and I will construct a boat the likes of which you have never seen!
- **7524**: Finished already? That was quicker than I had anticipated. Hold on one moment, and I shall craft your reward.
- **7525**: It is done. Yet do not think a boat alone is sufficient for transport--you must first learn how to use it properly if you are to keep yourself safe.
- **7526**: Of course, practice makes perfect. Take your boat, cross the river once, and come back to me.
- **7527**: Boats are merely vessels for navigating the water. You must feel the currents, understand the eddies, and master the waves if you are to brave the river.
- **7528**: Cast off from the bank here, make your way to the other side, and return.
- **7531**: Boating is not merely about paddling, but also about controlling your center of gravity so as not to capsize. Have you learned this in your nautical jaunt?
- **7532**: ...Well done! From here, it is but a simple task to find where to set sail and lay anchor.
- **7533**: I am duly impressed with your skill and tenacity. Few are able to cross such venomous waters.
- **7534**: It is difficult to express with words the wondrous feeling of becoming one with your watercraft. The dangerous poisons in this river should pose no more of a threat than if you were sailing on a stream of afternoon tea.

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
| Data Size    | 47 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 1C 01 80 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ...f..........tl
0020: 6B 31 53 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 00  k1S........tlk1.
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x0010 [0x1C] WAIT(50* ticks)
  2: 0x0013 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  3: 0x0022 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  4: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 68 6B 31 00  f..........thk1.
```

#### Opcodes

```
  0: 0x0030 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 53 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 00        S........thk1.  
```

#### Opcodes

```
  0: 0x0040 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            66 00                f.
0050: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 32 00        .........thk2.  
```

#### Opcodes

```
  0: 0x004E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=29*
  1: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            53 F8                S.
0060: FF FF 7F F8 FF FF 7F 74  68 6B 32 00              .......thk2.    
```

#### Opcodes

```
  0: 0x005E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      66 02 80 F8              f...
0070: FF FF 7F F8 FF FF 7F 74  6C 6B 30 00              .......tlk0.    
```

#### Opcodes

```
  0: 0x006C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=169*
  1: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      53 F8 FF FF              S...
0080: 7F F8 FF FF 7F 74 6C 6B  30 00                    .....tlk0.      
```

#### Opcodes

```
  0: 0x007C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                66 02 80 F8 FF FF            f.....
0090: 7F F8 FF FF 7F 74 6C 6B  31 00                    .....tlk1.      
```

#### Opcodes

```
  0: 0x008A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=169*
  1: 0x0099 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                53 F8 FF FF 7F F8            S.....
00A0: FF FF 7F 74 6C 6B 31 00                           ...tlk1.        
```

#### Opcodes

```
  0: 0x009A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x00A7 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A8   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                          66 03 80 F8 FF FF 7F F8          f.......
00B0: FF FF 7F 70 61 73 30 53  F8 FF FF 7F F8 FF FF 7F  ...pas0S........
00C0: 70 61 73 30 00                                    pas0.           
```

#### Opcodes

```
  0: 0x00A8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=91*
  1: 0x00B7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  2: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C5  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                5E 69 64  6C 30 1C 04 80 00             ^idl0....  
```

#### Opcodes

```
  0: 0x00C5 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00CA [0x1C] WAIT(30* ticks)
  2: 0x00CD [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CE   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            6E 2E                n.
00D0: 62 10 01 05 80 99 2E 62  10 01 1C 04 80 00        b......b......  
```

#### Opcodes

```
  0: 0x00CE [0x6E] Choubollet (ID: 17850926/0x0110622E) uses emote 7*
  1: 0x00D5 [0x99] Wait for Choubollet (ID: 17850926/0x0110622E) animation to complete
  2: 0x00DA [0x1C] WAIT(30* ticks)
  3: 0x00DD [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DE   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                            6E 2E                n.
00E0: 62 10 01 06 80 99 2E 62  10 01 1C 04 80 00        b......b......  
```

#### Opcodes

```
  0: 0x00DE [0x6E] Choubollet (ID: 17850926/0x0110622E) uses emote 14*
  1: 0x00E5 [0x99] Wait for Choubollet (ID: 17850926/0x0110622E) animation to complete
  2: 0x00EA [0x1C] WAIT(30* ticks)
  3: 0x00ED [0x00] END_REQSTACK()
```

### Event 2560

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EE   |
| Data Size    | 31 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                            1E F0                ..
00F0: FF FF 7F 6F 70 27 08 2E  62 10 01 01 03 02 10 07  ...op'..b.......
0100: 80 1D 08 80 23 2A 08 2E  62 10 01 21 00           ....#*..b..!.   
```

#### Opcodes

```
  0: 0x00EE [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00F3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00F4 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00F5 [0x27] REQ_SET(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x01)
  4: 0x00FC [0x03] Work_Zone[2] = 2157*
  5: 0x0101 [0x1D] PRINT_EVENT_MESSAGE(message_id=7518*)
    → "You think I would have some work to do for one of your ilk? Bah. I only deal with those who have $6 from the Pioneers' Coalition in Western Adoulin."
  6: 0x0104 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0105 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Choubollet (ID: 17850926/0x0110622E))
  8: 0x010B [0x21] END_EVENT
  9: 0x010C [0x00] END_REQSTACK()
```

### Event 2561

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x010D    |
| Data Size    | 101 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         42 1E F0               B..
0110: FF FF 7F 6F 70 03 02 10  09 80 03 03 10 0A 80 03  ...op...........
0120: 04 10 0B 80 29 08 2E 62  10 01 02 1D 0C 80 23 29  ....)..b......#)
0130: 08 2E 62 10 01 03 29 08  2E 62 10 01 04 1D 0D 80  ..b...)..b......
0140: 23 29 08 2E 62 10 01 05  29 08 2E 62 10 01 06 1D  #)..b...)..b....
0150: 0E 80 23 1D 0F 80 23 29  08 2E 62 10 01 07 29 08  ..#...#)..b...).
0160: 2E 62 10 01 08 1D 10 80  23 29 08 2E 62 10 01 09  .b......#)..b...
0170: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x010D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x010E [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0113 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0114 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0115 [0x03] Work_Zone[2] = 848*
  5: 0x011A [0x03] Work_Zone[3] = 3935*
  6: 0x011F [0x03] Work_Zone[4] = 3931*
  7: 0x0124 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x02)
  8: 0x012B [0x1D] PRINT_EVENT_MESSAGE(message_id=7519*)
    → "You are a pioneer, are you not? Surely you must have laid eyes on the noxious fumes rising up from the Zoldeff River while on duty!"
  9: 0x012E [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x012F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x03)
 11: 0x0136 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x04)
 12: 0x013D [0x1D] PRINT_EVENT_MESSAGE(message_id=7520*)
    → "They pose an obstacle, though not an unsurmountable one, for pioneer expeditions in the area. In fact, the Inventors' Coalition has devised portable boats to aid in crossing the river."
 13: 0x0140 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0141 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x05)
 15: 0x0148 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x06)
 16: 0x014F [0x1D] PRINT_EVENT_MESSAGE(message_id=7521*)
    → "Yet all things come with a price. In this case, you will have to procure the materials yourself. Do that, and I will create such a device to assist you in traversing the toxic tributary."
 17: 0x0152 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0153 [0x1D] PRINT_EVENT_MESSAGE(message_id=7522*)
    → "Three $0 and one $1 and $2 each should be sufficient."
 19: 0x0156 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0157 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x07)
 21: 0x015E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x08)
 22: 0x0165 [0x1D] PRINT_EVENT_MESSAGE(message_id=7523*)
    → "Do this for me, and I will construct a boat the likes of which you have never seen!"
 23: 0x0168 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x0169 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x09)
 25: 0x0170 [0x21] END_EVENT
 26: 0x0171 [0x00] END_REQSTACK()
```

### Event 2562

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0172   |
| Data Size    | 45 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:       1E F0 FF FF 7F 6F  70 03 02 10 09 80 03 03    .....op.......
0180: 10 0A 80 03 04 10 0B 80  27 08 2E 62 10 01 01 1D  ........'..b....
0190: 0F 80 23 1D 10 80 23 2A  08 2E 62 10 01 21 00     ..#...#*..b..!. 
```

#### Opcodes

```
  0: 0x0172 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0177 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0178 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0179 [0x03] Work_Zone[2] = 848*
  4: 0x017E [0x03] Work_Zone[3] = 3935*
  5: 0x0183 [0x03] Work_Zone[4] = 3931*
  6: 0x0188 [0x27] REQ_SET(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x01)
  7: 0x018F [0x1D] PRINT_EVENT_MESSAGE(message_id=7522*)
    → "Three $0 and one $1 and $2 each should be sufficient."
  8: 0x0192 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0193 [0x1D] PRINT_EVENT_MESSAGE(message_id=7523*)
    → "Do this for me, and I will construct a boat the likes of which you have never seen!"
 10: 0x0196 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0197 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Choubollet (ID: 17850926/0x0110622E))
 12: 0x019D [0x21] END_EVENT
 13: 0x019E [0x00] END_REQSTACK()
```

### Event 2576

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x019F    |
| Data Size    | 115 bytes |
| Instructions | 21        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                               42                 B
01A0: 1E F0 FF FF 7F 6F 70 27  08 2E 62 10 01 0D 1D 11  .....op'..b.....
01B0: 80 23 45 12 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  .#E..........fdo
01C0: 31 13 80 55 12 80 F0 FF  FF 7F F0 FF FF 7F 66 64  1..U..........fd
01D0: 6F 31 1C 14 80 2A 08 2E  62 10 01 45 12 80 F0 FF  o1...*..b..E....
01E0: FF 7F F0 FF FF 7F 66 64  69 31 13 80 55 12 80 F0  ......fdi1..U...
01F0: FF FF 7F F0 FF FF 7F 66  64 69 31 1D 15 80 23 27  .......fdi1...#'
0200: 08 2E 62 10 01 0A 1D 16  80 23 2A 08 2E 62 10 01  ..b......#*..b..
0210: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x019F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x01A0 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x01A5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x01A6 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x01A7 [0x27] REQ_SET(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x0D)
  5: 0x01AE [0x1D] PRINT_EVENT_MESSAGE(message_id=7524*)
    → "Finished already? That was quicker than I had anticipated. Hold on one moment, and I shall craft your reward."
  6: 0x01B1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x01B2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x01C3 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  9: 0x01D2 [0x1C] WAIT(60* ticks)
 10: 0x01D5 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Choubollet (ID: 17850926/0x0110622E))
 11: 0x01DB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x01EC [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 13: 0x01FB [0x1D] PRINT_EVENT_MESSAGE(message_id=7525*)
    → "It is done. Yet do not think a boat alone is sufficient for transport--you must first learn how to use it properly if you are to keep yourself safe."
 14: 0x01FE [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x01FF [0x27] REQ_SET(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x0A)
 16: 0x0206 [0x1D] PRINT_EVENT_MESSAGE(message_id=7526*)
    → "Of course, practice makes perfect. Take your boat, cross the river once, and come back to me."
 17: 0x0209 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x020A [0x2A] GET_REQ_LEVEL(level=8, entity_id=Choubollet (ID: 17850926/0x0110622E))
 19: 0x0210 [0x21] END_EVENT
 20: 0x0211 [0x00] END_REQSTACK()
```

### Event 2577

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0212   |
| Data Size    | 30 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:       1E F0 FF FF 7F 6F  70 27 08 2E 62 10 01 01    .....op'..b...
0220: 1D 17 80 23 1D 18 80 23  2A 08 2E 62 10 01 21 00  ...#...#*..b..!.
```

#### Opcodes

```
  0: 0x0212 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0217 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0218 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0219 [0x27] REQ_SET(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x01)
  4: 0x0220 [0x1D] PRINT_EVENT_MESSAGE(message_id=7527*)
    → "Boats are merely vessels for navigating the water. You must feel the currents, understand the eddies, and master the waves if you are to brave the river."
  5: 0x0223 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0224 [0x1D] PRINT_EVENT_MESSAGE(message_id=7528*)
    → "Cast off from the bank here, make your way to the other side, and return."
  7: 0x0227 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0228 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Choubollet (ID: 17850926/0x0110622E))
  9: 0x022E [0x21] END_EVENT
 10: 0x022F [0x00] END_REQSTACK()
```

### Event 2563

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0230   |
| Data Size    | 67 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230: 42 1E F0 FF FF 7F 6F 70  29 08 2E 62 10 01 06 1D  B.....op)..b....
0240: 19 80 23 1D 1A 80 23 29  08 2E 62 10 01 07 29 08  ..#...#)..b...).
0250: 2E 62 10 01 08 1D 1B 80  23 29 08 2E 62 10 01 09  .b......#)..b...
0260: 45 1C 80 F8 FF FF 7F F8  FF FF 7F 71 73 74 63 13  E..........qstc.
0270: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0230 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0231 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0236 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0237 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0238 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x06)
  5: 0x023F [0x1D] PRINT_EVENT_MESSAGE(message_id=7531*)
    → "Boating is not merely about paddling, but also about controlling your center of gravity so as not to capsize. Have you learned this in your nautical jaunt?"
  6: 0x0242 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0243 [0x1D] PRINT_EVENT_MESSAGE(message_id=7532*)
    → "...Well done! From here, it is but a simple task to find where to set sail and lay anchor."
  8: 0x0246 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0247 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x07)
 10: 0x024E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x08)
 11: 0x0255 [0x1D] PRINT_EVENT_MESSAGE(message_id=7533*)
    → "I am duly impressed with your skill and tenacity. Few are able to cross such venomous waters."
 12: 0x0258 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0259 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x09)
 14: 0x0260 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 15: 0x0271 [0x21] END_EVENT
 16: 0x0272 [0x00] END_REQSTACK()
```

### Event 2564

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0273   |
| Data Size    | 26 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:          1E F0 FF FF 7F  6F 70 27 08 2E 62 10 01     .....op'..b..
0280: 01 1D 1D 80 23 2A 08 2E  62 10 01 21 00           ....#*..b..!.   
```

#### Opcodes

```
  0: 0x0273 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0278 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0279 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x027A [0x27] REQ_SET(priority=0x08, entity_id=Choubollet (ID: 17850926/0x0110622E), tag_num=0x01)
  4: 0x0281 [0x1D] PRINT_EVENT_MESSAGE(message_id=7534*)
    → "It is difficult to express with words the wondrous feeling of becoming one with your watercraft. The dangerous poisons in this river should pose no more of a threat than if you were sailing on a stream of afternoon tea."
  5: 0x0284 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0285 [0x2A] GET_REQ_LEVEL(level=8, entity_id=Choubollet (ID: 17850926/0x0110622E))
  7: 0x028B [0x21] END_EVENT
  8: 0x028C [0x00] END_REQSTACK()
```
