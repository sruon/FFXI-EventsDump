# 17867180 - Orsa-Porsa

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Marjami Ravine (ID: 266) |
| Block Size       | 464 bytes                |
| Total Events     | 22                       |
| References Count | 15                       |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     22 |              4 |
| [65535.3](#event-655353)   | 0x0027       |      6 |              2 |
| [65535.4](#event-655354)   | 0x002D       |     16 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     14 |              2 |
| [65535.6](#event-655356)   | 0x004B       |     16 |              2 |
| [65535.7](#event-655357)   | 0x005B       |     14 |              2 |
| [65535.8](#event-655358)   | 0x0069       |     16 |              2 |
| [65535.9](#event-655359)   | 0x0079       |     14 |              2 |
| [65535.10](#event-6553510) | 0x0087       |     16 |              2 |
| [65535.11](#event-6553511) | 0x0097       |     14 |              2 |
| [65535.12](#event-6553512) | 0x00A5       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00B5       |     14 |              2 |
| [65535.14](#event-6553514) | 0x00C3       |     16 |              2 |
| [65535.15](#event-6553515) | 0x00D3       |     14 |              2 |
| [65535.16](#event-6553516) | 0x00E1       |     16 |              2 |
| [65535.17](#event-6553517) | 0x00F1       |     14 |              2 |
| [51](#event-51)            | 0x00FF       |      1 |              1 |
| [65535.18](#event-6553518) | 0x0100       |     10 |              2 |
| [65535.19](#event-6553519) | 0x010A       |     22 |              6 |
| [65535.20](#event-6553520) | 0x0120       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x0029      |          41 |
|       3 | 0x5AFB0     |      372656 |
|       4 | 0x22E37     |      142903 |
|       5 | 0xFFFF18FA  |  4294908154 |
|       6 | 0x02A7      |         679 |
|       7 | 0x000D      |          13 |
|       8 | 0x5AC1A     |      371738 |
|       9 | 0x22C39     |      142393 |
|      10 | 0xFFFF193D  |  4294908221 |
|      11 | 0x5B233     |      373299 |
|      12 | 0x2281B     |      141339 |
|      13 | 0xFFFF1918  |  4294908184 |
|      14 | 0x07AB      |        1963 |

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5E  69 64 6C 30 00                  ^idl0.   
```

#### Opcodes

```
  0: 0x0027 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         66 00 80               f..
0030: F8 FF FF 7F F8 FF FF 7F  70 6F 69 30 00           ........poi0.   
```

#### Opcodes

```
  0: 0x002D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=40*
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         53 F8 FF               S..
0040: FF 7F F8 FF FF 7F 70 6F  69 30 00                 ......poi0.     
```

#### Opcodes

```
  0: 0x003D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   66 02 80 F8 FF             f....
0050: FF 7F F8 FF FF 7F 65 68  6E 30 00                 ......ehn0.     
```

#### Opcodes

```
  0: 0x004B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ehn0" with entities [EventEntity, EventEntity], work=41*
  1: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   53 F8 FF FF 7F             S....
0060: F8 FF FF 7F 65 68 6E 30  00                       ....ehn0.       
```

#### Opcodes

```
  0: 0x005B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ehn0" with entities [EventEntity, EventEntity]
  1: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             66 02 80 F8 FF FF 7F           f......
0070: F8 FF FF 7F 65 68 6E 31  00                       ....ehn1.       
```

#### Opcodes

```
  0: 0x0069 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ehn1" with entities [EventEntity, EventEntity], work=41*
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             53 F8 FF FF 7F F8 FF           S......
0080: FF 7F 65 68 6E 31 00                              ..ehn1.         
```

#### Opcodes

```
  0: 0x0079 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ehn1" with entities [EventEntity, EventEntity]
  1: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      66  00 80 F8 FF FF 7F F8 FF         f........
0090: FF 7F 7A 69 74 30 00                              ..zit0.         
```

#### Opcodes

```
  0: 0x0087 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "zit0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00A0: 7A 69 74 30 00                                    zit0.           
```

#### Opcodes

```
  0: 0x0097 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "zit0" with entities [EventEntity, EventEntity]
  1: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                66 00 80  F8 FF FF 7F F8 FF FF 7F       f..........
00B0: 77 61 69 30 00                                    wai0.           
```

#### Opcodes

```
  0: 0x00A5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wai0" with entities [EventEntity, EventEntity], work=40*
  1: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                53 F8 FF  FF 7F F8 FF FF 7F 77 61       S........wa
00C0: 69 30 00                                          i0.             
```

#### Opcodes

```
  0: 0x00B5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wai0" with entities [EventEntity, EventEntity]
  1: 0x00C2 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 68     f..........th
00D0: 6B 31 00                                          k1.             
```

#### Opcodes

```
  0: 0x00C3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          53 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31     S........thk1
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00D3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x00E0 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32   f..........thk2
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00E1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
  1: 0x00F0 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F1   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    53 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 00      S........thk2. 
```

#### Opcodes

```
  0: 0x00F1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x00FE [0x00] END_REQSTACK()
```

### Event 51

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00FF  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                               00                 .
```

#### Opcodes

```
  0: 0x00FF [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0100   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100: 37 03 80 04 80 05 80 06  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0100 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=372.656*, z=142.903*, y=-59.142*, direction=59.7°*
  1: 0x0109 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010A   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                2F 00 F8 FF FF 7F            /.....
0110: 22 00 32 07 80 1F 00 08  80 09 80 0A 80 1F 01 00  ".2.............
```

#### Opcodes

```
  0: 0x010A [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0110 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x0112 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x0115 [0x1F] MOVE_ENTITY: EventEntity moves to X=371.738*, Z=142.393*, Y=-59.075*
  4: 0x011D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x011F [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0120   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120: 37 0B 80 0C 80 0D 80 0E  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0120 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=373.299*, z=141.339*, y=-59.112*, direction=172.5°*
  1: 0x0129 [0x00] END_REQSTACK()
```
