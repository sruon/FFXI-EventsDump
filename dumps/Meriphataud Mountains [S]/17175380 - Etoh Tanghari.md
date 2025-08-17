# 17175380 - Etoh Tanghari

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Meriphataud Mountains [S] (ID: 97) |
| Block Size       | 396 bytes                          |
| Total Events     | 19                                 |
| References Count | 23                                 |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [3](#event-3)              | 0x0001       |      1 |              1 |
| [4](#event-4)              | 0x0002       |      1 |              1 |
| [5](#event-5)              | 0x0003       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0004       |     19 |              3 |
| [65535.2](#event-655352)   | 0x0017       |     16 |              4 |
| [65535.3](#event-655353)   | 0x0027       |     14 |              4 |
| [65535.4](#event-655354)   | 0x0035       |     24 |              6 |
| [65535.5](#event-655355)   | 0x004D       |     14 |              4 |
| [65535.6](#event-655356)   | 0x005B       |     31 |              7 |
| [65535.7](#event-655357)   | 0x007A       |     10 |              2 |
| [65535.8](#event-655358)   | 0x0084       |     10 |              2 |
| [65535.9](#event-655359)   | 0x008E       |      1 |              1 |
| [65535.10](#event-6553510) | 0x008F       |     18 |              4 |
| [65535.11](#event-6553511) | 0x00A1       |     10 |              2 |
| [65535.12](#event-6553512) | 0x00AB       |      9 |              3 |
| [65535.13](#event-6553513) | 0x00B4       |      9 |              3 |
| [65535.14](#event-6553514) | 0x00BD       |     10 |              2 |
| [65535.15](#event-6553515) | 0x00C7       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000F      |          15 |
|       1 | 0x052E      |        1326 |
|       2 | 0x001E      |          30 |
|       3 | 0x000C      |          12 |
|       4 | 0x0028      |          40 |
|       5 | 0xA6220     |      680480 |
|       6 | 0x6CDD      |       27869 |
|       7 | 0xFFFFA3A3  |  4294943651 |
|       8 | 0xA7D90     |      687504 |
|       9 | 0x40B0      |       16560 |
|      10 | 0xFFFFA0E1  |  4294942945 |
|      11 | 0xA8FAF     |      692143 |
|      12 | 0x1665      |        5733 |
|      13 | 0xFFFF9F09  |  4294942473 |
|      14 | 0x602BC     |      393916 |
|      15 | 0x110DA     |       69850 |
|      16 | 0xFFFFC06F  |  4294951023 |
|      17 | 0x005A      |          90 |
|      18 | 0x000A      |          10 |
|      19 | 0x0276      |         630 |
|      20 | 0x0000      |           0 |
|      21 | 0x0001      |           1 |
|      22 | 0x0080      |         128 |

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
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             1C 00 80 5B  01 80 F8 FF FF 7F F8 FF      ...[........
0010: FF 7F 6E 79 61 31 00                              ..nya1.         
```

#### Opcodes

```
  0: 0x0004 [0x1C] WAIT(15* ticks)
  1: 0x0007 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "nya1" with entities [EventEntity, EventEntity], work=1326*
  2: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      1C  02 80 6E F8 FF FF 7F 03         ...n.....
0020: 80 99 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0017 [0x1C] WAIT(30* ticks)
  1: 0x001A [0x6E] EventEntity uses emote 12*
  2: 0x0021 [0x99] Wait for EventEntity animation to complete
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      32  04 80 1F 00 05 80 06 80         2........
0030: 07 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0027 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x002A [0x1F] MOVE_ENTITY: EventEntity moves to X=680.480*, Z=27.869*, Y=-23.645*
  2: 0x0032 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                32 04 80  1F 00 08 80 09 80 0A 80       2..........
0040: 1F 01 1F 00 0B 80 0C 80  0D 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x0035 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0038 [0x1F] MOVE_ENTITY: EventEntity moves to X=687.504*, Z=16.560*, Y=-24.351*
  2: 0x0040 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0042 [0x1F] MOVE_ENTITY: EventEntity moves to X=692.143*, Z=5.733*, Y=-24.823*
  4: 0x004A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         32 04 80               2..
0050: 1F 00 0E 80 0F 80 10 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x004D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0050 [0x1F] MOVE_ENTITY: EventEntity moves to X=393.916*, Z=69.850*, Y=-16.273*
  2: 0x0058 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 31 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   1C 11 80 6E 54             ...nT
0060: 13 06 01 12 80 99 54 13  06 01 1C 13 80 6E 54 13  ......T......nT.
0070: 06 01 03 80 99 54 13 06  01 00                    .....T....      
```

#### Opcodes

```
  0: 0x005B [0x1C] WAIT(90* ticks)
  1: 0x005E [0x6E] Etoh Tanghari (ID: 17175380/0x01061354) uses emote 10*
  2: 0x0065 [0x99] Wait for Etoh Tanghari (ID: 17175380/0x01061354) animation to complete
  3: 0x006A [0x1C] WAIT(630* ticks)
  4: 0x006D [0x6E] Etoh Tanghari (ID: 17175380/0x01061354) uses emote 12*
  5: 0x0074 [0x99] Wait for Etoh Tanghari (ID: 17175380/0x01061354) animation to complete
  6: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                6C F8 FF FF 7F 14            l.....
0080: 80 15 80 00                                       ....            
```

#### Opcodes

```
  0: 0x007A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             6C F8 FF FF  7F 16 80 15 80 00            l.........  
```

#### Opcodes

```
  0: 0x0084 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x008D [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            00                   . 
```

#### Opcodes

```
  0: 0x008E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008F   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               22                 "
0090: 00 2F 00 F8 FF FF 7F 6C  F8 FF FF 7F 14 80 15 80  ./.....l........
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x008F [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0091 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0097 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x00A0 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A1   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:    6C F8 FF FF 7F 16 80  15 80 00                  l.........     
```

#### Opcodes

```
  0: 0x00A1 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00AA [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AB  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   22 00 2F 00 F8             "./..
00B0: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x00AB [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00AD [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x00B3 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B4  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             22 01 2F 01  F8 FF FF 7F 00               "./......   
```

#### Opcodes

```
  0: 0x00B4 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x00B6 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x00BC [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BD   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                         6C F8 FF               l..
00C0: FF 7F 14 80 15 80 00                              .......         
```

#### Opcodes

```
  0: 0x00BD [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x00C6 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C7   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                      6C  F8 FF FF 7F 16 80 15 80         l........
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00C7 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00D0 [0x00] END_REQSTACK()
```
