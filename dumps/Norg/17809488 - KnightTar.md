# 17809488 - KnightTar

## Common Data

| Field            | Value          |
|------------------|----------------|
| Zone             | Norg (ID: 252) |
| Block Size       | 308 bytes      |
| Total Events     | 15             |
| References Count | 19             |

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
| [175](#event-175)          | 0x0044       |      1 |              1 |
| [1](#event-1)              | 0x0045       |      1 |              1 |
| [65535.7](#event-655357)   | 0x0046       |     12 |              3 |
| [65535.8](#event-655358)   | 0x0052       |     32 |              6 |
| [65535.9](#event-655359)   | 0x0072       |     15 |              3 |
| [65535.10](#event-6553510) | 0x0081       |     10 |              2 |
| [65535.11](#event-6553511) | 0x008B       |     15 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0xFFF8C2D0  |  4294492880 |
|       4 | 0xFFFC59C0  |  4294728128 |
|       5 | 0xFFFD5D2F  |  4294794543 |
|       6 | 0x00F0      |         240 |
|       7 | 0xFFF8A1A1  |  4294484385 |
|       8 | 0xFFFC5CA3  |  4294728867 |
|       9 | 0xFFFD6021  |  4294795297 |
|      10 | 0x002D      |          45 |
|      11 | 0xFFF91268  |  4294513256 |
|      12 | 0xFFFC4F01  |  4294725377 |
|      13 | 0xFFFD7370  |  4294800240 |
|      14 | 0x0989      |        2441 |
|      15 | 0xFFF8D5AB  |  4294497707 |
|      16 | 0xFFFC5E37  |  4294729271 |
|      17 | 0xFFFD73A8  |  4294800296 |
|      18 | 0x0094      |         148 |

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

### Event 175

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

### Event 1

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

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   33 01  37 03 80 04 80 05 80 06        3.7.......
0050: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0046 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0048 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-474.416*, z=-239.168*, y=-172.753*, direction=21.1°*
  2: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 32 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       33 00 6C F8 FF FF  7F 02 80 01 80 37 07 80    3.l........7..
0060: 08 80 09 80 0A 80 5E 64  66 74 30 94 01 F8 FF FF  ......^dft0.....
0070: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0052 [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  1: 0x0054 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  2: 0x005D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-482.911*, z=-238.429*, y=-171.999*, direction=4.0°*
  3: 0x0066 [0x5E] EventEntity goes idle (kills current action) (animation: "dft0")
  4: 0x006B [0x94] EventEntity->Render.Flags3 ^= 0x01
  5: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       37 0B 80 0C 80 0D  80 0E 80 5E 69 64 6C 30    7........^idl0
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0072 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-454.040*, z=-241.919*, y=-167.056*, direction=214.5°*
  1: 0x007B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0080 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0081   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    37 0B 80 0C 80 0D 80  0E 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0081 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-454.040*, z=-241.919*, y=-167.056*, direction=214.5°*
  1: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   37 0F 80 10 80             7....
0090: 11 80 12 80 5E 69 64 6C  30 00                    ....^idl0.      
```

#### Opcodes

```
  0: 0x008B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-469.589*, z=-238.025*, y=-167.000*, direction=13.0°*
  1: 0x0094 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0099 [0x00] END_REQSTACK()
```
