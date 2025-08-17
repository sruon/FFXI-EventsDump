# 17776866 - Toto Kupeliaure

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 584 bytes             |
| Total Events     | 25                    |
| References Count | 22                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     22 |              6 |
| [65535.2](#event-655352)   | 0x0017       |     10 |              2 |
| [65535.3](#event-655353)   | 0x0021       |     10 |              2 |
| [10182](#event-10182)      | 0x002B       |      1 |              1 |
| [65535.4](#event-655354)   | 0x002C       |     23 |              5 |
| [65535.5](#event-655355)   | 0x0043       |     19 |              3 |
| [65535.6](#event-655356)   | 0x0056       |     16 |              2 |
| [65535.7](#event-655357)   | 0x0066       |     19 |              3 |
| [65535.8](#event-655358)   | 0x0079       |     19 |              3 |
| [65535.9](#event-655359)   | 0x008C       |     19 |              3 |
| [65535.10](#event-6553510) | 0x009F       |     16 |              2 |
| [65535.11](#event-6553511) | 0x00AF       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00BF       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00CF       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00DF       |     16 |              2 |
| [65535.15](#event-6553515) | 0x00EF       |     19 |              3 |
| [65535.16](#event-6553516) | 0x0102       |     16 |              2 |
| [65535.17](#event-6553517) | 0x0112       |     19 |              3 |
| [65535.18](#event-6553518) | 0x0125       |     19 |              3 |
| [65535.19](#event-6553519) | 0x0138       |     19 |              3 |
| [65535.20](#event-6553520) | 0x014B       |     16 |              2 |
| [65535.21](#event-6553521) | 0x015B       |     16 |              2 |
| [65535.22](#event-6553522) | 0x016B       |     14 |              4 |
| [10185](#event-10185)      | 0x0179       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x093B      |        2363 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0000      |           0 |
|       4 | 0x000A      |          10 |
|       5 | 0xFFFEAE8E  |  4294880910 |
|       6 | 0x125E7     |       75239 |
|       7 | 0x0A52      |        2642 |
|       8 | 0x00A0      |         160 |
|       9 | 0x0A4C      |        2636 |
|      10 | 0x003C      |          60 |
|      11 | 0x0AC1      |        2753 |
|      12 | 0x0078      |         120 |
|      13 | 0x008C      |         140 |
|      14 | 0x0140      |         320 |
|      15 | 0x0A57      |        2647 |
|      16 | 0x0050      |          80 |
|      17 | 0x0AC2      |        2754 |
|      18 | 0x01F4      |         500 |
|      19 | 0xFFFEB46A  |  4294882410 |
|      20 | 0x11BC1     |       72641 |
|      21 | 0xFFFFFB50  |  4294966096 |

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
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    B6 00 00 80 22 00 92  01 F8 FF FF 7F 94 01 F8   ...."..........
0010: FF FF 7F C0 01 80 00                              .......         
```

#### Opcodes

```
  0: 0x0001 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2363*)
  1: 0x0005 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x0007 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x000D [0x94] EventEntity->Render.Flags3 ^= 0x01
  4: 0x0013 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  5: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      6C  F8 FF FF 7F 02 80 03 80         l........
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0017 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=0*)
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    6C F8 FF FF 7F 03 80  03 80 00                  l.........     
```

#### Opcodes

```
  0: 0x0021 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  1: 0x002A [0x00] END_REQSTACK()
```

### Event 10182

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   00                         .    
```

#### Opcodes

```
  0: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      32 04 80 1F              2...
0030: 00 05 80 06 80 03 80 1F  01 4A F8 FF FF 7F E0 40  .........J.....@
0040: 0F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x002C [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x002F [0x1F] MOVE_ENTITY: EventEntity moves to X=-86.386*, Z=75.239*, Y=0.000*
  2: 0x0037 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0039 [0x4A] EventEntity looks at Moogle (ID: 17776864/0x010F40E0)
  4: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          5B 07 80 F8 FF  FF 7F F8 FF FF 7F 6E 6F     [..........no
0050: 30 30 1C 08 80 00                                 00....          
```

#### Opcodes

```
  0: 0x0043 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "no00" with entities [EventEntity, EventEntity], work=2642*
  1: 0x0052 [0x1C] WAIT(160* ticks)
  2: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   5B 09  80 F8 FF FF 7F F8 FF FF        [.........
0060: 7F 74 6C 6B 30 00                                 .tlk0.          
```

#### Opcodes

```
  0: 0x0056 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=2636*
  1: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   5B 09  80 F8 FF FF 7F F8 FF FF        [.........
0070: 7F 73 74 64 30 1C 0A 80  00                       .std0....       
```

#### Opcodes

```
  0: 0x0066 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "std0" with entities [EventEntity, EventEntity], work=2636*
  1: 0x0075 [0x1C] WAIT(60* ticks)
  2: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             5B 0B 80 F8 FF FF 7F           [......
0080: F8 FF FF 7F 74 73 64 30  1C 0C 80 00              ....tsd0....    
```

#### Opcodes

```
  0: 0x0079 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tsd0" with entities [EventEntity, EventEntity], work=2753*
  1: 0x0088 [0x1C] WAIT(120* ticks)
  2: 0x008B [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008C   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      5B 0B 80 F8              [...
0090: FF FF 7F F8 FF FF 7F 74  73 64 31 1C 0D 80 00     .......tsd1.... 
```

#### Opcodes

```
  0: 0x008C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tsd1" with entities [EventEntity, EventEntity], work=2753*
  1: 0x009B [0x1C] WAIT(140* ticks)
  2: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               5B                 [
00A0: 0B 80 F8 FF FF 7F F8 FF  FF 7F 74 73 74 64 00     ..........tstd. 
```

#### Opcodes

```
  0: 0x009F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tstd" with entities [EventEntity, EventEntity], work=2753*
  1: 0x00AE [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               5B                 [
00B0: 0B 80 F8 FF FF 7F F8 FF  FF 7F 74 74 6C 30 00     ..........ttl0. 
```

#### Opcodes

```
  0: 0x00AF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ttl0" with entities [EventEntity, EventEntity], work=2753*
  1: 0x00BE [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               5B                 [
00C0: 0B 80 F8 FF FF 7F F8 FF  FF 7F 74 74 6C 31 00     ..........ttl1. 
```

#### Opcodes

```
  0: 0x00BF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ttl1" with entities [EventEntity, EventEntity], work=2753*
  1: 0x00CE [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                               5B                 [
00D0: 0B 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 61 75 00     ..........tlau. 
```

#### Opcodes

```
  0: 0x00CF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlau" with entities [EventEntity, EventEntity], work=2753*
  1: 0x00DE [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                               5B                 [
00E0: 0B 80 F8 FF FF 7F F8 FF  FF 7F 74 64 77 30 00     ..........tdw0. 
```

#### Opcodes

```
  0: 0x00DF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tdw0" with entities [EventEntity, EventEntity], work=2753*
  1: 0x00EE [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EF   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                               5B                 [
00F0: 0B 80 F8 FF FF 7F F8 FF  FF 7F 74 64 77 31 1C 0E  ..........tdw1..
0100: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x00EF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tdw1" with entities [EventEntity, EventEntity], work=2753*
  1: 0x00FE [0x1C] WAIT(320* ticks)
  2: 0x0101 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0102   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:       5B 0F 80 F8 FF FF  7F F8 FF FF 7F 70 6E 74    [..........pnt
0110: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0102 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pnt0" with entities [EventEntity, EventEntity], work=2647*
  1: 0x0111 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0112   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:       5B 07 80 F8 FF FF  7F F8 FF FF 7F 79 65 73    [..........yes
0120: 30 1C 10 80 00                                    0....           
```

#### Opcodes

```
  0: 0x0112 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "yes0" with entities [EventEntity, EventEntity], work=2642*
  1: 0x0121 [0x1C] WAIT(80* ticks)
  2: 0x0124 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0125   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                5B 07 80  F8 FF FF 7F F8 FF FF 7F       [..........
0130: 79 65 73 31 1C 08 80 00                           yes1....        
```

#### Opcodes

```
  0: 0x0125 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "yes1" with entities [EventEntity, EventEntity], work=2642*
  1: 0x0134 [0x1C] WAIT(160* ticks)
  2: 0x0137 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0138   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                          5B 11 80 F8 FF FF 7F F8          [.......
0140: FF FF 7F 74 6B 77 30 1C  12 80 00                 ...tkw0....     
```

#### Opcodes

```
  0: 0x0138 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tkw0" with entities [EventEntity, EventEntity], work=2754*
  1: 0x0147 [0x1C] WAIT(500* ticks)
  2: 0x014A [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                   5B 11 80 F8 FF             [....
0150: FF 7F F8 FF FF 7F 66 72  69 30 00                 ......fri0.     
```

#### Opcodes

```
  0: 0x014B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fri0" with entities [EventEntity, EventEntity], work=2754*
  1: 0x015A [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                   5B 11 80 F8 FF             [....
0160: FF 7F F8 FF FF 7F 62 69  6B 30 00                 ......bik0.     
```

#### Opcodes

```
  0: 0x015B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bik0" with entities [EventEntity, EventEntity], work=2754*
  1: 0x016A [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                   32 04 80 1F 00             2....
0170: 13 80 14 80 15 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x016B [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x016E [0x1F] MOVE_ENTITY: EventEntity moves to X=-84.886*, Z=72.641*, Y=-1.200*
  2: 0x0176 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0178 [0x00] END_REQSTACK()
```

### Event 10185

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0179  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                             00                             .      
```

#### Opcodes

```
  0: 0x0179 [0x00] END_REQSTACK()
```
