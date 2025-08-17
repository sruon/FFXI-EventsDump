# 17801268 - Magriffon

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 292 bytes        |
| Total Events     | 12               |
| References Count | 17               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001F       |     16 |              2 |
| [65535.4](#event-655354)   | 0x002F       |     14 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     16 |              2 |
| [65535.6](#event-655356)   | 0x004D       |     14 |              2 |
| [65535.7](#event-655357)   | 0x005B       |      1 |              1 |
| [148](#event-148)          | 0x005C       |      1 |              1 |
| [65535.8](#event-655358)   | 0x005D       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0067       |     24 |              6 |
| [65535.10](#event-6553510) | 0x007F       |     31 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0018      |          24 |
|       1 | 0x437F      |       17279 |
|       2 | 0x1C798     |      116632 |
|       3 | 0x0396      |         918 |
|       4 | 0x0C38      |        3128 |
|       5 | 0x000D      |          13 |
|       6 | 0x61F6      |       25078 |
|       7 | 0x1A711     |      108305 |
|       8 | 0x00EE      |         238 |
|       9 | 0x4E0F      |       19983 |
|      10 | 0x1BC2F     |      113711 |
|      11 | 0x0192      |         402 |
|      12 | 0x0028      |          40 |
|      13 | 0x422C      |       16940 |
|      14 | 0x1B5F0     |      112112 |
|      15 | 0x04AF      |        1199 |
|      16 | 0x0078      |         120 |

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
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 31 72 64 79   f..........1rdy
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rdy" with entities [EventEntity, EventEntity], work=24*
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
0010:    53 F8 FF FF 7F F8 FF  FF 7F 31 72 64 79 00      S........1rdy. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1rdy" with entities [EventEntity, EventEntity]
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
0010:                                               66                 f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 31 73 6C 68 00     ..........1slh. 
```

#### Opcodes

```
  0: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1slh" with entities [EventEntity, EventEntity], work=24*
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
0030: F8 FF FF 7F F8 FF FF 7F  31 73 6C 68 00           ........1slh.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1slh" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         66 00 80               f..
0040: F8 FF FF 7F F8 FF FF 7F  31 72 74 6E 00           ........1rtn.   
```

#### Opcodes

```
  0: 0x003D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rtn" with entities [EventEntity, EventEntity], work=24*
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         53 F8 FF               S..
0050: FF 7F F8 FF FF 7F 31 72  74 6E 00                 ......1rtn.     
```

#### Opcodes

```
  0: 0x004D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1rtn" with entities [EventEntity, EventEntity]
  1: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   00                         .    
```

#### Opcodes

```
  0: 0x005B [0x00] END_REQSTACK()
```

### Event 148

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      00                       .   
```

#### Opcodes

```
  0: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         37 01 80               7..
0060: 02 80 03 80 04 80 00                              .......         
```

#### Opcodes

```
  0: 0x005D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=17.279*, z=116.632*, y=0.918*, direction=274.9°*
  1: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      32  05 80 1F 00 06 80 07 80         2........
0070: 08 80 1F 01 1F 00 09 80  0A 80 0B 80 1F 01 00     ............... 
```

#### Opcodes

```
  0: 0x0067 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006A [0x1F] MOVE_ENTITY: EventEntity moves to X=25.078*, Z=108.305*, Y=0.238*
  2: 0x0072 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0074 [0x1F] MOVE_ENTITY: EventEntity moves to X=19.983*, Z=113.711*, Y=0.402*
  4: 0x007C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 31 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               32                 2
0080: 0C 80 1F 00 0D 80 0E 80  0F 80 1F 01 29 08 34 A0  ............).4.
0090: 0F 01 01 1C 10 80 29 08  34 A0 0F 01 03 00        ......).4.....  
```

#### Opcodes

```
  0: 0x007F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0082 [0x1F] MOVE_ENTITY: EventEntity moves to X=16.940*, Z=112.112*, Y=1.199*
  2: 0x008A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x008C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Magriffon (ID: 17801268/0x010FA034), tag_num=0x01)
  4: 0x0093 [0x1C] WAIT(120* ticks)
  5: 0x0096 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Magriffon (ID: 17801268/0x010FA034), tag_num=0x03)
  6: 0x009D [0x00] END_REQSTACK()
```
