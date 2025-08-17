# 17167256 - Perih Vashai

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | West Sarutabaruta [S] (ID: 95) |
| Block Size       | 328 bytes                      |
| Total Events     | 19                             |
| References Count | 18                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [105](#event-105)          | 0x0001       |      1 |              1 |
| [106](#event-106)          | 0x0002       |      1 |              1 |
| [110](#event-110)          | 0x0003       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0004       |      5 |              2 |
| [65535.2](#event-655352)   | 0x0009       |      5 |              2 |
| [65535.3](#event-655353)   | 0x000E       |      5 |              2 |
| [65535.4](#event-655354)   | 0x0013       |     26 |              6 |
| [65535.5](#event-655355)   | 0x002D       |     24 |              6 |
| [65535.6](#event-655356)   | 0x0045       |      5 |              2 |
| [65535.7](#event-655357)   | 0x004A       |     10 |              2 |
| [65535.8](#event-655358)   | 0x0054       |     10 |              2 |
| [65535.9](#event-655359)   | 0x005E       |      1 |              1 |
| [65535.10](#event-6553510) | 0x005F       |     18 |              4 |
| [65535.11](#event-6553511) | 0x0071       |     10 |              2 |
| [65535.12](#event-6553512) | 0x007B       |      9 |              3 |
| [65535.13](#event-6553513) | 0x0084       |      9 |              3 |
| [65535.14](#event-6553514) | 0x008D       |     10 |              2 |
| [65535.15](#event-6553515) | 0x0097       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0108      |         264 |
|       1 | 0x08CB      |        2251 |
|       2 | 0x08CA      |        2250 |
|       3 | 0x0122      |         290 |
|       4 | 0x002A      |          42 |
|       5 | 0xFFFB428D  |  4294656653 |
|       6 | 0xFFFFC8E8  |  4294953192 |
|       7 | 0xFFFF4480  |  4294919296 |
|       8 | 0x0046      |          70 |
|       9 | 0xFFFB56FE  |  4294661886 |
|      10 | 0xFFFFCAF1  |  4294953713 |
|      11 | 0xFFFF4481  |  4294919297 |
|      12 | 0xFFFB774C  |  4294670156 |
|      13 | 0x279B      |       10139 |
|      14 | 0x02E4      |         740 |
|      15 | 0x0000      |           0 |
|      16 | 0x0001      |           1 |
|      17 | 0x0080      |         128 |

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             B6 00 00 80  00                           .....       
```

#### Opcodes

```
  0: 0x0004 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=264*)
  1: 0x0008 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             B6 00 01 80 00                 .....  
```

#### Opcodes

```
  0: 0x0009 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2251*)
  1: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000E  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            B6 00                ..
0010: 02 80 00                                          ...             
```

#### Opcodes

```
  0: 0x000E [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2250*)
  1: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 26 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          1C 03 80 6B 69  64 6C 30 F8 FF FF 7F 32     ...kidl0....2
0020: 04 80 1F 00 05 80 06 80  07 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x0013 [0x1C] WAIT(290* ticks)
  1: 0x0016 [0x6B] STOP_AND_IDLE: EventEntity stops current action and resets to idle (animation="idl0")
  2: 0x001F [0x32] ExtData[1]->MainSpeed = 42* * 0.1
  3: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=-310.643*, Z=-14.104*, Y=-48.000*
  4: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         32 08 80               2..
0030: 1F 00 09 80 0A 80 0B 80  1F 01 1F 00 0C 80 0D 80  ................
0040: 0B 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x002D [0x32] ExtData[1]->MainSpeed = 70* * 0.1
  1: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=-305.410*, Z=-13.583*, Y=-47.999*
  2: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003A [0x1F] MOVE_ENTITY: EventEntity moves to X=-297.140*, Z=10.139*, Y=-47.999*
  4: 0x0042 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                B6 00 0E  80 00                         .....      
```

#### Opcodes

```
  0: 0x0045 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=740*)
  1: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                6C F8 FF FF 7F 0F            l.....
0050: 80 10 80 00                                       ....            
```

#### Opcodes

```
  0: 0x004A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             6C F8 FF FF  7F 11 80 10 80 00            l.........  
```

#### Opcodes

```
  0: 0x0054 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            00                   . 
```

#### Opcodes

```
  0: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               22                 "
0060: 00 2F 00 F8 FF FF 7F 6C  F8 FF FF 7F 0F 80 10 80  ./.....l........
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x005F [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0061 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0067 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    6C F8 FF FF 7F 11 80  10 80 00                  l.........     
```

#### Opcodes

```
  0: 0x0071 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007B  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   22 00 2F 00 F8             "./..
0080: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x007B [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x007D [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0084  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             22 01 2F 01  F8 FF FF 7F 00               "./......   
```

#### Opcodes

```
  0: 0x0084 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0086 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         6C F8 FF               l..
0090: FF 7F 0F 80 10 80 00                              .......         
```

#### Opcodes

```
  0: 0x008D [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      6C  F8 FF FF 7F 11 80 10 80         l........
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x0097 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00A0 [0x00] END_REQSTACK()
```
