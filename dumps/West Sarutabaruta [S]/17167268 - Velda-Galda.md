# 17167268 - Velda-Galda

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | West Sarutabaruta [S] (ID: 95) |
| Block Size       | 280 bytes                      |
| Total Events     | 14                             |
| References Count | 16                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [111](#event-111)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0003       |     21 |              2 |
| [65535.3](#event-655353)   | 0x0018       |     21 |              2 |
| [65535.4](#event-655354)   | 0x002D       |     19 |              4 |
| [65535.5](#event-655355)   | 0x0040       |     12 |              4 |
| [65535.6](#event-655356)   | 0x004C       |      1 |              1 |
| [65535.7](#event-655357)   | 0x004D       |     18 |              4 |
| [65535.8](#event-655358)   | 0x005F       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0069       |      9 |              3 |
| [65535.10](#event-6553510) | 0x0072       |      9 |              3 |
| [65535.11](#event-6553511) | 0x007B       |     10 |              2 |
| [65535.12](#event-6553512) | 0x0085       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001D      |          29 |
|       1 | 0x0003      |           3 |
|       2 | 0x0000      |           0 |
|       3 | 0x0004      |           4 |
|       4 | 0x0005      |           5 |
|       5 | 0x000C      |          12 |
|       6 | 0x00BA      |         186 |
|       7 | 0x0025      |          37 |
|       8 | 0xFFF9B754  |  4294555476 |
|       9 | 0x572A0     |      357024 |
|      10 | 0xFFFF9419  |  4294939673 |
|      11 | 0xFFF9D12E  |  4294562094 |
|      12 | 0x57E3F     |      359999 |
|      13 | 0xFFFF92DB  |  4294939355 |
|      14 | 0x0001      |           1 |
|      15 | 0x0080      |         128 |

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

### Event 111

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

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          B6 0B 00 80 01  80 02 80 03 80 02 80 02     .............
0010: 80 01 80 01 80 01 80 00                           ........        
```

#### Opcodes

```
  0: 0x0003 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=29*, hair=3*, head=0*, body=4*, hands=0*, legs=0*, feet=3*, main=3*, sub=3*)
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          B6 0B 04 80 05 80 02 80          ........
0020: 06 80 06 80 06 80 06 80  02 80 02 80 00           .............   
```

#### Opcodes

```
  0: 0x0018 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=12*, head=0*, body=186*, hands=186*, legs=186*, feet=186*, main=0*, sub=0*)
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 19 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         59 04 F8               Y..
0030: FF FF 7F 07 80 1F 00 08  80 09 80 0A 80 1F 01 00  ................
```

#### Opcodes

```
  0: 0x002D [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 37* * 0.1
  1: 0x0035 [0x1F] MOVE_ENTITY: EventEntity moves to X=-411.820*, Z=357.024*, Y=-27.623*
  2: 0x003D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 1F 00 0B 80 0C 80 0D 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x0040 [0x1F] MOVE_ENTITY: EventEntity moves to X=-405.202*, Z=359.999*, Y=-27.941*
  1: 0x0048 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x004A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      00                       .   
```

#### Opcodes

```
  0: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         22 00 2F               "./
0050: 00 F8 FF FF 7F 6C F8 FF  FF 7F 02 80 0E 80 00     .....l......... 
```

#### Opcodes

```
  0: 0x004D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x004F [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0055 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               6C                 l
0060: F8 FF FF 7F 0F 80 0E 80  00                       .........       
```

#### Opcodes

```
  0: 0x005F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0069  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             22 00 2F 00 F8 FF FF           "./....
0070: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0069 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x006B [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0072  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       22 01 2F 01 F8 FF  FF 7F 00                   "./......     
```

#### Opcodes

```
  0: 0x0072 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0074 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   6C F8 FF FF 7F             l....
0080: 02 80 0E 80 00                                    .....           
```

#### Opcodes

```
  0: 0x007B [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                6C F8 FF  FF 7F 0F 80 0E 80 00          l......... 
```

#### Opcodes

```
  0: 0x0085 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x008E [0x00] END_REQSTACK()
```
