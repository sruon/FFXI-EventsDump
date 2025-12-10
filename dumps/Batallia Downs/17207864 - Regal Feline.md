# 17207864 - Regal Feline

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Batallia Downs (ID: 105) |
| Block Size       | 280 bytes                |
| Total Events     | 15                       |
| References Count | 13                       |

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
| [500](#event-500)          | 0x0044       |      4 |              2 |
| [501](#event-501)          | 0x0048       |      4 |              2 |
| [65535.8](#event-655358)   | 0x004C       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0056       |     10 |              2 |
| [65535.10](#event-6553510) | 0x0060       |     23 |              7 |
| [65535.11](#event-6553511) | 0x0077       |     15 |              5 |
| [65535.12](#event-6553512) | 0x0086       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000B      |          11 |
|       4 | 0xFFF997FF  |  4294547455 |
|       5 | 0xFFFCCD8F  |  4294757775 |
|       6 | 0x4E1F      |       19999 |
|       7 | 0x003C      |          60 |
|       8 | 0xFFF997D9  |  4294547417 |
|       9 | 0xFFFCD4ED  |  4294759661 |
|      10 | 0x000D      |          13 |
|      11 | 0xFFF99CC1  |  4294548673 |
|      12 | 0xFFFCC611  |  4294755857 |

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

### Event 500

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             C0 01 80 00                               ....        
```

#### Opcodes

```
  0: 0x0044 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0047 [0x00] END_REQSTACK()
```

### Event 501

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0048  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          C0 01 80 00                      ....    
```

#### Opcodes

```
  0: 0x0048 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      6C F8 FF FF              l...
0050: 7F 02 80 01 80 00                                 ......          
```

#### Opcodes

```
  0: 0x004C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   6C F8  FF FF 7F 00 80 01 80 00        l.........
```

#### Opcodes

```
  0: 0x0056 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 32 03 80 1F 00 04 80 05  80 06 80 1F 01 6F 1E F0  2............o..
0070: FF FF 7F 1C 07 80 00                              .......         
```

#### Opcodes

```
  0: 0x0060 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0063 [0x1F] MOVE_ENTITY: EventEntity moves to X=-419.841*, Z=-209.521*, Y=19.999*
  2: 0x006B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x006E [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0073 [0x1C] WAIT(60* ticks)
  6: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      32  03 80 1F 00 08 80 09 80         2........
0080: 06 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0077 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x007A [0x1F] MOVE_ENTITY: EventEntity moves to X=-419.879*, Z=-207.635*, Y=19.999*
  2: 0x0082 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0084 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0086   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   32 0A  80 1F 00 0B 80 0C 80 06        2.........
0090: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0086 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0089 [0x1F] MOVE_ENTITY: EventEntity moves to X=-418.623*, Z=-211.439*, Y=19.999*
  2: 0x0091 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0093 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0094 [0x00] END_REQSTACK()
```
