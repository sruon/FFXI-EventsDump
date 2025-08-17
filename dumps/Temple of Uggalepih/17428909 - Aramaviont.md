# 17428909 - Aramaviont

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Temple of Uggalepih (ID: 159) |
| Block Size       | 240 bytes                     |
| Total Events     | 5                             |
| References Count | 12                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [67](#event-67)          | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     37 |              9 |
| [65535.2](#event-655352) | 0x0030       |     29 |              3 |
| [65535.3](#event-655353) | 0x004D       |     78 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xE678      |       59000 |
|       1 | 0xFFFE9704  |  4294874884 |
|       2 | 0x05E3      |        1507 |
|       3 | 0x0BC0      |        3008 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFEAA34  |  4294879796 |
|       6 | 0x05FE      |        1534 |
|       7 | 0x0018      |          24 |
|       8 | 0x003C      |          60 |
|       9 | 0x0078      |         120 |
|      10 | 0xFFFE725B  |  4294865499 |
|      11 | 0x05D6      |        1494 |

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

### Event 67

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=59.000*, z=-92.412*, y=1.507*, direction=264.4°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 37 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 04 80 1F 00             2....
0010: 00 80 05 80 06 80 1F 01  6F 1E A9 F1 09 01 6F 70  ........o.....op
0020: 66 07 80 F8 FF FF 7F F8  FF FF 7F 31 72 64 79 00  f..........1rdy.
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=59.000*, Z=-87.500*, Y=1.534*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0019 [0x1E] EventEntity looks at Ancolain (ID: 17428905/0x0109F1A9) and starts talking
  5: 0x001E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x001F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0020 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rdy" with entities [EventEntity, EventEntity], work=24*
  8: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 66 07 80 F8 FF FF 7F F8  FF FF 7F 31 72 74 6E 53  f..........1rtnS
0040: F8 FF FF 7F F8 FF FF 7F  31 72 74 6E 00           ........1rtn.   
```

#### Opcodes

```
  0: 0x0030 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rtn" with entities [EventEntity, EventEntity], work=24*
  1: 0x003F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1rtn" with entities [EventEntity, EventEntity]
  2: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 78 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         66 07 80               f..
0050: F8 FF FF 7F F8 FF FF 7F  31 72 74 6E 27 03 AC F1  ........1rtn'...
0060: 09 01 03 53 F8 FF FF 7F  F8 FF FF 7F 31 72 74 6E  ...S........1rtn
0070: 27 04 AC F1 09 01 04 1C  08 80 29 03 A9 F1 09 01  '.........).....
0080: 0B 27 04 A9 F1 09 01 04  1C 09 80 32 04 80 1F 00  .'.........2....
0090: 00 80 0A 80 0B 80 1F 01  22 01 00                 ........"..     
```

#### Opcodes

```
  0: 0x004D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rtn" with entities [EventEntity, EventEntity], work=24*
  1: 0x005C [0x27] REQ_SET(priority=0x03, entity_id=Milchupain (ID: 17428908/0x0109F1AC), tag_num=0x03)
  2: 0x0063 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1rtn" with entities [EventEntity, EventEntity]
  3: 0x0070 [0x27] REQ_SET(priority=0x04, entity_id=Milchupain (ID: 17428908/0x0109F1AC), tag_num=0x04)
  4: 0x0077 [0x1C] WAIT(60* ticks)
  5: 0x007A [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Ancolain (ID: 17428905/0x0109F1A9), tag_num=0x0B)
  6: 0x0081 [0x27] REQ_SET(priority=0x04, entity_id=Ancolain (ID: 17428905/0x0109F1A9), tag_num=0x04)
  7: 0x0088 [0x1C] WAIT(120* ticks)
  8: 0x008B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  9: 0x008E [0x1F] MOVE_ENTITY: EventEntity moves to X=59.000*, Z=-101.797*, Y=1.494*
 10: 0x0096 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x0098 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
 12: 0x009A [0x00] END_REQSTACK()
```
