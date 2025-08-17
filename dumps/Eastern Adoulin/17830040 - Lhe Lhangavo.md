# 17830040 - Lhe Lhangavo

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 308 bytes                 |
| Total Events     | 20                        |
| References Count | 13                        |

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
| [1500](#event-1500)        | 0x0044       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0045       |      5 |              2 |
| [65535.9](#event-655359)   | 0x004A       |      8 |              3 |
| [65535.10](#event-6553510) | 0x0052       |      2 |              2 |
| [65535.11](#event-6553511) | 0x0054       |     13 |              3 |
| [65535.12](#event-6553512) | 0x0061       |     33 |              9 |
| [1532](#event-1532)        | 0x0082       |      5 |              2 |
| [1533](#event-1533)        | 0x0087       |      5 |              2 |
| [1535](#event-1535)        | 0x008C       |      5 |              2 |
| [1551](#event-1551)        | 0x0091       |      5 |              2 |
| [1552](#event-1552)        | 0x0096       |      5 |              2 |
| [1549](#event-1549)        | 0x009B       |      5 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0A9A      |        2714 |
|       4 | 0x0A9B      |        2715 |
|       5 | 0x0002      |           2 |
|       6 | 0x000D      |          13 |
|       7 | 0x0129      |         297 |
|       8 | 0xFFFFE454  |  4294960212 |
|       9 | 0xFFFFFA24  |  4294965796 |
|      10 | 0x1C30      |        7216 |
|      11 | 0xFFFFD7D2  |  4294957010 |
|      12 | 0x0800      |        2048 |

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

### Event 1500

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
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                B6 00 03  80 00                         .....      
```

#### Opcodes

```
  0: 0x0045 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2714*)
  1: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004A  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                B6 00 04 80 95 05            ......
0050: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x004A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2715*)
  1: 0x004E [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 2*)
  2: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0052  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       96 00                                         ..            
```

#### Opcodes

```
  0: 0x0052 [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  1: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             92 01 F8 FF  FF 7F 94 01 F8 FF FF 7F      ............
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0054 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x005A [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    32 06 80 1F 00 07 80  08 80 09 80 1F 01 6F 1F   2............o.
0070: 00 0A 80 0B 80 09 80 1F  01 6F 4B F8 FF FF 7F 0C  .........oK.....
0080: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0061 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0064 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.297*, Z=-7.084*, Y=-1.500*
  2: 0x006C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x006F [0x1F] MOVE_ENTITY: EventEntity moves to X=7.216*, Z=-10.286*, Y=-1.500*
  5: 0x0077 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0079 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x007A [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=11.2°*)
  8: 0x0081 [0x00] END_REQSTACK()
```

### Event 1532

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0082  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       B6 00 03 80 00                                .....         
```

#### Opcodes

```
  0: 0x0082 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2714*)
  1: 0x0086 [0x00] END_REQSTACK()
```

### Event 1533

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0087  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      B6  00 04 80 00                     .....    
```

#### Opcodes

```
  0: 0x0087 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2715*)
  1: 0x008B [0x00] END_REQSTACK()
```

### Event 1535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008C  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      B6 00 04 80              ....
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x008C [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2715*)
  1: 0x0090 [0x00] END_REQSTACK()
```

### Event 1551

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0091  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    B6 00 04 80 00                                  .....          
```

#### Opcodes

```
  0: 0x0091 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2715*)
  1: 0x0095 [0x00] END_REQSTACK()
```

### Event 1552

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0096  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   B6 00  04 80 00                       .....     
```

#### Opcodes

```
  0: 0x0096 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2715*)
  1: 0x009A [0x00] END_REQSTACK()
```

### Event 1549

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009B  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   B6 00 04 80 00             .....
```

#### Opcodes

```
  0: 0x009B [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2715*)
  1: 0x009F [0x00] END_REQSTACK()
```
