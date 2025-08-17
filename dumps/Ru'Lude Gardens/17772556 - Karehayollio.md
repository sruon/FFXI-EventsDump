# 17772556 - Karehayollio

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 588 bytes                 |
| Total Events     | 31                        |
| References Count | 17                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      3 |              2 |
| [58](#event-58)            | 0x0003       |     22 |              4 |
| [65](#event-65)            | 0x0019       |     32 |              5 |
| [128](#event-128)          | 0x0039       |      1 |              1 |
| [60](#event-60)            | 0x003A       |      1 |              1 |
| [65535.1](#event-655351)   | 0x003B       |     29 |              3 |
| [65535.2](#event-655352)   | 0x0058       |     29 |              3 |
| [65535.3](#event-655353)   | 0x0075       |     29 |              3 |
| [65535.4](#event-655354)   | 0x0092       |      9 |              3 |
| [65535.5](#event-655355)   | 0x009B       |      9 |              3 |
| [65535.6](#event-655356)   | 0x00A4       |      1 |              1 |
| [65535.7](#event-655357)   | 0x00A5       |     16 |              2 |
| [65535.8](#event-655358)   | 0x00B5       |     16 |              2 |
| [65535.9](#event-655359)   | 0x00C5       |     16 |              2 |
| [65535.10](#event-6553510) | 0x00D5       |     16 |              2 |
| [65535.11](#event-6553511) | 0x00E5       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00F5       |     16 |              2 |
| [65535.13](#event-6553513) | 0x0105       |      1 |              1 |
| [65535.14](#event-6553514) | 0x0106       |     18 |              4 |
| [65535.15](#event-6553515) | 0x0118       |     10 |              2 |
| [65535.16](#event-6553516) | 0x0122       |      9 |              3 |
| [65535.17](#event-6553517) | 0x012B       |      9 |              3 |
| [65535.18](#event-6553518) | 0x0134       |     10 |              2 |
| [65535.19](#event-6553519) | 0x013E       |     10 |              2 |
| [10188](#event-10188)      | 0x0148       |      1 |              1 |
| [10189](#event-10189)      | 0x0149       |      1 |              1 |
| [10190](#event-10190)      | 0x014A       |      1 |              1 |
| [10200](#event-10200)      | 0x014B       |      1 |              1 |
| [10208](#event-10208)      | 0x014C       |      1 |              1 |
| [65535.20](#event-6553520) | 0x014D       |     45 |             11 |
| [10199](#event-10199)      | 0x017A       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFF5FF  |  4294964735 |
|       1 | 0x16030     |       90160 |
|       2 | 0xFFFFE706  |  4294960902 |
|       3 | 0x027B      |         635 |
|       4 | 0x00E9      |         233 |
|       5 | 0x003C      |          60 |
|       6 | 0x00EA      |         234 |
|       7 | 0x0000      |           0 |
|       8 | 0x0001      |           1 |
|       9 | 0x0080      |         128 |
|      10 | 0x000D      |          13 |
|      11 | 0xFFFFF9AE  |  4294965678 |
|      12 | 0x1647F     |       91263 |
|      13 | 0xFFFFE63F  |  4294960703 |
|      14 | 0xFFFFFBCE  |  4294966222 |
|      15 | 0x155C0     |       87488 |
|      16 | 0xFFFFEBB5  |  4294962101 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 22 00 00                                          "..             
```

#### Opcodes

```
  0: 0x0000 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0002 [0x00] END_REQSTACK()
```

### Event 58

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          94 01 F8 FF FF  7F 92 01 F8 FF FF 7F 37     ............7
0010: 00 80 01 80 02 80 03 80  00                       .........       
```

#### Opcodes

```
  0: 0x0003 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0009 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-2.561*, z=90.160*, y=-6.394*, direction=55.8°*
  3: 0x0018 [0x00] END_REQSTACK()
```

### Event 65

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 32 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             94 01 F8 FF FF 7F 92           .......
0020: 01 F8 FF FF 7F 37 00 80  01 80 02 80 03 80 79 00  .....7........y.
0030: F8 FF FF 7F 77 30 0F 01  00                       ....w0...       
```

#### Opcodes

```
  0: 0x0019 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x001F [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0025 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-2.561*, z=90.160*, y=-6.394*, direction=55.8°*
  3: 0x002E [0x79] EventEntity looks at Tenzen (ID: 17772663/0x010F3077) (Basic look)
  4: 0x0038 [0x00] END_REQSTACK()
```

### Event 128

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0039  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             00                             .      
```

#### Opcodes

```
  0: 0x0039 [0x00] END_REQSTACK()
```

### Event 60

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                00                           .     
```

#### Opcodes

```
  0: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   5B 04 80 F8 FF             [....
0040: FF 7F F8 FF FF 7F 74 6C  6B 30 53 F8 FF FF 7F F8  ......tlk0S.....
0050: FF FF 7F 74 6C 6B 30 00                           ...tlk0.        
```

#### Opcodes

```
  0: 0x003B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=233*
  1: 0x004A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          5B 04 80 F8 FF FF 7F F8          [.......
0060: FF FF 7F 70 61 73 30 53  F8 FF FF 7F F8 FF FF 7F  ...pas0S........
0070: 70 61 73 30 00                                    pas0.           
```

#### Opcodes

```
  0: 0x0058 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=233*
  1: 0x0067 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  2: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                5B 04 80  F8 FF FF 7F F8 FF FF 7F       [..........
0080: 74 6C 6B 30 53 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  tlk0S........tlk
0090: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0075 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=233*
  1: 0x0084 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x0091 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0092  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       5E 69 64 6C 30 1C  05 80 00                   ^idl0....     
```

#### Opcodes

```
  0: 0x0092 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0097 [0x1C] WAIT(60* ticks)
  2: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009B  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   5E 69 64 6C 30             ^idl0
00A0: 1C 05 80 00                                       ....            
```

#### Opcodes

```
  0: 0x009B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00A0 [0x1C] WAIT(60* ticks)
  2: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             00                                        .           
```

#### Opcodes

```
  0: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                5B 06 80  F8 FF FF 7F F8 FF FF 7F       [..........
00B0: 72 69 67 30 00                                    rig0.           
```

#### Opcodes

```
  0: 0x00A5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "rig0" with entities [EventEntity, EventEntity], work=234*
  1: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                5B 06 80  F8 FF FF 7F F8 FF FF 7F       [..........
00C0: 72 69 67 31 00                                    rig1.           
```

#### Opcodes

```
  0: 0x00B5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "rig1" with entities [EventEntity, EventEntity], work=234*
  1: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                5B 06 80  F8 FF FF 7F F8 FF FF 7F       [..........
00D0: 6C 65 66 30 00                                    lef0.           
```

#### Opcodes

```
  0: 0x00C5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "lef0" with entities [EventEntity, EventEntity], work=234*
  1: 0x00D4 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                5B 06 80  F8 FF FF 7F F8 FF FF 7F       [..........
00E0: 6C 65 66 31 00                                    lef1.           
```

#### Opcodes

```
  0: 0x00D5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "lef1" with entities [EventEntity, EventEntity], work=234*
  1: 0x00E4 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                5B 06 80  F8 FF FF 7F F8 FF FF 7F       [..........
00F0: 64 77 6E 30 00                                    dwn0.           
```

#### Opcodes

```
  0: 0x00E5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dwn0" with entities [EventEntity, EventEntity], work=234*
  1: 0x00F4 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                5B 06 80  F8 FF FF 7F F8 FF FF 7F       [..........
0100: 64 77 6E 31 00                                    dwn1.           
```

#### Opcodes

```
  0: 0x00F5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dwn1" with entities [EventEntity, EventEntity], work=234*
  1: 0x0104 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0105  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                00                                      .          
```

#### Opcodes

```
  0: 0x0105 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0106   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                   22 00  2F 00 F8 FF FF 7F 6C F8        "./.....l.
0110: FF FF 7F 07 80 08 80 00                           ........        
```

#### Opcodes

```
  0: 0x0106 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0108 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x010E [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0117 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0118   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                          6C F8 FF FF 7F 09 80 08          l.......
0120: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0118 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0121 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0122  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:       22 00 2F 00 F8 FF  FF 7F 00                   "./......     
```

#### Opcodes

```
  0: 0x0122 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0124 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x012A [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x012B  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                   22 01 2F 01 F8             "./..
0130: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x012B [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x012D [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x0133 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0134   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:             6C F8 FF FF  7F 07 80 08 80 00            l.........  
```

#### Opcodes

```
  0: 0x0134 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x013D [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                            6C F8                l.
0140: FF FF 7F 09 80 08 80 00                           ........        
```

#### Opcodes

```
  0: 0x013E [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0147 [0x00] END_REQSTACK()
```

### Event 10188

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0148  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                          00                               .       
```

#### Opcodes

```
  0: 0x0148 [0x00] END_REQSTACK()
```

### Event 10189

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0149  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                             00                             .      
```

#### Opcodes

```
  0: 0x0149 [0x00] END_REQSTACK()
```

### Event 10190

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x014A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                00                           .     
```

#### Opcodes

```
  0: 0x014A [0x00] END_REQSTACK()
```

### Event 10200

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x014B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                   00                         .    
```

#### Opcodes

```
  0: 0x014B [0x00] END_REQSTACK()
```

### Event 10208

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x014C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                      00                       .   
```

#### Opcodes

```
  0: 0x014C [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014D   |
| Data Size    | 45 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                         32 0A 80               2..
0150: 1F 00 0B 80 0C 80 0D 80  1F 01 1F 00 0E 80 0F 80  ................
0160: 10 80 1F 01 6F 1E F0 FF  FF 7F 4A F0 FF FF 7F 0B  ....o.....J.....
0170: 30 0F 01 6F 76 F8 FF FF  7F 00                    0..ov.....      
```

#### Opcodes

```
  0: 0x014D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0150 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.618*, Z=91.263*, Y=-6.593*
  2: 0x0158 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x015A [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.074*, Z=87.488*, Y=-5.195*
  4: 0x0162 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0164 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0165 [0x1E] EventEntity looks at LocalPlayer and starts talking
  7: 0x016A [0x4A] LocalPlayer looks at Mawl'gofaur (ID: 17772555/0x010F300B)
  8: 0x0173 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x0174 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
 10: 0x0179 [0x00] END_REQSTACK()
```

### Event 10199

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x017A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                00                           .     
```

#### Opcodes

```
  0: 0x017A [0x00] END_REQSTACK()
```
