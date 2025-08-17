# 17788997 - Chelvadurai

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Rabao (ID: 247) |
| Block Size       | 384 bytes       |
| Total Events     | 18              |
| References Count | 21              |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001F       |     16 |              2 |
| [65535.4](#event-655354)   | 0x002F       |     14 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     16 |              2 |
| [65535.6](#event-655356)   | 0x004D       |     22 |              4 |
| [65535.7](#event-655357)   | 0x0063       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0073       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0081       |      1 |              1 |
| [117](#event-117)          | 0x0082       |      1 |              1 |
| [65535.10](#event-6553510) | 0x0083       |     10 |              2 |
| [65535.11](#event-6553511) | 0x008D       |     15 |              5 |
| [65535.12](#event-6553512) | 0x009C       |     15 |              5 |
| [65535.13](#event-6553513) | 0x00AB       |     15 |              5 |
| [128](#event-128)          | 0x00BA       |      1 |              1 |
| [65535.14](#event-6553514) | 0x00BB       |     10 |              2 |
| [65535.15](#event-6553515) | 0x00C5       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0041      |          65 |
|       1 | 0x001E      |          30 |
|       2 | 0x1F6F3     |      128755 |
|       3 | 0xE4D7      |       58583 |
|       4 | 0x1F52      |        8018 |
|       5 | 0x09CC      |        2508 |
|       6 | 0x0028      |          40 |
|       7 | 0x1EA42     |      125506 |
|       8 | 0xE9F6      |       59894 |
|       9 | 0x1F40      |        8000 |
|      10 | 0x1E37C     |      123772 |
|      11 | 0xDE41      |       56897 |
|      12 | 0x1F3F      |        7999 |
|      13 | 0x000D      |          13 |
|      14 | 0x1F0AC     |      127148 |
|      15 | 0x162CC     |       90828 |
|      16 | 0xFFFF6BCF  |  4294929359 |
|      17 | 0x15E4B     |       89675 |
|      18 | 0x0577      |        1399 |
|      19 | 0xFFFF59DB  |  4294924763 |
|      20 | 0x1476D     |       83821 |

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31   [..........thk1
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=65*
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
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 31 00      S........thk1. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
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
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 00     ..........thk2. 
```

#### Opcodes

```
  0: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=65*
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
0030: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 00           ........thk2.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
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
0030:                                         5B 00 80               [..
0040: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 00           ........tlk0.   
```

#### Opcodes

```
  0: 0x003D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=65*
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         53 F8 FF               S..
0050: FF 7F F8 FF FF 7F 74 6C  6B 30 5E 69 64 6C 30 1C  ......tlk0^idl0.
0060: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x004D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x005A [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x005F [0x1C] WAIT(30* ticks)
  3: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          5B 00 80 F8 FF  FF 7F F8 FF FF 7F 70 61     [..........pa
0070: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x0063 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=65*
  1: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          53 F8 FF FF 7F  F8 FF FF 7F 70 61 73 30     S........pas0
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0073 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x0080 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0081  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    00                                              .              
```

#### Opcodes

```
  0: 0x0081 [0x00] END_REQSTACK()
```

### Event 117

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0082  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       00                                            .             
```

#### Opcodes

```
  0: 0x0082 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0083   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:          37 02 80 03 80  04 80 05 80 00              7.........   
```

#### Opcodes

```
  0: 0x0083 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=128.755*, z=58.583*, y=8.018*, direction=220.4°*
  1: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         32 06 80               2..
0090: 1F 00 07 80 08 80 09 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x008D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0090 [0x1F] MOVE_ENTITY: EventEntity moves to X=125.506*, Z=59.894*, Y=8.000*
  2: 0x0098 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      32 06 80 1F              2...
00A0: 00 0A 80 0B 80 0C 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x009C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x009F [0x1F] MOVE_ENTITY: EventEntity moves to X=123.772*, Z=56.897*, Y=7.999*
  2: 0x00A7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00AA [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AB   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   32 0D 80 1F 00             2....
00B0: 0E 80 0F 80 0C 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x00AB [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00AE [0x1F] MOVE_ENTITY: EventEntity moves to X=127.148*, Z=90.828*, Y=7.999*
  2: 0x00B6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00B9 [0x00] END_REQSTACK()
```

### Event 128

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BA  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                00                           .     
```

#### Opcodes

```
  0: 0x00BA [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BB   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                   37 10 80 11 80             7....
00C0: 0C 80 12 80 00                                    .....           
```

#### Opcodes

```
  0: 0x00BB [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-37.937*, z=89.675*, y=7.999*, direction=123.0°*
  1: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                32 06 80  1F 00 13 80 14 80 0C 80       2..........
00D0: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x00C5 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00C8 [0x1F] MOVE_ENTITY: EventEntity moves to X=-42.533*, Z=83.821*, Y=7.999*
  2: 0x00D0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00D3 [0x00] END_REQSTACK()
```
