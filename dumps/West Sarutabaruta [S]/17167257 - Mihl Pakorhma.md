# 17167257 - Mihl Pakorhma

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | West Sarutabaruta [S] (ID: 95) |
| Block Size       | 372 bytes                      |
| Total Events     | 20                             |
| References Count | 23                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [105](#event-105)          | 0x0001       |      1 |              1 |
| [106](#event-106)          | 0x0002       |      1 |              1 |
| [110](#event-110)          | 0x0003       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0004       |     24 |              6 |
| [65535.2](#event-655352)   | 0x001C       |     10 |              2 |
| [65535.3](#event-655353)   | 0x0026       |     10 |              2 |
| [65535.4](#event-655354)   | 0x0030       |     14 |              4 |
| [107](#event-107)          | 0x003E       |      1 |              1 |
| [112](#event-112)          | 0x003F       |      1 |              1 |
| [113](#event-113)          | 0x0040       |      1 |              1 |
| [65535.5](#event-655355)   | 0x0041       |     25 |              3 |
| [65535.6](#event-655356)   | 0x005A       |     25 |              3 |
| [65535.7](#event-655357)   | 0x0073       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0074       |     18 |              4 |
| [65535.9](#event-655359)   | 0x0086       |     10 |              2 |
| [65535.10](#event-6553510) | 0x0090       |      9 |              3 |
| [65535.11](#event-6553511) | 0x0099       |      9 |              3 |
| [65535.12](#event-6553512) | 0x00A2       |     10 |              2 |
| [65535.13](#event-6553513) | 0x00AC       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000C      |          12 |
|       1 | 0x4DFAA     |      319402 |
|       2 | 0xFFFFD84B  |  4294957131 |
|       3 | 0xFFFFEEDE  |  4294962910 |
|       4 | 0x0000      |           0 |
|       5 | 0x0001      |           1 |
|       6 | 0x0080      |         128 |
|       7 | 0x0028      |          40 |
|       8 | 0x4E856     |      321622 |
|       9 | 0xFFFFEE55  |  4294962773 |
|      10 | 0xFFFFF03F  |  4294963263 |
|      11 | 0x0007      |           7 |
|      12 | 0x00B7      |         183 |
|      13 | 0x0089      |         137 |
|      14 | 0x000F      |          15 |
|      15 | 0x00AC      |         172 |
|      16 | 0x0061      |          97 |
|      17 | 0x000D      |          13 |
|      18 | 0x002D      |          45 |
|      19 | 0x0010      |          16 |
|      20 | 0x000E      |          14 |
|      21 | 0x006E      |         110 |
|      22 | 0x0059      |          89 |

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

### Event 105

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

### Event 106

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 110

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             32 00 80 1F  00 01 80 02 80 03 80 1F      2...........
0010: 01 6F 4A 99 F3 05 01 96  F3 05 01 00              .oJ.........    
```

#### Opcodes

```
  0: 0x0004 [0x32] ExtData[1]->MainSpeed = 12* * 0.1
  1: 0x0007 [0x1F] MOVE_ENTITY: EventEntity moves to X=319.402*, Z=-10.165*, Y=-4.386*
  2: 0x000F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0011 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0012 [0x4A] Mihl Pakorhma (ID: 17167257/0x0105F399) looks at Romaa Mihgo (ID: 17167254/0x0105F396)
  5: 0x001B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      6C F8 FF FF              l...
0020: 7F 04 80 05 80 00                                 ......          
```

#### Opcodes

```
  0: 0x001C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   6C F8  FF FF 7F 06 80 05 80 00        l.........
```

#### Opcodes

```
  0: 0x0026 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 32 07 80 1F 00 08 80 09  80 0A 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0030 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0033 [0x1F] MOVE_ENTITY: EventEntity moves to X=321.622*, Z=-4.523*, Y=-4.033*
  2: 0x003B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003D [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            00                   . 
```

#### Opcodes

```
  0: 0x003E [0x00] END_REQSTACK()
```

### Event 112

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               00                 .
```

#### Opcodes

```
  0: 0x003F [0x00] END_REQSTACK()
```

### Event 113

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0040  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    B6 0B 0B 80 05 80 0C  80 0D 80 0C 80 0E 80 0F   ...............
0050: 80 07 80 04 80 B6 0F 10  80 00                    ..........      
```

#### Opcodes

```
  0: 0x0041 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=1*, head=183*, body=137*, hands=183*, legs=15*, feet=172*, main=40*, sub=0*)
  1: 0x0055 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=97*)
  2: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                B6 0B 0B 80 11 80            ......
0060: 04 80 12 80 13 80 14 80  14 80 15 80 04 80 B6 0F  ................
0070: 16 80 00                                          ...             
```

#### Opcodes

```
  0: 0x005A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=13*, head=0*, body=45*, hands=16*, legs=14*, feet=14*, main=110*, sub=0*)
  1: 0x006E [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=89*)
  2: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0073  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          00                                          .            
```

#### Opcodes

```
  0: 0x0073 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0074   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             22 00 2F 00  F8 FF FF 7F 6C F8 FF FF      "./.....l...
0080: 7F 04 80 05 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0074 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0076 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x007C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0086   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   6C F8  FF FF 7F 06 80 05 80 00        l.........
```

#### Opcodes

```
  0: 0x0086 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x008F [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0090  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: 22 00 2F 00 F8 FF FF 7F  00                       "./......       
```

#### Opcodes

```
  0: 0x0090 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0092 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0099  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             22 01 2F 01 F8 FF FF           "./....
00A0: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0099 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x009B [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x00A1 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A2   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       6C F8 FF FF 7F 04  80 05 80 00                l.........    
```

#### Opcodes

```
  0: 0x00A2 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x00AB [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AC   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      6C F8 FF FF              l...
00B0: 7F 06 80 05 80 00                                 ......          
```

#### Opcodes

```
  0: 0x00AC [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00B5 [0x00] END_REQSTACK()
```
