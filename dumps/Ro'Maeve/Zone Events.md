# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Ro'Maeve (ID: 122) |
| Block Size       | 376 bytes          |
| Total Events     | 17                 |
| References Count | 28                 |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65534](#event-65534)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     10 |              2 |
| [65535.2](#event-655352)   | 0x000C       |      6 |              2 |
| [65535.3](#event-655353)   | 0x0012       |      6 |              2 |
| [65535.4](#event-655354)   | 0x0018       |      6 |              2 |
| [65535.5](#event-655355)   | 0x001E       |      6 |              2 |
| [65535.6](#event-655356)   | 0x0024       |      6 |              2 |
| [65535.7](#event-655357)   | 0x002A       |     10 |              2 |
| [65535.8](#event-655358)   | 0x0034       |     10 |              2 |
| [65535.9](#event-655359)   | 0x003E       |     14 |              4 |
| [65535.10](#event-6553510) | 0x004C       |      9 |              3 |
| [65535.11](#event-6553511) | 0x0055       |     23 |              5 |
| [65535.12](#event-6553512) | 0x006C       |     14 |              4 |
| [65535.13](#event-6553513) | 0x007A       |     29 |              5 |
| [65535.14](#event-6553514) | 0x0097       |     13 |              3 |
| [65535.15](#event-6553515) | 0x00A4       |     14 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFFDB3  |  4294966707 |
|       1 | 0xF7C7      |       63431 |
|       2 | 0xFFFF8D74  |  4294937972 |
|       3 | 0x0DED      |        3565 |
|       4 | 0x013D      |         317 |
|       5 | 0xFB78      |       64376 |
|       6 | 0x0B90      |        2960 |
|       7 | 0x0060      |          96 |
|       8 | 0xFFFC0427  |  4294706215 |
|       9 | 0x17DF4     |       97780 |
|      10 | 0x0C06      |        3078 |
|      11 | 0x000D      |          13 |
|      12 | 0xFFFFFFC6  |  4294967238 |
|      13 | 0xFFFC4F78  |  4294725496 |
|      14 | 0x189D8     |      100824 |
|      15 | 0x0032      |          50 |
|      16 | 0xFFFCCF78  |  4294758264 |
|      17 | 0x8BB9      |       35769 |
|      18 | 0xFFFFF0C6  |  4294963398 |
|      19 | 0x0028      |          40 |
|      20 | 0xFFFD12A0  |  4294775456 |
|      21 | 0x555B      |       21851 |
|      22 | 0xFFFFEF98  |  4294963096 |
|      23 | 0x0050      |          80 |
|      24 | 0x044C      |        1100 |
|      25 | 0x05DC      |        1500 |
|      26 | 0x0015      |          21 |
|      27 | 0x000F      |          15 |

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

### Event 65534

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.589*, z=63.431*, y=-29.324*, direction=313.3°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      03 02 10 0B              ....
0010: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x000C [0x03] Work_Zone[2] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       03 02 10 07 7F 00                             ......        
```

#### Opcodes

```
  0: 0x0012 [0x03] Work_Zone[2] = Entity->Race
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0018  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          03 09 10 07 7F 00                ......  
```

#### Opcodes

```
  0: 0x0018 [0x03] Work_Zone[9] = Entity->Race
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            03 09                ..
0020: 10 06 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x001E [0x03] Work_Zone[9] = Entity->JobId (if LocalPlayer)
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             03 08 10 06  7F 00                        ......      
```

#### Opcodes

```
  0: 0x0024 [0x03] Work_Zone[8] = Entity->JobId (if LocalPlayer)
  1: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                37 04 80 05 80 02            7.....
0030: 80 06 80 00                                       ....            
```

#### Opcodes

```
  0: 0x002A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.317*, z=64.376*, y=-29.324*, direction=260.1°*
  1: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             37 07 80 08  80 09 80 0A 80 00            7.........  
```

#### Opcodes

```
  0: 0x0034 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.096*, z=-261.081*, y=97.780*, direction=270.5°*
  1: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            32 0B                2.
0040: 80 5A 00 0C 80 0D 80 0E  80 5A 01 00              .Z.......Z..    
```

#### Opcodes

```
  0: 0x003E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0041 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-0.058*, Z=-241.800*, Y=100.824*
  2: 0x0049 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004C  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      22 00 94 01              "...
0050: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x004C [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x004E [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                32 0F 80  1F 00 10 80 11 80 12 80       2..........
0060: 1F 01 4A F8 FF FF 7F 3B  A1 07 01 00              ..J....;....    
```

#### Opcodes

```
  0: 0x0055 [0x32] ExtData[1]->MainSpeed = 50* * 0.1
  1: 0x0058 [0x1F] MOVE_ENTITY: EventEntity moves to X=-209.032*, Z=35.769*, Y=-3.898*
  2: 0x0060 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0062 [0x4A] EventEntity looks at Shantotto (ID: 17277243/0x0107A13B)
  4: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      32 13 80 1F              2...
0070: 00 14 80 15 80 16 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x006C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x006F [0x1F] MOVE_ENTITY: EventEntity moves to X=-191.840*, Z=21.851*, Y=-4.200*
  2: 0x0077 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 29 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                1C 17 80 4B F8 FF            ...K..
0080: FF 7F 18 80 59 03 F8 FF  FF 7F 19 80 79 00 F8 FF  ....Y.......y...
0090: FF 7F 3C A1 07 01 00                              ..<....         
```

#### Opcodes

```
  0: 0x007A [0x1C] WAIT(80* ticks)
  1: 0x007D [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=6.0°*)
  2: 0x0084 [0x59] UPDATE_ENTITY_DATA: Set EventEntity turn speed head = 1500*
  3: 0x008C [0x79] EventEntity looks at Aldo (ID: 17277244/0x0107A13C) (Basic look)
  4: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      6E  F8 FF FF 7F 1A 80 99 F8         n........
00A0: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0097 [0x6E] EventEntity uses emote 21*
  1: 0x009E [0x99] Wait for EventEntity animation to complete
  2: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A4   |
| Data Size    | 14 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             1C 1B 80 79  00 F8 FF FF 7F 3A A1 07      ...y.....:..
00B0: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x00A4 [0x1C] WAIT(15* ticks)
  1: 0x00A7 [0x79] EventEntity looks at Unnamed NPC (ID: 17277242/0x0107A13A) (Basic look)
  2: 0x00B1 [0x00] END_REQSTACK()
```
