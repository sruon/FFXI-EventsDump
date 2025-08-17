# 17175375 - Ghyo Molkot

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Meriphataud Mountains [S] (ID: 97) |
| Block Size       | 308 bytes                          |
| Total Events     | 17                                 |
| References Count | 16                                 |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [3](#event-3)              | 0x0001       |      1 |              1 |
| [4](#event-4)              | 0x0002       |      1 |              1 |
| [5](#event-5)              | 0x0003       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0004       |     16 |              4 |
| [65535.2](#event-655352)   | 0x0014       |     24 |              6 |
| [65535.3](#event-655353)   | 0x002C       |     14 |              4 |
| [65535.4](#event-655354)   | 0x003A       |     10 |              2 |
| [65535.5](#event-655355)   | 0x0044       |     10 |              2 |
| [65535.6](#event-655356)   | 0x004E       |      1 |              1 |
| [65535.7](#event-655357)   | 0x004F       |     18 |              4 |
| [65535.8](#event-655358)   | 0x0061       |     10 |              2 |
| [65535.9](#event-655359)   | 0x006B       |      9 |              3 |
| [65535.10](#event-6553510) | 0x0074       |      9 |              3 |
| [65535.11](#event-6553511) | 0x007D       |     10 |              2 |
| [65535.12](#event-6553512) | 0x0087       |     10 |              2 |
| [65535.13](#event-6553513) | 0x0091       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x0024      |          36 |
|       2 | 0x0028      |          40 |
|       3 | 0xA539F     |      676767 |
|       4 | 0x67A7      |       26535 |
|       5 | 0xFFFFA289  |  4294943369 |
|       6 | 0xA87A1     |      690081 |
|       7 | 0x0D0F      |        3343 |
|       8 | 0xFFFF9E87  |  4294942343 |
|       9 | 0x0000      |           0 |
|      10 | 0x0001      |           1 |
|      11 | 0x0080      |         128 |
|      12 | 0x000D      |          13 |
|      13 | 0x61729     |      399145 |
|      14 | 0x1098A     |       67978 |
|      15 | 0xFFFFC2B6  |  4294951606 |

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

### Event 3

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

### Event 4

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

### Event 5

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
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             1C 00 80 6E  F8 FF FF 7F 01 80 99 F8      ...n........
0010: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0004 [0x1C] WAIT(20* ticks)
  1: 0x0007 [0x6E] EventEntity uses emote 36*
  2: 0x000E [0x99] Wait for EventEntity animation to complete
  3: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             32 02 80 1F  00 03 80 04 80 05 80 1F      2...........
0020: 01 1F 00 06 80 07 80 08  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x0014 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0017 [0x1F] MOVE_ENTITY: EventEntity moves to X=676.767*, Z=26.535*, Y=-23.927*
  2: 0x001F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0021 [0x1F] MOVE_ENTITY: EventEntity moves to X=690.081*, Z=3.343*, Y=-24.953*
  4: 0x0029 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      32 02 80 1F              2...
0030: 00 06 80 07 80 08 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x002C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x002F [0x1F] MOVE_ENTITY: EventEntity moves to X=690.081*, Z=3.343*, Y=-24.953*
  2: 0x0037 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 09            l.....
0040: 80 0A 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             6C F8 FF FF  7F 0B 80 0A 80 00            l.........  
```

#### Opcodes

```
  0: 0x0044 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            00                   . 
```

#### Opcodes

```
  0: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               22                 "
0050: 00 2F 00 F8 FF FF 7F 6C  F8 FF FF 7F 09 80 0A 80  ./.....l........
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x004F [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0051 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0057 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    6C F8 FF FF 7F 0B 80  0A 80 00                  l.........     
```

#### Opcodes

```
  0: 0x0061 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006B  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   22 00 2F 00 F8             "./..
0070: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x006B [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x006D [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0073 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0074  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             22 01 2F 01  F8 FF FF 7F 00               "./......   
```

#### Opcodes

```
  0: 0x0074 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0076 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         6C F8 FF               l..
0080: FF 7F 09 80 0A 80 00                              .......         
```

#### Opcodes

```
  0: 0x007D [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      6C  F8 FF FF 7F 0B 80 0A 80         l........
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0087 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    32 0C 80 1F 00 0D 80  0E 80 0F 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0091 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0094 [0x1F] MOVE_ENTITY: EventEntity moves to X=399.145*, Z=67.978*, Y=-15.690*
  2: 0x009C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009E [0x00] END_REQSTACK()
```
