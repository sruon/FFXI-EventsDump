# 16982158 - Naja Salaheem

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 404 bytes                     |
| Total Events     | 19                            |
| References Count | 16                            |

## List of Events

| Event ID                    | Entrypoint   |   Size |   Instructions |
|-----------------------------|--------------|--------|----------------|
| [65535](#event-65535)       | 0x0000       |      1 |              1 |
| [65535.1](#event-65535-1)   | 0x0001       |      1 |              1 |
| [65535.2](#event-65535-2)   | 0x0002       |     18 |              4 |
| [65535.3](#event-65535-3)   | 0x0014       |     10 |              2 |
| [65535.4](#event-65535-4)   | 0x001E       |      9 |              3 |
| [65535.5](#event-65535-5)   | 0x0027       |      9 |              3 |
| [65535.6](#event-65535-6)   | 0x0030       |     10 |              2 |
| [65535.7](#event-65535-7)   | 0x003A       |     10 |              2 |
| [3074](#event-3074)         | 0x0044       |      1 |              1 |
| [3076](#event-3076)         | 0x0045       |      1 |              1 |
| [65535.8](#event-65535-8)   | 0x0046       |     10 |              2 |
| [65535.9](#event-65535-9)   | 0x0050       |     21 |              2 |
| [65535.10](#event-65535-10) | 0x0065       |     21 |              2 |
| [65535.11](#event-65535-11) | 0x007A       |     21 |              2 |
| [65535.12](#event-65535-12) | 0x008F       |     21 |              2 |
| [65535.13](#event-65535-13) | 0x00A4       |     21 |              2 |
| [65535.14](#event-65535-14) | 0x00B9       |     21 |              2 |
| [65535.15](#event-65535-15) | 0x00CE       |     21 |              2 |
| [65535.16](#event-65535-16) | 0x00E3       |     21 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x5B62      |       23394 |
|       4 | 0xFFFF5C59  |  4294925401 |
|       5 | 0xFFFFE188  |  4294959496 |
|       6 | 0x01EC      |         492 |
|       7 | 0x0007      |           7 |
|       8 | 0x0037      |          55 |
|       9 | 0x00AE      |         174 |
|      10 | 0x00AB      |         171 |
|      11 | 0x006D      |         109 |
|      12 | 0x009F      |         159 |
|      13 | 0x008F      |         143 |
|      14 | 0x00AF      |         175 |
|      15 | 0x00B0      |         176 |

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

### Event 3074

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

### Event 3076

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

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   37 03  80 04 80 05 80 06 80 00        7.........
```

#### Opcodes

```
  0: 0x0046 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=23.394*, z=-41.895*, y=-7.800*, direction=43.2°*
  1: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: B6 0B 07 80 07 80 00 80  08 80 08 80 08 80 08 80  ................
0060: 00 80 00 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0050 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=7*, head=0*, body=55*, hands=55*, legs=55*, feet=55*, main=0*, sub=0*)
  1: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                B6 0B 07  80 07 80 00 80 09 80 09       ...........
0070: 80 09 80 09 80 00 80 00  80 00                    ..........      
```

#### Opcodes

```
  0: 0x0065 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=7*, head=0*, body=174*, hands=174*, legs=174*, feet=174*, main=0*, sub=0*)
  1: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                B6 0B 07 80 07 80            ......
0080: 00 80 0A 80 0A 80 0A 80  0A 80 00 80 00 80 00     ............... 
```

#### Opcodes

```
  0: 0x007A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=7*, head=0*, body=171*, hands=171*, legs=171*, feet=171*, main=0*, sub=0*)
  1: 0x008E [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008F   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               B6                 .
0090: 0B 07 80 07 80 00 80 0B  80 0B 80 0B 80 0B 80 00  ................
00A0: 80 00 80 00                                       ....            
```

#### Opcodes

```
  0: 0x008F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=7*, head=0*, body=109*, hands=109*, legs=109*, feet=109*, main=0*, sub=0*)
  1: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A4   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             B6 0B 07 80  07 80 00 80 0C 80 0C 80      ............
00B0: 0C 80 0C 80 00 80 00 80  00                       .........       
```

#### Opcodes

```
  0: 0x00A4 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=7*, head=0*, body=159*, hands=159*, legs=159*, feet=159*, main=0*, sub=0*)
  1: 0x00B8 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             B6 0B 07 80 07 80 00           .......
00C0: 80 0D 80 0D 80 0D 80 0D  80 00 80 00 80 00        ..............  
```

#### Opcodes

```
  0: 0x00B9 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=7*, head=0*, body=143*, hands=143*, legs=143*, feet=143*, main=0*, sub=0*)
  1: 0x00CD [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CE   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            B6 0B                ..
00D0: 07 80 07 80 00 80 0E 80  0E 80 0E 80 0E 80 00 80  ................
00E0: 00 80 00                                          ...             
```

#### Opcodes

```
  0: 0x00CE [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=7*, head=0*, body=175*, hands=175*, legs=175*, feet=175*, main=0*, sub=0*)
  1: 0x00E2 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E3   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:          B6 0B 07 80 07  80 00 80 0F 80 0F 80 0F     .............
00F0: 80 0F 80 00 80 00 80 00                           ........        
```

#### Opcodes

```
  0: 0x00E3 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=7*, head=0*, body=176*, hands=176*, legs=176*, feet=176*, main=0*, sub=0*)
  1: 0x00F7 [0x00] END_REQSTACK()
```
