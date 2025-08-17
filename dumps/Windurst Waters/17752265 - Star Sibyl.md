# 17752265 - Star Sibyl

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 308 bytes                 |
| Total Events     | 7                         |
| References Count | 14                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [715](#event-715)        | 0x0027       |     10 |              2 |
| [65535.3](#event-655353) | 0x0031       |     20 |              5 |
| [65535.4](#event-655354) | 0x0045       |     56 |              6 |
| [65535.5](#event-655355) | 0x007D       |     80 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00AA      |         170 |
|       1 | 0x001E      |          30 |
|       2 | 0xFFFFFF97  |  4294967191 |
|       3 | 0xAC26      |       44070 |
|       4 | 0xFFFEF854  |  4294899796 |
|       5 | 0x03A9      |         937 |
|       6 | 0x0000      |           0 |
|       7 | 0xFFFF0FAF  |  4294905775 |
|       8 | 0x0429      |        1065 |
|       9 | 0x00D3      |         211 |
|      10 | 0x02BC      |         700 |
|      11 | 0x00C8      |         200 |
|      12 | 0x003C      |          60 |
|      13 | 0x00C9      |         201 |

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 63 30   [..........tlc0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlc0" with entities [EventEntity, EventEntity], work=170*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 63 30 5E 69   S........tlc0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 715

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      37  02 80 03 80 04 80 05 80         7........
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0027 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.105*, z=44.070*, y=-67.500*, direction=82.4°*
  1: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    92 01 F8 FF FF 7F 33  01 37 06 80 03 80 07 80   ......3.7......
0040: 08 80 33 01 00                                    ..3..           
```

#### Opcodes

```
  0: 0x0031 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0037 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  2: 0x0039 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=44.070*, y=-61.521*, direction=93.6°*
  3: 0x0042 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  4: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 56 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                45 09 80  F8 FF FF 7F F8 FF FF 7F       E..........
0050: 73 30 30 38 06 80 1C 0A  80 45 0B 80 F8 FF FF 7F  s008.....E......
0060: F8 FF FF 7F 66 64 6F 31  06 80 1C 0C 80 52 09 80  ....fdo1.....R..
0070: F8 FF FF 7F F8 FF FF 7F  73 30 30 38 00           ........s008.   
```

#### Opcodes

```
  0: 0x0045 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s008" with entities [EventEntity, EventEntity], work=[211*, 0*]
  1: 0x0056 [0x1C] WAIT(700* ticks)
  2: 0x0059 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  3: 0x006A [0x1C] WAIT(60* ticks)
  4: 0x006D [0x52] END_LOAD_SCHEDULER: End scheduler "s008" with entities [EventEntity, EventEntity], work=211*
  5: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 80 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         45 09 80               E..
0080: F8 FF FF 7F F8 FF FF 7F  73 30 31 30 06 80 45 0B  ........s010..E.
0090: 80 F8 FF FF 7F F8 FF FF  7F 66 64 69 31 06 80 55  .........fdi1..U
00A0: 09 80 F8 FF FF 7F F8 FF  FF 7F 73 30 31 30 27 0A  ..........s010'.
00B0: CB E0 0E 01 02 1C 0C 80  45 0D 80 F0 FF FF 7F F0  ........E.......
00C0: FF FF 7F 77 68 6F 31 06  80 1C 0C 80 00           ...who1......   
```

#### Opcodes

```
  0: 0x007D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s010" with entities [EventEntity, EventEntity], work=[211*, 0*]
  1: 0x008E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x009F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s010" with entities [EventEntity, EventEntity], work=211*
  3: 0x00AE [0x27] REQ_SET(priority=0x0A, entity_id=Marble Door (ID: 17752267/0x010EE0CB), tag_num=0x02)
  4: 0x00B5 [0x1C] WAIT(60* ticks)
  5: 0x00B8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  6: 0x00C9 [0x1C] WAIT(60* ticks)
  7: 0x00CC [0x00] END_REQSTACK()
```
