# 16999081 - Apkallu Guide

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Arrapago Reef (ID: 54) |
| Block Size       | 456 bytes              |
| Total Events     | 22                     |
| References Count | 30                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     13 |              2 |
| [65535.2](#event-655352)   | 0x000E       |      4 |              2 |
| [65535.3](#event-655353)   | 0x0012       |      7 |              3 |
| [65535.4](#event-655354)   | 0x0019       |      7 |              3 |
| [242](#event-242)          | 0x0020       |      1 |              1 |
| [243](#event-243)          | 0x0021       |      1 |              1 |
| [246](#event-246)          | 0x0022       |      1 |              1 |
| [247](#event-247)          | 0x0023       |      1 |              1 |
| [65535.5](#event-655355)   | 0x0024       |     15 |              5 |
| [65535.6](#event-655356)   | 0x0033       |     15 |              5 |
| [248](#event-248)          | 0x0042       |      1 |              1 |
| [65535.7](#event-655357)   | 0x0043       |     15 |              5 |
| [65535.8](#event-655358)   | 0x0052       |     15 |              5 |
| [65535.9](#event-655359)   | 0x0061       |     15 |              5 |
| [65535.10](#event-6553510) | 0x0070       |     21 |              7 |
| [250](#event-250)          | 0x0085       |      1 |              1 |
| [65535.11](#event-6553511) | 0x0086       |     15 |              5 |
| [65535.12](#event-6553512) | 0x0095       |     22 |              8 |
| [65535.13](#event-6553513) | 0x00AB       |     22 |              8 |
| [65535.14](#event-6553514) | 0x00C1       |     22 |              8 |
| [65535.15](#event-6553515) | 0x00D7       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0488      |        1160 |
|       1 | 0x005A      |          90 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFF79AD5  |  4294417109 |
|       6 | 0x4624A     |      287306 |
|       7 | 0xFFFFEB7B  |  4294962043 |
|       8 | 0xFFF73EE2  |  4294393570 |
|       9 | 0x47D1D     |      294173 |
|      10 | 0xFFFFF04E  |  4294963278 |
|      11 | 0x0028      |          40 |
|      12 | 0xFFF710CC  |  4294381772 |
|      13 | 0x487B0     |      296880 |
|      14 | 0xFFFFE3FC  |  4294960124 |
|      15 | 0xFFF72166  |  4294386022 |
|      16 | 0x4AC06     |      306182 |
|      17 | 0xFFFFDD3A  |  4294958394 |
|      18 | 0xFFF713BB  |  4294382523 |
|      19 | 0x4766A     |      292458 |
|      20 | 0xFFFFEDD7  |  4294962647 |
|      21 | 0xFFF726D3  |  4294387411 |
|      22 | 0x474F3     |      292083 |
|      23 | 0xFFFFED4E  |  4294962510 |
|      24 | 0xFFF7901F  |  4294414367 |
|      25 | 0x448AC     |      280748 |
|      26 | 0xFFFFED09  |  4294962441 |
|      27 | 0xFFF7ABA5  |  4294421413 |
|      28 | 0x449F6     |      281078 |
|      29 | 0xFFFFEB87  |  4294962055 |

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    C4 02 00 80 F8 FF FF  7F 5A 62 03 01 00         ........Zb...  
```

#### Opcodes

```
  0: 0x0001 [0xC4] SCHEDULE_MAGIC_CASTING_ALT (arg=18): EventEntity casts magic 1160* on Mutihb (ID: 16999002/0x0103625A)
  1: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000E  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            1C 01                ..
0010: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x000E [0x1C] WAIT(90* ticks)
  1: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       AB 03 AC 01 02 80  00                         .......       
```

#### Opcodes

```
  0: 0x0012 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0014 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             AC 01 03 80 AB 04 00           .......
```

#### Opcodes

```
  0: 0x0019 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x001D [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x001F [0x00] END_REQSTACK()
```

### Event 242

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0020  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0020 [0x00] END_REQSTACK()
```

### Event 243

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0021  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    00                                              .              
```

#### Opcodes

```
  0: 0x0021 [0x00] END_REQSTACK()
```

### Event 246

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0022  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       00                                            .             
```

#### Opcodes

```
  0: 0x0022 [0x00] END_REQSTACK()
```

### Event 247

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0023  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          00                                          .            
```

#### Opcodes

```
  0: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             32 04 80 1F  00 05 80 06 80 07 80 1F      2...........
0030: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0024 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=-550.187*, Z=287.306*, Y=-5.253*
  2: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0031 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          32 04 80 1F 00  08 80 09 80 0A 80 1F 01     2............
0040: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0033 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=-573.726*, Z=294.173*, Y=-4.018*
  2: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0040 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0041 [0x00] END_REQSTACK()
```

### Event 248

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0042  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       00                                            .             
```

#### Opcodes

```
  0: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          32 04 80 1F 00  05 80 06 80 07 80 1F 01     2............
0050: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0043 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0046 [0x1F] MOVE_ENTITY: EventEntity moves to X=-550.187*, Z=287.306*, Y=-5.253*
  2: 0x004E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0050 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       32 04 80 1F 00 08  80 09 80 0A 80 1F 01 6F    2............o
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0052 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0055 [0x1F] MOVE_ENTITY: EventEntity moves to X=-573.726*, Z=294.173*, Y=-4.018*
  2: 0x005D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    32 0B 80 1F 00 0C 80  0D 80 0E 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0061 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0064 [0x1F] MOVE_ENTITY: EventEntity moves to X=-585.524*, Z=296.880*, Y=-7.172*
  2: 0x006C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x006F [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0070   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070: 32 04 80 1F 00 0F 80 10  80 11 80 1F 01 6F AC 01  2............o..
0080: 03 80 AB 04 00                                    .....           
```

#### Opcodes

```
  0: 0x0070 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0073 [0x1F] MOVE_ENTITY: EventEntity moves to X=-581.274*, Z=306.182*, Y=-8.902*
  2: 0x007B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x007E [0xAC] EventEntity->StatusEvent = 0*
  5: 0x0082 [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  6: 0x0084 [0x00] END_REQSTACK()
```

### Event 250

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0085  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                00                                      .          
```

#### Opcodes

```
  0: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0086   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   32 0B  80 1F 00 05 80 06 80 07        2.........
0090: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0086 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0089 [0x1F] MOVE_ENTITY: EventEntity moves to X=-550.187*, Z=287.306*, Y=-5.253*
  2: 0x0091 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0093 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                32 04 80  1F 00 12 80 13 80 14 80       2..........
00A0: 1F 01 6F 1E F0 FF FF 7F  6F 70 00                 ..o.....op.     
```

#### Opcodes

```
  0: 0x0095 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0098 [0x1F] MOVE_ENTITY: EventEntity moves to X=-584.773*, Z=292.458*, Y=-4.649*
  2: 0x00A0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00A3 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x00A8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00A9 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x00AA [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AB   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   32 04 80 1F 00             2....
00B0: 15 80 16 80 17 80 1F 01  6F 1E AB 62 03 01 6F 70  ........o..b..op
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x00AB [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00AE [0x1F] MOVE_ENTITY: EventEntity moves to X=-579.885*, Z=292.083*, Y=-4.786*
  2: 0x00B6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00B9 [0x1E] EventEntity looks at Bijoux (ID: 16999083/0x010362AB) and starts talking
  5: 0x00BE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00BF [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x00C0 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C1   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:    32 04 80 1F 00 18 80  19 80 1A 80 1F 01 6F 1E   2............o.
00D0: F0 FF FF 7F 6F 70 00                              ....op.         
```

#### Opcodes

```
  0: 0x00C1 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00C4 [0x1F] MOVE_ENTITY: EventEntity moves to X=-552.929*, Z=280.748*, Y=-4.855*
  2: 0x00CC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00CE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00CF [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x00D4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00D5 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x00D6 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D7   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                      32  04 80 1F 00 1B 80 1C 80         2........
00E0: 1D 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x00D7 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00DA [0x1F] MOVE_ENTITY: EventEntity moves to X=-545.883*, Z=281.078*, Y=-5.241*
  2: 0x00E2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00E4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00E5 [0x00] END_REQSTACK()
```
