# 16912926 - Makki-Chebukki

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al'Taieu (ID: 33) |
| Block Size       | 496 bytes         |
| Total Events     | 23                |
| References Count | 33                |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [0](#event-0)              | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     18 |              4 |
| [65535.2](#event-655352)   | 0x0014       |     10 |              2 |
| [65535.3](#event-655353)   | 0x001E       |      9 |              3 |
| [65535.4](#event-655354)   | 0x0027       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0030       |     10 |              2 |
| [65535.6](#event-655356)   | 0x003A       |     10 |              2 |
| [1](#event-1)              | 0x0044       |      1 |              1 |
| [65535.7](#event-655357)   | 0x0045       |     10 |              2 |
| [65535.8](#event-655358)   | 0x004F       |     29 |              3 |
| [65535.9](#event-655359)   | 0x006C       |     14 |              4 |
| [65535.10](#event-6553510) | 0x007A       |     16 |              2 |
| [65535.11](#event-6553511) | 0x008A       |     16 |              2 |
| [65535.12](#event-6553512) | 0x009A       |     10 |              2 |
| [65535.13](#event-6553513) | 0x00A4       |     16 |              2 |
| [165](#event-165)          | 0x00B4       |      1 |              1 |
| [166](#event-166)          | 0x00B5       |      1 |              1 |
| [167](#event-167)          | 0x00B6       |      1 |              1 |
| [65535.14](#event-6553514) | 0x00B7       |     10 |              2 |
| [65535.15](#event-6553515) | 0x00C1       |     10 |              2 |
| [65535.16](#event-6553516) | 0x00CB       |     39 |              9 |
| [65535.17](#event-6553517) | 0x00F2       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x60095     |      393365 |
|       4 | 0xFFF9337A  |  4294521722 |
|       5 | 0xFFFFB654  |  4294948436 |
|       6 | 0x0243      |         579 |
|       7 | 0x0152      |         338 |
|       8 | 0x09E7      |        2535 |
|       9 | 0x0150      |         336 |
|      10 | 0x0154      |         340 |
|      11 | 0x6009A     |      393370 |
|      12 | 0xFFF933F6  |  4294521846 |
|      13 | 0x0B01      |        2817 |
|      14 | 0xFFFFFEE8  |  4294967016 |
|      15 | 0xFFF84B51  |  4294462289 |
|      16 | 0xFFFFE77A  |  4294961018 |
|      17 | 0x03E0      |         992 |
|      18 | 0xFFFFFF4D  |  4294967117 |
|      19 | 0xFFF839B8  |  4294457784 |
|      20 | 0xFFFFEA1F  |  4294961695 |
|      21 | 0x0C3B      |        3131 |
|      22 | 0x0028      |          40 |
|      23 | 0xFFFFFF6A  |  4294967146 |
|      24 | 0xFFF808FC  |  4294445308 |
|      25 | 0xFFFFF16D  |  4294963565 |
|      26 | 0x05B4      |        1460 |
|      27 | 0x002D      |          45 |
|      28 | 0x0F99      |        3993 |
|      29 | 0x003C      |          60 |
|      30 | 0xFFFFFF48  |  4294967112 |
|      31 | 0xFFF893DD  |  4294480861 |
|      32 | 0xFFFFDC9A  |  4294958234 |

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

### Event 0

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 00    "./.....l.....
0010: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             6C F8 FF FF  7F 02 80 01 80 00            l.........  
```

#### Opcodes

```
  0: 0x0014 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            22 00                ".
0020: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x001E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0020 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x0027 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0029 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 02            l.....
0040: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             00                                        .           
```

#### Opcodes

```
  0: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                37 03 80  04 80 05 80 06 80 00          7......... 
```

#### Opcodes

```
  0: 0x0045 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=393.365*, z=-445.574*, y=-18.860*, direction=50.9°*
  1: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               5B                 [
0050: 07 80 1E 12 02 01 1E 12  02 01 73 68 6B 30 53 1E  ..........shk0S.
0060: 12 02 01 1E 12 02 01 73  68 6B 30 00              .......shk0.    
```

#### Opcodes

```
  0: 0x004F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "shk0" with entities [Makki-Chebukki (ID: 16912926/0x0102121E), Makki-Chebukki (ID: 16912926/0x0102121E)], work=338*
  1: 0x005E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "shk0" with entities [Makki-Chebukki (ID: 16912926/0x0102121E), Makki-Chebukki (ID: 16912926/0x0102121E)]
  2: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      4B 1E 12 02              K...
0070: 01 08 80 6F 76 1E 12 02  01 00                    ...ov.....      
```

#### Opcodes

```
  0: 0x006C [0x4B] UPDATE_ENTITY_YAW(entity=Makki-Chebukki (ID: 16912926/0x0102121E), yaw=13.9°*)
  1: 0x0073 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0074 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Makki-Chebukki (ID: 16912926/0x0102121E) Render.Flags0 and Render.Flags3 conditions are met
  3: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                5B 09 80 1E 12 02            [.....
0080: 01 1E 12 02 01 6F 62 69  30 00                    .....obi0.      
```

#### Opcodes

```
  0: 0x007A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "obi0" with entities [Makki-Chebukki (ID: 16912926/0x0102121E), Makki-Chebukki (ID: 16912926/0x0102121E)], work=336*
  1: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                5B 0A 80 1E 12 02            [.....
0090: 01 1E 12 02 01 62 69 6B  30 00                    .....bik0.      
```

#### Opcodes

```
  0: 0x008A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bik0" with entities [Makki-Chebukki (ID: 16912926/0x0102121E), Makki-Chebukki (ID: 16912926/0x0102121E)], work=340*
  1: 0x0099 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                37 0B 80 0C 80 05            7.....
00A0: 80 0D 80 00                                       ....            
```

#### Opcodes

```
  0: 0x009A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=393.370*, z=-445.450*, y=-18.860*, direction=247.6°*
  1: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A4   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             5B 09 80 1E  12 02 01 1E 12 02 01 7A      [..........z
00B0: 69 74 30 00                                       it0.            
```

#### Opcodes

```
  0: 0x00A4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "zit0" with entities [Makki-Chebukki (ID: 16912926/0x0102121E), Makki-Chebukki (ID: 16912926/0x0102121E)], work=336*
  1: 0x00B3 [0x00] END_REQSTACK()
```

### Event 165

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             00                                        .           
```

#### Opcodes

```
  0: 0x00B4 [0x00] END_REQSTACK()
```

### Event 166

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B5  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                00                                      .          
```

#### Opcodes

```
  0: 0x00B5 [0x00] END_REQSTACK()
```

### Event 167

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B6  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                   00                                    .         
```

#### Opcodes

```
  0: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B7   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      37  0E 80 0F 80 10 80 11 80         7........
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x00B7 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.280*, z=-505.007*, y=-6.278*, direction=87.2°*
  1: 0x00C0 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C1   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:    37 12 80 13 80 14 80  15 80 00                  7.........     
```

#### Opcodes

```
  0: 0x00C1 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.179*, z=-509.512*, y=-5.601*, direction=275.2°*
  1: 0x00CA [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CB   |
| Data Size    | 39 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                   32 16 80 5A 00             2..Z.
00D0: 17 80 18 80 19 80 5A 01  4B F8 FF FF 7F 1A 80 1C  ......Z.K.......
00E0: 1B 80 4B F8 FF FF 7F 1C  80 1C 1D 80 1E 24 12 02  ..K..........$..
00F0: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x00CB [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00CE [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-0.150*, Z=-521.988*, Y=-3.731*
  2: 0x00D6 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x00D8 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=8.0°*)
  4: 0x00DF [0x1C] WAIT(45* ticks)
  5: 0x00E2 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=21.9°*)
  6: 0x00E9 [0x1C] WAIT(60* ticks)
  7: 0x00EC [0x1E] EventEntity looks at Promathia (ID: 16912932/0x01021224) and starts talking
  8: 0x00F1 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F2   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:       32 16 80 5A 00 1E  80 1F 80 20 80 5A 01 00    2..Z..... .Z..
```

#### Opcodes

```
  0: 0x00F2 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00F5 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-0.184*, Z=-486.435*, Y=-9.062*
  2: 0x00FD [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x00FF [0x00] END_REQSTACK()
```
