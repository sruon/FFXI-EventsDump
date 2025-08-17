# 17175383 - Nri Sarabah

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Meriphataud Mountains [S] (ID: 97) |
| Block Size       | 304 bytes                          |
| Total Events     | 18                                 |
| References Count | 13                                 |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [3](#event-3)              | 0x0001       |      1 |              1 |
| [4](#event-4)              | 0x0002       |      1 |              1 |
| [5](#event-5)              | 0x0003       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0004       |     13 |              3 |
| [65535.2](#event-655352)   | 0x0011       |     24 |              6 |
| [65535.3](#event-655353)   | 0x0029       |     14 |              4 |
| [65535.4](#event-655354)   | 0x0037       |     19 |              3 |
| [65535.5](#event-655355)   | 0x004A       |     10 |              2 |
| [65535.6](#event-655356)   | 0x0054       |     10 |              2 |
| [11](#event-11)            | 0x005E       |      1 |              1 |
| [65535.7](#event-655357)   | 0x005F       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0060       |     18 |              4 |
| [65535.9](#event-655359)   | 0x0072       |     10 |              2 |
| [65535.10](#event-6553510) | 0x007C       |      9 |              3 |
| [65535.11](#event-6553511) | 0x0085       |      9 |              3 |
| [65535.12](#event-6553512) | 0x008E       |     10 |              2 |
| [65535.13](#event-6553513) | 0x0098       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x002B      |          43 |
|       1 | 0x0028      |          40 |
|       2 | 0xA52D6     |      676566 |
|       3 | 0x76B6      |       30390 |
|       4 | 0xFFFFA25C  |  4294943324 |
|       5 | 0xA81A1     |      688545 |
|       6 | 0x239D      |        9117 |
|       7 | 0xFFFFA208  |  4294943240 |
|       8 | 0x003C      |          60 |
|       9 | 0x0530      |        1328 |
|      10 | 0x0000      |           0 |
|      11 | 0x0001      |           1 |
|      12 | 0x0080      |         128 |

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
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             6E F8 FF FF  7F 00 80 99 F8 FF FF 7F      n...........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0004 [0x6E] EventEntity uses emote 43*
  1: 0x000B [0x99] Wait for EventEntity animation to complete
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 01 80 1F 00 02 80  03 80 04 80 1F 01 1F 00   2..............
0020: 05 80 06 80 07 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=676.566*, Z=30.390*, Y=-23.972*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x1F] MOVE_ENTITY: EventEntity moves to X=688.545*, Z=9.117*, Y=-24.056*
  4: 0x0026 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             32 01 80 1F 00 05 80           2......
0030: 06 80 07 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0029 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x002C [0x1F] MOVE_ENTITY: EventEntity moves to X=688.545*, Z=9.117*, Y=-24.056*
  2: 0x0034 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      1C  08 80 5B 09 80 57 13 06         ...[..W..
0040: 01 57 13 06 01 69 72 6F  30 00                    .W...iro0.      
```

#### Opcodes

```
  0: 0x0037 [0x1C] WAIT(60* ticks)
  1: 0x003A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "iro0" with entities [Nri Sarabah (ID: 17175383/0x01061357), Nri Sarabah (ID: 17175383/0x01061357)], work=1328*
  2: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                6C F8 FF FF 7F 0A            l.....
0050: 80 0B 80 00                                       ....            
```

#### Opcodes

```
  0: 0x004A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             6C F8 FF FF  7F 0C 80 0B 80 00            l.........  
```

#### Opcodes

```
  0: 0x0054 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x005D [0x00] END_REQSTACK()
```

### Event 11

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

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               00                 .
```

#### Opcodes

```
  0: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 22 00 2F 00 F8 FF FF 7F  6C F8 FF FF 7F 0A 80 0B  "./.....l.......
0070: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0060 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0062 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0068 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       6C F8 FF FF 7F 0C  80 0B 80 00                l.........    
```

#### Opcodes

```
  0: 0x0072 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007C  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      22 00 2F 00              "./.
0080: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x007C [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x007E [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0085  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                22 01 2F  01 F8 FF FF 7F 00             "./......  
```

#### Opcodes

```
  0: 0x0085 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0087 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x008D [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            6C F8                l.
0090: FF FF 7F 0A 80 0B 80 00                           ........        
```

#### Opcodes

```
  0: 0x008E [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0097 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0098   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          6C F8 FF FF 7F 0C 80 0B          l.......
00A0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0098 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00A1 [0x00] END_REQSTACK()
```
