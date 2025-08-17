# 16892166 - Mildaurion

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Sacrarium (ID: 28) |
| Block Size       | 260 bytes          |
| Total Events     | 9                  |
| References Count | 10                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     14 |              2 |
| [65535.3](#event-655353) | 0x001F       |     16 |              2 |
| [65535.4](#event-655354) | 0x002F       |     14 |              2 |
| [65535.5](#event-655355) | 0x003D       |      7 |              2 |
| [65535.6](#event-655356) | 0x0044       |     58 |              6 |
| [65535.7](#event-655357) | 0x007E       |     32 |              7 |
| [5](#event-5)            | 0x009E       |      9 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x01BE      |         446 |
|       1 | 0x0075      |         117 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C8      |         200 |
|       4 | 0x012C      |         300 |
|       5 | 0x003C      |          60 |
|       6 | 0x001E      |          30 |
|       7 | 0x23C9A     |      146586 |
|       8 | 0x21D86     |      138630 |
|       9 | 0x0E10      |        3600 |

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 6B 74 61 30   [..........kta0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kta0" with entities [EventEntity, EventEntity], work=446*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 6B 74 61 30 00      S........kta0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kta0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               5B                 [
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 6B 74 61 31 00     ..........kta1. 
```

#### Opcodes

```
  0: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kta1" with entities [EventEntity, EventEntity], work=446*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               53                 S
0030: F8 FF FF 7F F8 FF FF 7F  6B 74 61 31 00           ........kta1.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kta1" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         92 01 F8               ...
0040: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x003D [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 58 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             45 01 80 F8  FF FF 7F F8 FF FF 7F 73      E..........s
0050: 30 35 34 02 80 45 03 80  F8 FF FF 7F F8 FF FF 7F  054..E..........
0060: 66 64 69 31 02 80 1C 04  80 45 03 80 F8 FF FF 7F  fdi1.....E......
0070: F8 FF FF 7F 66 64 6F 31  02 80 1C 05 80 00        ....fdo1......  
```

#### Opcodes

```
  0: 0x0044 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s054" with entities [EventEntity, EventEntity], work=[117*, 0*]
  1: 0x0055 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x0066 [0x1C] WAIT(300* ticks)
  3: 0x0069 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  4: 0x007A [0x1C] WAIT(60* ticks)
  5: 0x007D [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 32 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            1C 06                ..
0080: 80 A4 01 29 08 06 C1 01  01 01 1C 06 80 37 07 80  ...).........7..
0090: 08 80 02 80 09 80 29 08  06 C1 01 01 02 00        ......).......  
```

#### Opcodes

```
  0: 0x007E [0x1C] WAIT(30* ticks)
  1: 0x0081 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  2: 0x0083 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mildaurion (ID: 16892166/0x0101C106), tag_num=0x01)
  3: 0x008A [0x1C] WAIT(30* ticks)
  4: 0x008D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=146.586*, z=138.630*, y=0.000*, direction=316.4°*
  5: 0x0096 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mildaurion (ID: 16892166/0x0101C106), tag_num=0x02)
  6: 0x009D [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            A4 01                ..
00A0: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x009E [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x00A0 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x00A6 [0x00] END_REQSTACK()
```
