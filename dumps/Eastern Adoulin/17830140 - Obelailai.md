# 17830140 - Obelailai

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 328 bytes                 |
| Total Events     | 12                        |
| References Count | 17                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |     16 |              2 |
| [65535.4](#event-655354) | 0x0037       |     14 |              2 |
| [34](#event-34)          | 0x0045       |      1 |              1 |
| [65535.5](#event-655355) | 0x0046       |     18 |              4 |
| [65535.6](#event-655356) | 0x0058       |     14 |              4 |
| [37](#event-37)          | 0x0066       |      1 |              1 |
| [65535.7](#event-655357) | 0x0067       |     18 |              4 |
| [65535.8](#event-655358) | 0x0079       |     42 |              6 |
| [65535.9](#event-655359) | 0x00A3       |     30 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x063E      |        1598 |
|       3 | 0xFFFFBE31  |  4294950449 |
|       4 | 0xFFFFFFFD  |  4294967293 |
|       5 | 0x0BBB      |        3003 |
|       6 | 0x000D      |          13 |
|       7 | 0x027C      |         636 |
|       8 | 0xFFFFC230  |  4294951472 |
|       9 | 0x0000      |           0 |
|      10 | 0x0111      |         273 |
|      11 | 0x02FC      |         764 |
|      12 | 0x0C08      |        3080 |
|      13 | 0xFFFFFA20  |  4294965792 |
|      14 | 0x0578      |        1400 |
|      15 | 0x0561      |        1377 |
|      16 | 0xFFFFF818  |  4294965272 |

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      66  00 80 F8 FF FF 7F F8 FF         f........
0030: FF 7F 70 6F 69 30 00                              ..poi0.         
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0040: 70 6F 69 30 00                                    poi0.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 34

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                00                                      .          
```

#### Opcodes

```
  0: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   2F 00  F8 FF FF 7F 37 02 80 03        /.....7...
0050: 80 04 80 05 80 22 00 00                           ....."..        
```

#### Opcodes

```
  0: 0x0046 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x004C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=1.598*, z=-16.847*, y=-0.003*, direction=263.9°*
  2: 0x0055 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          32 06 80 1F 00 07 80 08          2.......
0060: 80 09 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0058 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005B [0x1F] MOVE_ENTITY: EventEntity moves to X=0.636*, Z=-15.824*, Y=0.000*
  2: 0x0063 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0065 [0x00] END_REQSTACK()
```

### Event 37

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0066  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   00                                    .         
```

#### Opcodes

```
  0: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      2F  00 F8 FF FF 7F 37 0A 80         /.....7..
0070: 0B 80 09 80 0C 80 22 00  00                       ......"..       
```

#### Opcodes

```
  0: 0x0067 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x006D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.273*, z=0.764*, y=0.000*, direction=270.7°*
  2: 0x0076 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 42 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             32 00 80 1F 00 0A 80           2......
0080: 0D 80 09 80 1F 01 66 00  80 F8 FF FF 7F F8 FF FF  ......f.........
0090: 7F 70 6F 69 30 53 F8 FF  FF 7F F8 FF FF 7F 70 6F  .poi0S........po
00A0: 69 30 00                                          i0.             
```

#### Opcodes

```
  0: 0x0079 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x007C [0x1F] MOVE_ENTITY: EventEntity moves to X=0.273*, Z=-1.504*, Y=0.000*
  2: 0x0084 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0086 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=40*
  4: 0x0095 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  5: 0x00A2 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A3   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          1C 01 80 32 06  80 1F 00 0E 80 0F 80 09     ...2.........
00B0: 80 1F 01 4B F8 FF FF 7F  10 80 6F 76 F8 FF FF 7F  ...K......ov....
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x00A3 [0x1C] WAIT(30* ticks)
  1: 0x00A6 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x00A9 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.400*, Z=1.377*, Y=0.000*
  3: 0x00B1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00B3 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=348.9°*)
  5: 0x00BA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00BB [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  7: 0x00C0 [0x00] END_REQSTACK()
```
