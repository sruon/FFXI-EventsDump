# 17756214 - Kohpo-Akuupo

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 288 bytes                |
| Total Events     | 9                        |
| References Count | 20                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [443](#event-443)        | 0x001A       |      7 |              2 |
| [261](#event-261)        | 0x0021       |     33 |             12 |
| [11](#event-11)          | 0x0042       |     10 |              2 |
| [65535.3](#event-655353) | 0x004C       |     10 |              2 |
| [65535.4](#event-655354) | 0x0056       |     38 |             10 |
| [209](#event-209)        | 0x007C       |     29 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x1E10      |        7696 |
|       3 | 0x1E11      |        7697 |
|       4 | 0x09B4      |        2484 |
|       5 | 0xFFFFFF7E  |  4294967166 |
|       6 | 0xFFFFDB3F  |  4294957887 |
|       7 | 0x0503      |        1283 |
|       8 | 0x807D      |       32893 |
|       9 | 0xFFFEE98E  |  4294896014 |
|      10 | 0xFFFFF9E3  |  4294965731 |
|      11 | 0x0F86      |        3974 |
|      12 | 0x00C8      |         200 |
|      13 | 0x0032      |          50 |
|      14 | 0x000D      |          13 |
|      15 | 0x2A6E      |       10862 |
|      16 | 0xFFFFDD6C  |  4294958444 |
|      17 | 0xFFFFDBE7  |  4294958055 |
|      18 | 0x02CC      |         716 |
|      19 | 0x1D8A      |        7562 |

## String References

- **7562**: There seems to have been a minor earthquake-o out in West Sarutabaruta the other day-o. I s'pose an airship-o dropped its cargo or somethin' naff like that-o...!
- **7696**: If you hear of any useful news-o, pass it onto me, won't ya? I'm hoping to give up this guard-o gig-o and try my hand at a spot of adventurin' meself.
- **7697**: It's just that lately, I hear reports from all over the place-o that the beastmen are on the move again. Come to think of it, perhaps it's not the right time-o to be either a guard-o or an adventurer, is it then!?

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
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 443

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                92 01 F8 FF FF 7F            ......
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x001A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 261

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    1E F0 FF FF 7F 6F 70  29 0B 36 F0 0E 01 01 1D   .....op).6.....
0030: 02 80 23 1D 03 80 23 29  0B 36 F0 0E 01 02 20 00  ..#...#).6.... .
0040: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0021 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0026 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0027 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0028 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohpo-Akuupo (ID: 17756214/0x010EF036), tag_num=0x01)
  4: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=7696*)
    → "If you hear of any useful news-o, pass it onto me, won't ya? I'm hoping to give up this guard-o gig-o and try my hand at a spot of adventurin' meself."
  5: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=7697*)
    → "It's just that lately, I hear reports from all over the place-o that the beastmen are on the move again. Come to think of it, perhaps it's not the right time-o to be either a guard-o or an adventurer, is it then!?"
  7: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0037 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohpo-Akuupo (ID: 17756214/0x010EF036), tag_num=0x02)
  9: 0x003E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0040 [0x21] END_EVENT
 11: 0x0041 [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       37 04 80 05 80 06  80 07 80 00                7.........    
```

#### Opcodes

```
  0: 0x0042 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=2.484*, z=-0.130*, y=-9.409*, direction=112.8°*
  1: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      37 08 80 09              7...
0050: 80 0A 80 0B 80 00                                 ......          
```

#### Opcodes

```
  0: 0x004C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=32.893*, z=-71.282*, y=-1.565*, direction=349.3°*
  1: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 38 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   29 0B  36 F0 0E 01 01 29 0B 36        ).6....).6
0060: F0 0E 01 02 1C 0C 80 1C  0D 80 32 0E 80 1F 00 0F  ..........2.....
0070: 80 10 80 11 80 1F 01 6F  39 12 80 00              .......o9...    
```

#### Opcodes

```
  0: 0x0056 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohpo-Akuupo (ID: 17756214/0x010EF036), tag_num=0x01)
  1: 0x005D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohpo-Akuupo (ID: 17756214/0x010EF036), tag_num=0x02)
  2: 0x0064 [0x1C] WAIT(200* ticks)
  3: 0x0067 [0x1C] WAIT(50* ticks)
  4: 0x006A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x006D [0x1F] MOVE_ENTITY: EventEntity moves to X=10.862*, Z=-8.852*, Y=-9.241*
  6: 0x0075 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0077 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0078 [0x39] SET_ENTITY_DIRECTION(direction=3.9°*)
  9: 0x007B [0x00] END_REQSTACK()
```

### Event 209

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      1E F0 FF FF              ....
0080: 7F 6F 70 29 0B 36 F0 0E  01 01 1D 13 80 23 29 0B  .op).6.......#).
0090: 36 F0 0E 01 02 20 00 21  00                       6.... .!.       
```

#### Opcodes

```
  0: 0x007C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0081 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0082 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0083 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohpo-Akuupo (ID: 17756214/0x010EF036), tag_num=0x01)
  4: 0x008A [0x1D] PRINT_EVENT_MESSAGE(message_id=7562*)
    → "There seems to have been a minor earthquake-o out in West Sarutabaruta the other day-o. I s'pose an airship-o dropped its cargo or somethin' naff like that-o...!"
  5: 0x008D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x008E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kohpo-Akuupo (ID: 17756214/0x010EF036), tag_num=0x02)
  7: 0x0095 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0097 [0x21] END_EVENT
  9: 0x0098 [0x00] END_REQSTACK()
```
