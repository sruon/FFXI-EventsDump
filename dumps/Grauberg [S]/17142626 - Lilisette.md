# 17142626 - Lilisette

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Grauberg [S] (ID: 89) |
| Block Size       | 460 bytes             |
| Total Events     | 21                    |
| References Count | 25                    |

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
| [26](#event-26)            | 0x0044       |      9 |              3 |
| [65535.8](#event-655358)   | 0x004D       |      3 |              2 |
| [65535.9](#event-655359)   | 0x0050       |      3 |              2 |
| [30](#event-30)            | 0x0053       |      7 |              2 |
| [32](#event-32)            | 0x005A       |      7 |              2 |
| [36](#event-36)            | 0x0061       |      1 |              1 |
| [37](#event-37)            | 0x0062       |      1 |              1 |
| [38](#event-38)            | 0x0063       |      1 |              1 |
| [45](#event-45)            | 0x0064       |      1 |              1 |
| [65535.10](#event-6553510) | 0x0065       |     10 |              2 |
| [65535.11](#event-6553511) | 0x006F       |     10 |              2 |
| [65535.12](#event-6553512) | 0x0079       |     74 |             16 |
| [65535.13](#event-6553513) | 0x00C3       |     64 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0028      |          40 |
|       4 | 0xFFFDCBF2  |  4294822898 |
|       5 | 0x86CE1     |      552161 |
|       6 | 0xFFFFD29F  |  4294955679 |
|       7 | 0xFFFDCDF9  |  4294823417 |
|       8 | 0x8745F     |      554079 |
|       9 | 0xFFFFD85E  |  4294957150 |
|      10 | 0xFFFDCF70  |  4294823792 |
|      11 | 0x8796F     |      555375 |
|      12 | 0xFFFFDC74  |  4294958196 |
|      13 | 0xFFFDD12B  |  4294824235 |
|      14 | 0x881B4     |      557492 |
|      15 | 0xFFFFE0B8  |  4294959288 |
|      16 | 0xFFFDD349  |  4294824777 |
|      17 | 0x88A81     |      559745 |
|      18 | 0xFFFFE3AF  |  4294960047 |
|      19 | 0xFFFDD4AE  |  4294825134 |
|      20 | 0x88FC8     |      561096 |
|      21 | 0xFFFFE46F  |  4294960239 |
|      22 | 0xFFFDD712  |  4294825746 |
|      23 | 0x89A3F     |      563775 |
|      24 | 0xFFFFE5A2  |  4294960546 |

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

### Event 26

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             92 01 F8 FF  FF 7F A4 01 00               .........   
```

#### Opcodes

```
  0: 0x0044 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x004A [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  2: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004D  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         A5 01 00               ...
```

#### Opcodes

```
  0: 0x004D [0xA5] EventEntity->Flags3.BallistaTeam |= 0x08  // Set bit 3 of BallistaTeam
  1: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0050  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: A5 00 00                                          ...             
```

#### Opcodes

```
  0: 0x0050 [0xA5] EventEntity->Flags3.BallistaTeam &= ~0x08  // Clear bit 3 of BallistaTeam
  1: 0x0052 [0x00] END_REQSTACK()
```

### Event 30

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0053  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x0053 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0059 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                92 01 F8 FF FF 7F            ......
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x005A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0060 [0x00] END_REQSTACK()
```

### Event 36

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0061  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    00                                              .              
```

#### Opcodes

```
  0: 0x0061 [0x00] END_REQSTACK()
```

### Event 37

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0062  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       00                                            .             
```

#### Opcodes

```
  0: 0x0062 [0x00] END_REQSTACK()
```

### Event 38

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          00                                          .            
```

#### Opcodes

```
  0: 0x0063 [0x00] END_REQSTACK()
```

### Event 45

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0064  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             00                                        .           
```

#### Opcodes

```
  0: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                6C 62 93  05 01 00 80 01 80 00          lb........ 
```

#### Opcodes

```
  0: 0x0065 [0x6C] FADE_ENTITY_COLOR(entity_id=Lilisette (ID: 17142626/0x01059362), end_alpha=0*, fade_time=1*)
  1: 0x006E [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               6C                 l
0070: 62 93 05 01 02 80 01 80  00                       b........       
```

#### Opcodes

```
  0: 0x006F [0x6C] FADE_ENTITY_COLOR(entity_id=Lilisette (ID: 17142626/0x01059362), end_alpha=128*, fade_time=1*)
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 74 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             32 03 80 1F 00 04 80           2......
0080: 05 80 06 80 1F 01 1F 00  07 80 08 80 09 80 1F 01  ................
0090: 1F 00 0A 80 0B 80 0C 80  1F 01 1F 00 0D 80 0E 80  ................
00A0: 0F 80 1F 01 1F 00 10 80  11 80 12 80 1F 01 1F 00  ................
00B0: 13 80 14 80 15 80 1F 01  1F 00 16 80 17 80 18 80  ................
00C0: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0079 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x007C [0x1F] MOVE_ENTITY: EventEntity moves to X=-144.398*, Z=552.161*, Y=-11.617*
  2: 0x0084 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0086 [0x1F] MOVE_ENTITY: EventEntity moves to X=-143.879*, Z=554.079*, Y=-10.146*
  4: 0x008E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0090 [0x1F] MOVE_ENTITY: EventEntity moves to X=-143.504*, Z=555.375*, Y=-9.100*
  6: 0x0098 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x009A [0x1F] MOVE_ENTITY: EventEntity moves to X=-143.061*, Z=557.492*, Y=-8.008*
  8: 0x00A2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x00A4 [0x1F] MOVE_ENTITY: EventEntity moves to X=-142.519*, Z=559.745*, Y=-7.249*
 10: 0x00AC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x00AE [0x1F] MOVE_ENTITY: EventEntity moves to X=-142.162*, Z=561.096*, Y=-7.057*
 12: 0x00B6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 13: 0x00B8 [0x1F] MOVE_ENTITY: EventEntity moves to X=-141.550*, Z=563.775*, Y=-6.750*
 14: 0x00C0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 15: 0x00C2 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C3   |
| Data Size    | 64 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          32 03 80 1F 00  13 80 14 80 15 80 1F 01     2............
00D0: 1F 00 10 80 11 80 12 80  1F 01 1F 00 0D 80 0E 80  ................
00E0: 0F 80 1F 01 1F 00 0A 80  0B 80 0C 80 1F 01 1F 00  ................
00F0: 07 80 08 80 09 80 1F 01  1F 00 04 80 05 80 06 80  ................
0100: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x00C3 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00C6 [0x1F] MOVE_ENTITY: EventEntity moves to X=-142.162*, Z=561.096*, Y=-7.057*
  2: 0x00CE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D0 [0x1F] MOVE_ENTITY: EventEntity moves to X=-142.519*, Z=559.745*, Y=-7.249*
  4: 0x00D8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00DA [0x1F] MOVE_ENTITY: EventEntity moves to X=-143.061*, Z=557.492*, Y=-8.008*
  6: 0x00E2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00E4 [0x1F] MOVE_ENTITY: EventEntity moves to X=-143.504*, Z=555.375*, Y=-9.100*
  8: 0x00EC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x00EE [0x1F] MOVE_ENTITY: EventEntity moves to X=-143.879*, Z=554.079*, Y=-10.146*
 10: 0x00F6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x00F8 [0x1F] MOVE_ENTITY: EventEntity moves to X=-144.398*, Z=552.161*, Y=-11.617*
 12: 0x0100 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 13: 0x0102 [0x00] END_REQSTACK()
```
