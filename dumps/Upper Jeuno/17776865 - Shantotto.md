# 17776865 - Shantotto

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 392 bytes             |
| Total Events     | 17                    |
| References Count | 13                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      2 |              2 |
| [65535.2](#event-655352)   | 0x0003       |     18 |              5 |
| [65535.3](#event-655353)   | 0x0015       |     10 |              2 |
| [65535.4](#event-655354)   | 0x001F       |     10 |              2 |
| [10182](#event-10182)      | 0x0029       |      1 |              1 |
| [65535.5](#event-655355)   | 0x002A       |     16 |              2 |
| [65535.6](#event-655356)   | 0x003A       |     16 |              2 |
| [65535.7](#event-655357)   | 0x004A       |     16 |              2 |
| [65535.8](#event-655358)   | 0x005A       |     16 |              2 |
| [65535.9](#event-655359)   | 0x006A       |     16 |              2 |
| [65535.10](#event-6553510) | 0x007A       |     13 |              3 |
| [65535.11](#event-6553511) | 0x0087       |     16 |              2 |
| [65535.12](#event-6553512) | 0x0097       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00A7       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00B7       |     71 |             15 |
| [65535.15](#event-6553515) | 0x00FE       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0080      |         128 |
|       2 | 0x0000      |           0 |
|       3 | 0x0560      |        1376 |
|       4 | 0x002B      |          43 |
|       5 | 0x0029      |          41 |
|       6 | 0x0006      |           6 |
|       7 | 0x0801      |        2049 |
|       8 | 0x0032      |          50 |
|       9 | 0x0AAA      |        2730 |
|      10 | 0x02AA      |         682 |
|      11 | 0x001E      |          30 |
|      12 | 0x0064      |         100 |

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    84 00                                           ..             
```

#### Opcodes

```
  0: 0x0001 [0x84] ADJUST_RENDER_FLAGS3_BIT0()
  1: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 18 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          22 00 92 01 F8  FF FF 7F 94 01 F8 FF FF     "............
0010: 7F C0 00 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0003 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0005 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000B [0x94] EventEntity->Render.Flags3 ^= 0x01
  3: 0x0011 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  4: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                6C F8 FF  FF 7F 01 80 02 80 00          l......... 
```

#### Opcodes

```
  0: 0x0015 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=0*)
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               6C                 l
0020: F8 FF FF 7F 02 80 02 80  00                       .........       
```

#### Opcodes

```
  0: 0x001F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 10182

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             00                             .      
```

#### Opcodes

```
  0: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                5B 03 80 F8 FF FF            [.....
0030: 7F F8 FF FF 7F 68 6F 6B  30 00                    .....hok0.      
```

#### Opcodes

```
  0: 0x002A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hok0" with entities [EventEntity, EventEntity], work=1376*
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                66 04 80 F8 FF FF            f.....
0040: 7F F8 FF FF 7F 63 61 77  68 00                    .....cawh.      
```

#### Opcodes

```
  0: 0x003A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "cawh" with entities [EventEntity, EventEntity], work=43*
  1: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                66 04 80 F8 FF FF            f.....
0050: 7F F8 FF FF 7F 73 68 77  68 00                    .....shwh.      
```

#### Opcodes

```
  0: 0x004A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "shwh" with entities [EventEntity, EventEntity], work=43*
  1: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                66 05 80 F8 FF FF            f.....
0060: 7F F8 FF FF 7F 6F 68 68  30 00                    .....ohh0.      
```

#### Opcodes

```
  0: 0x005A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ohh0" with entities [EventEntity, EventEntity], work=41*
  1: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                66 05 80 F8 FF FF            f.....
0070: 7F F8 FF FF 7F 6F 68 68  31 00                    .....ohh1.      
```

#### Opcodes

```
  0: 0x006A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ohh1" with entities [EventEntity, EventEntity], work=41*
  1: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                6E F8 FF FF 7F 06            n.....
0080: 80 99 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x007A [0x6E] EventEntity uses emote 6*
  1: 0x0081 [0x99] Wait for EventEntity animation to complete
  2: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      5B  07 80 F8 FF FF 7F F8 FF         [........
0090: FF 7F 68 6F 75 30 00                              ..hou0.         
```

#### Opcodes

```
  0: 0x0087 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hou0" with entities [EventEntity, EventEntity], work=2049*
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      5B  07 80 F8 FF FF 7F F8 FF         [........
00A0: FF 7F 68 6F 75 31 00                              ..hou1.         
```

#### Opcodes

```
  0: 0x0097 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hou1" with entities [EventEntity, EventEntity], work=2049*
  1: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      5B  07 80 F8 FF FF 7F F8 FF         [........
00B0: FF 7F 68 6F 75 32 00                              ..hou2.         
```

#### Opcodes

```
  0: 0x00A7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hou2" with entities [EventEntity, EventEntity], work=2049*
  1: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B7   |
| Data Size    | 71 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      59  01 F8 FF FF 7F 08 80 4B         Y.......K
00C0: F8 FF FF 7F 09 80 6F 76  F8 FF FF 7F 7B F8 FF FF  ......ov....{...
00D0: 7F 4B F8 FF FF 7F 0A 80  6F 76 F8 FF FF 7F 1C 0B  .K......ov......
00E0: 80 59 01 F8 FF FF 7F 0C  80 7B F8 FF FF 7F 4A F8  .Y.......{....J.
00F0: FF FF 7F F0 FF FF 7F 6F  76 F8 FF FF 7F 00        .......ov.....  
```

#### Opcodes

```
  0: 0x00B7 [0x59] UPDATE_ENTITY_DATA: Set EventEntity turn speed = 50*
  1: 0x00BF [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=15.0°*)
  2: 0x00C6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00C7 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  4: 0x00CC [0x7B] EventEntity stops talking
  5: 0x00D1 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=3.7°*)
  6: 0x00D8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x00D9 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  8: 0x00DE [0x1C] WAIT(30* ticks)
  9: 0x00E1 [0x59] UPDATE_ENTITY_DATA: Set EventEntity turn speed = 100*
 10: 0x00E9 [0x7B] EventEntity stops talking
 11: 0x00EE [0x4A] EventEntity looks at LocalPlayer
 12: 0x00F7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 13: 0x00F8 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
 14: 0x00FD [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00FE  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                            00                   . 
```

#### Opcodes

```
  0: 0x00FE [0x00] END_REQSTACK()
```
