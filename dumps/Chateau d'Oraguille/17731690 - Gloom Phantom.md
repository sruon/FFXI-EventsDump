# 17731690 - Gloom Phantom

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 924 bytes                     |
| Total Events     | 47                            |
| References Count | 7                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [604](#event-604)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351)   | 0x0008       |     22 |              8 |
| [65535.2](#event-655352)   | 0x001E       |     16 |              2 |
| [65535.3](#event-655353)   | 0x002E       |     14 |              2 |
| [65535.4](#event-655354)   | 0x003C       |     16 |              2 |
| [65535.5](#event-655355)   | 0x004C       |     14 |              2 |
| [65535.6](#event-655356)   | 0x005A       |     16 |              2 |
| [65535.7](#event-655357)   | 0x006A       |     14 |              2 |
| [65535.8](#event-655358)   | 0x0078       |     16 |              2 |
| [65535.9](#event-655359)   | 0x0088       |     14 |              2 |
| [65535.10](#event-6553510) | 0x0096       |     16 |              2 |
| [65535.11](#event-6553511) | 0x00A6       |     14 |              2 |
| [65535.12](#event-6553512) | 0x00B4       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00C4       |     14 |              2 |
| [65535.14](#event-6553514) | 0x00D2       |     16 |              2 |
| [65535.15](#event-6553515) | 0x00E2       |     14 |              2 |
| [65535.16](#event-6553516) | 0x00F0       |     16 |              2 |
| [65535.17](#event-6553517) | 0x0100       |     14 |              2 |
| [65535.18](#event-6553518) | 0x010E       |     16 |              2 |
| [65535.19](#event-6553519) | 0x011E       |     14 |              2 |
| [65535.20](#event-6553520) | 0x012C       |     16 |              2 |
| [65535.21](#event-6553521) | 0x013C       |     14 |              2 |
| [65535.22](#event-6553522) | 0x014A       |     16 |              2 |
| [65535.23](#event-6553523) | 0x015A       |     14 |              2 |
| [65535.24](#event-6553524) | 0x0168       |     16 |              2 |
| [65535.25](#event-6553525) | 0x0178       |     14 |              2 |
| [65535.26](#event-6553526) | 0x0186       |     16 |              2 |
| [65535.27](#event-6553527) | 0x0196       |     14 |              2 |
| [65535.28](#event-6553528) | 0x01A4       |     16 |              2 |
| [65535.29](#event-6553529) | 0x01B4       |     14 |              2 |
| [65535.30](#event-6553530) | 0x01C2       |     16 |              2 |
| [65535.31](#event-6553531) | 0x01D2       |     14 |              2 |
| [65535.32](#event-6553532) | 0x01E0       |     16 |              2 |
| [65535.33](#event-6553533) | 0x01F0       |     14 |              2 |
| [65535.34](#event-6553534) | 0x01FE       |     16 |              2 |
| [65535.35](#event-6553535) | 0x020E       |     14 |              2 |
| [65535.36](#event-6553536) | 0x021C       |     16 |              2 |
| [65535.37](#event-6553537) | 0x022C       |     14 |              2 |
| [65535.38](#event-6553538) | 0x023A       |     16 |              2 |
| [65535.39](#event-6553539) | 0x024A       |     14 |              2 |
| [65535.40](#event-6553540) | 0x0258       |     16 |              2 |
| [65535.41](#event-6553541) | 0x0268       |     14 |              2 |
| [65535.42](#event-6553542) | 0x0276       |     16 |              2 |
| [65535.43](#event-6553543) | 0x0286       |     14 |              2 |
| [65535.44](#event-6553544) | 0x0294       |     16 |              2 |
| [65535.45](#event-6553545) | 0x02A4       |     14 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x3B26F     |      242287 |
|       2 | 0x3AB52     |      240466 |
|       3 | 0x0000      |           0 |
|       4 | 0x00D7      |         215 |
|       5 | 0x00D8      |         216 |
|       6 | 0x0A1B      |        2587 |

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

### Event 604

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 6F 1E 6E  90 0E 01 6F 70 00        .....o.n...op.  
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=242.287*, Z=240.466*, Y=0.000*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0016 [0x1E] EventEntity looks at Uran-Mafran (ID: 17731694/0x010E906E) and starts talking
  5: 0x001B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x001C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            5B 04                [.
0020: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 00        .........tlk0.  
```

#### Opcodes

```
  0: 0x001E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=215*
  1: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            53 F8                S.
0030: FF FF 7F F8 FF FF 7F 74  6C 6B 30 00              .......tlk0.    
```

#### Opcodes

```
  0: 0x002E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      5B 04 80 F8              [...
0040: FF FF 7F F8 FF FF 7F 74  6C 6B 31 00              .......tlk1.    
```

#### Opcodes

```
  0: 0x003C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=215*
  1: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      53 F8 FF FF              S...
0050: 7F F8 FF FF 7F 74 6C 6B  31 00                    .....tlk1.      
```

#### Opcodes

```
  0: 0x004C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                5B 04 80 F8 FF FF            [.....
0060: 7F F8 FF FF 7F 70 61 73  30 00                    .....pas0.      
```

#### Opcodes

```
  0: 0x005A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=215*
  1: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                53 F8 FF FF 7F F8            S.....
0070: FF FF 7F 70 61 73 30 00                           ...pas0.        
```

#### Opcodes

```
  0: 0x006A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x0077 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          5B 04 80 F8 FF FF 7F F8          [.......
0080: FF FF 7F 63 6F 72 30 00                           ...cor0.        
```

#### Opcodes

```
  0: 0x0078 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "cor0" with entities [EventEntity, EventEntity], work=215*
  1: 0x0087 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0088   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          53 F8 FF FF 7F F8 FF FF          S.......
0090: 7F 63 6F 72 30 00                                 .cor0.          
```

#### Opcodes

```
  0: 0x0088 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "cor0" with entities [EventEntity, EventEntity]
  1: 0x0095 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0096   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   5B 04  80 F8 FF FF 7F F8 FF FF        [.........
00A0: 7F 6F 6B 69 30 00                                 .oki0.          
```

#### Opcodes

```
  0: 0x0096 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "oki0" with entities [EventEntity, EventEntity], work=215*
  1: 0x00A5 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A6   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                   53 F8  FF FF 7F F8 FF FF 7F 6F        S........o
00B0: 6B 69 30 00                                       ki0.            
```

#### Opcodes

```
  0: 0x00A6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "oki0" with entities [EventEntity, EventEntity]
  1: 0x00B3 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B4   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             5B 04 80 F8  FF FF 7F F8 FF FF 7F 74      [..........t
00C0: 6C 6B 32 00                                       lk2.            
```

#### Opcodes

```
  0: 0x00B4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=215*
  1: 0x00C3 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C4   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:             53 F8 FF FF  7F F8 FF FF 7F 74 6C 6B      S........tlk
00D0: 32 00                                             2.              
```

#### Opcodes

```
  0: 0x00C4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
  1: 0x00D1 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D2   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:       5B 04 80 F8 FF FF  7F F8 FF FF 7F 74 69 64    [..........tid
00E0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x00D2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tid0" with entities [EventEntity, EventEntity], work=215*
  1: 0x00E1 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E2   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:       53 F8 FF FF 7F F8  FF FF 7F 74 69 64 30 00    S........tid0.
```

#### Opcodes

```
  0: 0x00E2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tid0" with entities [EventEntity, EventEntity]
  1: 0x00EF [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F0   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0: 5B 04 80 F8 FF FF 7F F8  FF FF 7F 74 61 6F 30 00  [..........tao0.
```

#### Opcodes

```
  0: 0x00F0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tao0" with entities [EventEntity, EventEntity], work=215*
  1: 0x00FF [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0100   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100: 53 F8 FF FF 7F F8 FF FF  7F 74 61 6F 30 00        S........tao0.  
```

#### Opcodes

```
  0: 0x0100 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tao0" with entities [EventEntity, EventEntity]
  1: 0x010D [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                            5B 05                [.
0110: 80 F8 FF FF 7F F8 FF FF  7F 61 6E 67 30 00        .........ang0.  
```

#### Opcodes

```
  0: 0x010E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang0" with entities [EventEntity, EventEntity], work=216*
  1: 0x011D [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                            53 F8                S.
0120: FF FF 7F F8 FF FF 7F 61  6E 67 30 00              .......ang0.    
```

#### Opcodes

```
  0: 0x011E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ang0" with entities [EventEntity, EventEntity]
  1: 0x012B [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                      5B 05 80 F8              [...
0130: FF FF 7F F8 FF FF 7F 61  6E 67 31 00              .......ang1.    
```

#### Opcodes

```
  0: 0x012C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang1" with entities [EventEntity, EventEntity], work=216*
  1: 0x013B [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                      53 F8 FF FF              S...
0140: 7F F8 FF FF 7F 61 6E 67  31 00                    .....ang1.      
```

#### Opcodes

```
  0: 0x013C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ang1" with entities [EventEntity, EventEntity]
  1: 0x0149 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                5B 05 80 F8 FF FF            [.....
0150: 7F F8 FF FF 7F 62 69 6B  30 00                    .....bik0.      
```

#### Opcodes

```
  0: 0x014A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bik0" with entities [EventEntity, EventEntity], work=216*
  1: 0x0159 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                53 F8 FF FF 7F F8            S.....
0160: FF FF 7F 62 69 6B 30 00                           ...bik0.        
```

#### Opcodes

```
  0: 0x015A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bik0" with entities [EventEntity, EventEntity]
  1: 0x0167 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0168   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                          5B 05 80 F8 FF FF 7F F8          [.......
0170: FF FF 7F 62 69 6B 31 00                           ...bik1.        
```

#### Opcodes

```
  0: 0x0168 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bik1" with entities [EventEntity, EventEntity], work=216*
  1: 0x0177 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0178   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                          53 F8 FF FF 7F F8 FF FF          S.......
0180: 7F 62 69 6B 31 00                                 .bik1.          
```

#### Opcodes

```
  0: 0x0178 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bik1" with entities [EventEntity, EventEntity]
  1: 0x0185 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0186   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                   5B 05  80 F8 FF FF 7F F8 FF FF        [.........
0190: 7F 62 79 65 30 00                                 .bye0.          
```

#### Opcodes

```
  0: 0x0186 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bye0" with entities [EventEntity, EventEntity], work=216*
  1: 0x0195 [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0196   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                   53 F8  FF FF 7F F8 FF FF 7F 62        S........b
01A0: 79 65 30 00                                       ye0.            
```

#### Opcodes

```
  0: 0x0196 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bye0" with entities [EventEntity, EventEntity]
  1: 0x01A3 [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A4   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:             5B 05 80 F8  FF FF 7F F8 FF FF 7F 66      [..........f
01B0: 75 6D 30 00                                       um0.            
```

#### Opcodes

```
  0: 0x01A4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fum0" with entities [EventEntity, EventEntity], work=216*
  1: 0x01B3 [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B4   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:             53 F8 FF FF  7F F8 FF FF 7F 66 75 6D      S........fum
01C0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x01B4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "fum0" with entities [EventEntity, EventEntity]
  1: 0x01C1 [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C2   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:       5B 05 80 F8 FF FF  7F F8 FF FF 7F 66 75 6D    [..........fum
01D0: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x01C2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fum1" with entities [EventEntity, EventEntity], work=216*
  1: 0x01D1 [0x00] END_REQSTACK()
```

### Event 65535.31

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D2   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:       53 F8 FF FF 7F F8  FF FF 7F 66 75 6D 31 00    S........fum1.
```

#### Opcodes

```
  0: 0x01D2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "fum1" with entities [EventEntity, EventEntity]
  1: 0x01DF [0x00] END_REQSTACK()
```

### Event 65535.32

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E0   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0: 5B 05 80 F8 FF FF 7F F8  FF FF 7F 68 61 70 30 00  [..........hap0.
```

#### Opcodes

```
  0: 0x01E0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hap0" with entities [EventEntity, EventEntity], work=216*
  1: 0x01EF [0x00] END_REQSTACK()
```

### Event 65535.33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01F0   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0: 53 F8 FF FF 7F F8 FF FF  7F 68 61 70 30 00        S........hap0.  
```

#### Opcodes

```
  0: 0x01F0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hap0" with entities [EventEntity, EventEntity]
  1: 0x01FD [0x00] END_REQSTACK()
```

### Event 65535.34

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01FE   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                                            5B 05                [.
0200: 80 F8 FF FF 7F F8 FF FF  7F 68 61 70 31 00        .........hap1.  
```

#### Opcodes

```
  0: 0x01FE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hap1" with entities [EventEntity, EventEntity], work=216*
  1: 0x020D [0x00] END_REQSTACK()
```

### Event 65535.35

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x020E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                                            53 F8                S.
0210: FF FF 7F F8 FF FF 7F 68  61 70 31 00              .......hap1.    
```

#### Opcodes

```
  0: 0x020E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hap1" with entities [EventEntity, EventEntity]
  1: 0x021B [0x00] END_REQSTACK()
```

### Event 65535.36

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x021C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                                      5B 05 80 F8              [...
0220: FF FF 7F F8 FF FF 7F 6D  6D 6D 30 00              .......mmm0.    
```

#### Opcodes

```
  0: 0x021C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mmm0" with entities [EventEntity, EventEntity], work=216*
  1: 0x022B [0x00] END_REQSTACK()
```

### Event 65535.37

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x022C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                                      53 F8 FF FF              S...
0230: 7F F8 FF FF 7F 6D 6D 6D  30 00                    .....mmm0.      
```

#### Opcodes

```
  0: 0x022C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "mmm0" with entities [EventEntity, EventEntity]
  1: 0x0239 [0x00] END_REQSTACK()
```

### Event 65535.38

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x023A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:                                5B 05 80 F8 FF FF            [.....
0240: 7F F8 FF FF 7F 6D 6D 6D  31 00                    .....mmm1.      
```

#### Opcodes

```
  0: 0x023A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mmm1" with entities [EventEntity, EventEntity], work=216*
  1: 0x0249 [0x00] END_REQSTACK()
```

### Event 65535.39

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x024A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                53 F8 FF FF 7F F8            S.....
0250: FF FF 7F 6D 6D 6D 31 00                           ...mmm1.        
```

#### Opcodes

```
  0: 0x024A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "mmm1" with entities [EventEntity, EventEntity]
  1: 0x0257 [0x00] END_REQSTACK()
```

### Event 65535.40

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0258   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0250:                          5B 05 80 F8 FF FF 7F F8          [.......
0260: FF FF 7F 66 6E 64 30 00                           ...fnd0.        
```

#### Opcodes

```
  0: 0x0258 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fnd0" with entities [EventEntity, EventEntity], work=216*
  1: 0x0267 [0x00] END_REQSTACK()
```

### Event 65535.41

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0268   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0260:                          53 F8 FF FF 7F F8 FF FF          S.......
0270: 7F 66 6E 64 30 00                                 .fnd0.          
```

#### Opcodes

```
  0: 0x0268 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "fnd0" with entities [EventEntity, EventEntity]
  1: 0x0275 [0x00] END_REQSTACK()
```

### Event 65535.42

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0276   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:                   5B 05  80 F8 FF FF 7F F8 FF FF        [.........
0280: 7F 66 6E 64 31 00                                 .fnd1.          
```

#### Opcodes

```
  0: 0x0276 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fnd1" with entities [EventEntity, EventEntity], work=216*
  1: 0x0285 [0x00] END_REQSTACK()
```

### Event 65535.43

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0286   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0280:                   53 F8  FF FF 7F F8 FF FF 7F 66        S........f
0290: 6E 64 31 00                                       nd1.            
```

#### Opcodes

```
  0: 0x0286 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "fnd1" with entities [EventEntity, EventEntity]
  1: 0x0293 [0x00] END_REQSTACK()
```

### Event 65535.44

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0294   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0290:             5B 06 80 F8  FF FF 7F F8 FF FF 7F 65      [..........e
02A0: 64 62 31 00                                       db1.            
```

#### Opcodes

```
  0: 0x0294 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "edb1" with entities [EventEntity, EventEntity], work=2587*
  1: 0x02A3 [0x00] END_REQSTACK()
```

### Event 65535.45

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02A4   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02A0:             53 F8 FF FF  7F F8 FF FF 7F 65 64 62      S........edb
02B0: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x02A4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "edb1" with entities [EventEntity, EventEntity]
  1: 0x02B1 [0x00] END_REQSTACK()
```
