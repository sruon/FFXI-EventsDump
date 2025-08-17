# 17453346 - Riko Kupenreich

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Throne Room (ID: 165) |
| Block Size       | 424 bytes             |
| Total Events     | 18                    |
| References Count | 12                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     19 |              5 |
| [65535.2](#event-655352)   | 0x0014       |     12 |              3 |
| [65535.3](#event-655353)   | 0x0020       |     12 |              3 |
| [4](#event-4)              | 0x002C       |      1 |              1 |
| [65535.4](#event-655354)   | 0x002D       |     16 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     16 |              2 |
| [65535.6](#event-655356)   | 0x004D       |     19 |              3 |
| [65535.7](#event-655357)   | 0x0060       |     19 |              3 |
| [65535.8](#event-655358)   | 0x0073       |     18 |              2 |
| [65535.9](#event-655359)   | 0x0085       |     36 |              4 |
| [5](#event-5)              | 0x00A9       |      1 |              1 |
| [65535.10](#event-6553510) | 0x00AA       |     21 |              3 |
| [65535.11](#event-6553511) | 0x00BF       |     18 |              2 |
| [65535.12](#event-6553512) | 0x00D1       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00E1       |     21 |              3 |
| [65535.14](#event-6553514) | 0x00F6       |     21 |              3 |
| [65535.15](#event-6553515) | 0x010B       |     21 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0938      |        2360 |
|       1 | 0x0000      |           0 |
|       2 | 0x0080      |         128 |
|       3 | 0x0A57      |        2647 |
|       4 | 0x0A56      |        2646 |
|       5 | 0x0046      |          70 |
|       6 | 0x008E      |         142 |
|       7 | 0x008A      |         138 |
|       8 | 0x000F      |          15 |
|       9 | 0x0A52      |        2642 |
|      10 | 0x02BC      |         700 |
|      11 | 0x0109      |         265 |

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
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 B6 00 00 80 92  01 F8 FF FF 7F 94 01 F8   "..............
0010: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2360*)
  2: 0x0007 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x000D [0x94] EventEntity->Render.Flags3 ^= 0x01
  4: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             A4 00 6C F8  FF FF 7F 01 80 01 80 00      ..l.........
```

#### Opcodes

```
  0: 0x0014 [0xA4] EventEntity->Flags3.unknown_3_2 = 0
  1: 0x0016 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  2: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: A4 01 6C F8 FF FF 7F 02  80 01 80 00              ..l.........    
```

#### Opcodes

```
  0: 0x0020 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x0022 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=0*)
  2: 0x002B [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      00                       .   
```

#### Opcodes

```
  0: 0x002C [0x00] END_REQSTACK()
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
0020:                                         5B 03 80               [..
0030: F8 FF FF 7F F8 FF FF 7F  70 6E 74 30 00           ........pnt0.   
```

#### Opcodes

```
  0: 0x002D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pnt0" with entities [EventEntity, EventEntity], work=2647*
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
0030:                                         5B 04 80               [..
0040: F8 FF FF 7F F8 FF FF 7F  6E 73 74 64 00           ........nstd.   
```

#### Opcodes

```
  0: 0x003D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "nstd" with entities [EventEntity, EventEntity], work=2646*
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         5B 04 80               [..
0050: F8 FF FF 7F F8 FF FF 7F  74 69 74 30 1C 05 80 00  ........tit0....
```

#### Opcodes

```
  0: 0x004D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tit0" with entities [EventEntity, EventEntity], work=2646*
  1: 0x005C [0x1C] WAIT(70* ticks)
  2: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 5B 04 80 F8 FF FF 7F F8  FF FF 7F 74 69 74 31 1C  [..........tit1.
0070: 05 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0060 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tit1" with entities [EventEntity, EventEntity], work=2646*
  1: 0x006F [0x1C] WAIT(70* ticks)
  2: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          C5 06 80 F8 FF  FF 7F F8 FF FF 7F 73 30     ...........s0
0080: 30 30 01 80 00                                    00...           
```

#### Opcodes

```
  0: 0x0073 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80013030 for entities [EventEntity, EventEntity], work=142*, param=12403
  1: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 36 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                C5 06 80  F8 FF FF 7F F8 FF FF 7F       ...........
0090: 73 30 30 31 01 80 1C 05  80 C6 06 80 F8 FF FF 7F  s001............
00A0: F8 FF FF 7F 73 30 30 31  00                       ....s001.       
```

#### Opcodes

```
  0: 0x0085 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80013130 for entities [EventEntity, EventEntity], work=142*, param=12403
  1: 0x0096 [0x1C] WAIT(70* ticks)
  2: 0x0099 [0xC6] WAIT_LOAD_SCHEDULER_ALT3: Wait for scheduler "s001" with entities [EventEntity, EventEntity], work=142*
  3: 0x00A8 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A9  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             00                             .      
```

#### Opcodes

```
  0: 0x00A9 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AA   |
| Data Size    | 21 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                C5 07 80 F8 FF FF            ......
00B0: 7F F8 FF FF 7F 73 30 30  30 01 80 1C 08 80 00     .....s000...... 
```

#### Opcodes

```
  0: 0x00AA [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80013030 for entities [EventEntity, EventEntity], work=138*, param=12403
  1: 0x00BB [0x1C] WAIT(15* ticks)
  2: 0x00BE [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BF   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               C5                 .
00C0: 07 80 F8 FF FF 7F F8 FF  FF 7F 6B 69 6C 30 01 80  ..........kil0..
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00BF [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x8001306C for entities [EventEntity, EventEntity], work=138*, param=26987
  1: 0x00D0 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D1   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:    5B 09 80 F8 FF FF 7F  F8 FF FF 7F 6B 79 6F 30   [..........kyo0
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00D1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kyo0" with entities [EventEntity, EventEntity], work=2642*
  1: 0x00E0 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 21 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    C5 07 80 F8 FF FF 7F  F8 FF FF 7F 73 30 30 31   ...........s001
00F0: 01 80 1C 08 80 00                                 ......          
```

#### Opcodes

```
  0: 0x00E1 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80013130 for entities [EventEntity, EventEntity], work=138*, param=12403
  1: 0x00F2 [0x1C] WAIT(15* ticks)
  2: 0x00F5 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F6   |
| Data Size    | 21 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                   C5 07  80 F8 FF FF 7F F8 FF FF        ..........
0100: 7F 73 30 30 32 01 80 1C  0A 80 00                 .s002......     
```

#### Opcodes

```
  0: 0x00F6 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80013230 for entities [EventEntity, EventEntity], work=138*, param=12403
  1: 0x0107 [0x1C] WAIT(700* ticks)
  2: 0x010A [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010B   |
| Data Size    | 21 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                   C5 07 80 F8 FF             .....
0110: FF 7F F8 FF FF 7F 73 30  30 33 01 80 1C 0B 80 00  ......s003......
```

#### Opcodes

```
  0: 0x010B [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80013330 for entities [EventEntity, EventEntity], work=138*, param=12403
  1: 0x011C [0x1C] WAIT(265* ticks)
  2: 0x011F [0x00] END_REQSTACK()
```
