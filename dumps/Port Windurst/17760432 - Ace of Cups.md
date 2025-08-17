# 17760432 - Ace of Cups

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 324 bytes               |
| Total Events     | 11                      |
| References Count | 14                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     14 |              2 |
| [65535.3](#event-655353) | 0x001F       |     16 |              2 |
| [65535.4](#event-655354) | 0x002F       |     14 |              2 |
| [522](#event-522)        | 0x003D       |     10 |              2 |
| [65535.5](#event-655355) | 0x0047       |     17 |              5 |
| [65535.6](#event-655356) | 0x0058       |     71 |             13 |
| [65535.7](#event-655357) | 0x009F       |     26 |              7 |
| [534](#event-534)        | 0x00B9       |     10 |              2 |
| [542](#event-542)        | 0x00C3       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00B5      |         181 |
|       1 | 0xFFFFE3B9  |  4294960057 |
|       2 | 0x2E2EA     |      189162 |
|       3 | 0xFFFFE890  |  4294961296 |
|       4 | 0x07C2      |        1986 |
|       5 | 0xFFFFE770  |  4294961008 |
|       6 | 0x2EB7B     |      191355 |
|       7 | 0xFFFFE891  |  4294961297 |
|       8 | 0x02F0      |         752 |
|       9 | 0x000D      |          13 |
|      10 | 0x009A      |         154 |
|      11 | 0x2D14D     |      184653 |
|      12 | 0xFFFFF73C  |  4294965052 |
|      13 | 0x2AB43     |      174915 |

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 6A 74 30 30   [..........jt00
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "jt00" with entities [EventEntity, EventEntity], work=181*
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
0010:    53 F8 FF FF 7F F8 FF  FF 7F 6A 74 30 30 00      S........jt00. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "jt00" with entities [EventEntity, EventEntity]
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
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 6A 74 30 31 00     ..........jt01. 
```

#### Opcodes

```
  0: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "jt01" with entities [EventEntity, EventEntity], work=181*
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
0030: F8 FF FF 7F F8 FF FF 7F  6A 74 30 31 00           ........jt01.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "jt01" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 522

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         37 01 80               7..
0040: 02 80 03 80 04 80 00                              .......         
```

#### Opcodes

```
  0: 0x003D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-7.239*, z=189.162*, y=-6.000*, direction=174.5°*
  1: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      37  05 80 06 80 07 80 08 80         7........
0050: 1E 5B 00 0F 01 6F 70 00                           .[...op.        
```

#### Opcodes

```
  0: 0x0047 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-6.288*, z=191.355*, y=-5.999*, direction=66.1°*
  1: 0x0050 [0x1E] EventEntity looks at Joker (ID: 17760347/0x010F005B) and starts talking
  2: 0x0055 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0056 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 71 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          4A B0 00 0F 01 5B 00 0F          J....[..
0060: 01 4A 58 00 0F 01 5B 00  0F 01 6F 76 B0 00 0F 01  .JX...[...ov....
0070: 6F 76 58 00 0F 01 27 0A  58 00 0F 01 08 29 08 B0  ovX...'.X....)..
0080: 00 0F 01 01 2A 0A 58 00  0F 01 27 0A 58 00 0F 01  ....*.X...'.X...
0090: 09 29 08 B0 00 0F 01 02  2A 0A 58 00 0F 01 00     .)......*.X.... 
```

#### Opcodes

```
  0: 0x0058 [0x4A] Ace of Cups (ID: 17760432/0x010F00B0) looks at Joker (ID: 17760347/0x010F005B)
  1: 0x0061 [0x4A] Shanruru (ID: 17760344/0x010F0058) looks at Joker (ID: 17760347/0x010F005B)
  2: 0x006A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x006B [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Ace of Cups (ID: 17760432/0x010F00B0) Render.Flags0 and Render.Flags3 conditions are met
  4: 0x0070 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0071 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Shanruru (ID: 17760344/0x010F0058) Render.Flags0 and Render.Flags3 conditions are met
  6: 0x0076 [0x27] REQ_SET(priority=0x0A, entity_id=Shanruru (ID: 17760344/0x010F0058), tag_num=0x08)
  7: 0x007D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ace of Cups (ID: 17760432/0x010F00B0), tag_num=0x01)
  8: 0x0084 [0x2A] GET_REQ_LEVEL(level=10, entity_id=Shanruru (ID: 17760344/0x010F0058))
  9: 0x008A [0x27] REQ_SET(priority=0x0A, entity_id=Shanruru (ID: 17760344/0x010F0058), tag_num=0x09)
 10: 0x0091 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ace of Cups (ID: 17760432/0x010F00B0), tag_num=0x02)
 11: 0x0098 [0x2A] GET_REQ_LEVEL(level=10, entity_id=Shanruru (ID: 17760344/0x010F0058))
 12: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               32                 2
00A0: 09 80 1F 00 0A 80 0B 80  07 80 1F 01 1F 00 0C 80  ................
00B0: 0D 80 07 80 1F 01 22 01  00                       ......"..       
```

#### Opcodes

```
  0: 0x009F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00A2 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.154*, Z=184.653*, Y=-5.999*
  2: 0x00AA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AC [0x1F] MOVE_ENTITY: EventEntity moves to X=-2.244*, Z=174.915*, Y=-5.999*
  4: 0x00B4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00B6 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  6: 0x00B8 [0x00] END_REQSTACK()
```

### Event 534

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             37 01 80 02 80 03 80           7......
00C0: 04 80 00                                          ...             
```

#### Opcodes

```
  0: 0x00B9 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-7.239*, z=189.162*, y=-6.000*, direction=174.5°*
  1: 0x00C2 [0x00] END_REQSTACK()
```

### Event 542

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C3   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          37 01 80 02 80  03 80 04 80 00              7.........   
```

#### Opcodes

```
  0: 0x00C3 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-7.239*, z=189.162*, y=-6.000*, direction=174.5°*
  1: 0x00CC [0x00] END_REQSTACK()
```
