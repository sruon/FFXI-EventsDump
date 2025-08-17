# 17723443 - Ranchuriome

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 392 bytes                     |
| Total Events     | 12                            |
| References Count | 24                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [73](#event-73)          | 0x0001       |     10 |              2 |
| [67](#event-67)          | 0x000B       |     29 |              6 |
| [65535.1](#event-655351) | 0x0028       |     31 |              9 |
| [65535.2](#event-655352) | 0x0047       |     13 |              4 |
| [70](#event-70)          | 0x0054       |     10 |              2 |
| [65535.3](#event-655353) | 0x005E       |     20 |              6 |
| [65535.4](#event-655354) | 0x0072       |     21 |              5 |
| [65535.5](#event-655355) | 0x0087       |     29 |              3 |
| [65535.6](#event-655356) | 0x00A4       |      9 |              3 |
| [65535.7](#event-655357) | 0x00AD       |     29 |              3 |
| [65535.8](#event-655358) | 0x00CA       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFD51A7  |  4294791591 |
|       1 | 0x275E6     |      161254 |
|       2 | 0x2EDF      |       11999 |
|       3 | 0x06B6      |        1718 |
|       4 | 0xFFFD5BB4  |  4294794164 |
|       5 | 0x3C794     |      247700 |
|       6 | 0x0000      |           0 |
|       7 | 0x0B71      |        2929 |
|       8 | 0x0001      |           1 |
|       9 | 0x000D      |          13 |
|      10 | 0xFFFD4783  |  4294788995 |
|      11 | 0x26CA0     |      158880 |
|      12 | 0xFFFD582F  |  4294793263 |
|      13 | 0x2701E     |      159774 |
|      14 | 0x0F9F      |        3999 |
|      15 | 0x0075      |         117 |
|      16 | 0xFFFD6371  |  4294796145 |
|      17 | 0x26E03     |      159235 |
|      18 | 0xFFFD48D5  |  4294789333 |
|      19 | 0x2756F     |      161135 |
|      20 | 0xFFFD3722  |  4294784802 |
|      21 | 0x27527     |      161063 |
|      22 | 0x001E      |          30 |
|      23 | 0x003C      |          60 |

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

### Event 73

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-175.705*, z=161.254*, y=11.999*, direction=151.0°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 67

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 29 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   33 01 37 04 80             3.7..
0010: 05 80 06 80 07 80 6C F8  FF FF 7F 06 80 08 80 22  ......l........"
0020: 00 92 01 F8 FF FF 7F 00                           ........        
```

#### Opcodes

```
  0: 0x000B [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-173.132*, z=247.700*, y=0.000*, direction=257.4°*
  2: 0x0016 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x001F [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  4: 0x0021 [0x92] EventEntity->Render.Flags3 ^= 0x01
  5: 0x0027 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 31 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          32 09 80 1F 00 0A 80 0B          2.......
0030: 80 02 80 1F 01 6F 1E 32  70 0E 01 6F 70 4A 32 70  .....o.2p..opJ2p
0040: 0E 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0028 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002B [0x1F] MOVE_ENTITY: EventEntity moves to X=-178.301*, Z=158.880*, Y=11.999*
  2: 0x0033 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0036 [0x1E] EventEntity looks at Miaux (ID: 17723442/0x010E7032) and starts talking
  5: 0x003B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x003C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x003D [0x4A] Miaux (ID: 17723442/0x010E7032) looks at EventEntity
  8: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 13 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      1F  00 00 80 01 80 02 80 1F         .........
0050: 01 22 01 00                                       ."..            
```

#### Opcodes

```
  0: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=-175.705*, Z=161.254*, Y=11.999*
  1: 0x004F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0051 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  3: 0x0053 [0x00] END_REQSTACK()
```

### Event 70

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             37 0C 80 0D  80 0E 80 0F 80 00            7.........  
```

#### Opcodes

```
  0: 0x0054 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-174.033*, z=159.774*, y=3.999*, direction=10.3°*
  1: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            32 09                2.
0060: 80 1F 00 10 80 11 80 0E  80 1F 01 6F 1E 32 70 0E  ...........o.2p.
0070: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x005E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0061 [0x1F] MOVE_ENTITY: EventEntity moves to X=-171.151*, Z=159.235*, Y=3.999*
  2: 0x0069 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x006C [0x1E] EventEntity looks at Miaux (ID: 17723442/0x010E7032) and starts talking
  5: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       1F 00 12 80 13 80  0E 80 1F 01 1F 00 14 80    ..............
0080: 15 80 0E 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0072 [0x1F] MOVE_ENTITY: EventEntity moves to X=-177.963*, Z=161.135*, Y=3.999*
  1: 0x007A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x007C [0x1F] MOVE_ENTITY: EventEntity moves to X=-182.494*, Z=161.063*, Y=3.999*
  3: 0x0084 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      5B  16 80 F8 FF FF 7F F8 FF         [........
0090: FF 7F 74 6C 6B 30 53 F8  FF FF 7F F8 FF FF 7F 74  ..tlk0S........t
00A0: 6C 6B 30 00                                       lk0.            
```

#### Opcodes

```
  0: 0x0087 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  1: 0x0096 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A4  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             5E 69 64 6C  30 1C 17 80 00               ^idl0....   
```

#### Opcodes

```
  0: 0x00A4 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00A9 [0x1C] WAIT(60* ticks)
  2: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         5B 16 80               [..
00B0: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 53 F8 FF FF  ........thk1S...
00C0: 7F F8 FF FF 7F 74 68 6B  31 00                    .....thk1.      
```

#### Opcodes

```
  0: 0x00AD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=30*
  1: 0x00BC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x00C9 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CA   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                5B 16 80 F8 FF FF            [.....
00D0: 7F F8 FF FF 7F 74 68 6B  32 53 F8 FF FF 7F F8 FF  .....thk2S......
00E0: FF 7F 74 68 6B 32 00                              ..thk2.         
```

#### Opcodes

```
  0: 0x00CA [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=30*
  1: 0x00D9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x00E6 [0x00] END_REQSTACK()
```
