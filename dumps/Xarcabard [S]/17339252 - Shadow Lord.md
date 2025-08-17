# 17339252 - Shadow Lord

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Xarcabard [S] (ID: 137) |
| Block Size       | 360 bytes               |
| Total Events     | 24                      |
| References Count | 19                      |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0002       |     18 |              4 |
| [65535.3](#event-655353)   | 0x0014       |     10 |              2 |
| [65535.4](#event-655354)   | 0x001E       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0027       |      9 |              3 |
| [65535.6](#event-655356)   | 0x0030       |     10 |              2 |
| [65535.7](#event-655357)   | 0x003A       |     10 |              2 |
| [18](#event-18)            | 0x0044       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0045       |      8 |              3 |
| [65535.9](#event-655359)   | 0x004D       |      8 |              3 |
| [65535.10](#event-6553510) | 0x0055       |      8 |              3 |
| [65535.11](#event-6553511) | 0x005D       |      8 |              3 |
| [65535.12](#event-6553512) | 0x0065       |      8 |              3 |
| [65535.13](#event-6553513) | 0x006D       |      5 |              2 |
| [65535.14](#event-6553514) | 0x0072       |      5 |              2 |
| [65535.15](#event-6553515) | 0x0077       |     10 |              2 |
| [65535.16](#event-6553516) | 0x0081       |      5 |              2 |
| [65535.17](#event-6553517) | 0x0086       |      5 |              2 |
| [65535.18](#event-6553518) | 0x008B       |      5 |              2 |
| [65535.19](#event-6553519) | 0x0090       |      5 |              2 |
| [65535.20](#event-6553520) | 0x0095       |      5 |              2 |
| [65535.21](#event-6553521) | 0x009A       |      5 |              2 |
| [65535.22](#event-6553522) | 0x009F       |     10 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x054F      |        1359 |
|       4 | 0x02E5      |         741 |
|       5 | 0x0109      |         265 |
|       6 | 0x08B1      |        2225 |
|       7 | 0x08A9      |        2217 |
|       8 | 0x0417      |        1047 |
|       9 | 0x0419      |        1049 |
|      10 | 0x007F      |         127 |
|      11 | 0x003C      |          60 |
|      12 | 0x08AB      |        2219 |
|      13 | 0x02F0      |         752 |
|      14 | 0x02EB      |         747 |
|      15 | 0x0550      |        1360 |
|      16 | 0x0108      |         264 |
|      17 | 0x087C      |        2172 |
|      18 | 0x0002      |           2 |

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

### Event 65535.2

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

### Event 65535.3

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

### Event 65535.4

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

### Event 65535.5

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

### Event 65535.6

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

### Event 65535.7

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

### Event 18

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

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                B6 00 03  80 C0 01 80 00                ........   
```

#### Opcodes

```
  0: 0x0045 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1359*)
  1: 0x0049 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004D  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         B6 00 04               ...
0050: 80 C0 01 80 00                                    .....           
```

#### Opcodes

```
  0: 0x004D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=741*)
  1: 0x0051 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0055  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                B6 00 05  80 C0 01 80 00                ........   
```

#### Opcodes

```
  0: 0x0055 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=265*)
  1: 0x0059 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005D  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         B6 00 06               ...
0060: 80 C0 01 80 00                                    .....           
```

#### Opcodes

```
  0: 0x005D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2225*)
  1: 0x0061 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0065  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                B6 00 07  80 C0 01 80 00                ........   
```

#### Opcodes

```
  0: 0x0065 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2217*)
  1: 0x0069 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006D  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         B6 00 08               ...
0070: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x006D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1047*)
  1: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0072  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       B6 00 09 80 00                                .....         
```

#### Opcodes

```
  0: 0x0072 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1049*)
  1: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      6C  F8 FF FF 7F 0A 80 0B 80         l........
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0077 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=127*, fade_time=60*)
  1: 0x0080 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0081  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    B6 00 0C 80 00                                  .....          
```

#### Opcodes

```
  0: 0x0081 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2219*)
  1: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0086  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   B6 00  0D 80 00                       .....     
```

#### Opcodes

```
  0: 0x0086 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=752*)
  1: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008B  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   B6 00 0E 80 00             .....
```

#### Opcodes

```
  0: 0x008B [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=747*)
  1: 0x008F [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0090  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: B6 00 0F 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0090 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1360*)
  1: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0095  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                B6 00 06  80 00                         .....      
```

#### Opcodes

```
  0: 0x0095 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2225*)
  1: 0x0099 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009A  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                B6 00 10 80 00               ..... 
```

#### Opcodes

```
  0: 0x009A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=264*)
  1: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 10 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               B6                 .
00A0: 00 11 80 95 12 80 AB 08  00                       .........       
```

#### Opcodes

```
  0: 0x009F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2172*)
  1: 0x00A3 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 2*)
  2: 0x00A6 [0xAB] EventEntity->Render.Flags2 |= 0x02 // Set bit 1
  3: 0x00A8 [0x00] END_REQSTACK()
```
